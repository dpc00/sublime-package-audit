---
name: portable-channels-override-2026-10-31
description: empty Install Package picker on the portable was MY rig's `channels` override (v4 only, no package channel), not a public-channel fault; fixed by deleting the override
metadata:
  type: feedback
---

On 2026-10-31 (local 2026-10-30 evening) Donald said Install Package listed packages in his main ST and said "portable is misconfigured or bugged". He was right.

Cause: Package Control's default `channels` are two entries, `channel_v4.json` (libraries only, python 3.8 libraries) FOLLOWED BY `https://packagecontrol.io/channel_v3.json` (the packages). The portable's `Data\Packages\User\Package Control.sublime-settings` had `"channels": [ channel_v4 ]` only, so the packages channel was dropped and the picker said "There are no packages available for installation".

Fix: removed the `channels` block from that file (defaults apply). Install Package then listed 4728 packages. New baseline for that file: in_process_packages [], installed_packages three baseline entries, repositories [].

**Why:** I told Donald and wrote in the baton/README work that the public channel was empty and used release-zip installs for batches 199-211. The first claim was wrong for the packages channel: only the v4 file is (near) empty by design; my own override hid the v3 channel.

**How to apply:** installs go through the picker again (policy). When a picker is empty, compare the portable's User channels with the package default before blaming the public file. Release-zip results of batches 199-211 stay valid as tests but were not the user flow; note it in the log, do not redo them unasked.
