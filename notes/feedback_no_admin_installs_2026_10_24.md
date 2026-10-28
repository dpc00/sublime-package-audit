---
name: no-admin-installs-2026-10-24
description: HIS ORDER - never install anything that needs administrator rights, even to test a package prerequisite
metadata:
  type: feedback
---

2026-10-24, M4Expand (row 781): the package needs `m4` on PATH, which is not on this machine. I downloaded the GnuWin32 M4 installer with winget and started an install that raised a Windows admin prompt. Donald stopped it twice: "i am not interested in that happening. Don't install anything that takes admin privileges."

**Why:** admin prompts and system installs on his laptop are unwelcome; this overrides the older "install free tools and test" rule ([[feedback_never_skip_for_missing_prereqs]]) whenever the tool needs admin.

**How to apply:** if a prerequisite can only be installed with admin rights (winget/msi/Inno setups that elevate), do not start the install. Test what can be tested without it (read the code, run the command and show the console error), log the package as "prerequisite needs admin, not installed", and move on. A user-level unzip into `tools` is still fine.

The downloaded installer folder `C:\Users\donal\tools\m4_test` was left in place because he declined the recycle call; ask before deleting it.
