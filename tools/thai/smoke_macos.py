#!/usr/bin/env python3
"""Run an isolated app smoke test using FilmCraft's documented control API."""
import json
import os
import secrets
import socket
import subprocess
import sys
import time
from pathlib import Path
root = Path(__file__).resolve().parents[2]
qa = Path(os.environ.get('FILMCRAFT_THAI_QA_DIR', str(root / 'target/thai-qa')))
qa.mkdir(parents=True, exist_ok=True)
with socket.socket() as listener:
    listener.bind(('127.0.0.1', 0))
    port = listener.getsockname()[1]
token = secrets.token_hex(32)
env = dict(os.environ, FILMCRAFT_CONTROL_TOKEN=token)
binary = Path(sys.argv[1]) if len(sys.argv) > 1 else root / 'target/release/filmcraft'
log = (qa / 'app.log').open('w')
process = subprocess.Popen([str(binary), '--control', str(port), '--data-dir', str(qa / 'data'), '--empty'], env=env, stdout=log, stderr=log)
def call(method, params=None):
    with socket.create_connection(('127.0.0.1', port), timeout=30) as connection:
        request = dict(id=1, token=token, method=method, params=params or {})
        connection.sendall((json.dumps(request) + '\n').encode())
        reply = json.loads(connection.makefile('rb').readline())
        if not reply.get('ok'):
            raise RuntimeError((method, reply))
        return reply.get('result')
try:
    for attempt in range(120):
        if process.poll() is not None:
            raise RuntimeError('App exited; see target/thai-qa/app.log')
        try:
            call('ui.inspect')
            break
        except (ConnectionError, OSError):
            time.sleep(0.5)
        except RuntimeError as error:
            if "still starting" not in str(error):
                raise
            time.sleep(0.5)
    call('ui.focus')
    assert call('ui.menu.invoke', {'id': 'app.language.thai'}) == 'th'
    # Capture a real app window. Retina captures retain their native pixels;
    # their PNG container can be compressed losslessly without resizing.
    call('ui.resize', {'width': 1360, 'height': 850})
    menus = call('ui.menu.list')
    (qa / 'menus.json').write_text(json.dumps(menus, ensure_ascii=False, indent=2), encoding='utf-8')
    assert any(m.get('id') == 'app.language.thai' and m.get('checked') for m in menus)
    call('engine.execute', {'command': 'file.openDemoProject', 'params': {}})
    project = qa / 'filmcraft-th-demo.fcproj'
    call('engine.execute', {'command': 'file.saveAs', 'params': {'path': str(project)}})
    before = call('engine.execute', {'command': 'project.inspect', 'params': {}})
    call('engine.execute', {'command': 'file.open', 'params': {'path': str(project)}})
    after = call('engine.execute', {'command': 'project.inspect', 'params': {}})
    for key in ('name', 'root', 'activeSequence', 'sourceItem'):
        assert before[key] == after[key], ('native project round-trip changed', key)
    (qa / 'project-roundtrip.json').write_text(json.dumps({'before': before, 'after': after}, ensure_ascii=False, indent=2), encoding='utf-8')
    assert project.stat().st_size > 100
    call('ui.set', {'mode': 'edit'})
    time.sleep(1)
    call('ui.screenshot', {'path': str(qa / 'editing.png')})
    call('ui.menu.invoke', {'id': 'app.settings.general'})
    call('ui.screenshot', {'path': str(qa / 'settings.png')})
    call('ui.key', {'key': 'Escape'})
    call('ui.set', {'mode': 'export'})
    call('ui.screenshot', {'path': str(qa / 'export.png')})
    state = call('ui.inspect')
    (qa / 'state.json').write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    prefs = json.loads((qa / 'data/preferences.json').read_text(encoding='utf-8'))
    assert prefs['general']['interfaceLanguage'] == 'th'
    print('PASS: Thai menu selection, preferences, native project save/reopen, demo project, editing/settings/export screenshots')
finally:
    try:
        call('app.quit')
        process.wait(timeout=20)
    except Exception:
        process.terminate()
        process.wait(timeout=10)
    log.close()
