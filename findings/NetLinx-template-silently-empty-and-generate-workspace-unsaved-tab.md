# NetLinx (amclain/sublime-netlinx 2.1.2): two defects reproduced by running the package

Found 2026-10-27 on Sublime Text 4 build 4215, Python 3.14 host, Windows, package installed from the Package Control picker. NOT filed: amclain asked us to open nothing more in his repositories (sublime-netlinx#10, 2026-10-27). Kept here for Donald to decide.

What was run: the package's own commands, through sublime-mcp. No NetLinx Studio, no `nlrc.exe`, no `netlinx-compile` (not installed), so nothing about building or uploading was tested.

## 1. New From Template does nothing when the tab already has text

`new_from_template.py`: `load_template` creates a new view with `self.view.window().new_file()` when the current view is not empty, then calls `v.insert(edit, 0, content)` with the `edit` of the ORIGINAL view.

Run: tab containing `hello`, command `netlinx_new_from_template_standard`. Result: a new tab with the NetLinx syntax set and size 0. No traceback in the console. In an empty tab the same command inserts the 2336-character template (works). The other three templates (Test Suite 1433, Include 2378, Overview 1599 characters) work in empty tabs.

Not checked: whether Sublime Text 3 accepts an edit token from another view (the README says the package is designed for ST3).

## 2. Generate .apw From workspace.config.yaml fails on an unsaved tab

`generate_workspace.py`: `path = self.view.file_name()` is `None` for an unsaved tab, and `os.path.dirname(path)` raises.

Run: unsaved tab, command `netlinx_generate_workspace`. Console: `TypeError: expected str, bytes or os.PathLike object, not NoneType` at `generate_workspace.py` line 6.

## Checked and fine

- Syntax scopes: `DEFINE_DEVICE`, `DEFINE_EVENT`, `DEFINE_START`, `PROGRAM_NAME` are `source.netlinx constant.other.netlinx`.
- Fix Indentation: tab-indented lines become 8-space indentation as documented, and the view's tab size (4) is put back.
- Launch NetLinx Diagnostics and Launch File Transfer: print "Could not find the ... executable." when AMX's programs are absent.

## What a real test would still need

AMX NetLinx Studio (free 80 MB download, installs under Program Files, so administrator rights), the Ruby gem `netlinx-compile`, and a NetLinx Master for file transfer. Plan agreed with Donald 2026-10-27: step 1 (this file) done; step 2 (download the zip into tools\ and inspect the installer, ask first) and step 3 (portable Ruby, then the Build command) wait for his go. Open question: whether the compiler can be extracted without administrator rights.
