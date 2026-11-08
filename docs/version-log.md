# FilmCraft TH — Version Log

## 0.18.0-th.1 — 7 November 2026

Based on the complete [upstream v0.18.0 release](https://github.com/storytold/filmcraft/releases/tag/v0.18.0), commit `015d5b3ea37e1202a529e6245d3cc021c8c16ffd`.

### การเปลี่ยนแปลงจากต้นฉบับ / Upstream changes

- กำหนด Usage_TopLevel ให้ composition ระดับบนของ AAF / Set the registered Usage_TopLevel on AAF top-level compositions: [upstream change](https://github.com/storytold/filmcraft/pull/3987).
- แก้เครื่องหมาย `<` ที่ไม่ปิดในคำบรรยาย TTML / Handle an unclosed `<` in TTML caption text: [upstream change](https://github.com/storytold/filmcraft/pull/4105).
- ตรวจช่วงข้อมูล sample ของ MP4 ก่อนจองหน่วยความจำบนเว็บ / Validate MP4 sample spans before web allocation: [upstream change](https://github.com/storytold/filmcraft/pull/4102).

The release tag was merged in full. These are selected upstream highlights, credited to their original contributors; they are not new features authored by the Thai project.

### การปรับรุ่นภาษาไทย / Thai edition changes

- เพิ่มคำแปล 23 รายการ รวม 3,786 รายการ / Added 23 translations, 3,786 catalog entries total.
- รวมข้อความเมนูใหม่ที่พบจาก compiled source report อีก 1 รายการ / Includes one additional dynamic menu label found by the compiled report.
- แพ็กเกจ Mac เพิ่ม `filmcraft-cli` ใน `.app` สำหรับ MCP / The Mac app bundle now includes `filmcraft-cli` for MCP.
- แยก DMG สำหรับ Apple Silicon และ MSI/portable ZIP สำหรับ Windows x64 / Separate Mac Apple Silicon and Windows x64 downloads.
- คงช่องทางตรวจอัปเดตรุ่นไทย ฟอนต์ ใบอนุญาต และเครดิตเดิม / Preserve the Thai update channel, fonts, licenses and attribution.

### ผลตรวจ / Validation

Complete source gate passed ([workflow](https://github.com/tapanapon-com/filmcraft-th/actions/runs/42388230021)); the compiled interface report has zero missing Thai strings. Catalog format, placeholders and reference-key coverage passed.

Mac: mounted-DMG integrity, strict ad-hoc signatures, arm64 GUI/CLI, Thai interface, native file save/reopen and real screenshots passed; MCP 17 tools. Windows x64: native build, CLI version, MCP 17 tools, installer policy, MSI/portable structure and SHA-256 checks passed ([workflow](https://github.com/tapanapon-com/filmcraft-th/actions/runs/42398974125)). Manual testing of every Windows GUI workflow is not claimed.

See [current validation](validation-0.18.0-th.1.json) for artifact hashes and exact build provenance.

Mac packages use ad-hoc signatures and are not notarized. Windows packages are unsigned. Native Windows CI checks do not claim manual testing of every Windows GUI workflow.

Thai updates are manual downloads from this repository’s Releases. The upstream automatic checker accepts stable versions only and excludes the `-th.1` release names.

## 0.17.1-th.1 — previous release

3,763 Thai entries and the upstream OGG packet-list memory-budget fix. Previous platform reports remain dated historical records; they do not establish validation of 0.18.0-th.1.
