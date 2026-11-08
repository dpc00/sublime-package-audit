# Sweep 2026-11-10 — negative results, kept so the classes are not "found" twice

Run over all 4,769 releases in `channel_pc.json` (one release per package, platform any).
Total rows produced by the script: 94,880. **Confirmed defects: 0.** The file that held the
raw rows was replaced by this summary because two of its three classes turned out to be
supported behaviour, and a 85,911-row "finding" list is worse than no list.

## Class 1 — TextMate XML under a `.sublime-snippet` name (85,911 files, 785 packages)
**Not a defect.** Sublime Text 4 loads TextMate `<snippet>` XML under that extension.
Measured on 4215 / Windows, one snippet per case, each in a fresh buffer:
- unscoped TextMate XML, `tmtest` + Tab in a `.txt` buffer → expanded to `TM-EXPANDED`;
- the same form with `<scope>source.python</scope>`, `tm2test` in a `.py` buffer → expanded
  to `SCOPED-EXPANDED`, and in a `.txt` buffer it did not expand, so the TM `<scope>` element
  is honoured.

This was the premise of orgmir/mint-sublime-text#2, filed and withdrawn the same night. The
real defect in that package is #1: its syntax never loads.

## Class 2 — `push: scope:...` in a `.sublime-syntax` (47 files, 35 packages)
**Not a defect.** The construct appears in syntaxes that demonstrably work and are widely used
(Julia 1.0.11, Less 3.0.5, ElixirSyntax 4.1.0, Vue 5.0.3, Racket 2.3.0, PackageDev 3.7.2 among
them), which contradicts the assumption that a scope name is an invalid push target. Nothing
was filed. Mint Lang's `Sublime Text` load error stands on its own evidence — the dialog text
"Apparent recursion within a with_prototype action: 25000 context sanity limit hit" — and no
cause is claimed here.

## Class 3 — `.sublime-snippet` that is neither plist nor TextMate (8,844 files)
**Unexamined.** Kept only as a count; the first two classes were enough to show that the
detector needs a positive control before any row is called a defect.

## What a second attempt should do
Pick ~150 packages at random, load a snippet of each class in the rig and watch it expand or
not, and only then run the sweep. Two of the three classes written on 2026-11-10 were supported
behaviour; the detector was never validated against a control that Sublime demonstrably loads.
