# FilmCraft TH 0.17.1-th.1 — Windows x64

รุ่นภาษาไทยสำหรับ Windows 10/11 บนพีซี Intel/AMD 64 บิต ต่อยอดจาก [FilmCraft 0.17.1](https://github.com/storytold/filmcraft/releases/tag/v0.17.1) พร้อมคำแปลไทย 3,763 รายการ เป็นงานแปลอิสระ ไม่ใช่รุ่นที่รับรองโดยผู้พัฒนา ArtCraft ต้นฉบับ

## ดาวน์โหลด

- [ตัวติดตั้ง MSI](https://github.com/tapanapon-com/filmcraft-th/releases/download/v0.17.1-th.1/filmcraft-0.17.1-th.1-windows-x64.msi)
- [Portable ZIP](https://github.com/tapanapon-com/filmcraft-th/releases/download/v0.17.1-th.1/filmcraft-0.17.1-th.1-windows-x64-portable.zip)
- [SHA-256 checksums](https://github.com/tapanapon-com/filmcraft-th/releases/download/v0.17.1-th.1/SHA256SUMS-windows-x64.txt)

ไฟล์ใหม่อยู่ใน GitHub Releases ส่วนไฟล์ 0.17.0-th.1 ในโฟลเดอร์นี้เก็บเป็นประวัติ ไม่ใช่รุ่นล่าสุด

## ติดตั้งและเลือกภาษาไทย

1. บันทึกงานและปิด FilmCraft เดิมก่อนอัปเดต
2. ใช้ MSI แล้วทำตามตัวติดตั้ง หรือแตก ZIP ทั้งโฟลเดอร์แล้วเปิด `filmcraft.exe`
3. เลือก **Edit → Language → ไทย** หรือ **แก้ไข → ภาษา → ไทย**
4. Portable เก็บการตั้งค่าและข้อมูลในโฟลเดอร์ `data` ข้าง EXE เพราะมี `portable.txt` กำกับไว้ เก็บสำเนาข้อมูลเดิมก่อนแทนที่โฟลเดอร์

แพ็กเกจนี้ **ยังไม่มีลายเซ็น Authenticode** Windows จึงอาจแจ้ง SmartScreen ตรวจสอบแหล่งดาวน์โหลดและ SHA-256 ก่อนใช้งาน

```powershell
Get-FileHash .\filmcraft-0.17.1-th.1-windows-x64.msi -Algorithm SHA256
Get-FileHash .\filmcraft-0.17.1-th.1-windows-x64-portable.zip -Algorithm SHA256
```

## การตรวจสอบรุ่นนี้

รายละเอียด build และผลตรวจอยู่ใน [รายงาน Windows](validation-0.17.1-th.1.json) การตรวจ build, PE, CLI และไฟล์แพ็กเกจไม่เท่ากับการทดสอบตัดต่อผ่านหน้าจอครบทุกฟังก์ชัน ยังไม่ได้ทดสอบหน้าจอ Windows ของรุ่นใหม่นี้ด้วยมือ

## สร้างจากซอร์ส

ใช้ PowerShell 7, Rust MSVC toolchain, Windows SDK และ WiX v5 พร้อม UI extension ตาม [คู่มือ packaging](../packaging/windows/package.ps1) หากใช้ฟอนต์ craft-fonts ให้กำหนด `CRAFT_FONTS_DIR` ไปที่ checkout ของฟอนต์ด้วย

```powershell
python tools/thai/validate_catalog.py
rustup target add x86_64-pc-windows-msvc
$env:FILMCRAFT_VERSION = "0.17.1-th.1"
pwsh packaging/windows/package.ps1 -Arch x64
```

ได้ MSI และ Portable ZIP ใน `dist/release/` ใช้สคริปต์หลักข้างต้นสำหรับรุ่นใหม่ ส่วน `windows/package_windows.ps1` และ `tools/thai/package_windows.ps1` เป็นสคริปต์รุ่นเดิมที่ยังระบุ 0.17.0-th.1 ไว้

## English

**FilmCraft TH 0.17.1-th.1 for Windows x64** is an independent Thai localization of upstream FilmCraft 0.17.1. Download the MSI installer or portable ZIP above. Save work and quit the old app before updating. Extract the entire ZIP and run `filmcraft.exe`; portable settings live in its adjacent `data` folder. Select **Edit → Language → ไทย**.

These prerelease packages are **not Authenticode-signed** and may trigger SmartScreen. Verify the SHA-256 checksums. Build, architecture, CLI and archive checks do not establish complete GUI editing coverage; this version has not been manually GUI-tested on Windows.

Use the upstream `packaging/windows/package.ps1` command above for new builds. The app/UI identifies as **0.17.1-th.1** while engine/codec crates retain **0.17.1**, preserving upstream encoding behavior. Existing 0.17.0-th.1 files and scripts are retained as historical artifacts; see the [previous Windows documentation](README-0.17.0-th.1.md).
