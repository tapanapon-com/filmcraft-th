#!/usr/bin/env python3
"""Package the locally built binary without changing /Applications."""
import plistlib
import os
import tomllib
import shutil
import subprocess
from pathlib import Path
root = Path(__file__).resolve().parents[2]
binary = root / 'target/release/filmcraft'
cli = root / 'target/release/filmcraft-cli'
if not binary.is_file() or not cli.is_file():
    raise SystemExit('Build both filmcraft and filmcraft-cli in release mode first')
app = root / 'dist/thai/FilmCraft.app'
contents = app / 'Contents'
resources = contents / 'Resources'
resources.mkdir(parents=True, exist_ok=True)
(contents / 'MacOS').mkdir(exist_ok=True)
shutil.copy2(binary, contents / 'MacOS/FilmCraft')
shutil.copy2(cli, contents / 'MacOS/filmcraft-cli')
shutil.copy2(root / 'assets/app-icon/filmcraft.icns', resources / 'FilmCraft.icns')
for name in ['NOTICE', 'LICENSE-MIT', 'LICENSE-APACHE', 'ATTRIBUTION.md']:
    shutil.copy2(root / name, resources / name)
sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
version = tomllib.loads((root / 'apps/filmcraft/Cargo.toml').read_text())['package']['version']
text = (root / 'packaging/macos/Info.plist.in').read_text().replace('@VERSION@', version).replace('@SHORT_VERSION@', version.split('-')[0]).replace('@BUILD_SHA@', sha + '-thai-local')
info = plistlib.loads(text.encode())
info['FilmCraftLocalBuild'] = 'Independent Thai localization, 2026-11-07'
(contents / 'Info.plist').write_bytes(plistlib.dumps(info))
(contents / 'PkgInfo').write_bytes(b'APPL????')
(resources / 'th.lproj').mkdir(exist_ok=True)
(resources / 'th.lproj/InfoPlist.strings').write_text('"NSMicrophoneUsageDescription" = "FilmCraft ใช้ไมโครโฟนเพื่อบันทึกเสียงบรรยายลงในไทม์ไลน์";\n"CFBundleDisplayName" = "FilmCraft";\n')
fonts = Path(os.environ.get('CRAFT_FONTS_DIR', str(root.parent / 'craft-fonts'))) / 'fonts'
licenses = resources / 'Licenses'
licenses.mkdir(exist_ok=True)
for license_file in fonts.glob('*/OFL.txt'):
    shutil.copy2(license_file, licenses / ('OFL-' + license_file.parent.name + '.txt'))
for executable in [contents / 'MacOS/FilmCraft', contents / 'MacOS/filmcraft-cli']:
    subprocess.run(['lipo', str(executable), '-verify_arch', 'arm64'], check=True)
    subprocess.run(['codesign', '--force', '--sign', '-', '--timestamp=none', str(executable)], check=True)
subprocess.run(['codesign', '--force', '--sign', '-', '--timestamp=none', str(app)], check=True)
subprocess.run(['codesign', '--verify', '--deep', '--strict', str(app)], check=True)
print(app)
