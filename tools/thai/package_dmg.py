"""Create and checksum the independently signed Apple Silicon Thai DMG."""
from pathlib import Path
import hashlib
import platform
import shutil
import subprocess
import tomllib

root = Path(__file__).resolve().parents[2]
version = tomllib.loads((root / 'apps/filmcraft/Cargo.toml').read_text())['package']['version']
arch = platform.machine()
if arch != 'arm64':
    raise SystemExit('This local Thai package is currently validated for Apple Silicon only')
dist = root / 'dist/thai'
app = dist / 'FilmCraft.app'
subprocess.run(['codesign', '--verify', '--deep', '--strict', str(app)], check=True)
stage = dist / ('dmg-stage-' + version)
if stage.exists():
    shutil.rmtree(stage)
stage.mkdir()
subprocess.run(['ditto', str(app), str(stage / app.name)], check=True)
(stage / 'Applications').symlink_to('/Applications')
dmg = dist / f'FilmCraft-TH-{version}-macOS-{arch}.dmg'
subprocess.run(['hdiutil', 'create', '-ov', '-fs', 'HFS+', '-format', 'UDZO', '-srcfolder', str(stage), '-volname', 'FilmCraft Thai', str(dmg)], check=True)
subprocess.run(['hdiutil', 'verify', str(dmg)], check=True)
with dmg.open('rb') as f:
    checksum = hashlib.file_digest(f, 'sha256').hexdigest()
dmg.with_suffix('.dmg.sha256').write_text(f'{checksum}  {dmg.name}\n')
print(dmg)
print('Ad-hoc signed; not Apple-notarized')
