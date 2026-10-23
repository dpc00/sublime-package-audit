Status: not filed (no repository or issue tracker: the package is listed only on packagecontrol.io, "Fuzzy Clock" 0.0.3, author Sarthak Upadhyay)

Claude reports:

The status bar text is wrong at minute 33 of every hour, and shows "Thirteen" after 12:33 and between 00:34 and 00:59 (Sublime Text 4, build 4215, package 0.0.3). Both come from `fuzzyTime` in `FuzzyClock.py`; I ran the function on sample times with the sublime modules stubbed.

1. `if minutes > 33: hour = next(hour)` advances the hour from minute 34, but `cond = ((minutes + 2) % 60) // 5` already switches to the "to" wording at minute 33. At 1:33 the result is `Twenty Five to One`; it should be `Twenty Five to Two`. Fix: `if minutes >= 33:`.

2. `def next(n): return 12 if n == 11 else n + 1` never wraps 12 back to 1. At 12:34, 0:34 and 12:50 the results are `Twenty Five to Thirteen`, `Twenty Five to Thirteen` and `Ten to Thirteen`. Fix: `return n % 12 + 1`.

Tested with both changes (function run directly): 1:33 gives `Twenty Five to Two`, 12:33 and 0:33 give `Twenty Five to One`, 12:34 gives `Twenty Five to One`, 12:50 gives `Ten to One`; 11:34 still gives `Twenty Five to Twelve` and 1:58 still gives `Two o'clock`. Not tried: the status bar itself after the change.

Also seen in the source, not tested: `'Fourty'` in `TENS_DICT` (cannot appear, since the minute words only go up to twenty-five); and `on_activated` starts a new 10-second timer chain each time a tab is activated while an older chain for that tab may still be pending, so chains can pile up.
