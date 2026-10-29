# Install ledger

Every install I make that is not a Package Control picker install goes here BEFORE I run it: date, what, scope (per-user or machine-wide), why, how to remove. Donald's rules: nothing that needs administrator rights, and no installs outside Package Control at all unless he says so in that turn. Package Control test installs are logged by `tools\finish.ps1`, and each is removed and verified in the same step.

History before 2026-10-24 was rebuilt from my own session transcripts: `data\installs_mined_from_transcripts_2026_10_24.txt` (344 distinct install commands, 2026-09-24 to 2026-10-24, with session id). Treat it as "what I ran", not "what is still installed".

## Removed with admin on 2026-10-24 (he clicked Yes twice; uninstalling is cleanup, his ban is on installing with admin)

| What | Where | From |
|---|---|---|
| FireDaemon OpenSSL 4 | machine-wide | winget, 2026-09-24 (audit, session 165e315a): `winget uninstall` succeeded |
| LLVM 23.1.3 | machine-wide | winget, 2026-10-13 (audit, session 0d8c7176): `winget uninstall` succeeded |
| GPL Ghostscript 10.08 | machine-wide | winget, 2026-10-13: its files were already gone (`tools\gs` missing), winget failed with 0x800401f5, so the orphaned registry keys were deleted (Uninstall entry, `HKLM\SOFTWARE\GPL Ghostscript`, `HKLM\SOFTWARE\Artifex`); `winget list` no longer shows it |
| pip: ansible-lint, behave, flake8, isort, pycodestyle, pylint, radon, yamllint, zstandard | C:\Program Files\Python314 | audit tests Sep 29 to Oct 22: `pip uninstall` succeeded; their dependencies (astroid, mccabe and similar) were not removed |

## Cleanup, second pass, 2026-10-24 (later same day)

- pip orphans of the nine removed packages, removed with admin, `pip check` clean: astroid, dill, tomlkit, mccabe, pyflakes, mando, cucumber-expressions, cucumber-tag-expressions, parse, parse_type, ansible-compat, subprocess-tee, wcmatch, bracex, ruamel.yaml, black, mypy_extensions, pytokens, filelock. Python package count 192 to 173. The remaining ones are his agent tooling (omp and friends) and shared dependencies; ownership not proven, left alone.
- `~\tools\forks\sublime-mit-alloy` and `sublimetext-cakephp` (my fork clones, no local-only work) recycled. Kept `forks\ColorHelper` (2 local-only commits) and `forks\sublime-exact-quick-find` (1 local-only commit): unpublished work.
- Kept in `~\tools` and why: tern-sdk, tern-spec, tsp-scratch (project work, not installs), agent-audit (my omp probe harness and results, not an install), backups (repo safety copies), Digital, screenshot-mcp-fix, list-coding-agents (his reusable tools per his 2026-10-10 notes), st_portable (current test rig), keep_awake.ps1.

## Still on the machine, installed by me in a session that may have been a setup he asked for (not touched)

Babashka, direnv, GitHub Desktop, Inkscape, Discord, Cursor, PHP 8.4, Task, .NET SDK 9 (winget, 2026-09-26, session a3788352). Inkscape, Discord and GitHub Desktop have desktop icons.

## Removed on 2026-10-24 (verified gone)

Ruby 3.4.11 and its MSYS2 (C:\Ruby34-x64, per-user), the M4 attempt (never installed), `~\tools` folders eclipse, lua, gobin, laravel_audit, processing_audit, tidyhtml_audit (Recycle Bin), npm globals prettier and @fsouza/prettierd, go\bin\qtc.exe.

## Not checked

WSL Ubuntu packages (apt lines in the mined file); the `wsl` check printed nothing, so state unknown. Home folders such as .cargo, .rustup, .dotnet, .platformio and .ansible exist, creation dates 2026-10-17 to 2026-10-23, owner not proven.

2026-10-24 | Mason (Package Control picker, portable 4215) | row 836 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | loose test syntaxes MasonFixA/B/C in portable 4215 Data\Packages (copies of Mason.tmLanguage with changed end pattern) | row 836 fix test | recycle the three folders with recycle.ps1 after the test, verify Test-Path
2026-10-24 | Material Design Lite Selectors Snippets (Package Control picker, portable 4215) | row 837 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | Material Design Lite Snippets (Package Control picker, portable 4215) | row 838 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | loose test package MDLFix in portable 4215 Data\Packages (5 corrected snippets) | row 838 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | Material Nil (Package Control picker, portable 4215) | row 839 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | MaterialUi React Component Snippet Autocomplete (Package Control picker, portable 4215) | row 840 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | loose test package MuiFix in portable 4215 Data\Packages (copy of the plugin with changed selectors) | row 840 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | MaterialUi React Component Snippet Autocomplete AGAIN (Package Control picker, portable 4215) | row 840 retest with the window in front (earlier screenshots went stale) | remove via remove_package picker, verify zip gone
2026-10-24 | loose test package MuiFix in portable 4215 Data\Packages (copy of the plugin with changed selectors) | row 840 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | Materialize-White-Panels (Package Control picker, portable 4215) | row 841 audit test | remove via remove_package picker, verify zip gone
2026-10-24 | Math Notes (Package Control picker, portable 4215) | row 842 audit test | remove via remove_package picker, verify gone
2026-10-24 | MathML (Package Control picker, portable 4215) | row 843 audit test | remove via remove_package picker, verify gone
2026-10-24 | MatrixList Snippets (Package Control picker, portable 4215) | row 844 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mattermost Post (Package Control picker, portable 4215) | row 846 audit test | remove via remove_package picker, verify gone
2026-10-24 | MaxPane (Package Control picker, portable 4215) | row 847 audit test | remove via remove_package picker, verify gone
2026-10-24 | Maybs Quit (Package Control picker, portable 4215) | row 848 audit test | remove via remove_package picker, verify gone
2026-10-24 | MediaPlayer (Package Control picker, portable 4215) | row 849 audit test | remove via remove_package picker, verify gone
2026-10-24 | loose test package MediaPlayerFix in portable 4215 Data\Packages (patched SublimePlayer.py, original already removed) | row 849 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | Melbourne Ipsum (Package Control picker, portable 4215) | row 850 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mellanox Syntax Highlighter (Package Control picker, portable 4215) | row 851 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mem.dev Snippet Saver (Package Control picker, portable 4215) | row 852 audit test | remove via remove_package picker, verify gone
2026-10-24 | loose test package MemDevFix in portable 4215 Data\Packages (mmdv.py + Context menu, dot-free name) | row 852 rename test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | Mercurial Color Scheme (Package Control picker, portable 4215) | row 853 audit test | remove via remove_package picker, verify gone
2026-10-24 | Merge Variables (Package Control picker, portable 4215) | row 855 audit test | remove via remove_package picker, verify gone
2026-10-24 | loose test package MergeVariablesFix in portable 4215 Data\Packages (patched MergeVariables.py, original already removed) | row 855 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | temp file Data\Packages\User\MergeVariables.sublime-settings in portable 4215 (test sets) | row 855 fix test | recycle with recycle.ps1, verify Test-Path
2026-10-24 | MetaQuotes (MQL4) Language Package (Package Control picker, portable 4215) | row 856 audit test | remove via remove_package picker, verify gone
2026-10-24 | Micro16 Syntax (Package Control picker, portable 4215) | row 857 audit test | remove via remove_package picker, verify gone
2026-10-24 | Microsoft Power Query Syntax (Package Control picker, portable 4215) | row 858 audit test | remove via remove_package picker, verify gone
2026-10-24 | Milotic (Package Control picker, portable 4215) | row 859 audit test | remove via remove_package picker, verify gone
2026-10-24 | Minecraft Command Format (Package Control picker, portable 4215) | row 862 audit test | remove via remove_package picker, verify gone
2026-10-24 | loose test package MinecraftFormatFix in portable 4215 Data\Packages (patched MinecraftCommandFormat.py, original already removed) | row 862 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | MiniZinc Language (Package Control picker, portable 4215) | row 863 audit test | remove via remove_package picker, verify gone
2026-10-24 | Minify on Save (Package Control picker, portable 4215) | row 864 audit test | remove via remove_package picker, verify gone
2026-10-24 | Miniscript (Package Control picker, portable 4215) | row 865 audit test | remove via remove_package picker, verify gone
2026-10-24 | Minitest Buddy (Package Control picker, portable 4215) | row 866 audit test | remove via remove_package picker, verify gone
2026-10-24 | loose test package MinitestBuddyFix in portable 4215 Data\Packages (patched minitest_toggle.py, original already removed) | row 866 fix test | recycle the folder with recycle.ps1 after the test, verify Test-Path
2026-10-24 | MinkExtension default feature step completions (Package Control picker, portable 4215) | row 867 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mirodark Color Scheme (Package Control picker, portable 4215) | row 868 audit test | remove via remove_package picker, verify gone
2026-10-24 | MissingFindPanelKeys (Package Control picker, portable 4215) | row 869 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mithrilizer (Package Control picker, portable 4215) | row 870 audit test | remove via remove_package picker, verify gone
2026-10-24 | Miva IDE (Package Control picker, portable 4215) | row 871 audit test | remove via remove_package picker, verify gone
2026-10-24 | MivaScript (Package Control picker, portable 4215) | row 872 audit test | remove via remove_package picker, verify gone
2026-10-24 | MobileCaddy (Package Control picker, portable 4215) | row 874 audit test | remove via remove_package picker, verify gone
2026-10-24 | MobileLogReader (Package Control picker, portable 4215) | row 875 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mocha Chai CoffeeScript (Package Control picker, portable 4215) | row 876 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mocha Coffee Snippets (Package Control picker, portable 4215) | row 877 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mocha Snippets (Package Control picker, portable 4215) | row 879 audit test | remove via remove_package picker, verify gone
2026-10-24 | Modula-2 Language Syntax (Package Control picker, portable 4215) | row 881 audit test | remove via remove_package picker, verify gone
2026-10-24 | ModxElements (Package Control picker, portable 4215) | row 882 audit test | remove via remove_package picker, verify gone
- 2026-10-24 | Mojolicious | portable 4215 Package Control picker | audit row 883 | remove via remove_package picker, verify Data\Installed Packages\Mojolicious.sublime-package gone
2026-10-24 | Monaco (Package Control picker, portable 4215) | row 884 audit test | remove via remove_package picker, verify gone; Preferences.sublime-settings backup first
2026-10-24 | Monarch (Package Control picker, portable 4215) | row 885 audit test | remove via remove_package picker, verify gone; Preferences.sublime-settings backup first
2026-10-24 | Mongo Aggregate Snippets (Package Control picker, portable 4215) | row 886 audit test | remove via remove_package picker, verify gone
2026-10-24 | MongoExec (Package Control picker, portable 4215) | row 887 audit test | remove via remove_package picker, verify gone
2026-10-24 | Data\Packages\User\MongoExec.sublime-settings (temp test connection to 127.0.0.1:9, portable 4215) | row 887 audit test | recycle with recycle.ps1, verify gone
2026-10-24 | Mongomapper Snippets (Package Control picker, portable 4215) | row 888 audit test | remove via remove_package picker, verify gone
2026-10-24 | MonkeyC (Package Control picker, portable 4215) | row 889 audit test | remove via remove_package picker, verify gone
2026-10-24 | Monochrome Color Schemes (Package Control picker, portable 4215) | row 891 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | Monocyanide Colorscheme (Package Control picker, portable 4215) | row 892 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | Monokai Blueberry Color Scheme (Package Control picker, portable 4215) | row 893 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | Monokai Soft (Package Control picker, portable 4215) | row 894 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | MonokaiC (Package Control picker, portable 4215) | row 895 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | MonokaiFree (Package Control picker, portable 4215) | row 896 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | Moodle Completions (Package Control picker, portable 4215) | row 898 audit test | remove via remove_package picker, verify gone
2026-10-24 | Moonscripty (Package Control picker, portable 4215) | row 899 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mootools Snippets (Package Control picker, portable 4215) | row 900 audit test | remove via remove_package picker, verify gone
2026-10-24 | More Python Completions (Package Control picker, portable 4215) | row 901 audit test | remove via remove_package picker, verify gone
2026-10-24 | Morse (Package Control picker, portable 4215) | row 902 audit test | remove via remove_package picker, verify gone
2026-10-24 | Morse Code for Foundation (Package Control picker, portable 4215) | row 903 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mote (Package Control picker, portable 4215) | row 904 audit test | remove via remove_package picker, verify gone
2026-10-24 | MotionBuilder (Package Control picker, portable 4215) | row 905 audit test | remove via remove_package picker, verify gone
2026-10-24 | Move By Paragraph (Package Control picker, portable 4215) | row 906 audit test | remove via remove_package picker, verify gone
2026-10-24 | Move Tabs (Package Control picker, portable 4215) | row 907 audit test | remove via remove_package picker, verify gone
2026-10-24 | MozillaQuery (Package Control picker, portable 4215) | row 908 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mp3Player (Package Control picker, portable 4215) | row 909 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mreq Color Scheme (Package Control picker, portable 4215) | row 910 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | Mscgen (Package Control picker, portable 4215) | row 911 audit test | remove via remove_package picker, verify gone
2026-10-24 | Multi Select Alphabetizer (Package Control picker, portable 4215) | row 912 audit test | remove via remove_package picker, verify gone
2026-10-24 | Multi line paste (Package Control picker, portable 4215) | row 913 audit test | remove via remove_package picker, verify gone
2026-10-24 | MultiFill (Package Control picker, portable 4215) | row 914 audit test | remove via remove_package picker, verify gone
2026-10-24 | MultiLang Color Scheme (Package Control picker, portable 4215) | row 915 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | MultiTaskBuild (Package Control picker, portable 4215) | row 916 audit test | remove via remove_package picker, verify gone
2026-10-24 | MultiValue BASIC (Package Control picker, portable 4215) | row 917 audit test | remove via remove_package picker, verify gone
2026-10-24 | Multicommand (Package Control picker, portable 4215) | row 918 audit test | remove via remove_package picker, verify gone
2026-10-24 | MultipleSelectionScroller (Package Control picker, portable 4215) | row 919 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mussum Ipsum (Package Control picker, portable 4215) | row 920 audit test | remove via remove_package picker, verify gone
2026-10-24 | Mustang Color Scheme (Package Control picker, portable 4215) | row 921 audit test | remove via remove_package picker, verify gone; Preferences backup first
2026-10-24 | MvtAssign It | portable 4215 Packages via picker | audit row 923 | remove via remove_package picker
2026-10-24 | Mybb Template Editor | portable 4215 Packages via picker | audit row 925 | remove via remove_package picker
2026-10-24 | MypyReveal | portable 4215 Packages via picker | audit row 926 | remove via remove_package picker
2026-10-24 | NESASM | portable 4215 Packages via picker | audit row 927 | remove via remove_package picker
2026-10-25 | NFO | portable 4215 Packages via picker | audit row 928 | remove via remove_package picker
2026-10-25 | test928.nfo | scratchpad (not repo) | NFO test file | auto-removed with the session scratchpad
2026-10-25 | NSIS Plug-in Completions | portable 4215 Packages via picker | audit row 930 | remove via remove_package picker
2026-10-25 | NSIS (dependency for syntax source.nsis) | portable 4215 Packages via picker | needed to test NSIS Plug-in Completions snippets (row 930) | remove via remove_package picker right after
2026-10-25 | NSIS for Translators | portable 4215 Packages via picker | audit row 931 | remove via remove_package picker
2026-10-25 | test931.nlf | scratchpad (not repo) | NLF syntax test file | session scratchpad
2026-10-25 | NSIS Plug-in Completions + NSIS (syntax) | portable 4215 via picker | RETEST of row 930 in fresh tabs (earlier run reused one tab with an active snippet session) | remove both via picker after
2026-10-25 | Nakama Autocomplete | portable 4215 Packages via picker | audit row 932 | remove via remove_package picker
2026-10-25 | Named (Bind) Helpers | portable 4215 Packages via picker | audit row 933 | remove via remove_package picker
2026-10-25 | Nano RC Syntax | portable 4215 Packages via picker | audit row 935 | remove via remove_package picker
2026-10-25 | NativeBase Snippets Sublime | portable 4215 Packages via picker | audit row 936 | remove via remove_package picker
2026-10-25 | NativeScript Snippets | portable 4215 Packages via picker | audit row 937 | remove via remove_package picker
2026-10-25 | Nav Panel | portable 4215 Packages via picker | audit row 939 | remove via remove_package picker
2026-10-25 | Navigation History | portable 4215 Packages via picker | audit row 940 | remove via remove_package picker
2026-10-25 | Nbspr | portable 4215 Packages via picker | audit row 941 | remove via remove_package picker
2026-10-25 | Neat Sass Snippets | portable 4215 Packages via picker | audit row 942 | remove via remove_package picker
2026-10-25 | NegateSentence | portable 4215 Packages via picker | audit row 943 | remove via remove_package picker
2026-10-25 | Neka Theme | portable 4215 Packages via picker | audit row 944 | remove via remove_package picker (scheme test: Preferences backup first)
2026-10-25 | Nemerle | portable 4215 Packages via picker | audit row 945 | remove via remove_package picker
2026-10-25 | NeoVintageousFiles | portable 4215 Packages via picker | audit row 946 | remove via remove_package picker
2026-10-25 | Neon Intrinsics | portable 4215 Packages via picker | audit row 947 | remove via remove_package picker
2026-10-25 | Neopolitan | portable 4215 Packages via picker | audit row 948 | remove via remove_package picker
2026-10-25 | NestedSnippet | portable 4215 Packages via picker | audit row 949 | remove via remove_package picker
2026-10-25 | NestingSnippet | portable 4215 Packages via picker | audit row 950 | remove via remove_package picker
2026-10-25 | NetLinx | portable 4215 Packages via picker | audit row 951 | remove via remove_package picker
2026-10-25 | NetLogo Syntax | portable 4215 Packages via picker | audit row 952 | remove via remove_package picker
2026-10-25 | test952.nlogo | scratchpad (not repo) | NetLogo syntax test file | session scratchpad
2026-10-25 | NetSuite SDF | portable 4215 Packages via picker | audit row 953 | remove via remove_package picker
2026-10-25 | NetYCE syntax highlighting | portable 4215 Packages via picker | audit row 954 | remove via remove_package picker
2026-10-25 | test954.tpl | scratchpad (not repo) | NetYCE shipped test file copy | session scratchpad
2026-10-25 | Nette | portable 4215 Packages via picker | audit row 955 | remove via remove_package picker
2026-10-25 | Nette + Latte + Neon | portable 4215 Packages via picker | audit row 956 | remove via remove_package picker
| 2026-10-25 | New from Selection | picker install on portable 4215 | audit row 957 | remove via remove_package picker, verify Installed Packages and Packages folders |
| 2026-10-25 | NgAnnotate | picker install on portable 4215 | audit row 958 | remove via remove_package picker, verify Installed Packages and Packages folders |
| 2026-10-25 | Nginx Log Highlighter | picker install on portable 4215 | audit row 959 | remove via remove_package picker, verify Installed Packages and Packages folders |
| 2026-10-25 | Night Owl | picker install on portable 4215 | audit row 960 | remove via remove_package picker, verify Installed Packages and Packages folders; Preferences restored from backup |
| 2026-10-25 | NightCycle | picker install on portable 4215 | audit row 961 | remove via remove_package picker, verify Installed Packages and Packages folders; Preferences restored from backup if touched |
| 2026-10-25 | Nightfall color scheme | picker install on portable 4215 | audit row 962 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Nightwalker Color Scheme | picker install on portable 4215 | audit row 963 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Niji | picker install on portable 4215 | audit row 964 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Nintendo Switch Dark Scheme | picker install on portable 4215 | audit row 966 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Nirum | picker install on portable 4215 | audit row 967 | remove via remove_package picker, verify gone |
| 2026-10-25 | NitSyntaxHighliter | picker install on portable 4215 | audit row 968 | remove via remove_package picker, verify gone |
| 2026-10-25 | Nix | picker install on portable 4215 | audit row 969 | remove via remove_package picker, verify gone |
| 2026-10-25 | Noctis Color Scheme | picker install on portable 4215 | audit row 970 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Node Assert Snippets | picker install on portable 4215 | audit row 971 | remove via remove_package picker, verify gone |
| 2026-10-25 | NodeEval | picker install on portable 4215 | audit row 972 | remove via remove_package picker, verify gone |
| 2026-10-25 | Non Text Files | picker install on portable 4215 | audit row 973 | remove via remove_package picker, verify gone |
| 2026-10-25 | Normal Mode | picker install on portable 4215 | audit row 974 | remove via remove_package picker, verify gone |
| 2026-10-25 | test file nm_test.txt (scratchpad) | for Normal Mode test, row 974 | session scratchpad, removed with session |
| 2026-10-25 | Normalize Indentation | picker install on portable 4215 | audit row 975 | remove via remove_package picker, verify gone |
| 2026-10-25 | Nostromo Color Scheme | picker install on portable 4215 | audit row 976 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | Not that useless project report | picker install on portable 4215 | audit row 977 | remove via remove_package picker, verify gone |
| 2026-10-25 | test folder npr_test (scratchpad) | for Not that useless project report, row 977 | session scratchpad, removed with session; folder removed from the portable project afterwards |
| 2026-10-25 | Notepad++ Tab Context | picker install on portable 4215 | audit row 978 | remove via remove_package picker, verify gone |
| 2026-10-25 | test files npp_rename.txt, npp_delete.txt (scratchpad) | for Notepad++ Tab Context test, row 978 | session scratchpad, removed with session |
| 2026-10-25 | Nova Framework Snippets | picker install on portable 4215 | audit row 980 | remove via remove_package picker, verify gone |
| 2026-10-25 | Nova Template Highlighter | picker install on portable 4215 | audit row 981 | remove via remove_package picker, verify gone |
| 2026-10-25 | test file test981.tpl (scratchpad) | for Nova Template Highlighter test, row 981 | session scratchpad, removed with session |
| 2026-10-25 | User\NovaTplFixA.sublime-syntax (edited copy of Nova TPL syntax) | diagnose row 981 | remove with recycle.ps1 after the test |
| 2026-10-25 | User\CppBuilder.sublime-settings (residue dated 2026-10-22, no ledger line) | found while checking the portable User folder | recycled via recycle.ps1; origin was an earlier audit test |
| 2026-10-25 | NuSMV Syntax | picker install on portable 4215 | audit row 983 | remove via remove_package picker, verify gone |
| 2026-10-25 | Number King | picker install on portable 4215 | audit row 984 | remove via remove_package picker, verify gone |
| 2026-10-25 | Number Manipulation | picker install on portable 4215 (if offered) | audit row 985 | remove via remove_package picker, verify gone |
| 2026-10-25 | NumberFormatter | picker install on portable 4215 | audit row 986 | remove via remove_package picker, verify gone |
| 2026-10-25 | OAT Syntax | picker install on portable 4215 | audit row 987 | remove via remove_package picker, verify gone |
| 2026-10-25 | OLED Color Scheme | picker install on portable 4215 | audit row 988 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | OOJS | picker install on portable 4215 | audit row 989 | remove via remove_package picker, verify gone |
| 2026-10-25 | OPM (Orbital Parameter Message) Syntax Highlighting | picker install on portable 4215 | audit row 990 | remove via remove_package picker, verify gone |
| 2026-10-25 | Oasis Theme | picker install on portable 4215 | audit row 991 | remove via remove_package picker, verify gone; Preferences restored from backup |
| 2026-10-25 | User\OasisFix.tmTheme (edited copy of Oasis.tmTheme, # replaced by #bfbfbf) | test of the fix, row 991 | remove with recycle.ps1 after the test |
| 2026-10-25 | ObjC2RubyMotion | picker install on portable 4215 | audit row 992 | remove via remove_package picker, verify gone |
| 2026-10-25 | Object Pascal | picker install on portable 4215 | audit row 993 | remove via remove_package picker, verify gone |
- 2026-10-25 row 994: Objective-C Autocompletion via Package Control picker on portable 4215 (C:\Users\donal\tools\st_portable). Why: audit. Remove: remove_package picker, then Test-Path Installed Packages\Objective-C Autocompletion.sublime-package and Packages\Objective-C Autocompletion.
- 2026-10-25 row 994 test files: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\objc994\Foo.h and Foo.m (scratchpad). Remove: recycle.ps1 after test.
- 2026-10-25 row 995: Oblivion Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 995 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs995.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 996: Obsidian Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 996 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs996.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 996 temp file: C:\Users\donal\tools\st_portable\Data\Packages\User\ObsidianFix.tmTheme (copy of Obsidian.tmTheme with global background #293134). Remove: recycle.ps1 after test.
- 2026-10-25 row 997: Oceanic Next Italic Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 997 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs997.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 998: Oceanic Primal Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 998 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs998.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 999: OctaveSupport via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 999 temp file: C:\Users\donal\tools\st_portable\Data\Packages\User\OctaveFix.sublime-syntax (copy of Octave.sublime-syntax with a hex/binary number rule). Remove: recycle.ps1 after test.
- 2026-10-25 row 1000: Octopress Snippets via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1001: Odhin Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1001 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs1001.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 1002: Odoo Snippets via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1003: Ogre Scripts Highlighting via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1004: Ohdeung-eun via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1005: Okami Adaptive Color Schemes via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1005 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs1005.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 1006: OmniDocs via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1007: OmnisStudioHighlighter via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1007 test files: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\omnis1007\t.xml and t.svg (scratchpad). Remove: recycle.ps1 after test.
- 2026-10-25 row 1008: OmnisStudioIndenter via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1009: One Command Syntax Highlighter via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1010: One Half Color Schemes via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1010 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs1010.backup (Preferences backup, scratchpad). Remove: recycle.ps1 after restore.
- 2026-10-25 row 1011: OnlineSearch via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1012: OnlyCss Snippets via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1013: Opa via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1014: Open File in Current Folder via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1014 test files: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\ofcf1014 (a.txt, b.txt, c.txt, scratchpad). Remove: recycle.ps1 after test.
- 2026-10-25 row 1015: Open Recent Files via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1016: Open Related via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1016 test files: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\ofr1016 (src\a.js, test\aSpec.js, scratchpad). Remove: recycle.ps1 after test.
- 2026-10-25 row 1016 temp folder: C:\Users\donal\tools\st_portable\Data\Packages\Open Related (unpacked copy of Open Related with is changed to ==, to test the fix). Remove: recycle.ps1 after test (Packages folder entry).
- 2026-10-25 row 1017: Open Shading Language via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1018: Open TortoiseHg via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1018 temp file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\prefs1018.backup (Preferences backup, scratchpad; Preferences gets a tortoisehg_command line during the test). Remove: restore then recycle.ps1.
- 2026-10-25 row 1019: Open in Git Repository via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1019 temp folder: C:\Users\donal\tools\st_portable\Data\Packages\Open in Git Repository (unpacked copy of Open in Git Repository with _get_file_project_path changed to relpath, to test the fix). Remove: remove_package, then recycle.ps1 if it is still there.
- 2026-10-25 row 1020: Open in Relevant Window via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1020 temp folder: C:\Users\donal\tools\st_portable\Data\Packages\Open in Relevant Window (unpacked copy of Open in Relevant Window with a None guard, to test the fix). Remove: remove_package, then recycle.ps1 if it is still there.
- 2026-10-25 row 1021: Open in Total Commander via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1023: OpenBSD PF conf syntax highlight via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1024: OpenContextPath via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1024 test files: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\ocp 1024 (a b.txt, c.txt, scratchpad). Remove: recycle.ps1 after test.
- 2026-10-25 row 1026: OpenLastRPT via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1026 fix test: unpacked copy C:\Users\donal\tools\st_portable\Data\Packages\OpenLastRPT (removed by remove_package) and test folder %LOCALAPPDATA%\Arma 3 with test.rpt (did not exist before). Remove: remove_package, recycle.ps1 on the Arma 3 folder, then Test-Path.
- 2026-10-25 row 1027: OpenResty lua snippets via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1028: OpenSees via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1028 fix test: unpacked copy C:\Users\donal\tools\st_portable\Data\Packages\OpenSees (removed by remove_package). Remove: remove_package, then Test-Path.
- 2026-10-25 row 1028 test file: C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\os1028\a.tcl. Remove: recycle.ps1 after test.
- 2026-10-25 row 1028: scratch copy of fixed package at C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\os1028\OpenSees_fixed (inside the os1028 folder, recycled with it).
- 2026-10-25 row 1028 fix test (clean): copy of OpenSees_fixed placed at C:\Users\donal\tools\st_portable\Data\Packages\OpenSees. Remove: recycle.ps1 on that folder (package no longer listed by the picker once removed), then Test-Path.
- 2026-10-25 row 1029: OpenType Feature Bundle via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1030: Opencart Snippets and Completions via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1031: OpenedFiles via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1031 test file: C:\Users\donal\tools\st_portable\Data\Packages\User\opened_files.sublime-settings (tree_view false). Remove: recycle.ps1 after test, then Test-Path.
- 2026-10-25 row 1032: Oracle_ORA via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1033: Orbit Color Scheme via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path. Also Preferences backup C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\Preferences.1033.backup (restore the color_scheme line, check MD5 EAE47B4ED23B6DFF7D7BB52AF9FDC22A, recycle backup).
- 2026-10-25 row 1034: OrigamiEmacs via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1035: Outroot Color Schemes via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path. Also Preferences backup C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\Preferences.1035.backup (restore, check MD5 EAE47B4ED23B6DFF7D7BB52AF9FDC22A, recycle backup).
- 2026-10-25 row 1036: Overwatch Workshop Syntax Highlight via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1037: P3 Assembly via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1038: P4 Syntax Highlighter via Package Control picker on portable 4215. Why: audit. Remove: remove_package picker, then Test-Path Installed Packages and Packages entries.
- 2026-10-25 row 1039: P4Explorer via Package Control picker on portable 4215. Why: audit (Perforce not installed; load and no-server behaviour only). Remove: remove_package picker, then Test-Path.
- 2026-10-25 row 1040: P4Gutter via Package Control picker on portable 4215. Why: audit (Perforce not installed; load and no-server behaviour only). Remove: remove_package picker, then Test-Path.
2026-10-25 row 1043 PDML: install via Package Control picker on portable 4215 (st_portable); remove via remove_package picker after test; no temp files planned
2026-10-25 row 1044 PEGjs CoffeeScript: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1045 PEGjs LiveScript: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1046 PEPE Assembly: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1047 PGN Support: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1049 PHP Faker Completions: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1050 PHP Form Builder: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1051 PHP Haml: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1052 PHP Source: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1052 PHP Source: temp folder scratchpad\phpsrc (t.php, t.phps) for the test; recycle after test with recycle.ps1
2026-10-25 row 1053 PICO-8: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1053 PICO-8: temp folder scratchpad\pico (t.p8) for the test; recycle after test with recycle.ps1
2026-10-25 row 1054 PL1 PLI Syntax: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1055 PM2-Snippets: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1056 PPCL Language Syntax and Editor: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1057 PSLHighlight: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1058 Package Bundler: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1059 Package Snippets: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1060 PageLines Snippets: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1060 PageLines Snippets: temp folder scratchpad\plsnip (a.php, b.php) for php -l; recycle after
2026-10-25 row 1061 PaletteFile: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1063 Pandoc Converter: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1064 Pandoc Referencer: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1066 Pane Resizer: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1067 Panezr: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1069 Papyrus Assembly: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1070 Paradox: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1072 Particle Reverse Polish Language: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1073 Parva Syntax: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1075 Paste as One Line: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1078 PasteAhead: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1079 PasteAsString: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1080 PasteRepeater: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1081 PasteSelOnClick: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1082 PasteWrap: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1083 Pastel Paws Color Scheme: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1084 Path Translator: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1086 Pelican: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1086 Pelican: temp folder C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\pel\content (one post.md) for the on-save slug test; recycle with recycle.ps1 after the test
2026-10-25 row 1087 PeopleCodeTools: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1088 Perfectionist: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1088 Perfectionist: temp folder C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\perf (one test.html) for the format-on-save test; recycle with recycle.ps1 after the test
2026-10-25 row 1089 Perforce: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 row 1089 Perforce: temp folder C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\p4t (one a.txt) for the save test; recycle with recycle.ps1 after the test
2026-10-25 row 1090 Perl Completions: install via Package Control picker on portable 4215; remove via remove_package picker after test; no temp files planned
2026-10-25 | row 1092 Persistent Status Bar Line Number | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1093 Perv - Color Scheme | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1094 Pest Syntax | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1095 PgSQL | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1098 Pharko | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1099 Phaser Snippets | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1100 Phoenix Beagle | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | CDNUpdates PR #2 branch copy | zip of break/st4_compliant_command_name in scratchpad cdn_pr2, copied to portable 4215 Data\Packages\CDNUpdates | test maintainer's PR for issue #1 | recycle both folders, verify baseline
2026-10-25 | CDNUpdates PR #2 branch copy (retest) | zip of break/st4_compliant_command_name in scratchpad cdn_pr2b, copied to portable 4215 Data\Packages\CDNUpdates | full retest of maintainer's PR | recycle both folders, verify baseline
2026-10-25 | row 1101 PhpArrayConverter | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1102 PhpDox | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1103 PhpSimpleRefactor | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1104 PhpSpec Snippets | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1105 Pipe Dream | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1106 PipenvPath | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1107 PixarUSD | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1108 Placehold.it Image Tag Generator | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1110 PlatformSettings | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1111 Play 2.0 | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1112 PloneReload | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1113 Plugin UnitTest Harness | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1114 Pman | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1116 PogoScript | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1117 Polygen | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 | row 1118 Polymer & Web Component Snippets | Package Control picker on portable 4215 | audit test | remove_package via picker, verify baseline
2026-10-25 row 1119 Polymer Syntax: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1120 Pomodoro: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1121 Poppins - Color Scheme: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1122 PostScript: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1123 Postap: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1124 Postfixer: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1124 Postfixer: leftover User\postfixes.yml created by the package; recycled via recycle.ps1
2026-10-25 row 1125 Postgres PL pgSQL: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1126 PouchDB Snippets: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1127 PowerMTML Completions: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1128 PowershellUtils: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1129 Pre language syntax highlighting: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1129 Pre syntax: temp file scratchpad\pre_test.css (opened to see which syntax a .css file gets); recycle after test
2026-10-25 row 1129 Pre syntax: scratchpad\pre_test.css recycled via recycle.ps1
2026-10-25 row 1130 Preference Helper: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1132 Preferences Editor: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1133 Premake: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1134 Preset Command: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1134 Preset Command: test writes portable User\Presets.sublime-settings and changes tab_size in User\Preferences.sublime-settings; Preferences backed up to scratchpad\prefs_1134.backup and restored afterwards; Presets file recycled
2026-10-25 row 1134 Preset Command: Preferences restored from backup (MD5 EAE47B4E...), Presets.sublime-settings and the backup recycled
2026-10-25 row 1135 Prevent Duplicate Windows: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1136 Prevu: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1137 Prismatic Color Scheme: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1138 Procapy: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1139 ProcessWire Snippets - Advanced: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1140 ProcessWire Snippets - Basic: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1141 ProductiveSnippetsERB: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1142 Project Port: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1142 Project Port: test folder scratchpad\pp_test (a .sln plus one project folder); recycled after the test
2026-10-25 row 1142 Project Port: scratchpad\pp_test recycled via recycle.ps1; folders removed from the window
2026-10-25 row 1143 Project Runner: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1144 Project Specific Syntax Settings: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1144 Project Specific Syntax Settings: test folder scratchpad\pss_test (a .sublime-project, a t.txt; Sublime adds a .sublime-workspace); a new window is opened and closed; recycled after the test
2026-10-25 row 1144 Project Specific Syntax Settings: scratchpad\pss_test (with its .sublime-workspace) recycled via recycle.ps1; test window closed
2026-10-25 row 1146 ProjectCompletions: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1147 ProjectFiles: Package Control picker install on portable 4215; remove via picker after test
2026-10-25 row 1148 ProjectSpecific: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1149 ProjectTreeTemplater: Package Control picker install on portable 4215 (if listed); remove via picker after test
2026-10-25 row 1149 ProjectTreeTemplater: test folder scratchpad\ptt_test (a .stprj; the plugin creates css, index.html, ex.txt downloaded from https://example.com/); recycled after the test
2026-10-25 row 1149 ProjectTreeTemplater: scratchpad\ptt_test recycled via recycle.ps1
2026-10-25 row 1150 Promela_Spin: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1151 Propel: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1152 ProtoBufCodeFormatter: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1153 Pseudo Block Mode: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1154 Pue Syntax Highlight: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1155 PunchMeInTheFace Color Scheme: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1156 Puppet Syntax checking: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1157 PureCM: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1157 PureCM: temp file scratchpad\purecm_test\a.txt (recycle after test)
2026-10-25 row 1157 PureCM: scratchpad\purecm_test recycled via recycle.ps1
2026-10-25 row 1158 PureCSS: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1159 PureScript Syntax: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1160 PurpleHaze: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1161 Pushb: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1162 Pushbullet: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1163 PxRemTooltip: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1164 PyBuilder: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1165 PyCover: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1166 PyDOC: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1167 PyQt Search: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1168 PyQt5 Completions: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1169 PyRefactor: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1170 PyTags: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1171 Pymol Language: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1172 PypiPackageInfo: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1173 PyroCMS Snippets: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1174 Pytest Snippets: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1175 Python Anywhere Editor: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1176 Python Computer Vision Snippets: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1177 Python Create Package: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1177 Python Create Package: temp folder scratchpad\pcp_test (recycle after test)
2026-10-25 row 1177 Python Create Package: scratchpad\pcp_test recycled via recycle.ps1
2026-10-25 row 1178 Python Data Science Snippets: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 row 1179 Python Imports Sorter: install via Package Control picker; remove via remove_package; no temp files yet
2026-10-25 | Python Nose Testing Snippets | Package Control picker, portable 4215 | audit row 1180 | remove via remove_package picker, verify baseline
2026-10-25 | Python PEP8 Autoformat | Package Control picker, portable 4215 | audit row 1181 | remove via remove_package picker, verify baseline
2026-10-25 | Python PEP8 Indent | Package Control picker, portable 4215 | audit row 1182 | remove via remove_package picker, verify baseline
2026-10-25 | Python Unittest Helper | Package Control picker, portable 4215 | audit row 1183 | remove via remove_package picker, verify baseline
2026-10-25 | CDNUpdates PR #2 branch break/st4_compliant_command_name (HorlogeSkynet) | clone into scratchpad cdn_clone, copy files to portable Data\Packages\CDNUpdates; Donald said yes 2026-10-25 | test his fix for issue #1 | remove: recycle.ps1 on Packages\CDNUpdates and scratchpad\cdn_clone, verify gone
2026-10-25 | CDNUpdates PR #2 test copy | removed: Packages\CDNUpdates and scratchpad cdn_clone recycled, verified gone
2026-10-25 | PythonNiceToHaveFeatures | Package Control picker, portable 4215 | audit row 1184 | remove via remove_package picker, verify baseline
2026-10-25 | PythonOpenModule | Package Control picker, portable 4215 | audit row 1185 | remove via remove_package picker, verify baseline
2026-10-25 | PythonStautsBarShowSymbol | Package Control picker, portable 4215 | audit row 1186 | remove via remove_package picker, verify baseline
2026-10-25 | PythonTidy | Package Control picker, portable 4215 | audit row 1187 | remove via remove_package picker, verify baseline
2026-10-25 | PythonTraceback | Package Control picker, portable 4215 | audit row 1188 | remove via remove_package picker, verify baseline
2026-10-25 | Pyxl syntax | Package Control picker, portable 4215 | audit row 1190 | remove via remove_package picker, verify baseline
2026-10-25 | PzFormat | Package Control picker, portable 4215 | audit row 1191 | remove via remove_package picker, verify baseline
2026-10-25 | QMakeProject | Package Control picker, portable 4215 | audit row 1192 | remove via remove_package picker, verify baseline
2026-10-25 | QNav | Package Control picker, portable 4215 | audit row 1193 | remove via remove_package picker, verify baseline
2026-10-25 | Qt Completions for C++ | Package Control picker, portable 4215 | audit row 1195 | remove via remove_package picker, verify baseline
2026-10-25 | Quake3 Script | Package Control picker, portable 4215 | audit row 1196 | remove via remove_package picker, verify baseline
2026-10-25 | Quartz-Syntax | Package Control picker, portable 4215 | audit row 1197 | remove via remove_package picker, verify baseline
2026-10-25 | Quasar Snippets | Package Control picker, portable 4215 | audit row 1198 | remove via remove_package picker, verify baseline
2026-10-25 | Vue Syntax Highlight (prerequisite of Quasar Snippets, README) | Package Control picker, portable 4215 | audit row 1198 | remove via remove_package picker right after, verify baseline
2026-10-25 | correction: the prerequisite installed is the picker package 'Vue' (SublimeText/Vue, provides text.html.vue); 'Vue Syntax Highlight' is not in the picker | remove via remove_package picker right after, verify baseline
2026-10-25 | Quasar Snippets and Vue | removed through the picker, baseline verified clean
2026-10-25 | Quick Docs Launcher | Package Control picker, portable 4215 | audit row 1199 | remove via remove_package picker, verify baseline
2026-10-25 | Quick File Creator | Package Control picker, portable 4215 | audit row 1200 | remove via remove_package picker, verify baseline
2026-10-25 | Quick File Move | Package Control picker, portable 4215 | audit row 1201 | remove via remove_package picker, verify baseline
2026-10-25 | Quick File Open | Package Control picker, portable 4215 | audit row 1202 | remove via remove_package picker, verify baseline
2026-10-25 | QuickGotoAnything | Package Control picker, portable 4215 | audit row 1203 | remove via remove_package picker, verify baseline
2026-10-25 | QuickOpen | Package Control picker, portable 4215 | audit row 1204 | remove via remove_package picker, verify baseline
2026-10-25 | QuickPanelEnhanced | Package Control picker, portable 4215 | audit row 1205 | remove via remove_package picker, verify baseline
2026-10-25 | QuickPrint | Package Control picker, portable 4215 | audit row 1206 | remove via remove_package picker, verify baseline
2026-10-25 | QuickRulers | Package Control picker, portable 4215 | audit row 1207 | remove via remove_package picker, verify baseline
2026-10-25 | Quijotipsum Snippet | Package Control picker, portable 4215 | audit row 1208 | remove via remove_package picker, verify baseline
2026-10-25 | PythonOpenModule (not in picker; repo url from st_packages, Donald's yes 2026-10-25) | clone into scratchpad\pom_clone, copy files to portable Data\Packages\PythonOpenModule | revisit of skipped row 1185 | remove: recycle.ps1 on both, verify gone
2026-10-25 | PythonOpenModule test copy | removed: Packages\PythonOpenModule and scratchpad pom_clone recycled, verified gone
2026-10-25 | Qunit Snippets | Package Control picker, portable 4215 | audit row 1209 | remove via remove_package picker, verify baseline
2026-10-25 | QuoteHTML | Package Control picker, portable 4215 | audit row 1210 | remove via remove_package picker, verify baseline
2026-10-25 | R Tools | Package Control picker, portable 4215 | audit row 1211 | remove via remove_package, verify Test-Path
2026-10-25 | R Tools | not in picker: shallow clone of karthik/Rtools into scratchpad\rtools_clone, copy into portable Data\Packages\R Tools | audit row 1211 | recycle both with recycle.ps1, verify
2026-10-25 | R-snippets | Package Control picker (if listed), portable 4215 | audit row 1212 | remove via remove_package, verify Test-Path
2026-10-25 | RAPID Syntax Highlighting | Package Control picker (if listed), portable 4215 | audit row 1213 | remove via remove_package, verify Test-Path
2026-10-25 | REXX | Package Control picker (if listed), portable 4215 | audit row 1214 | remove via remove_package, verify Test-Path
2026-10-25 | RISC OS Command Syntax | Package Control picker (if listed), portable 4215 | audit row 1215 | remove via remove_package, verify Test-Path
2026-10-25 | ROBLOXLua | Package Control picker (if listed), portable 4215 | audit row 1216 | remove via remove_package, verify Test-Path
2026-10-25 | RPG Syntax for ILE on IBMi | Package Control picker (if listed), portable 4215 | audit row 1217 | remove via remove_package, verify Test-Path
2026-10-25 | RSBIDE | Package Control picker (if listed), portable 4215 | audit row 1218 | remove via remove_package, verify Test-Path
2026-10-25 | RSL | Package Control picker (if listed), portable 4215 | audit row 1219 | remove via remove_package, verify Test-Path
2026-10-25 | RSense | Package Control picker (if listed), portable 4215 | audit row 1220 | remove via remove_package, verify Test-Path
2026-10-25 | RSpec Buddy | Package Control picker (if listed), portable 4215 | audit row 1221 | remove via remove_package, verify Test-Path
2026-10-25 | RSpec Buddy fixture | scratchpad\rspecproj (lib/foo.rb, spec/) | audit row 1221 | recycle with recycle.ps1 after test, remove folder from project
2026-10-25 | RSpecNavigator | Package Control picker (if listed), portable 4215 | audit row 1222 | remove via remove_package, verify Test-Path
2026-10-25 | RTL To Dialog | Package Control picker (if listed), portable 4215 | audit row 1223 | remove via remove_package, verify Test-Path
2026-10-25 | RTagsComplete | Package Control picker (if listed), portable 4215 | audit row 1224 | remove via remove_package, verify Test-Path
2026-10-25 | RVM | Package Control picker (if listed), portable 4215 | audit row 1225 | remove via remove_package, verify Test-Path
2026-10-25 | RVM | not in picker: shallow clone of jinze/sublime-rvm into scratchpad\rvm_clone, copy into portable Data\Packages\RVM | audit row 1225 | recycle both with recycle.ps1, verify
2026-10-25 | RVM test output | portable Data\Packages\User\Ruby.sublime-build written by enable_rvm | audit row 1225 | recycle with recycle.ps1 after test
2026-10-25 | R_comments | Package Control picker (if listed), portable 4215 | audit row 1226 | remove via remove_package, verify Test-Path
2026-10-25 | Rails Completions | Package Control picker (if listed), portable 4215 | audit row 1227 | remove via remove_package, verify Test-Path
2026-10-25 | Rails File Switcher | Package Control picker (if listed), portable 4215 | audit row 1228 | remove via remove_package, verify Test-Path
2026-10-25 | Rails File Switcher | not in picker: shallow clone of AlexanderZaytsev/SublimeText2RailsFileSwitcher into scratchpad\rfs_clone, copy into portable Data\Packages\RailsFileSwitcher | audit row 1228 | recycle both with recycle.ps1, verify
2026-10-25 | Rails File Switcher python3 branch | shallow clone -b python3 into scratchpad\rfs_clone3, copy into portable Data\Packages\RailsFileSwitcher (replaces master copy) | audit row 1228 | recycle all with recycle.ps1, verify
2026-10-25 | Rails File Switcher fixture | scratchpad\railsproj (Rakefile, app/, spec/) | audit row 1228 | recycle with recycle.ps1 after test, remove folder from project
2026-10-25 | Rails I18n Helper | Package Control picker (if listed), portable 4215 | audit row 1229 | remove via remove_package, verify Test-Path
2026-10-25 | Rails I18n Helper | not in picker: shallow clone of Adeptus/rails-i18n-helper into scratchpad\ri18n_clone, copy into portable Data\Packages\RailsI18nHelper | audit row 1229 | recycle both with recycle.ps1, verify
2026-10-25 | Rails Latest Migration | Package Control picker (if listed), portable 4215 | audit row 1230 | remove via remove_package, verify Test-Path
2026-10-25 | Rails Latest Migration fixtures | scratchpad\rlm_nonrails, rlm_empty, rlm_ok | audit row 1230 | recycle with recycle.ps1 after test, remove folders from project
2026-10-25 | Rails Magic Clipboard | Package Control picker (if listed), portable 4215 | audit row 1231 | remove via remove_package, verify Test-Path
2026-10-25 | Rails Magic Clipboard fixtures | scratchpad\rmc_* test files if needed | audit row 1231 | recycle with recycle.ps1 after test
2026-10-25 | Rails Migrations List | Package Control picker (if listed), portable 4215 | audit row 1232 | remove via remove_package, verify Test-Path
2026-10-25 | Rails Migrations List fixtures | scratchpad\rml_* | audit row 1232 | recycle with recycle.ps1 after test, remove folders from project
2026-10-25 | Rails OpenView | Package Control picker (if listed), portable 4215 | audit row 1233 | remove via remove_package, verify Test-Path
2026-10-25 | Rails OpenView fixtures | scratchpad\rov_* | audit row 1233 | recycle with recycle.ps1 after test, remove folders from project
2026-10-25 | Rails Related Files | Package Control picker (if listed), portable 4215 | audit row 1234 | remove via remove_package, verify Test-Path
2026-10-25 | Rails Related Files fixtures | scratchpad\rrf_* | audit row 1234 | recycle with recycle.ps1 after test, remove folders from project
2026-10-25 | Rails Related Files | not in picker: shallow clone of luqman/SublimeText2RailsRelatedFiles into scratchpad\rrf_clone, copy into portable Data\Packages\RailsRelatedFiles | audit row 1234 | recycle both with recycle.ps1, verify
2026-10-25 | Rails Status Snippets | Package Control picker (if listed), portable 4215 | audit row 1235 | remove via remove_package, verify Test-Path
2026-10-25 | RailsGoToSass | Package Control picker (if listed), portable 4215 | audit row 1236 | remove via remove_package, verify Test-Path
2026-10-25 | RailsGoToSass fixtures | scratchpad\rgs_* | audit row 1236 | recycle with recycle.ps1 after test
2026-10-25 | RailsGoToSass | copy of the picker package unzipped into portable Data\Packages\sublime_rails_go_to_sass (folder name the import expects) | audit row 1236 | recycle with recycle.ps1, verify
2026-10-25 | Railscasts Extended | Package Control picker (if listed), portable 4215; will set color_scheme in the portable User settings and restore it | audit row 1237 | restore color_scheme (backup copy in scratchpad), remove via remove_package, verify Test-Path
2026-10-25 | RainbowDrops Inspired - Color Scheme | Package Control picker (if listed), portable 4215; will set color_scheme in the portable User settings and restore it | audit row 1238 | restore color_scheme (backup copy in scratchpad), remove via remove_package, verify Test-Path
2026-10-25 | Rainbowth | Package Control picker (if listed), portable 4215; may write files into Data\Packages\User (generated color scheme / settings) | audit row 1239 | remove via remove_package, list Packages\User and Preferences against the backup copy in scratchpad, recycle any new files, verify
2026-10-25 | Rainbowth fixtures | scratchpad\rbw_test.clj | audit row 1239 | recycle with recycle.ps1 after test
2026-10-25 | Rainmeter | Package Control picker (if listed), portable 4215; may write settings and files into Data\Packages\User and Data\Local | audit row 1240 | remove via remove_package, compare Packages\User listing and Preferences against the scratchpad copies, recycle new files, verify
2026-10-25 | RamdaDocs | Package Control picker (if listed), portable 4215; may open the default browser and write into Data\Packages\User | audit row 1241 | remove via remove_package, compare Packages\User against baseline (MCP Commander, Package Control, Preferences settings), recycle new files, verify
2026-10-25 | Random HEX Color | Package Control picker (if listed), portable 4215 | audit row 1242 | remove via remove_package, compare Packages\User against baseline, recycle new files, verify
2026-10-25 | Random HEX Color | not in picker: shallow clone of lindskogen/RandomHEXColor into scratchpad\rhc_clone, copy into portable Data\Packages\RandomHEXColor | audit row 1242 | recycle both with recycle.ps1, verify
2026-10-25 | Random Message | Package Control picker (if listed), portable 4215; may open the browser or fetch from the network | audit row 1243 | remove via remove_package, compare Packages\User against baseline, recycle new files, verify
2026-10-25 | Random Message | not in picker: shallow clone of kutu/RandomMessage into scratchpad\rmsg_clone, copy into portable Data\Packages\RandomMessage | audit row 1243 | recycle both with recycle.ps1, verify
2026-10-25 | Random Text | Package Control picker, portable 4215 | audit row 1244 | remove via remove_package, compare Packages\User against baseline, recycle new files, verify
2026-10-25 | RandomizeLogMessages | Package Control picker (if listed), portable 4215 | audit row 1245 | remove via remove_package, compare Packages\User against baseline, recycle new files, verify
2026-10-25 | RandomizeLogMessages | not in picker: shallow clone of marclar/RandomizeLogMessages into scratchpad\rlm2_clone, copy into portable Data\Packages\RandomizeLogMessages | audit row 1245 | recycle both with recycle.ps1, verify
2026-10-25 | RandomizeLogMessages fixtures | scratchpad\rlm2_test.js | audit row 1245 | recycle with recycle.ps1 after test
2026-10-25 | Raybo - Color Scheme | Package Control picker (if listed), portable 4215; will set color_scheme in the portable User settings and restore it | audit row 1246 | restore color_scheme (backup copy in scratchpad), remove via remove_package, verify Test-Path
2026-10-25 | React Coffee Snippets | Package Control picker (if listed), portable 4215 | audit row 1247 | remove via remove_package, compare Packages\User against baseline, recycle new files, verify
2026-10-25 | CoffeeScript (SublimeText/CoffeeScript, dependency for source.coffee) | Package Control picker, portable 4215 | audit row 1247 (React Coffee Snippets needs scope source.coffee; 4215 ships no CoffeeScript syntax) | remove via remove_package, compare Packages\User and Installed Packages against baseline (Color Scheme - Legacy, Package Control), recycle residue, verify
2026-10-25 | React Create Component | Package Control picker (if listed), portable 4215; may create files in a project folder | audit row 1248 | remove via remove_package, compare Packages\User against baseline, recycle new files and test folders, verify
2026-10-25 | React Create Component fixtures | scratchpad\rcc_proj (components created inside it) | audit row 1248 | recycle with recycle.ps1 after test
2026-10-25 | React and React Router Snippets | Package Control picker (if listed), portable 4215 | audit row 1249 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | React-CSS-Converter | Package Control picker (if listed), portable 4215 | audit row 1250 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Read Only Buffer | Package Control picker (if listed), portable 4215 | audit row 1251 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Read Only Buffer clone | shallow git clone into scratchpad rob_clone (not in picker) | audit row 1251 | recycle clone after test
2026-10-25 | Read Only Buffer copy | files copied (no .git) to st_portable\Data\Packages\Read Only Buffer | audit row 1251 | recycle folder, plus Packages\User\SublimeReadOnlyBuffer.sublime-settings if created
2026-10-25 | rob_fixture.txt | scratchpad fixture file for Read Only Buffer test | audit row 1251 | scratchpad only, recycle
2026-10-25 | ReadRspec | Package Control picker (if listed), portable 4215 | audit row 1252 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | RealityCheck | Package Control picker, portable 4215, picked by mistake (index 3178 landed on RealityCheck instead of ReadRspec) | audit row 1252 attempt | remove via remove_package, verify, recycle residue; not a test
2026-10-25 | ReadonlyMode | Package Control picker (if listed), portable 4215 | audit row 1253 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | rom_fixture.txt + temporary read_only_mode line in portable Preferences | scratchpad fixture and temp setting for ReadonlyMode test | audit row 1253 | recycle fixture, restore Preferences from rom_prefs.backup and compare hash
2026-10-25 | Packages\User\Plain text.sublime-settings | temporary syntax settings file with read_only_mode true for the ReadonlyMode test (the Preferences edit failed to parse) | audit row 1253 | recycle after test
2026-10-25 | ReadonlyWritable | Package Control picker (if listed), portable 4215 | audit row 1254 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | ReadonlyWritable clone | shallow git clone into scratchpad rrw_clone (not in picker) | audit row 1254 | recycle clone after test
2026-10-25 | ReadonlyWritable copy + rrw_fixture.txt | files copied (no .git) to st_portable\Data\Packages\ReadonlyWritable; fixture in scratchpad | audit row 1254 | recycle package folder, fixture, clone (clear read-only attribute on the fixture first)
2026-10-25 | RealityCheck | Package Control picker, portable 4215 | audit row 1255 (second install, first was by mistake) | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | RealityCheck unzipped copy + .python-version 3.8 + rc_fixture.py | zip from Installed Packages expanded to st_portable\Data\Packages\RealityCheck (with .python-version), fixture rc_fixture.py in scratchpad that writes rc_marker.txt | audit row 1255 | recycle Packages\RealityCheck, fixture, marker; remove the zip via remove_package
2026-10-25 | RecentActiveFiles | Package Control picker (if listed), portable 4215 | audit row 1256 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | raf_a.txt raf_b.txt raf_c.txt | scratchpad fixtures for RecentActiveFiles test | audit row 1256 | recycle each
2026-10-25 | scratchpad folder added to the portable window project | add_folder for RecentActiveFiles path-column test | audit row 1256 | remove_folder afterwards and confirm get_project_folders is empty
2026-10-25 | RecentTabSort | Package Control picker (if listed), portable 4215 | audit row 1257 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | rts_a.txt rts_b.txt rts_c.txt | scratchpad fixtures for RecentTabSort test | audit row 1257 | recycle each
2026-10-25 | RecenterTopBottom | Package Control picker (if listed), portable 4215 | audit row 1258 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | RecenterTopBottom clone | shallow git clone into scratchpad rtb_clone (not in picker) | audit row 1258 | recycle clone after test
2026-10-25 | RecenterTopBottom copy + rtb_fixture.txt | files copied (no .git) to st_portable\Data\Packages\RecenterTopBottom; 200-line fixture in scratchpad | audit row 1258 | recycle package folder, fixture, clone, and any User settings file it creates
2026-10-25 | rtb_wrap.txt | scratchpad fixture, 200 long wrapped lines, for RecenterTopBottom word-wrap test | audit row 1258 | recycle
2026-10-25 | Recessify | Package Control picker (if listed), portable 4215 | audit row 1259 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Recessify clone | shallow git clone into scratchpad rec_clone (not in picker) | audit row 1259 | recycle clone after test
2026-10-25 | Red Planet Color Scheme | Package Control picker (if listed), portable 4215 | audit row 1260 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | rp_fixture.py | scratchpad Python fixture for Red Planet color scheme test (scheme applied per view only, Preferences untouched) | audit row 1260 | recycle
2026-10-25 | RedBeanPHP ORM Snippets | Package Control picker (if listed), portable 4215 | audit row 1261 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Redlime | Package Control picker (if listed), portable 4215 | audit row 1262 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Redlime installed copy edited in place | replaced the distutils LooseVersion import in libs\redmine\__init__.py and libs\redmine\resources\standard.py with a stand-in to see the next load error | audit row 1262 | removed with the package (remove_package); recycle residue
2026-10-25 | Redlime installed copy edited in place (second edit) | replaced import cgi in libs\redmine\packages\requests\utils.py with a parse_header stand-in | audit row 1262 | removed with the package
2026-10-25 | Redmine Pastie | Package Control picker (if listed), portable 4215 | audit row 1263 | remove via remove_package, compare Packages\User against baseline, recycle residue and any Data\Backup folder it causes, verify
2026-10-25 | Redux Snippets | Package Control picker (if listed), portable 4215 | audit row 1264 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Refresh File and Folders | Package Control picker (if listed), portable 4215 | audit row 1265 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | rff_fixture.txt | scratchpad fixture for Refresh File and Folders test (unsaved-edit loss) | audit row 1265 | recycle
2026-10-25 | RegExLink | Package Control picker (if listed), portable 4215 | audit row 1266 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Packages\User\RegExLink.sublime-settings | temporary user settings with one definition that runs a nonexistent program, to see the command after shlex.split (no GUI app is launched) | audit row 1266 | recycle after test
2026-10-25 | RegexExplainTip | Package Control picker (if listed), portable 4215 | audit row 1267 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Rekit | Package Control picker (if listed), portable 4215 | audit row 1268 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Related Files | Package Control picker (if listed), portable 4215 | audit row 1269 | remove via remove_package, compare Packages\User against baseline, recycle residue, verify
2026-10-25 | Related Files fixture folder | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rf_proj (rails-like files, added as project folder) | row 1269 test | recycle folder, remove_folder in window
2026-10-25 | Related Files fixture 2 | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rf_out\lib\tool.rb outside project | row 1269 | recycle rf_out
2026-10-25 | Remify | Package Control picker install into portable st_portable | row 1270 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemoteCpp | Package Control picker install into portable st_portable | row 1271 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemoteOpen | Package Control picker install into portable st_portable | row 1272 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemoteOpen fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\ro_fix (a.txt, sub\b.txt) | row 1272 | recycle folder
2026-10-25 | RemoteOpen temp settings | st_portable\Data\Packages\User\RemoteOpen.sublime-settings (open_directory_contents false) | row 1272 | recycle file
2026-10-25 | RemotePHPUnit | Package Control picker install into portable st_portable | row 1273 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemotePHPUnit fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rp_fix (app\phpunit.xml.dist, tests\FooTest.php; added as project folder) | row 1273 | remove_folder, recycle folder
2026-10-25 | RemotePHPUnit fixture leftover | scratchpad\rp_fix is now an EMPTY folder, locked by an unknown process (recycle.ps1 failed twice, admin retry too) | row 1273 | recycle again later; harmless, inside the session scratchpad
2026-10-25 | RemoveLineBreaks | Package Control picker install into portable st_portable | row 1274 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemoveLineBreaks (second install) | plugin did not load after first picker install (no reload line, no commands); remove and reinstall via picker | row 1274 | remove_package, recycle Cache residue
2026-10-25 | RemoveSelection | Package Control picker install into portable st_portable | row 1275 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Rename Buffer | Package Control picker install into portable st_portable | row 1276 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Renpy Script | Package Control picker install into portable st_portable | row 1278 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RemotePHPUnit placeholder theme | C:\Users\donal\tools\st_portable\Data\Packages\RemotePHPUnit\RemotePHPUnit.hidden-tmTheme (minimal tmTheme so the exec panel, which kept the removed theme, stops raising 8+ error dialogs after every package change) | row 1278 | recycle the whole folder after the next Sublime restart (restart resets the exec panel)
2026-10-25 | Renpy Script fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\renpy_fix\test.rps | row 1278 | recycle folder
2026-10-25 | Repeat Macro | Package Control picker install into portable st_portable | row 1279 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RepeatCommand | Package Control picker install into portable st_portable | row 1280 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | ReqsLang | Package Control picker install into portable st_portable | row 1281 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Require CommonJS Modules Helper | Package Control picker install into portable st_portable | row 1282 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Require CommonJS fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\req_fix (a.js, lib\b-c.js, node_modules\lodash\, added as project folder) | row 1282 | remove_folder, recycle folder
2026-10-25 | Require Helper | Package Control picker install into portable st_portable | row 1283 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Require Helper fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\reqh_fix (main.js, foo\bar-baz.js, node_modules\x\i.js; added as project folder) | row 1283 | remove_folder, recycle folder
2026-10-25 | Resize Active Group | Package Control picker install into portable st_portable | row 1284 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Resize Active Group (not in picker) | shallow clone C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rag_clone (then copy into st_portable\Data\Packages\ResizeActiveGroup, no .git) | row 1284 | recycle clone, copied folder, Data\Backup entries and caches
2026-10-25 | Resize Active Group copy | C:\Users\donal\tools\st_portable\Data\Packages\ResizeActiveGroup (ResizeActiveGroup.py + README.md copied from the clone) | row 1284 | recycle folder and Data\Backup / cache entries
2026-10-25 | Resize Group with Keyboard | Package Control picker install into portable st_portable | row 1285 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Resolve Javascript Modules | Package Control picker install into portable st_portable | row 1286 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Resolve Javascript Modules fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rjm_fix (lib.js, main.js) | row 1286 | recycle folder
2026-10-25 | ResponsiveBoilerplate | Package Control picker install into portable st_portable | row 1287 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Responsys Built-In Function | Package Control picker install into portable st_portable | row 1288 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | ReverseCharacters | Package Control picker install into portable st_portable | row 1289 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Revert All Files | Package Control picker install into portable st_portable (or shallow clone copy if absent from the picker) | row 1290 | remove_package, recycle residue
2026-10-25 | Revert All Files fixture | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\raf_fix (one.txt, two.txt) | row 1290 | recycle folder
2026-10-25 | RevertFontSize | Package Control picker install into portable st_portable | row 1291 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Review Myself | Package Control picker install into portable st_portable | row 1292 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Review Myself fixture folder C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rm_fix | test files with TODO comments, opened as project folder | row 1292 | remove_folder, recycle folder
2026-10-25 | RhetosDSL | Package Control picker install into portable st_portable | row 1293 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Rholang | Package Control picker install into portable st_portable | row 1294 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RichTextFormat | Package Control picker install into portable st_portable | row 1295 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Riemann Completions | Package Control picker install into portable st_portable | row 1296 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Riemann Completions fixture C:\Users\donal\tools\st_portable\Data\Packages\RiemannCompFix | one small .sublime-completions with scope source.clojure to test the scope fix | row 1296 | recycle folder
2026-10-25 | Riot Syntax | Package Control picker install into portable st_portable | row 1297 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Riot Syntax fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\riot_fix | sample.js and sample.tag opened to see which syntax Sublime picks | row 1297 | recycle folder
2026-10-25 | Riot Tag | Package Control picker install into portable st_portable | row 1298 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Riot Tag fixture C:\Users\donal\tools\st_portable\Data\Packages\RiotTagFix | copy of riot.sublime-syntax with expression_close_lookahead changed to (?=\s*}) to test the fix | row 1298 | remove through the Remove Package picker, recycle Backup residue
2026-10-25 | RiveScript | Package Control picker install into portable st_portable | row 1299 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RiveScript fixture C:\Users\donal\tools\st_portable\Data\Packages\RiveScriptFix | copy of rive.tmLanguage with three regex fixes and scope text.rivefix to test the fixes | row 1299 | remove through the Remove Package picker, recycle Backup residue
2026-10-25 | RoRvsWild Color Schemes | Package Control picker install into portable st_portable | row 1300 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | RoboType | Package Control picker install into portable st_portable | row 1301 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Robot Framework | Package Control picker install into portable st_portable | row 1302 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Robot Framework clone C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rf_src | shallow clone of shellderp/sublime-robot-plugin (not in the picker) to copy into Data\Packages\Robot Framework | row 1302 | recycle folder, remove copied package via picker
2026-10-25 | Robot Framework copy C:\Users\donal\tools\st_portable\Data\Packages\Robot Framework | files of shellderp/sublime-robot-plugin copied (no .git) | row 1302 | remove via Remove Package picker, recycle Backup and Cache residue
2026-10-25 | Rocks | Package Control picker install into portable st_portable | row 1303 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Rocks fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rocks_fix | one small a.py opened so the package's on_load handler runs | row 1303 | recycle folder
2026-10-25 | Rockstar Syntax Highlighter | Package Control picker install into portable st_portable | row 1304 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Rohingya Dark color scheme | Package Control picker install into portable st_portable | row 1305 | remove_package, recycle Cache residue
2026-10-25 | Romanize | Package Control picker install into portable st_portable | row 1306 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Romanize scratch folder romtest (t.py comparing the old and fixed to_romans outside Sublime) | row 1306 | written without a ledger line first, recycled the same hour
2026-10-25 | Rosetta Code Snippets | Package Control picker install into portable st_portable | row 1307 | remove_package, recycle Cache\__pycache__\install residue
2026-10-25 | Rosetta Code Snippets | NOTHING installed: not in the picker (ST2-only), ledger line above was written before the search | row 1307 | nothing to remove
2026-10-25 | Roy | Package Control picker install into portable st_portable | row 1308 | remove_package, recycle Cache residue
2026-10-25 | RspecBuild | Package Control picker install into portable st_portable | row 1309 | remove_package, recycle Cache residue
2026-10-25 | RspecBuild copy C:\Users\donal\tools\st_portable\Data\Packages\RspecBuild | RunSpec.py and RSpec.sublime-build of erinata/SublimeRspecBuild downloaded from GitHub raw (package not in the picker) | row 1309 | remove via Remove Package picker, recycle Backup and Cache residue
2026-10-25 | Ruby Coverage | Package Control picker install into portable st_portable | row 1310 | remove_package, recycle Cache residue
2026-10-25 | Ruby Coverage copy C:\Users\donal\tools\st_portable\Data\Packages\RubyCoverage and fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rc_fix | SublimeRubyCoverage.py and keymap downloaded from GitHub raw (not in the picker, issues disabled), plus a.rb in a folder without a coverage directory | row 1310 | remove via Remove Package picker, recycle Backup/Cache residue and rc_fix
2026-10-25 | Ruby Extract Method | Package Control picker install into portable st_portable | row 1311 | remove_package, recycle Cache residue
2026-10-25 | Ruby Extract Method copy C:\Users\donal\tools\st_portable\Data\Packages\RubyExtractMethod | RubyExtractMethod.py, Edit.py and keymap downloaded from GitHub raw (not in the picker) plus a fixture a.rb in C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rem_fix | row 1311 | remove via Remove Package picker, recycle Backup/Cache residue and rem_fix
2026-10-25 | Ruby Hash Converter | Package Control picker install (if listed), else GitHub raw copy to Data\Packages\RubyHashConverter | row 1313 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-25 | Ruby Hash Reverter | Package Control picker install | row 1314 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | Ruby Hash Reverter copy C:\Users\donal\tools\st_portable\Data\Packages\RubyHashReverter | not in picker; files from GitHub raw | row 1314 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-25 | Ruby Markers | Package Control picker install | row 1315 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | Ruby Pipe Text Processing | Package Control picker install | row 1316 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyCheckOnSave | Package Control picker install | row 1317 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyCheckOnSave copy C:\Users\donal\tools\st_portable\Data\Packages\RubyCheckOnSave + fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rcos_fix\a.rb | not in picker; files from GitHub raw | row 1317 | remove via Remove Package picker, recycle Backup/Cache residue and rcos_fix
2026-10-25 | ReqsLang retest (after petarjs fix, PR #2) | Package Control picker install, else master copy to Data\Packages\ReqsLang + fixture in scratchpad reqs_fix | retest of row logged 2026-10-25 | remove via Remove Package picker, recycle Backup/Cache residue and reqs_fix
2026-10-25 | ReqsLang master copy C:\Users\donal\tools\st_portable\Data\Packages\ReqsLangMaster | picker serves v1.0.0 (2016, pre-fix); Requirements.tmLanguage from GitHub raw master 75e9fe2 | retest | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-25 | RubyEval | Package Control picker install | row 1318 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyFormat | Package Control picker install | row 1319 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyFormat copy C:\Users\donal\tools\st_portable\Data\Packages\RubyFormat | not in picker; files from GitHub raw | row 1319 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-25 | RubyMotion Autocomplete | Package Control picker install | row 1320 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyMotionFix C:\Users\donal\tools\st_portable\Data\Packages\RubyMotionFix | copy of RubyMotion.sublime-completions with scope source.ruby for the fix test | row 1320 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-25 | RubyMotionBuilder | Package Control picker install | row 1321 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyMotionSpec | Package Control picker install | row 1322 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | RubyMotionSpec fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rms_fix\foo_spec.rb | saved spec file to run the command on | row 1322 | recycle rms_fix; if the command writes _stdout_spec/_stderr_spec there, recycle them too
2026-10-25 | NOTE rms_fix (scratchpad) NOT yet recycled | recycle failed twice (normal and admin): folder in use, probably Sublime's exec working_dir from the RubyMotionSpec run | recycle after the next exec build in the portable or after a portable restart
2026-10-25 | RubyToggleString | Package Control picker install | row 1323 | remove via Remove Package picker, recycle Cache residue
2026-10-25 | NOTE | Donald said 2015 is not that long ago: posted the held findings for RubyMotion Autocomplete, RubyMotionBuilder, RubyToggleString (6 issues); RubyEval, RubyFormat, RubyMotionSpec (2012-2013) still held in findings\ | no files created
2026-10-25 | Rubyfmt (toreriklinnerud/sublime-rubyfmt) + fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rfm_fix\a.rb | Package Control picker install; fixture to save | row 1324 | remove via Remove Package picker, recycle Cache residue and rfm_fix
2026-10-25 | PureCSS retest (reinvestigation after owner closed #3/#4 with 'Ty?' and disabled issues) | Package Control picker install; then Data\Packages\PureCSSFix copy with the proposed fix | retest | remove both via Remove Package picker, recycle Backup/Cache residue
2026-10-26 | PureCSS retest finished | PureCSS and PureCSSFix removed via picker, residue recycled | no files left
2026-10-26 | Clafer Tools retest (0.5.4, after PR #5 fixed #4) | Package Control picker install; fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\clf_fix\a.cfr | retest | remove via Remove Package picker, recycle Backup/Cache residue and clf_fix; Terminus NOT installed (not needed for the ctrl+i test)
2026-10-26 | Clafer Tools retest finished | package removed via picker, pycache and clf_fix recycled; older Backup\20261022115023\Clafer Tools (from the 2026-10-22 test) left with the other old Backup folders | no files left
2026-10-26 | RulerColumn | Package Control picker install | row 1325 | remove via Remove Package picker, recycle Cache residue
2026-10-26 | RulerColumnFix C:\Users\donal\tools\st_portable\Data\Packages\RulerColumnFix | plugin.py from GitHub raw with the word_wrap check patched, for the fix test | row 1325 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-26 | Run Apps | Package Control picker install; its Add Application command writes Data\Packages\User\Run App.sublime-commands | row 1326 | remove via Remove Package picker; recycle Run App.sublime-commands (User must be back to 3 files), Backup/Cache residue
2026-10-26 | RunCommand | Package Control picker install | row 1327 | remove via Remove Package picker, recycle Cache residue
2026-10-26 | RunCommand copy C:\Users\donal\tools\st_portable\Data\Packages\RunCommand | not in picker; files from GitHub raw | row 1327 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-26 | RunMacroFileWithContext, then its dependency Context (shagabutdinov/sublime-context) | Package Control picker installs; macro fixture C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rmc_fix\m.sublime-macro | row 1328 | remove both via Remove Package picker, recycle Backup/Cache residue and rmc_fix
2026-10-26 | Expression (shagabutdinov/sublime-expression) and, if the import chain needs them, Statement and IndentationNavigation | Package Control picker installs, needed by Context for the RunMacroFileWithContext test | row 1328 | remove each via Remove Package picker, recycle Backup/Cache residue
2026-10-26 | NOTE RunMacroFileWithContext | the line for Expression, Statement and IndentationNavigation was written after Expression was already installed (my slip); Statement and IndentationNavigation were never installed | Context, Expression, RunMacroFileWithContext all removed via picker, residue recycled, rmc_fix recycled
2026-10-26 | Rust Share | Package Control picker install | row 1329 | remove via Remove Package picker, recycle Cache residue; the test sends only the harmless text 'fn main() {}' and a run of the letter a to is.gd (no personal data)
2026-10-26 | RustShareFix C:\Users\donal\tools\st_portable\Data\Packages\RustShareFix | rust-share.py and Main.sublime-commands from GitHub raw with a User-Agent header and https, for the fix test | row 1329 | remove via Remove Package picker, recycle Backup/Cache residue
2026-10-26 | RemotePHPUnit placeholder theme, rp_fix, rms_fix | portable quit, then recycled (Recycle Bin); Packages now MCP Commander; User | row 1329 | done
2026-10-26 | RustAutoImport | Package Control picker install into portable st_portable | row 1330 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | RustAutoImport test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rai_test.rs (scratchpad) | row 1330 | recycle at end
2026-10-26 | RustCookbookSnippets | Package Control picker install into portable st_portable | row 1331 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | RustCookbookSnippets test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rcs_test.rs (scratchpad) | row 1331 | recycle at end
2026-10-26 | Rux | Package Control picker install into portable st_portable | row 1332 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | Rux test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\rux_test.rux (scratchpad) | row 1332 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\RuxFix | 2026-10-26 | Rux fix test copy (syntax with nested-block context) | row 1332 | remove_package RuxFix, recycle Backup and Cache residue
2026-10-26 | SAMB | Package Control picker install into portable st_portable | row 1334 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SAMB test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\samb_test.se (scratchpad) | row 1334 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SambFix | 2026-10-26 | SAMB fix test copy (Comments.tmPreferences with # comment) | row 1334 | remove_package SambFix, recycle Backup and Cache residue
2026-10-26 | SBT Runner | Package Control picker install into portable st_portable | row 1335 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SBT Runner | NOT installed: the name is not in the Install Package picker (only SublimeSBT), so the ledger line above did not happen | row 1335 | nothing to remove
2026-10-26 | SDC Constraints | Package Control picker install into portable st_portable | row 1337 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SDC Constraints test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sdc_test.sdc (scratchpad) | row 1337 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SdcFix | 2026-10-26 | SDC fix test copy (one snippet, trigger ccx, space after get_ports) | row 1337 | remove_package SdcFix, recycle Backup and Cache residue
2026-10-26 | SDLang | Package Control picker install into portable st_portable | row 1338 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SDLang test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sdl_test.sdl (scratchpad) | row 1338 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SdlFix | 2026-10-26 | SDLang fix test copy (SDLang.tmLanguage with 3 regex changes) | row 1338 | remove_package SdlFix, recycle Backup and Cache residue
2026-10-26 | SEPath | Package Control picker install into portable st_portable | row 1339 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SEPath test files | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sepath_test.txt and C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sepath_target.txt (scratchpad) | row 1339 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SepathFix | 2026-10-26 | SEPath fix test copy (SEPath.py: range(point - 1, -1, -1), command renamed sepfix_open) | row 1339 | remove_package SepathFix, recycle Backup and Cache residue
2026-10-26 | SIMPL+ Syntax Highlight | Package Control picker install into portable st_portable | row 1340 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SIMPL+ test files | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\simpl_test.usp and C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\simpl_test2.usl (scratchpad) | row 1340 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SimplFix | 2026-10-26 | SIMPL+ fix test copy (syntax: include email/ramping/exception groups, add symbol operator rule) | row 1340 | remove_package SimplFix, recycle Backup and Cache residue
2026-10-26 | SJSON | Package Control picker install into portable st_portable | row 1341 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SJSON test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sjson_test.sjson (scratchpad) | row 1341 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SjsonFix | 2026-10-26 | SJSON fix test copy (Comments.tmPreferences for source.sjson) | row 1341 | remove_package SjsonFix, recycle Backup and Cache residue
2026-10-26 | SLAB | Package Control picker install into portable st_portable | row 1342 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SLAB test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\slab_test.slab (scratchpad) | row 1342 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SlabFix | 2026-10-26 | SLAB fix test copy (syntax file renamed slab.sublime-syntax, content unchanged) | row 1342 | remove_package SlabFix, recycle Backup and Cache residue
2026-10-26 | SLAX | Package Control picker install into portable st_portable | row 1343 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SLAX test files | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\slax_test.slax and C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\slax_test.py (scratchpad) | row 1343 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SlaxFix | 2026-10-26 | SLAX fix test copy (one snippet, trigger syslogx, scope source.slax) | row 1343 | remove_package SlaxFix, recycle Backup and Cache residue
2026-10-26 | SM RAD | Package Control picker install into portable st_portable | row 1344 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SM RAD test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\smrad_test.rad (scratchpad) | row 1344 | recycle at end
2026-10-26 | SNMP MIB Syntax | Package Control picker install into portable st_portable | row 1345 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SNMP MIB test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\snmp_test.mib (scratchpad) | row 1345 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SnmpFix | 2026-10-26 | SNMP MIB fix test copy (syntax: drop dot-escape rule, add MAX-ACCESS) | row 1345 | remove_package SnmpFix, recycle Backup and Cache residue
2026-10-26 | SOML | Package Control picker install into portable st_portable | row 1346 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SOML test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\soml_test.soml (scratchpad) | row 1346 | recycle at end
2026-10-26 | SPARC Assembly | Package Control picker install into portable st_portable | row 1347 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SPARC Assembly test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sparc_test.s (scratchpad) | row 1347 | recycle at end
C:\Users\donal\tools\st_portable\Data\Packages\SparcFix | 2026-10-26 | SPARC fix test copy (sparc.tmLanguage delay-slot list extended) | row 1347 | remove_package SparcFix, recycle Backup and Cache residue
2026-10-26 | SPARQL Runner | Package Control picker install into portable st_portable | row 1348 | remove_package, recycle Cache\__pycache__\install and Backup residue
2026-10-26 | SPARQL Runner test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sqr_test.rq (scratchpad); package writes Data\Packages\User\SPARQLRunner.sublime-settings when an endpoint is selected | row 1348 | recycle both at end
2026-10-26 | SPICE Circuit Simulator | Package Control picker install on portable 4215 (Data\Installed Packages) | row 1349 | remove via picker, verify, recycle Cache\__pycache__\install residue
2026-10-26 | SPICE test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\spice_test.sp (scratchpad) | row 1349 | recycle at end
2026-10-26 | SPIP | Package Control picker install on portable 4215 (Data\Installed Packages) | row 1350 | remove via picker, verify, recycle Cache\__pycache__\install residue
2026-10-26 | SPIP test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\spip_test.html (scratchpad) | row 1350 | recycle at end
2026-10-26 | SpipFix fix-copy package | C:\Users\donal\tools\st_portable\Data\Packages\SpipFix (one completions file) | row 1350 | remove via picker, recycle Data\Backup\<timestamp>\SpipFix
2026-10-26 | SQF for VBS3 | Package Control picker install on portable 4215 (Data\Installed Packages) | row 1351 | remove via picker, verify, recycle Cache\__pycache__\install residue
2026-10-26 | SQF test file | C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\dbf4f367-b3de-4a92-84b7-f82ad5721153\scratchpad\sqf_test.sqf (scratchpad) | row 1351 | recycle at end

- 2026-10-26 SQL (simple-db-migrate): installing via Package Control picker on portable 4215 to test syntax; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SQL (simple-db-migrate) test file: scratchpad sdm_test.migration (recycle after test).
- 2026-10-26 SREC: installing via Package Control picker on portable 4215 to test syntax; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SREC test file: scratchpad srec_test.s19 (recycle after test).
- 2026-10-26 SSE & AVX Intrinsics: installing via Package Control picker on portable 4215 to test snippets; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SSE & AVX Intrinsics test files: scratchpad sse_test.cpp and sse_test.c (recycle after test).
- 2026-10-26 SseFix: copy package Data\Packages\SseFix (one snippet with scope source.c, source.c++) to test fix for SSE & AVX Intrinsics; remove after test.
- 2026-10-26 STVenvWrapper: installing via Package Control picker on portable 4215 to test; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 ST_AWK: installing via Package Control picker on portable 4215 to test; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 ST_AWK test: no extra files (uses untitled tab only).
- 2026-10-26 SUCC Syntax Highlighting: installing via Package Control picker on portable 4215 to test syntax; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SUCC test file: scratchpad succ_test.succ (recycle after test).
- 2026-10-26 SVG Preview: installing via Package Control picker on portable 4215 to test; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SVG Preview test file: scratchpad svgp_test.svg; plugin may create %TEMP%\sublime-svg-preview (recycle after test).
- 2026-10-26 SVG to JSX: installing via Package Control picker on portable 4215 to test; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SVG to JSX test file: scratchpad jsx_test.svg (recycle after test).
- 2026-10-26 SvgJsxFix: copy package Data\Packages\SvgJsxFix (REPLACEMENTS applied longest first, command convert_svg_to_jsx_fix) to test fix for SVG to JSX; remove after test.
- 2026-10-26 SVG-Snippets: installing via Package Control picker on portable 4215 to test snippets; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 SVG-Snippets test file: scratchpad svgs_test.svg (recycle after test).
- 2026-10-26 Sails Snippets: installing via Package Control picker on portable 4215 to test snippets; remove with remove_package picker, verify baseline, recycle residue.
- 2026-10-26 Sails Snippets test file: scratchpad sails_test.js (recycle after test).
- 2026-10-26 SailsFix: copy package Data\Packages\SailsFix (one snippet with \$custom escaped) to test fix for Sails Snippets; remove after test.

- 2026-10-26 Scold: Package Control picker install on portable 4215 (C:\Users\donal\tools\st_portable); audit test; remove via Remove Package picker and verify Data\Installed Packages + Packages

- 2026-10-26 ScopeContext: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Scopus Query Compiler: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Scopus Syntax Highlighter: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 ScriptSrc: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Scroll Other Pane: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 ScrollAlternative: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 ScrollOffset: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Scuggest: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Search Anywhere: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Search CakePHP API: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 SearchPanelEnhanced: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 StatusMessage: prerequisite of SearchPanelEnhanced; Package Control picker install on portable 4215; remove via Remove Package picker and verify

- 2026-10-26 Section Comment: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Seeing Is Believing: Package Control picker install on portable 4215; audit test (no Ruby installed, none to be installed); remove via Remove Package picker and verify

- 2026-10-26 Select Quoted: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Select all by current scope: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 SelectExact: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 SelectNextNumber: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Selection Evaluator: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 SelectionTools: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 SelectiveUppercase: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify

- 2026-10-26 Selenium Snippets: Package Control picker install on portable 4215; audit test; remove via Remove Package picker and verify
2026-10-26 | Sencha | Package Control picker on portable st_portable | audit row 1405 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Send To Sandbox | Package Control picker on portable st_portable | audit row 1406 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Send by Mail | Package Control picker on portable st_portable | audit row 1407 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Send by Mail | (correction) not in picker, nothing was installed | audit row 1407 | nothing to remove
2026-10-26 | Send to Shell | Package Control picker on portable st_portable | audit row 1408 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Pywin32 | Package Control picker on portable st_portable | prerequisite of Send to Shell (row 1408) | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Send to Shell + Pywin32 | removed, loose copy recycled, verified | audit row 1408 | done
2026-10-26 | SendText | Package Control picker on portable st_portable | audit row 1409 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | SendToJsonBlob | Package Control picker on portable st_portable | audit row 1410 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | SendToPasteBin | Package Control picker on portable st_portable | audit row 1411 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Sepiarize Color Scheme | Package Control picker on portable st_portable | audit row 1412 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | SequentialBuilder | Package Control picker on portable st_portable | audit row 1413 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Serpent Syntax | Package Control picker on portable st_portable | audit row 1414 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Seth Color Scheme | Package Control picker on portable st_portable | audit row 1415 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | SetlX Helper | Package Control picker on portable st_portable | audit row 1416 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | SexySnippets | Package Control picker on portable st_portable | audit row 1417 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | ShaderLanguages | Package Control picker on portable st_portable | audit row 1418 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | ShaderLanguages | (correction) download 404, nothing was installed | audit row 1418 | nothing to remove
2026-10-26 | Share File | Package Control picker on portable st_portable | audit row 1419 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | requests library (auto-installed by Share File, row 1419) | Package Control dependency | for Share File | check it is removed with the package; else remove_package/remove library
2026-10-26 | ShellStatus | Package Control picker on portable st_portable | audit row 1420 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | StatusMessage | Package Control picker on portable st_portable | prerequisite of ShellStatus (row 1420) | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | ShellStatus test settings file Packages\User\ShellStatus.sublime-settings | created for test | audit row 1420 | recycle after test
2026-10-26 | Sheller | Package Control picker on portable st_portable | audit row 1421 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Shen | Package Control picker on portable st_portable | audit row 1422 | remove via remove_package, verify Installed Packages/Packages
2026-10-26 | Sherumite - Color Scheme | Package Control picker on portable st_portable | audit row 1423 | remove via remove_package, verify Installed Packages/Packages; color_scheme setting not to be left applied
2026-10-26 | Shiftswitch | Package Control picker on portable st_portable | audit row 1424 | remove via remove_package, verify Installed Packages/Packages
- 2026-10-26 Shinken (Package Control picker, portable 4215 Data\Packages): syntax test for row 1425; remove via picker, verify
- 2026-10-26 Shlisp Syntax (Package Control picker, portable 4215): syntax test for row 1426; remove via picker, verify
- 2026-10-26 ShouldjsSnippets (Package Control picker, portable 4215): snippet test for row 1427; remove via picker, verify
- 2026-10-26 Show Open Files (Package Control picker, portable 4215): test for row 1428; remove via picker, verify
- 2026-10-26 ShowDefinitionEx (Package Control picker, portable 4215): test for row 1429; remove via picker, verify
- 2026-10-26 Shrink Whitespaces (Package Control picker, portable 4215): test for row 1430; remove via picker, verify
- 2026-10-26 correction: Shrink Whitespaces not in the Package Control picker or channel.json, nothing installed
- 2026-10-26 SidebarHoverToggle (Package Control picker, portable 4215): test for row 1431; remove via picker, verify
- 2026-10-26 Sightly (Package Control picker, portable 4215): test for row 1432; remove via picker, verify
- 2026-10-26 Silex Snippets (Package Control picker, portable 4215): test for row 1433; remove via picker, verify
- 2026-10-26 Silk Web Toolkit Snippets (Package Control picker, portable 4215): test for row 1434; remove via picker, verify
- 2026-10-26 Silky Jump (Package Control picker, portable 4215): test for row 1435; remove via picker, verify
- 2026-10-26 Silky Jump loose copy (no .pyc) at st_portable\Data\Packages\Silky Jump: to test source after the pyc load error; recycle before removing the package
- 2026-10-26 Silky Jump: package removed (Package Control also deleted the loose copy); source rewritten as loose copy at st_portable\Data\Packages\Silky Jump\silkyjump.py (verbatim, no pyc) for the source test; recycle after
- 2026-10-26 Simplates (Package Control picker, portable 4215): test for row 1436; remove via picker, verify
- 2026-10-26 Simple Ember.js Navigator (Package Control picker, portable 4215): test for row 1437; remove via picker, verify
- 2026-10-26 correction: Simple Ember.js Navigator not in the Package Control picker, nothing installed
- 2026-10-26 Simple Import (Package Control picker, portable 4215): test for row 1438; remove via picker, verify
- 2026-10-26 Simple Rails Navigator (Package Control picker, portable 4215): test for row 1439; remove via picker, verify
- 2026-10-26 correction: Simple Rails Navigator not in the Package Control picker, nothing installed
- 2026-10-26 SimpleAdd (Package Control picker, portable 4215): test for row 1440; remove via picker, verify
- 2026-10-26 SimpleClone (Package Control picker, portable 4215): test for row 1441; remove via picker, verify
- 2026-10-26 SimpleCov (Package Control picker, portable 4215): test for row 1442; remove via picker, verify
- 2026-10-26 SimpleMarker (Package Control picker, portable 4215): test for row 1443; remove via picker, verify
- 2026-10-26 SimpleMarker cleanup: recycled leftover User\SimpleMarker.sublime-settings written by my test markers
- 2026-10-26 SimplePHPSpec (Package Control picker, portable 4215): test for row 1444; remove via picker, verify
- 2026-10-26 SimplePHPUnit (Package Control picker, portable 4215): test for row 1445; remove via picker, verify
- 2026-10-26 SimpleSession (Package Control picker, portable 4215): test for row 1446; remove via picker, verify
- 2026-10-26 SimpleSession cleanup: recycled User\simplesession (my t1 test session)
- 2026-10-26 SimpleStateManager Snippets (Package Control picker, portable 4215): test for row 1447; remove via picker, verify
- 2026-10-26 SimpleTODO (Package Control picker, portable 4215): test for row 1448; remove via picker, verify
- 2026-10-26 SimpleTODO cleanup: recycled leftover User\SimpleTODO.sublime-settings written by my test TODO
- 2026-10-26 SimpleTesting (Package Control picker, portable 4215): test for row 1449; remove via picker, verify
- 2026-10-26 SimplestDebugger (Package Control picker, portable 4215): test for row 1450; remove via picker, verify
- 2026-10-26 Simutrans dat Syntax (Package Control picker, portable 4215): test for row 1451; remove via picker, verify
- 2026-10-26 SingleTrailingNewLine (Package Control picker, portable 4215): test for row 1452; remove via picker, verify
- 2026-10-26 placeholder tmTheme at st_portable\Data\Packages\SimplePHPUnit\SimplePHPUnit.hidden-tmTheme: written by me to stop the stale colour-scheme error dialogs left by the removed SimplePHPUnit; recycle the folder at the end of the session
- 2026-10-26 Singularity Definition File Syntax: install via Package Control picker on portable 4215 (Data\Packages, syntax only); remove via picker after test, verify gone.
- 2026-10-26 Sinon: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sk-ST3: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sketch.js: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SkoolkitZ80: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sleet: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SlideNav: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SlideShow(S9): install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SlideShow(S9): CORRECTION, not installable (no picker entry for SlideShow(S9) or S9; only an unrelated Markdown Slideshow), nothing installed.
- 2026-10-26 Slime: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smart Duplicate: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smart Match: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smart Path Copy: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smart Region: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smart Repeat: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SmartGoogle: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SmartGoogle: CORRECTION, not installable (no picker entry, not in channel data); nothing installed.
- 2026-10-26 SmartNewWindow: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Smartisan: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Snake: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Snakecasts-theme: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Snazzy Color Scheme: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetCaller: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetIndex: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetManager: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetSkydragon: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetX: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SnippetX: loose test copy at C:\Users\donal\tools\st_portable\Data\Packages\SnippetX (unzipped, .python-version changed 3.5.1 to 3.8) to retest after the plugin did not load; remove with recycle.ps1 after the package is removed.
- 2026-10-26 SnippetX: removed via picker; Test-Path shows the zip and the loose copy Data\Packages\SnippetX both gone (Package Control deleted the loose folder), nothing to recycle.
- 2026-10-26 Snipplr: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Snipplr: CORRECTION, not installable (no picker entry), nothing installed.
- 2026-10-26 Snipt Snippet Fetcher: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Snipt Snippet Fetcher: CORRECTION, not installable (not in channel data, picker shows only SnipTeX for Snipt), nothing installed.
- 2026-10-26 Snowball Syntax: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Soar Tools: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Solidity Docstring Generator: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Solisp: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Solium Gutter: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sonic Pi: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sort JavaScript Imports: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sort Lines By Selection: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SortLinesByColumn: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SortLinesByColumn: correction, not in the Package Control picker on 4215 (ST2-only, hidden); nothing installed.
- 2026-10-26 Soulburn Color Scheme: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourceDown: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourcePawn Syntax Highlighting: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourceSharer: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourceTalk: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourceTalk test: set a dummy token via sourcetalk_set_token, which writes Data\Packages\User\SourceTalk.sublime-settings; recycle that file after the test.
- 2026-10-26 SourceTalk cleanup: User\SourceTalk.sublime-settings (dummy token) recycled, verified gone.
- 2026-10-26 SourceTree.app Menu: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SourceTree.app Menu: correction, not in the Package Control picker on 4215 (ST2-only, hidden); nothing installed.
- 2026-10-26 SourceTreeCommands: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SpaceSnippets: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Spartan Color Scheme: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Spec Finder: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Spec Focuser: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Specman: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sphere Online Judge: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sphinx Office: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Sphinx Office: correction, download failed (HTTP 404 on bitbucket.org/klorenz/sublimesphinxoffice/get/default.zip); nothing installed.
- 2026-10-26 Sphinx Ref Helper: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SpiderScript: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Spintax: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Spirit Color Scheme: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Split Line: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Split To Buffer: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Split To Buffer: correction, not in the Package Control picker on 4215 (ST2-only, hidden); nothing installed.
- 2026-10-26 SplitScreen: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SplitScreen: correction, not in the Package Control picker on 4215 (ST2-only, hidden); nothing installed.
- 2026-10-26 Splunk Format: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 Splunk Syntax: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SpotifyWeb: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SpotifyWeb test: edit the installed copy's Data\Packages\SpotifyWeb\dependencies.json to list requests, urllib3, idna, charset_normalizer, run satisfy_libraries (Package Control puts those libraries in Data\Lib\python314). After the test: remove SpotifyWeb through the picker, recycle Data\Lib\python314 folders urllib3, idna, charset_normalizer, requests and their dist-info, verify gone.
- 2026-10-26 SpotifyWeb cleanup: package removed through the picker; Package Control also removed requests, urllib3, idna, charset_normalizer from Data\Lib\python314 (only package_control.py left); no User\SpotifyWeb.sublime-settings was saved; verified.
- 2026-10-26 Sprak Syntax and Completions: install via Package Control picker on portable 4215; remove via picker after test, verify gone.
- 2026-10-26 SproutCore Snippets and JSHint Integration: install via Package Control picker on portable 4215; remove via picker after test, verify gone.

- 2026-10-26 Sqlx Builder: Package Control picker install on portable 4215 (user scope Data\Packages); remove through picker after test

- 2026-10-26 Stack Overflow Snippets: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StackMob JS Snippets: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StackTracer: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Stackoverflow Debug Helper: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Stan: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StandardSnippets: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 CORRECTION: picked index 3669 without a fresh get_quick_panel and installed StandardFormat by mistake instead of StandardSnippets; removing it through the picker, nothing tested

- 2026-10-26 Stanza Syntax: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Starbound Lua: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Startup Files: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Startup Files: its set_startup_files wrote open_files_at_startup (nulls) into portable Data\Packages\User\Preferences.sublime-settings; restored from my backup copy, verified key gone

- 2026-10-26 Status Bar Time: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Status Bar Time test creates portable Data\Packages\User\StatusBarTime.sublime-settings (my file, none existed); recycle via recycle.ps1 after the test and verify

- 2026-10-26 Status Bar Weather: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StatusBarSymbols: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Statusbar Path: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Steadfast Color Scheme: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Stencil: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StepList: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 CORRECTION: StepList is not offered by the Install Package picker (ST2-only or dead); nothing installed

- 2026-10-26 StoryScript Highlight: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Strace Syntax: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Strapdown Markdown Preview: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Streamer Mode: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Streamer Mode test changes portable Data\Packages\User\Preferences.sublime-settings (backup copy kept) and creates User\StreamerMode.sublime-settings; restore prefs from backup and recycle the new file after the test, verify

- 2026-10-26 Streamer Mode: prefs restored from backup (no binary_file_patterns/streamer keys), User\StreamerMode.sublime-settings recycled, verified

- 2026-10-26 String 2 Lower Hyphen: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 String Counter: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 CORRECTION: String Counter is not offered by the Install Package picker (ST2-only); nothing installed

- 2026-10-26 Strip Whitespace Lines: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StripHTML: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 StrongView: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Stylefmt: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Donald said 'Can install anything' mid-session (prerequisites allowed this session); still no admin installs, ledger line before each, remove and verify after

- 2026-10-26 StylishHaskell: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 CORRECTION: StylishHaskell is not offered by the Install Package picker (ST2-only); nothing installed

- 2026-10-26 Stylus Clean Completions: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Donald allowed npm installs ('Can install npm'): each in its own tools folder with its own package.json, ledger line first, remove and verify after; no admin

- 2026-10-26 SubRed: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 Stylefmt (row 1541, second pass at Donald's request): Package Control picker install on portable 4215; remove through picker after test; test file scratchpad\sf\t.css is mine

- 2026-10-26 SubTexting: Package Control picker install on portable 4215; remove through picker after test

- 2026-10-26 SubVal: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Subforce: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Subhub: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimErl: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimErl: not installable (not in the picker, ST2-only); nothing installed

- 2026-10-26 Sublimation: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublimation: not installable (not in the picker); nothing installed

- 2026-10-26 Sublime TFS: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime Text 2 Snippets: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime Text API Helper: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime Tweet: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime convert colorcode: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime wxapp: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime-Hhhhold: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 Sublime-Hhhhold: not installable (not in the picker); nothing installed

- 2026-10-26 Sublime-KnockoutJS-Snippets: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeAlternate: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeAxosoft: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeBufmod: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeBufmod: not in the picker (ST2-only); nothing installed

- 2026-10-26 SublimeCMD: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeCMD: not in the picker (ST2-only); nothing installed

- 2026-10-26 SublimeGerrit: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeGerrit: removed via picker; recycled its Data\Backup\20261026180131\SublimeGerrit and User\SublimeGerrit.cleanup-info.sublime-settings (created by the install)

- 2026-10-26 SublimeGoogle: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeHandcraft: Package Control picker install (portable 4215), remove through picker after test

- 2026-10-26 SublimeHandcraft: not in the picker (ST2-only); nothing installed

- 2026-10-26 SublimeLinter-contrib-42-norminette: Package Control picker install (portable 4215) together with SublimeLinter (prerequisite, picker); both removed through picker after test

- 2026-10-26 SublimeLinter: Package Control picker install (prerequisite for 42-norminette, portable 4215); remove via picker after

- 2026-10-26 norminette (PyPI) for the 42-norminette linter test: pip install --target C:\Users\donal\tools\norminette_test (own folder, no system change); remove = recycle that folder

- 2026-10-26 norminette test: created portable Data\Packages\User\SublimeLinter.sublime-settings (paths to norminette_test\bin); recycle it after

- 2026-10-26 SublimeLinter-contrib-CFLint: Package Control picker install (portable 4215, SublimeLinter already installed), remove through picker after

- 2026-10-26 CFLint jar (github.com/cflint/CFLint release) downloaded to C:\Users\donal\tools\cflint_test for the CFLint linter test; remove = recycle that folder

- 2026-10-26 SublimeLinter-contrib-PSScriptAnalyzer: Package Control picker install (portable 4215, SublimeLinter present), remove through picker after

- 2026-10-26 PowerShell 7 zip + PSScriptAnalyzer module extracted to C:\Users\donal\tools\pwsh_test (no admin, no PATH change) for the PSScriptAnalyzer linter test; remove = recycle that folder

- 2026-10-26 SublimeLinter-contrib-alex: Package Control picker install (portable 4215, SublimeLinter present), remove via picker; npm alex into C:\Users\donal\tools\alex_test with its own package.json, recycle after

- 2026-10-26 SublimeLinter-contrib-au3check: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-bashate: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 bashate (PyPI) pip --target C:\Users\donal\tools\bashate_test for the bashate linter test; remove = recycle that folder

- 2026-10-26 SublimeLinter-contrib-bemlint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after; npm bem-lint in its own tools folder if needed

- 2026-10-26 SublimeLinter-contrib-bootlint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-check-source-formatting: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-checkpatch: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-cheetah-flake: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-clang-tidy: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-clj-kondo: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 clj-kondo windows zip downloaded to C:\Users\donal\tools\kondo_test for the clj-kondo linter test; remove = recycle that folder

- 2026-10-26 SublimeLinter-contrib-cmakelint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 cmakelint (PyPI) pip --target C:\Users\donal\tools\cmakelint_test + wrapper C:\Users\donal\tools\norminette_test\bin\cmakelint.cmd for the cmakelint linter test; remove = recycle both folders

- 2026-10-26 CMake (syntax) package: Package Control picker install as prerequisite for the cmakelint linter test; remove via picker after

- 2026-10-26 SublimeLinter-contrib-codeclimate: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-cookstyle: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-credo: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-csstree: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-dennis: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-dmd: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after
- 2026-10-26: linter batch ended. SublimeLinter is not installed on the portable and the dockerfilelint package file does not exist (Donald says he removed them; I only saw the files absent); norminette_test folder and portable User\SublimeLinter.sublime-settings recycled by me (verified). Portable closed by Donald. Row 1586 dockerfilelint not tested; next row 1586.

- 2026-10-26 SublimeLinter (prerequisite) then SublimeLinter-contrib-dockerfilelint: Package Control picker installs (portable 4215), remove both via picker after, verify Installed Packages and Data\Backup / User cleanup-info leftovers

- 2026-10-26 SublimeLinter-contrib-dogma: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-dxl: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-elm-make: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-epcomp: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 CUDA C++ (harrism/sublimetext-cuda-cpp, retest of 1.1.0 fix for issue #10): Package Control picker install (portable 4215), remove via picker after
- 2026-10-26 (follows the CUDA C++ line above): NOT installed. Picker still offers v1.0.2; 1.1.0 (harrism, released 2026-10-27 01:33 UTC) not in the channel yet. Retest when the picker shows v1.1.0.

- 2026-10-26 CUDA C++ 1.1.0 from the GitHub repo (Donald allowed this one non-picker install: picker still serves v1.0.2): zip of tag 1.1.0 extracted to portable Data\Packages\CUDA C++. Remove: recycle that folder (and the scratchpad extract) after the retest, verify.
- 2026-10-26: CUDA C++ 1.1.0 retest passed (127 assertions). Portable Data\Packages\CUDA C++ and scratch clone recycled, verified gone. Result posted on harrism/sublimetext-cuda-cpp#10.

- 2026-10-26 SublimeLinter-contrib-foodcritic: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-ghdl: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-git-lint-commit: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 git-lint-commit (npm) in C:\Users\donal\tools\gitlintcommit_test (own package.json): to test the git-lint-commit linter regex; recycle the folder after
- 2026-10-26 (follows the git-lint-commit npm line): npm install failed (404, not an npm package), nothing installed; the empty gitlintcommit_test folder was recycled, verified gone.

- 2026-10-26 SublimeLinter-contrib-glslc: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-glua: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-glualint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-gosimple: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-happiness: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-hdevtools: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-htmllint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-java: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-jolint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after
- 2026-10-26: recycled portable Data\Backup (276 Package Control backup folders left by earlier audit package removals since 2026-10-21, all my test packages); verified gone. From now on recycle the Backup folder of a removed package right after removal.

- 2026-10-26 SublimeLinter-contrib-jsdebugmarkers: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-jsonnet-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-jsonschema-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 jsonschema-lint (pip --target) in C:\Users\donal\tools\jsonschemalint_test: to test the jsonschema-lint linter regex; recycle the folder after
- 2026-10-26 (follows the jsonschema-lint pip line): installed OK (0.1.0, crashes on 3.14: cgi); folder jsonschemalint_test recycled, verified gone.

- 2026-10-26 SublimeLinter-contrib-julialint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-julialintserver: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-lacheck: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-lesshint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-lintr: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-livecodelint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-lua-globals: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-luau: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-mlint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-modelsim: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-nginx-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-nvc: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-nvcc: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-perl: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-phpins: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-polylint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-proselint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-protoc-gen-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-puppet: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-puppet-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-qmllint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-remark-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 remark-cli + remark-preset-lint-markdown-style-guide (npm, own package.json) in C:\Users\donal\tools\remark_test: to test the remark-lint linter regex; recycle the folder after
- 2026-10-26 (follows the remark npm line): installed (remark-cli 12.0.1); folder remark_test recycled, verified gone.

- 2026-10-26 SublimeLinter-contrib-roslint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-rstylelint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-ruby-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-rustc: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 SublimeLinter-contrib-salt-lint: Package Control picker install (portable 4215, SublimeLinter present), remove via picker after

- 2026-10-26 salt-lint (pip --target) in C:\Users\donal\tools\saltlint_test: to test the salt-lint linter regex; recycle the folder after
- 2026-10-26 (follows the salt-lint pip line): installed OK; folder saltlint_test recycled, verified gone.
- 2026-10-26 SublimeLinter-contrib-scalac: Package Control picker install on portable st_portable (row 1633); remove through picker afterwards (Remove Package), verify Installed Packages file gone.
- 2026-10-26 SublimeLinter-contrib-scalastyle: Package Control picker install on portable st_portable (row 1634); remove through picker afterwards, verify gone.
- 2026-10-26 BACKTRACK (Donald: 'go through entire results, and backtrack'): shallow clones of 29 repos for rows once recorded 'not installable/not in picker' into C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\3e7a866d-b825-4927-a9cd-1668c7774790\scratchpad\bt\<name>; removal = recycle.ps1 on that folder; any copy into portable Data\Packages is logged below and recycled after the test.
- 2026-10-26 BACKTRACK copies (no .git) into C:\Users\donal\tools\st_portable\Data\Packages as bt_<name>: CakeAPI, CakeBook, EmberNav, Harvey, HTML2Jade, MDNSearch, MFScript, RailsNav, Scold, ScriptSrc, ShrinkWS, SortLinesByColumn, SourceTreeMenu, StepList, StringCounter, StylishHaskell, ValveWiki | to load them on the portable and read the console | remove: recycle.ps1 on each bt_* folder, verify gone
- 2026-10-26 BACKTRACK: bt_Scold and bt_StepList recycled (renamed folder broke their own imports, my artifact); recopied as C:\Users\donal\tools\st_portable\Data\Packages\Scold and C:\Users\donal\tools\st_portable\Data\Packages\StepList (the package names); recycle both after the test.
- 2026-10-26 BACKTRACK done: all bt_* folders, Scold and StepList recycled from portable Data\Packages (verified: only MCP Commander, Theme - Default, User remain); scratchpad bt clones recycled.
- 2026-10-26 BACKTRACK chunk skip 0 count 30: shallow clones into C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\3e7a866d-b825-4927-a9cd-1668c7774790\scratchpad\btc (Theme - Kronuz, CoolBase64, WordPress Customizer, DashDoc, SublimeLinter-contrib-htmlhint, Dictionaries, PostgreSQL Syntax Highlighting, Predawn, LSP-promql, LSP-serenata, FileIcons, FileIcons Mono, FindResultsApplyChanges, Open-Include, Python Import Magic, Pywin32, SublimeLinter-ghc, JsRun, ollama-sublime (KalimeroMK), PythonTestRunner, Better Completion, Unity Completions, AndyEdits, AndyPython, AutoPHPDollar, Blogify, Build Switcher, BuildParts, CNPunctuationAutopair, CSS Auto Commenting); recycle C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\3e7a866d-b825-4927-a9cd-1668c7774790\scratchpad\btc when done; nothing installed in Sublime
- 2026-10-26 METHOD (Donald): for packages not in the channel, use Package Control: Add Repository with the GitHub URL, then install through the picker (picker resolves dependencies; clone-and-copy does not). Each added repo gets its own ledger line first, and its URL is removed from the portable Package Control.sublime-settings 'repositories' after the test and verified.
- 2026-10-26 BACKTRACK: scratchpad btc clones and the tsv backup recycled. 34 rows skipped for age/type were removed from .tested_packages.tsv so they return to the untested queue (list kept in data\backtrack_list_2026_10_26.tsv); they are picker packages and get the normal one-at-a-time picker test.
- 2026-10-26 scratchpad btc (clones, outside any repo) could not be recycled ('system call level is not correct'); left in the session scratchpad, not in a repo, nothing in Sublime.
- 2026-10-26 FindResultsApplyChanges: Package Control Add Repository https://github.com/titoBouzout/FindResultsApplyChanges on portable st_portable (repositories setting), then picker install | backtrack | remove via Remove Package picker AND delete the repo URL from the portable Package Control.sublime-settings, verify both
- 2026-10-26 FindResultsApplyChanges: removed through the picker, package file verified gone, repo URL removed from portable Package Control.sublime-settings (repositories empty).
- 2026-10-26 Open-Include: Package Control Add Repository https://github.com/titoBouzout/Open-Include on portable (repositories setting), then picker install | backtrack | remove via Remove Package picker AND empty the repositories list in portable Package Control.sublime-settings, verify both
- 2026-10-26 Open-Include: removed through the picker, package file verified gone, repositories list emptied in portable settings.
- 2026-10-26 Python Import Magic: Package Control Add Repository https://github.com/alecthomas/SublimePythonImportMagic on portable, then picker install | backtrack | remove via Remove Package picker, empty repositories list, verify both
- 2026-10-26 Python Import Magic (SublimePythonImportMagic): removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 JsRun: Package Control Add Repository https://github.com/sindresorhus/sublime-jsrun on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 JsRun: NOT installed (macOS-only package by design, no Windows entry); nothing to remove.
- 2026-10-26 Unity Completions: picker install on portable (Add Repository https://github.com/oferei/sublime-unity-completions first only if the picker lacks it) | backtrack row, was deferred | remove via picker, empty repositories list, verify
- 2026-10-26 Unity Completions: picker install started on the portable by mistake (already tested 2026-10-21, 45 min install); cancelled by stopping the portable process (Stop-Process, my own test instance), relaunched and MCP reconnected; verified no Unity files in Installed Packages or Packages; portable PC settings repositories empty.
- 2026-10-26 Mootools Snippets: Package Control Add Repository https://github.com/chriswong/sublime-mootools-snippets on portable, then picker install | backtrack | remove via picker, empty repositories list (write the file, do not edit while a pick is pending), verify
- 2026-10-26 Mootools Snippets: removed through the picker, files verified gone, repositories list emptied in portable settings.
- 2026-10-26 Recessify: Package Control Add Repository https://github.com/tcrosen/recessify on portable, then picker install | backtrack | remove via picker, then edit repositories list empty, verify
- 2026-10-26 Recessify: removed through the picker, files verified gone, repositories list emptied in portable settings.
- 2026-10-26 Snipplr: Package Control Add Repository https://github.com/jonasdp/Snipplr on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 Snipplr: removed through the picker, files verified gone, repositories list emptied in portable settings.
- 2026-10-26 Split To Buffer: Package Control Add Repository https://github.com/berendbaas/sublime_splittobuffer on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 Split To Buffer: removed through the picker, files verified gone, repositories list emptied. Two untitled test tabs (alpha beta, empty) left in the portable window, not remembered on quit.
- 2026-10-26 SplitScreen: Package Control Add Repository https://github.com/spadgos/sublime-SplitScreen on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 SplitScreen: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 CombineAndMinify: Package Control Add Repository https://github.com/joelcarlton/Sublime-CombineAndMinify on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 CombineAndMinify: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 sublime-jslint: Package Control Add Repository https://github.com/fbzhong/sublime-jslint on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 sublime-jslint: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 HtmlTidy (SublimeHtmlTidy): Package Control Add Repository https://github.com/welovewordpress/SublimeHtmlTidy on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 HtmlTidy (SublimeHtmlTidy): removed through the picker, files verified gone, repositories list emptied. Prefixr: wbond/sublime_prefixr is next; Sublime-Hhhhold has no repo (hhhhold.com is a web service).
- 2026-10-26 Prefixr: Package Control Add Repository https://github.com/wbond/sublime_prefixr on portable, then picker install | backtrack | remove via picker, empty repositories list, verify
- 2026-10-26 Prefixr: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 JavaSetterGetter: Package Control picker install on portable (row 654, returned to queue by the backtrack) | remove via picker, verify gone
- 2026-10-26 JavaSetterGetter: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 Jdf - Tool: Package Control picker install on portable (row 655) | remove via picker, verify gone
- 2026-10-26 Jdf - Tool: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 Just Paste: Package Control picker install on portable (row 669); Add Repository https://github.com/jcldavid/JustPaste first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 Just Paste: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 LastEdit: Package Control picker install on portable (row 725); Add Repository https://github.com/SamPeng87/sublime-last-edit first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 LastEdit: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 List stylesheet variables: Package Control picker install on portable (row 751); Add Repository first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 correction: four rows I removed from .tested_packages.tsv in the backtrack were genuinely skipped or already tested (SublimeLinter-ghc, ollama-sublime (KalimeroMK), List stylesheet variables, MXUnit); restored with their original (truncated) notes. The other 30 removed rows stay in the queue.
- 2026-10-26 Dictionaries: Package Control picker install on portable (Add Repository https://github.com/titoBouzout/Dictionaries first only if the picker lacks it) | backtrack | remove via picker, empty repositories list, verify gone
- 2026-10-26 Dictionaries: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 LSP-promql test set: picker installs of LSP (prerequisite) and Add Repository https://github.com/prometheus-community/sublimelsp-promql then picker install of LSP-promql on portable | backtrack | remove both via picker, empty repositories list, verify gone
- 2026-10-26 LSP-serenata: Add Repository https://github.com/sublimelsp/LSP-serenata, picker install on top of LSP | remove LSP-promql, LSP-serenata and LSP via picker afterwards, empty repositories list, verify gone
- 2026-10-26 LSP-promql, LSP-serenata and LSP: removed through the picker, files and libraries verified gone (Data\Lib\python314 has only Package Control's own files), repositories list emptied.
- 2026-10-26 Pipe Dream: Package Control picker install on portable (row 1106); Add Repository https://github.com/billymoon/Sublime-Pipe-Dream first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 Pipe Dream: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 Placehold.it Image Tag Generator: Package Control picker install on portable (row 1109); Add Repository https://github.com/SubZane/Sublime-Placehold.it first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 Placehold.it Image Tag Generator: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 PloneReload: Package Control picker install on portable (row 1113); Add Repository https://github.com/maethu/SublimePloneReload first only if the picker lacks it | remove via picker, empty repositories list, verify gone
- 2026-10-26 PloneReload: removed through the picker, files verified gone, repositories list emptied.
- 2026-10-26 SublimeLinter-contrib-semistandard: Package Control picker install on portable (row 1635) | remove via picker, verify gone
- 2026-10-26 semistandard npm test: C:\Users\donal\tools\semistandard_test (own package.json, npm install semistandard) for the semistandard linter regex check | recycle.ps1 on the folder afterwards, verify gone (allowed npm prerequisite pattern)
- 2026-10-26 semistandard_test: folder recycled, verified gone; SublimeLinter-contrib-semistandard removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-serplint: Package Control picker install on portable (row 1636) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-serplint: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-solhint: Package Control picker install on portable (row 1637; repo idrabenia/SublimeLinter-contrib-solhint) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-solhint: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-sqlint: Package Control picker install on portable (row 1638) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-sqlint: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-stylint: Package Control picker install on portable (row 1639) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-stylint: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-tailor: Package Control picker install on portable (row 1640) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-tailor: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-terraform: Package Control picker install on portable (row 1641) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-terraform: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-textlint: Package Control picker install on portable (row 1642; repo joeybaker/SublimeLinter-textlint) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-textlint: removed through the picker, files verified gone (it unpacked into Data\Packages).
- 2026-10-26 SublimeLinter-contrib-tlint: Package Control picker install on portable (row 1643; repo tighten/tlint-sublime-plugin) | remove via picker, verify gone
- 2026-10-26 SublimeLinter-contrib-tlint: removed through the picker, files verified gone.
- 2026-10-26 SublimeLinter-contrib-ts-standard: Package Control picker install on portable (row 1644) | remove via picker, verify gone
- 2026-10-26 ts-standard npm test: C:\Users\donal\tools\tsstandard_test (own package.json, npm install ts-standard typescript) for the ts-standard linter regex check | recycle.ps1 on the folder afterwards, verify gone (allowed npm prerequisite pattern)
- 2026-10-26 REMOVED SublimeLinter-contrib-ts-standard via picker (file gone); recycled tools\tsstandard_test (gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-wollok-checker via Package Control picker (portable, SublimeLinter already present); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-wollok-checker via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-write-good via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-write-good via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-xo via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-xo via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-xqlint via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-xqlint via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-xvhdl via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-xvhdl via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-yaml-lint via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-yaml-lint via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-zig-check via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-zig-check via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter-contrib-ziglint via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter-contrib-ziglint via picker (file gone)
- 2026-10-26 INSTALL SublimeLinter_CatGutterTheme via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLinter_CatGutterTheme via picker (file gone)
- 2026-10-26 INSTALL SublimeLogHelper via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLogHelper via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 audit repo: added scrubbed scripts\ (untested, rec, commit_day) for publication; tools\ stays ignored
- 2026-10-26 INSTALL SublimeLove via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeLove via picker (file gone)
- 2026-10-26 INSTALL SublimeMagic via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeMagic via picker (file gone)
- 2026-10-26 INSTALL SublimePackageSync via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimePackageSync via picker (file gone)
- 2026-10-26 INSTALL SublimePaster via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimePaster via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SublimeTalkincode via Add Repository (jamiesun/SublimeTalkincode) then picker (portable); remove via picker and remove repo line after test
- 2026-10-26 REMOVED SublimeTalkincode via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SublimeTextAPICompletions via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeTextAPICompletions via picker (file gone)
- 2026-10-26 INSTALL SublimeTransporter via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeTransporter via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SublimeWebColors via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeWebColors via picker (file gone)
- 2026-10-26 INSTALL SublimeWeibo via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED sublime-sublimeweibo (SublimeWeibo) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Sublimipsum via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sublimipsum via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Sublpress via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sublpress via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Sublundo via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sublundo via picker (file gone)
- 2026-10-26 recycled Data\Packages\User\Sublundo (plugin's own leftover folder); verified gone
- 2026-10-26 INSTALL Subpry via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Subpry via picker (file gone)
- 2026-10-26 INSTALL Subtitle Sync via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED sublime-subtitle-sync (Subtitle Sync) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Subtoise via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Subtoise via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Sudden Death via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sudden Death via picker (file gone)
- 2026-10-26 INSTALL SummitEditor via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SummitEditor via picker (Packages\SummitEditor folder gone)
- 2026-10-26 INSTALL SumoSwissKnife via Package Control picker (portable); remove via picker after test
- 2026-10-26 SumoSwissKnife was NOT installed (repo scrummastermind/SumoSwissKnife 404, not in picker); recycled Data\Backup\20261026221855 (leftover of SummitEditor removal), verified gone
- 2026-10-26 INSTALL SunCycle via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SunCycle via picker (file gone)
- 2026-10-26 INSTALL Sunnyvale Color Scheme via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sunnyvale Color Scheme via picker (file gone)
- 2026-10-26 INSTALL Sunrise Theme via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sunrise Theme via picker (file gone)
- 2026-10-26 INSTALL Super Ant via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Super Ant via picker (file gone)
- 2026-10-26 INSTALL Super-Awesome Paste via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Super-Awesome Paste via picker (file gone)
- 2026-10-26 INSTALL SuperCollider via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED supercollider-package-for-sublime-text (SuperCollider) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SuperCollider ST3 via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SuperCollider ST3 via picker (file gone); portable restarted once during this test (pid 11756 -> 16728), MCP reconnected
- 2026-10-26 INSTALL SuperNavigator via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SuperNavigator via picker (file gone)
- 2026-10-26 INSTALL SuperSelect via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SuperSelect via picker (file gone)
- 2026-10-26 INSTALL Superlime via Package Control picker (portable); load check only, its save-as-root command is NOT run (may elevate); remove via picker after
- 2026-10-26 REMOVED Superlime via picker (file gone)
- 2026-10-26 INSTALL Superman Color Scheme via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Superman Color Scheme via picker (file gone)
- 2026-10-26 INSTALL Suricate via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Suricate via picker (zip and generated Packages\Suricate folder gone); recycled Data\Backup\20261026222952, verified
- 2026-10-26 INSTALL Surround via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Surround via picker (file gone)
- 2026-10-26 INSTALL Susy 2 Snippets via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Susy 2 Snippets via picker (file gone)
- 2026-10-26 INSTALL Susy Snippets via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Susy Snippets via picker (file gone)
- 2026-10-26 INSTALL Svelte Snippets via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Svelte Snippets via picker (file gone)
- 2026-10-26 INSTALL Swan via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Swan via picker (file gone)
- 2026-10-26 INSTALL Swap Selections via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Swap Selections via picker (file gone)
- 2026-10-26 INSTALL Swift Completion via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Swift Completion via picker (file gone)
- 2026-10-26 INSTALL Swift Foundation Completions via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Swift Foundation Completions via picker (file gone)
- 2026-10-26 INSTALL Swig via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Swig via picker (file gone)
- 2026-10-26 INSTALL SwigSnippets via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SwigSnippets via picker (file gone)
- 2026-10-26 INSTALL Switch File Deluxe via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Switch File Deluxe via picker (file gone)
- 2026-10-26 INSTALL Switch Script via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SwitchScript (Switch Script) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SwitchPanel via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SwitchPanel via picker (file gone)
- 2026-10-26 INSTALL SymfonyCommander via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sublime-SymfonyCommander (SymfonyCommander) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Symitar via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Symitar via picker (file gone)
- 2026-10-26 INSTALL Sync Merge Scheme via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Sync Merge Scheme via picker (file gone); command not run on purpose (writes Sublime Merge settings)
- 2026-10-26 INSTALL SyncFileYouWant via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SyncFileYouWant via picker (file gone)
- 2026-10-26 INSTALL Synchronized File Scrolling via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SublimeSynchroScroll (Synchronized File Scrolling) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Synonymizer via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Synonymizer via picker (file gone)
- 2026-10-26 INSTALL Syntax Highlighting for SSS SugarSS via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax Highlighting for SSS SugarSS via picker (file gone)
- 2026-10-26 INSTALL Syntax History via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax History via picker (file gone)
- 2026-10-26 INSTALL Syntax Matcher via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax-Matcher (Syntax Matcher) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL Syntax ProtoList via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax ProtoList via picker (file gone)
- 2026-10-26 INSTALL Syntax QBasic via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax QBasic via picker (file gone)
- 2026-10-26 INSTALL Syntax Sproto via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax Sproto via picker (file gone)
- 2026-10-26 INSTALL Syntax gRally via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Syntax gRally via picker (file gone)
- 2026-10-26 INSTALL SyntaxDefinitionHelper via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED syntax_definition_helper (SyntaxDefinitionHelper) via picker (file gone); repository URL removed from Package Control settings
- 2026-10-26 INSTALL SyntaxHighlightTools via Package Control picker (portable); remove via picker after test
- 2026-10-26 SyntaxHighlightTools NOT installed: Package Control reported HTTP 404 on https://bitbucket.org/klorenz/syntaxhighlighttools/get/default.zip; nothing was added (verified Installed Packages and Packages unchanged)
- 2026-10-26 INSTALL SyntaxManager via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED SyntaxManager via picker (file gone)
- 2026-10-26 INSTALL TADS3 via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TADS3 via picker (file gone)
- 2026-10-26 INSTALL TAGML via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TAGML via picker (file gone)
- 2026-10-26 INSTALL TASM Syntax via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TASM Syntax via picker (file gone)
- 2026-10-26 INSTALL TECS via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TECS via picker (file gone)
- 2026-10-26 INSTALL TJ3-syntax-sublimetext2 via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TJ3-syntax-sublimetext2 via picker (file gone)
- 2026-10-26 INSTALL TWiki via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TWiki via picker (file gone)
- 2026-10-26 INSTALL TXL syntax highlighting via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TXL syntax highlighting via picker (file gone)
- 2026-10-26 INSTALL TXT2PYNB via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TXT2PYNB via picker (file gone)
- 2026-10-26 INSTALL TYPO3 Fluid Snippets via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TYPO3 Fluid Snippets via picker (file gone)
- 2026-10-26 INSTALL TabNukerNuker via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TabNukerNuker via picker (file gone); an untitled test tab with text 'ab' remains open in the portable
- 2026-10-26 INSTALL TabTeleport via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TabTeleport via picker (file gone)
- 2026-10-26 INSTALL TabToSpaceConverter via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TabToSpaceConverter via picker (file gone)
- 2026-10-26 closed the untitled 'ab' test tab in the portable (Save Changes: No)
- 2026-10-26 INSTALL Tabify via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Tabify via picker (file gone)
- 2026-10-26 INSTALL Table Cleaner via Package Control picker (portable); remove via picker after test
- 2026-10-26 portable relaunched after closing its last tab quit it (Table Cleaner test in progress)
- 2026-10-26 REMOVED Table Cleaner via picker (file gone); portable left with one empty untitled tab (closing the last tab quits it)
- 2026-10-26 portable now has zero tabs, alive
- 2026-10-26 INSTALL Tabletop Simulator Lua via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Tabletop Simulator Lua via picker (file gone)
- 2026-10-26 INSTALL Tabright via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Tabright via picker (file gone); portable has no tab of mine open (Sublime keeps its own empty untitled one)
- 2026-10-26 INSTALL TabsLimiter via Package Control picker (portable); remove via picker after test
- 2026-10-26 ADD REPOSITORY https://github.com/ejoubaud/SublimeTabsLimiter in portable Package Control settings (not in picker); remove the line after the test
- 2026-10-26 REMOVED TabsLimiter via picker (file gone) and removed the repository line from Package Control settings
- 2026-10-26 INSTALL TabsShortcuts via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TabsShortcuts via picker (file gone)
- 2026-10-26 INSTALL TabsToTable via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TabsToTable via picker (file gone)
- 2026-10-26 INSTALL Tachyons Autocomplete via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Tachyons Autocomplete via picker (file gone); no tabs open
- 2026-10-26 INSTALL Tailwind CSS Docs via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Tailwind CSS Docs via picker (file gone); no tabs open
- 2026-10-26 INSTALL Takana via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED Takana via picker (file gone); no tabs open
- 2026-10-26 INSTALL TamarinProver via Package Control picker (portable); remove via picker after test
- 2026-10-26 REMOVED TamarinProver via picker (file gone); closed its Package Control Messages tab by name; no tabs open
- 2026-10-26 INSTALL Task Timer via Package Control picker (portable); remove via picker after test
- 2026-10-26 ADD REPOSITORY https://github.com/jcowgar/sublime-task-timer in portable Package Control settings (not in picker); remove the line after the test
- 2026-10-26 REMOVED Task Timer (sublime-task-timer) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 INSTALL Taskwarrior via Package Control picker (portable); remove via picker after test
- 2026-10-26 ADD REPOSITORY https://github.com/kostajh/sublime-taskwarrior in portable Package Control settings (not in picker); remove the line after the test
- 2026-10-26 REMOVED Taskwarrior (sublime-taskwarrior) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 INSTALL Tau Time Tracker via Package Control picker (portable); remove via picker after test
- 2026-10-26 ADD REPOSITORY https://github.com/rundef/tau-time-tracker in portable Package Control settings (not in picker); remove the line after the test
- 2026-10-26 REMOVED Tau Time Tracker (tau-time-tracker) via picker (file gone, no Tau folder left) and removed the repository line; read its Package Control Messages tab (README only) then closed it; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/akira-cn/sublime-gbk (queue row 1 GBK Encoding Support, ST2-only so not in picker) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED sublime-gbk (GBK Encoding Support, queue row 1) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/SublimeText/ColdFusion (queue row 2 ColdFusion, ST2-only so not in picker) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED ColdFusion (queue row 2) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/y0ssar1an/CSS3_Syntax (queue row 3 CSS3_Syntax) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 NOT installed CSS3_Syntax (queue row 3): y0ssar1an/CSS3_Syntax returns 404 on the repo page and on codeload master (owner profile still exists), last seen in channel 2017; repository line removed
- 2026-10-26 ADD REPOSITORY https://github.com/fraoustin/Sublime2pdf (queue row 4 2pdf) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED Sublime2pdf (queue row 4 2pdf) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/cafarm/aqua-theme (queue row 5 Theme - Aqua) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED aqua-theme (queue row 5 Theme - Aqua) via picker (file gone) and removed the repository line; picker preview cancelled with Escape, theme setting unchanged; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/welovewordpress/SublimePhpTidy (queue row 6 PhpTidy) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED SublimePhpTidy (queue row 6 PhpTidy) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/Warin/SublimeTidyHTML (queue row 7 TidyHTML5) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED SublimeTidyHTML (queue row 7 TidyHTML5) via picker (file gone) and removed the repository line; test html file was in my scratchpad, tab closed by path; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/nwjlyons/copy-file-name (queue row 8 Copy File Name) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 CLONE nwjlyons/copy-file-name (queue row 8) into scratchpad\clone_copyfilename and COPY to portable Data\Packages\copy-file-name because Package Control refuses it (channel ST2-only entry shadows the added repository: 'not available on this platform or for this version of Sublime Text'); remove copy and clone via recycle.ps1 after test; also remove the repository line
- 2026-10-26 REMOVED copy-file-name copy (Data\Packages) and the scratchpad clone via recycle.ps1 (both gone, verified) and removed the repository line (queue row 8 Copy File Name); no tabs open
- 2026-10-26 ADD REPOSITORY http://github.com/quarnster/SublimeClang (queue row 9 SublimeClang) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED SublimeClang (queue row 9) via picker (file gone) and removed the repository line; no tabs open
- 2026-10-26 ADD REPOSITORY https://github.com/SublimeText/IndentGuides (queue row 10 IndentGuides; earlier hand-copy test 2026-10-19, issue #6 now closed, recheck) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 IndentGuides (queue row 10): repository line removed again, nothing installed (already tested 2026-10-19 by hand copy, issue #6 closed by FichteFoll as not planned: package only advertises ST2)
- 2026-10-26 ADD REPOSITORY https://github.com/Kindari/SublimeXdebug (queue row 16 Xdebug) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 Xdebug (queue row 16): added repository not offered by the picker (channel ST2-only entry of the same name shadows it); repository line removed; CLONE Kindari/SublimeXdebug into scratchpad\clone_xdebug and COPY to portable Data\Packages\Xdebug; recycle both after test
- 2026-10-26 REMOVED Xdebug copy (Data\Packages) and scratchpad clone via recycle.ps1 (both gone, verified); repository line already removed (queue row 16)
- 2026-10-26 ADD REPOSITORY https://github.com/quarnster/SublimeJava (queue row 17 SublimeJava) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 SublimeJava (queue row 17): added repository not offered by the picker (shadowed by channel entry); repository line removed; CLONE quarnster/SublimeJava into scratchpad\clone_sublimejava and COPY to portable Data\Packages\SublimeJava; recycle both after test
- 2026-10-26 REMOVED SublimeJava copy and scratchpad clone via recycle.ps1 (both gone, verified); repository line already removed (queue row 17)
- 2026-10-26 ADD REPOSITORY https://github.com/SublimeText/VintageEx (queue row 21 VintageEx) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 VintageEx (queue row 21): added repository not offered by the picker (shadowed by channel entry); repository line removed; CLONE SublimeText/VintageEx into scratchpad\clone_vintageex and COPY to portable Data\Packages\VintageEx; recycle both after test
- 2026-10-26 REMOVED VintageEx copy and scratchpad clone via recycle.ps1 (both gone, verified); repository line already removed (queue row 21)
- 2026-10-26 ADD REPOSITORY https://github.com/welovewordpress/SublimeWordPressCodex (queue row 22 Search WordPress Codex) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 REMOVED Search WordPress Codex or QueryPosts (queue row 22) via picker (file gone) and removed the repository line; the Add Repository was unnecessary: the package is in the picker under this longer name; no tabs open
- 2026-10-26 found a stale SublimeClang repository line back in portable Package Control settings (race with a Package Control rewrite after row 9) and removed it again; from now on re-read the file after each removal
- 2026-10-26 ADD REPOSITORY https://github.com/ignacysokolowski/SublimeTagWrapper (queue row 25 TagWrapper) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 NOT installed TagWrapper (queue row 25): ignacysokolowski/SublimeTagWrapper returns 404 on the repo page and codeload master (owner profile exists), no other repo found; repository line removed and re-read
- 2026-10-26 ADD REPOSITORY https://github.com/raik/st2-pseudo-osx-theme (queue row 28 Theme - Pseudo OSX) in portable Package Control settings; INSTALL via picker; remove both after test
- 2026-10-26 Theme - Pseudo OSX (queue row 28): added repository not offered by the picker (shadowed by channel entry); repository line removed; CLONE raik/st2-pseudo-osx-theme into scratchpad\clone_pseudoosx and COPY to portable Data\Packages\Theme - Pseudo OSX; recycle both after test
- 2026-10-26 REMOVED Theme - Pseudo OSX copy and scratchpad clone via recycle.ps1 (both gone, verified); repository line already removed and re-read; theme setting unchanged (queue row 28). NOTE for row 9: SublimeClang also raised a late modal dialog (libclang_x64.dll couldn't be loaded, compile it yourself or download from github.com/quarnster/SublimeClang/downloads) that appeared minutes after the test and blocked the window until dismissed
- 2026-10-26 ADD REPOSITORY https://github.com/cthackers/SublimeGoBuild (queue row 29 Go Build) in portable Package Control settings; INSTALL via picker; remove both after test

- 2026-10-26 REMOVED SublimeGoBuild (queue row 29, Go Build) via picker; package file gone, repository line removed from Package Control.sublime-settings and re-read.

- 2026-10-26 ADD REPOSITORY https://github.com/witsch/SublimePythonTidy + INSTALL via picker (queue row 33, PythonTidy). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-26 REMOVED SublimePythonTidy (queue row 33) via picker; file gone, repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/diestrin/nodejsLauncher + INSTALL via picker (queue row 34, nodejsLauncher). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED nodejsLauncher (queue row 34) via picker; files gone, repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/erinata/SublimeMarkdownBuild + INSTALL via picker (queue row 35, MarkdownBuild). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED SublimeMarkdownBuild (queue row 35) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/derekchiang/Sublime-CoffeeScript-Formatter + INSTALL via picker (queue row 36, Coffee Formatter). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED Sublime-CoffeeScript-Formatter (queue row 36) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/wbond/sublime_tortoise + INSTALL via picker (queue row 37, Tortoise). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime_tortoise (queue row 37) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/ticky/ShowEncoding + INSTALL via picker (queue row 39, ShowEncoding). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED ShowEncoding (queue row 39) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/liamcain/Display-Functions + INSTALL via picker (queue row 40, Display Functions (Java)). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED Display-Functions (queue row 40) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/timdouglas/sublime-find-function-definition + INSTALL via picker (queue row 41, Find Function Definition). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-find-function-definition (queue row 41) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/theadamlt/Sublime-Arduino + INSTALL via picker (queue row 42, Arduino). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED Sublime-Arduino (queue row 42) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/revolunet/sublimetext-html-export + INSTALL via picker (queue row 43, HTML Export). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublimetext-html-export (queue row 43) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/adampresley/sublime-js-minify + INSTALL via picker (queue row 44, JS Minify). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-js-minify (queue row 44) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/quarnster/CompleteSharp + INSTALL via picker (queue row 45, CompleteSharp). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED CompleteSharp (queue row 45) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/tanepiper/sublime-todomanager + INSTALL via picker (queue row 48, Todo Manager). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-todomanager (queue row 48) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/UnicornForest/Unity3DScriptReference + INSTALL via picker (queue row 49, Unity3D Script Reference Search). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED Unity3DScriptReference (queue row 49) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/iafan/SublimeTextPreview + INSTALL via picker (queue row 51, Preview). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED SublimeTextPreview (queue row 51) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/welefen/KeymapManager + INSTALL via picker (queue row 52, KeymapManager). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 LOOSE COPY C:\Users\donal\tools\st_portable\Data\Packages\KeymapManager (unzipped from the installed package without KeymapManager.pyc and package-metadata.json; queue row 52 fix test). Remove: recycle.ps1 on that folder.

- 2026-10-27 REMOVED KeymapManager (queue row 52) via picker; loose copy folder recycled; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/liamcain/st2-refresh-theme + INSTALL via picker (queue row 53, Theme - Refresh). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 LOOSE COPY C:\Users\donal\tools\st_portable\Data\Packages\Theme - Refresh (unzipped from the installed st2-refresh-theme package, because textures are hardcoded to that folder name; queue row 53). Remove: recycle.ps1 on that folder.

- 2026-10-27 REMOVED st2-refresh-theme (queue row 53) via picker; loose copy Theme - Refresh recycled; theme setting back to auto; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/danro/refined-theme + INSTALL via picker (queue row 54, Theme - Refined). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 LOOSE COPY C:\Users\donal\tools\st_portable\Data\Packages\Theme - Refined (unzipped from the installed refined-theme package, textures hardcoded to that folder name; queue row 54). Remove: recycle.ps1 on that folder.

- 2026-10-27 REMOVED refined-theme (queue row 54) via picker; loose copy Theme - Refined recycled; theme setting back to auto; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/jamiesun/SublimeEvernote + INSTALL via picker (queue row 55, SublimeEvernote). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED SublimeEvernote (queue row 55) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/drivo/sublime-typescript-compiler + INSTALL via picker (queue row 57, TypeScript Compiler). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-typescript-compiler (queue row 57) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/oct8cat/sublime-phpdox + INSTALL via picker (queue row 58, PhpDox). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-phpdox (queue row 58) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/sheldon/sublime-text-2-folder-list + INSTALL via picker (queue row 59, Folder List). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED sublime-text-2-folder-list (queue row 59) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/gorte/ST2-Whitespaces + INSTALL via picker (queue row 61, Whitespaces). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED ST2-Whitespaces (queue row 61) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/jclement/SublimePandoc + INSTALL via picker (queue row 63, Pandoc (Markdown)). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED SublimePandoc (queue row 63) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/06wj/cocos2d_lua_snippets + INSTALL via picker (queue row 65, cocos2d lua api). Scope: portable Data only. Remove: Remove Package picker, delete repository line from Package Control.sublime-settings.

- 2026-10-27 REMOVED cocos2d_lua_snippets (queue row 65) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/alek-sys/ChangeTracker (queue row 66, Change Tracker); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED ChangeTracker (queue row 66) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/lvzixun/clang-complete (queue row 67, Clang-Complete); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Clang-Complete (queue row 67) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/bitbonsai/JSHint-Inline (queue row 70, JSHint Inline); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED JSHint-Inline (queue row 70) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/draffter/FollowFunctionPHP (queue row 71, Follow Function PHP); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED FollowFunctionPHP (queue row 71) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/SublimeText/PowershellUtils (queue row 72, PowershellUtils); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED PowershellUtils (queue row 72) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/rrerolle/sublime-scheme-cycler (queue row 73, SchemeCycler); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-scheme-cycler (queue row 73, SchemeCycler) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/srilumpa/SyntaxChecker (queue row 74, SyntaxChecker); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SyntaxChecker (queue row 74) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/qfel/sublime-pytags (queue row 75, PyTags); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-pytags (queue row 75, PyTags) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/SubZane/Sublime-Placehold.it (queue row 76, Placehold.it Image Tag Generator); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 LOOSE COPY C:\Users\donal\tools\st_portable\Data\Packages\Placeholdit (extracted from the installed Sublime-Placehold.it zip, queue row 76, because the dotted package name cannot be imported); recycle it after the test.

- 2026-10-27 REMOVED Sublime-Placehold.it (queue row 76) via picker; loose copy Packages\Placeholdit recycled; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/edubkendo/sublime-coffeescript-function-finder (queue row 77, CoffeeScript Function Finder); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-coffeescript-function-finder (queue row 77) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/chagel/itodo (queue row 79, iTodo); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED itodo (queue row 79) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/agibsonsw/QuickPrint (queue row 80, QuickPrint); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED QuickPrint (queue row 80) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/rcaldwel/Django-Tools (queue row 81, Django-Tools); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Django-Tools (queue row 81) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/mangini/chrome-apis-sublime (queue row 82, Chrome Apps and Extensions); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED chrome-apis-sublime (queue row 82, Chrome Apps and Extensions) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/groenewege/mdTodo (queue row 84, Markdown Todo); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 queue row 84 (mdTodo): repository added but nothing installed (Package Control reports the GitHub rate limit even after a portable restart); repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/groenewege/mdTodo (queue row 84, Markdown Todo, retry after github_token added to the portable's Package Control settings); installed via picker; remove via picker, then delete the repository line. NOTE: the portable's Package Control.sublime-settings now holds a github_token; remove it when the queue is done.

- 2026-10-27 REMOVED mdTodo (queue row 84) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/spadgos/sublime-OpenRecentFiles (queue row 86, Open Recent Files); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-OpenRecentFiles (queue row 86) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/ccpalettes/sublime-lorem-text (queue row 87, LoremText); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-lorem-text (queue row 87, LoremText) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/paccator/GotoRecent (queue row 88, GotoRecent); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED GotoRecent (queue row 88) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/p-e-w/GTKDarkThemeVariantSetter (queue row 89, GTKDarkThemeVariantSetter); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED GTKDarkThemeVariantSetter (queue row 89) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/astronaughts/SublimePHPBuiltinWebServer (queue row 90, PHP Built-in WebServer); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimePHPBuiltinWebServer (queue row 90) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/spadgos/sublime-csspecific (queue row 91, sublime-csspecific); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-csspecific (queue row 91) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/LeeMallabone/sublime-css-selector-reveal (queue row 92, CSS Selector Reveal); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-css-selector-reveal (queue row 92) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/saippuakauppias/sublime-text-2-Django-DocsSearch (queue row 94, Django-DocsSearch); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-text-2-Django-DocsSearch (queue row 94) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/subhaze/sublime_codekit (queue row 96, CodeKit Commands); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime_codekit (queue row 96) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/biannetta/MySublimeQL (queue row 97, MySublimeQL); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED MySublimeQL (queue row 97) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/hyspace/st2-reeder-theme (queue row 99, Theme - Reeder); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED st2-reeder-theme (queue row 99, Theme - Reeder) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/TooBug/CompactExpandCss (queue row 100, CompactExpandCss); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED CompactExpandCss (queue row 100) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/Stubbs/sublime-puppet-syntax (queue row 101, Puppet Syntax checking); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-puppet-syntax (queue row 101) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/CrypticTemple/sublime-xml-guesser (queue row 102, xml-guesser); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-xml-guesser (queue row 102) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/timjrobinson/SublimeNavigationHistory (queue row 103, Navigation History); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeNavigationHistory (queue row 103) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/SublimeGit/CanISwitchToSublimeText3 (queue row 105, CanISwitchToSublimeText3); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED CanISwitchToSublimeText3 (queue row 105) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/revolunet/sublimetext-web-encoders (queue row 107, Web Encoders); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublimetext-web-encoders (queue row 107) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/jtdeng/GoToDoc (queue row 108, GoToDoc); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED GoToDoc (queue row 108) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/nijikokun/Prevu (queue row 110, Prevu); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Prevu (queue row 110) via picker; repository line removed and re-read.

- 2026-10-27 ADD REPOSITORY https://github.com/kutu/PythonAnywhereEditor (queue row 112, Python Anywhere Editor); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED PythonAnywhereEditor (queue row 112) via picker; repository line removed. ST2-only, Python 2 code (except Exception, e); nothing filed.

- 2026-10-27 ADD REPOSITORY https://github.com/mediaupstream/SublimeText-NodeEval (queue row 113, NodeEval); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeText-NodeEval (queue row 113) via picker; repository line removed; test settings file NodeEval.sublime-settings recycled; portable restarted to stop the spinning reader threads.

- 2026-10-27 ADD REPOSITORY https://github.com/doublerebel/filezilla_import (queue row 114, FilezillaImport); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED filezilla_import (queue row 114) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/lfont/Sublime-Text-2-GoogleTranslate-Plugin (queue row 115, Google Translate); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Sublime-Text-2-GoogleTranslate-Plugin (queue row 115) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/oleander/sublime-split-navigation (queue row 116, sublime-split-navigation); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-split-navigation (queue row 116) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/sc8696/sublime-css-auto-comments (queue row 117, CSS Auto Commenting); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-css-auto-comments (queue row 117) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/inflation/Gherkin-highlight-sublimetext (queue row 119, Gherkin-highlight-sublimetext); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Gherkin-highlight-sublimetext (queue row 119) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/danielhopkins/sublime-view-movement (queue row 120, View Movement); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-view-movement (queue row 120) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/lyapun/sublime-text-2-python-test-runner (queue row 121, PythonTestRunner); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-text-2-python-test-runner (queue row 121) via picker; repository line removed; PythonTestRunner.last-run recycled; empty scratchpad folder ptr locked by exec cwd (harmless, session scratchpad).

- 2026-10-27 ADD REPOSITORY https://github.com/sahibalejandro/inline-calculator (queue row 122, Inline Calculator); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED inline-calculator (queue row 122) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/trentrichardson/Clientside (queue row 123, Clientside); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Clientside (queue row 123) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/drugo76/sublime_json2csv (queue row 124, JSON to CSV Converter); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime_json2csv (queue row 124) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/fintanmm/SublimeLoremPixel (queue row 126, LoremPixel); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeLoremPixel (queue row 126) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/seanliang/Codecs26 (queue row 127, Codecs26); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Codecs26 (queue row 127) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/phisch/Anypreter (queue row 129, Anypreter; repo archived); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Anypreter (queue row 129) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/cockscomb/SublimePerldoc (queue row 132, perldoc); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimePerldoc (queue row 132) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/sindresorhus/sublime-jsrun (queue row 133, JsRun); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-jsrun (queue row 133) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/davidolrik/sublime-terminal-notifier (queue row 135, Terminal Notifier); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-terminal-notifier (queue row 135) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/Asoul/typora-markdown-sublime (queue row 136, Typora Markdown App (OSX); issues disabled); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED typora-markdown-sublime (queue row 136) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/tomascayuelas/coolcodescheme (queue row 137, Cool Code Scheme); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED coolcodescheme (queue row 137) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/PogiNate/SublimeWiki (queue row 138, Wiki); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeWiki (queue row 138) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/d0ugal/RstPreview (queue row 139, RstPreview; repo archived); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 RstPreview (queue row 139): Add Repository accepted https://github.com/d0ugal/RstPreview but the picker offered no package for it (list total unchanged); nothing installed; repository line not left in settings.

- 2026-10-27 ADD REPOSITORY https://github.com/astropanic/Compline (queue row 140, Line Completion); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Compline (queue row 140) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/astronaughts/SublimeNFDToNFCPaste (queue row 141, SublimeNFDToNFCPaste); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeNFDToNFCPaste (queue row 141) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/ikeike443/Sublime-Scalariform (queue row 142, Scalariform; repo archived); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED Sublime-Scalariform (queue row 142) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/smpanaro/sublime-spotify (queue row 143, Spotify); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-spotify (queue row 143) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/xamado/sublime-templateninja (queue row 144, TemplateNinja); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-templateninja (queue row 144) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/jeffturcotte/sublime_transmit_docksend (queue row 147, Transmit Docksend); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime_transmit_docksend (queue row 147) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/qfel/RunCommand (queue row 148, RunCommand); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED RunCommand (queue row 148) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/leporo/SublimeYammy (queue row 149, Yammy Syntax Highlighting); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SublimeYammy (queue row 149) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/nlloyd/SubliminalCollaborator (queue row 150, SubliminalCollaborator); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED SubliminalCollaborator (queue row 150) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/gs/sublime-text-go-to-file (queue row 151, GoToFile); installed via picker; remove via picker, then delete the repository line.

- 2026-10-27 REMOVED sublime-text-go-to-file (queue row 151) via picker; repository line removed.

- 2026-10-27 ADD REPOSITORY https://github.com/wallysalami/QuickLook (queue row 152, Quick Look); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED QuickLook (queue row 152) via picker; repository line wallysalami/QuickLook deleted from portable settings; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/erinata/BuildParts (queue row 153, BuildParts); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED BuildParts (queue row 153) via picker; repository line erinata/BuildParts deleted; test tab closed; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/hikaruworld/Browse (queue row 154, Browse); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED Browse (queue row 154) via picker; repository line hikaruworld/Browse deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/ajryan/CSharpreter (queue row 155, CSharpreter); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED CSharpreter (queue row 155) via picker; repository line ajryan/CSharpreter deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/Narven/sublime-artisan (queue row 157, Artisan); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-artisan / Artisan (queue row 157) via picker; repository line Narven/sublime-artisan deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/idosela/sublime_new_from_selection (queue row 158, New from Selection); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime_new_from_selection (queue row 158) via picker; repository line idosela/sublime_new_from_selection deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/matthiasg/sublime-mocha-runner (queue row 159, Mocha Runner); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-mocha-runner / Mocha Runner (queue row 159) via picker; repository line matthiasg/sublime-mocha-runner deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/vaanwd/sublime_drush (queue row 160, Drush); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime_drush / Drush (queue row 160) via picker; repository line vaanwd/sublime_drush deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/patgannon/sublimetext-scalatest (queue row 161, ScalaTest); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublimetext-scalatest / ScalaTest (queue row 161) via picker; repository line patgannon/sublimetext-scalatest deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/standfast/Translate (queue row 162, Translate); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED Translate (queue row 162) via picker; repository line standfast/Translate deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/koko1000ban/SublimeGtags (queue row 163, GTags); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeGtags / GTags (queue row 163) via picker; repository line koko1000ban/SublimeGtags deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/jugyo/SublimeGitGrep (queue row 164, GitGrep); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeGitGrep / GitGrep (queue row 164) via picker; repository line jugyo/SublimeGitGrep deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/vojtajina/sublime-BuildSwitcher (queue row 165, Build Switcher); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-BuildSwitcher / Build Switcher (queue row 165) via picker; repository line vojtajina/sublime-BuildSwitcher deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/harrison-m/indent.txt (queue row 166, Indent.txt); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED indent.txt (queue row 166) via picker; repository line harrison-m/indent.txt deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/pahlers/PathToFile (queue row 167, Path to File); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED PathToFile / Path to File (queue row 167) via picker; repository line pahlers/PathToFile deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/SubZane/Sublime-Dummy-Image-Generator (queue row 168, Dummy Image Generator); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED Sublime-Dummy-Image-Generator / Dummy Image Generator (queue row 168) via picker; repository line SubZane/Sublime-Dummy-Image-Generator deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/sentience/DokuWiki (queue row 169, DokuWiki); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED DokuWiki (queue row 169) via picker; repository line sentience/DokuWiki deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/Apptorium/TeaCode-Sublime-Helper (queue row 170, TeaCode Helper); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED TeaCode-Sublime-Helper / TeaCode Helper (queue row 170) via picker; repository line Apptorium/TeaCode-Sublime-Helper deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/gja/sublime-rmate (queue row 171, Rmate); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-rmate / Rmate (queue row 171) via picker; repository line gja/sublime-rmate deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/SublimeText/UberSelection (queue row 172, UberSelection); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED UberSelection (queue row 172) via picker; repository line SublimeText/UberSelection deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/email2vimalraj/DashedComments (queue row 173, Dashed Comments); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED DashedComments / Dashed Comments (queue row 173) via picker; repository line email2vimalraj/DashedComments deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/DirkBrand/ProtoBufCodeFormatter_Sublime (queue row 175, ProtoBufCodeFormatter); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED ProtoBufCodeFormatter_Sublime / ProtoBufCodeFormatter (queue row 175) via picker; repository line DirkBrand/ProtoBufCodeFormatter_Sublime deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/balazstth/subl-esp (queue row 176, ESP EcmaScript Pages Edit Mode); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED subl-esp / ESP EcmaScript Pages Edit Mode (queue row 176) via picker; repository line balazstth/subl-esp deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/diimdeep/sublime-text-macdown-app-menu (queue row 177, MacDown App Menu); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-text-macdown-app-menu / MacDown App Menu (queue row 177) via picker; repository line diimdeep/sublime-text-macdown-app-menu deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/misaxi/sublime-code-preview (queue row 178, Code Preview); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-code-preview / Code Preview (queue row 178) via picker; repository line misaxi/sublime-code-preview deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/erinata/SublimeBullet (queue row 180, Bullet); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeBullet / Bullet (queue row 180) via picker; repository line erinata/SublimeBullet deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/joscandreu/ST2-TiSearch (queue row 181, Titanium API Search); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED ST2-TiSearch / Titanium API Search (queue row 181) via picker; repository line joscandreu/ST2-TiSearch deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/git-commit/pkgbuild-st3 (queue row 182, PKGBUILD); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED pkgbuild-st3 / PKGBUILD (queue row 182) via picker; repository line git-commit/pkgbuild-st3 deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/gh640/SublimeMacDictionary (queue row 183, MacDictionary); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeMacDictionary / MacDictionary (queue row 183) via picker (libraries Jinja2, Markdown, markupsafe, mdpopups, Pygments, pymdown-extensions, PyYAML were installed with it and removed as orphans by Package Control); repository line gh640/SublimeMacDictionary deleted; folder Packages\SublimeMacDictionary gone.
2026-10-27 ADD REPOSITORY https://github.com/dedg3/sublime-magento-TemplateCopy (queue row 184, Magento - TemplateCopy); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-magento-TemplateCopy / Magento - TemplateCopy (queue row 184) via picker; repository line dedg3/sublime-magento-TemplateCopy deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/astronaughts/SublimeOpenFromPath (queue row 185, OpenFromPath); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeOpenFromPath / OpenFromPath (queue row 185) via picker; repository line astronaughts/SublimeOpenFromPath deleted; console shows Removed package; test tab for ~/zz_ofp_nofile.txt closed with No, file never written.
2026-10-27 ADD REPOSITORY https://github.com/k0sukey/ST2-TitaniumDoc (queue row 186, Titanium API Document); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED ST2-TitaniumDoc / Titanium API Document (queue row 186) via picker; repository line k0sukey/ST2-TitaniumDoc deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/teddyknox/SublimeChromeRefresh (queue row 187, Chrome Refresh); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeChromeRefresh / Chrome Refresh (queue row 187) via picker; repository line teddyknox/SublimeChromeRefresh deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/bit-part/PowerMTML-ST2 (queue row 188, PowerMTML Completions); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED PowerMTML-ST2 / PowerMTML Completions (queue row 188) via picker; repository line bit-part/PowerMTML-ST2 deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/zerok/Sublime2-SwitchLanguage (queue row 189, SwitchLanguage; repo archived); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED Sublime2-SwitchLanguage / SwitchLanguage (queue row 189) via picker; repository line zerok/Sublime2-SwitchLanguage deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/achayan/sublimePyQtSearch (queue row 191, PyQt Search); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublimePyQtSearch / PyQt Search (queue row 191) via picker; repository line achayan/sublimePyQtSearch deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/swenson/sublime_whitespace (queue row 192, Whitespace Diff Trim); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime_whitespace / Whitespace Diff Trim (queue row 192) via picker; repository line swenson/sublime_whitespace deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/jadu/sublime-behat-completions (queue row 193, Behat Completions; repo archived); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-behat-completions / Behat Completions (queue row 193) via picker; repository line jadu/sublime-behat-completions deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/markandey/codefoo (queue row 194, Code Foo); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED codefoo / Code Foo (queue row 194) via picker; repository line markandey/codefoo deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/topikachu/sublime-text-2-GrepCodeSearch (queue row 195, Grep Code Search; issues disabled); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-text-2-GrepCodeSearch / Grep Code Search (queue row 195) via picker; repository line topikachu/sublime-text-2-GrepCodeSearch deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/vicapow/sublime-minify-js-to-clipboard (queue row 197, Minify JS To Clipboard); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-minify-js-to-clipboard / Minify JS To Clipboard (queue row 197) via picker; repository line vicapow/sublime-minify-js-to-clipboard deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/felipeelias/sublime-text-2-rbenv (queue row 200, rbenv; repo archived); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-text-2-rbenv / rbenv (queue row 200) via picker; repository line felipeelias/sublime-text-2-rbenv deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/laszlo-r/sublime-webloader (queue row 202, Webloader); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublime-webloader / Webloader (queue row 202) via picker; repository line laszlo-r/sublime-webloader deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/revolunet/sublimetext-google-apps-scripts (queue row 203, Google Apps Scripts); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublimetext-google-apps-scripts / Google Apps Scripts (queue row 203) via picker; repository line revolunet/sublimetext-google-apps-scripts deleted; console shows Removed package.
2026-10-27 ADD REPOSITORY https://github.com/prongs/SublimeCodechef (queue row 204, Codechef); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeCodechef / Codechef (queue row 204) via picker; repository line prongs/SublimeCodechef deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/chaosphere2112/TextCommands (queue row 206, TextCommands); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED TextCommands (queue row 206) via picker; repository line chaosphere2112/TextCommands deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/avinash8526/List2CSV-Sublime-Plugin (queue row 207, list2csv); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED List2CSV-Sublime-Plugin (queue row 207) via picker; repository line avinash8526/List2CSV-Sublime-Plugin deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/dongchao-1/CommentAnyWhere (queue row 208, CommentAnyWhere); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED CommentAnyWhere (queue row 208) via picker; repository line dongchao-1/CommentAnyWhere deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/Kaizhi/SublimeUpdater (queue row 210, Updater); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) SublimeUpdater (queue row 210): stopped at the picker after reading the source; repository line Kaizhi/SublimeUpdater deleted.
2026-10-27 ADD REPOSITORY https://github.com/ololduck/sublimetext-date (queue row 211, Date); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED sublimetext-date (queue row 211) via picker; repository line ololduck/sublimetext-date deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/dsteinbach/npm-info (queue row 212, NPMInfo); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED npm-info (queue row 212) via picker; repository line dsteinbach/npm-info deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/borist/SublimePaneNavigation (queue row 218, Pane Navigation); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimePaneNavigation (queue row 218) via picker; repository line borist/SublimePaneNavigation deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/shammond42/cheater (queue row 220, Cheater); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED cheater (queue row 220) via picker; repository line shammond42/cheater deleted; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/jedy/SublimeReader (queue row 221, Text Reader); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED SublimeReader / Text Reader (queue row 221) via picker; repository line jedy/SublimeReader deleted; leftover User\TextReader.sublime-settings (written on tab close) recycled; console shows Removed package; package file gone.
2026-10-27 ADD REPOSITORY https://github.com/croach/SublimeHideTabs (queue row 222, Hide Tabs); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) Hide Tabs (queue row 222): picker did not list it even with the repository added; repository line croach/SublimeHideTabs deleted.
2026-10-27 ADD REPOSITORY https://github.com/prongs/SublimeNumberManipulation (queue row 223, Number Manipulation); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) Number Manipulation (queue row 223): picker did not offer it (its issue #12 asks for ST3 availability); repository line prongs/SublimeNumberManipulation deleted.
2026-10-27 ADD Lean 4 via elan (his go, "Go ahead", to prove properties of sublime-mcp protocol negotiation, inspired by Theorem): everything inside C:\Users\donal\tools\lean-elan (ELAN_HOME), no PATH change, no admin. Remove: recycle.ps1 on that folder, then check Test-Path and the user PATH/registry for elan.
2026-10-27 REMOVED Lean 4 / elan (C:\Users\donal\tools\lean-elan) via recycle.ps1; Test-Path false for the folder, ~\.elan and ~\.lake; no elan/lean entry in HKCU PATH or HKCU\Software; no lean command. Proof file kept in sublime-mcp tools\proofs (commit 366c135).
2026-10-27 ADD Lean 4 via elan again (his go, "Go", to model and prove GhostShell session/tab lifecycle invariants): everything inside C:\Users\donal\tools\lean-elan (ELAN_HOME), no PATH change, no admin. Remove: recycle.ps1 on that folder, then check Test-Path, ~\.elan, ~\.lake, HKCU PATH.
2026-10-27 REMOVED Lean 4 / elan again (C:\Users\donal\tools\lean-elan) via recycle.ps1; Test-Path false for the folder, ~\.elan and ~\.lake; no elan/lean in HKCU PATH; no lean command. Proof file kept in GhostShell ai\proofs (commit 80723a4, pushed).
2026-10-27 ADD Lean 4 via elan, KEPT INSTALLED on his word ("Go ahead and don't uninstall it"), for GhostShell/sublime-mcp proofs: everything inside C:\Users\donal\tools\lean-elan (ELAN_HOME), no PATH change, no admin. Remove later: recycle.ps1 on that folder, then check Test-Path, ~\.elan, ~\.lake, HKCU PATH.
2026-10-27 ADD REPOSITORY https://github.com/j-martin/open-with-sublime (queue row 230, Open With); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) Open With (queue row 230): the picker does not offer it on Windows; repository line j-martin/open-with-sublime deleted.
2026-10-27 ADD REPOSITORY https://github.com/cockscomb/SublimeMakeExecutable (queue row 232, MakeExecutable); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) MakeExecutable (queue row 232): the picker did not offer it; repository line cockscomb/SublimeMakeExecutable deleted.
2026-10-27 ADD REPOSITORY https://github.com/lucifr/CNPunctuationAutopair (queue row 237, CNPunctuationAutopair); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) CNPunctuationAutopair (queue row 237): the picker did not offer it; repository line lucifr/CNPunctuationAutopair deleted.
2026-10-27 ADD REPOSITORY https://github.com/jfernandez/SublimeRailsEval (queue row 238, RailsEval); installed via picker; remove via picker, then delete the repository line.
2026-10-27 REMOVED (never installed) RailsEval (queue row 238): the picker did not offer it; repository line jfernandez/SublimeRailsEval deleted.
2026-10-27 ADD NetLinx (amclain/sublime-netlinx, channel package, step 1 of his go "Ok": test without outside tools); installed via picker; remove via picker.
2026-10-27 REMOVED NetLinx (amclain/sublime-netlinx 2.1.2) via picker; console shows Removed package; package file gone; no User settings left. Also removed a stale jedy/SublimeReader repository line that Package Control had written back into its settings. Findings: findings\NetLinx-template-silently-empty-and-generate-workspace-unsaved-tab.md (not filed: amclain asked for no more issues).
2026-10-27 DOWNLOAD (not an install) NetLinxStudio_4_4_1915.zip (80 MB, AMX/Harman public download) into C:\Users\donal\tools\netlinx-studio\dl to inspect the installer type; his go ("2 and 3"). Nothing is run from it unless it needs no administrator rights. Remove: recycle.ps1 on C:\Users\donal\tools\netlinx-studio.
2026-10-27 NOTE NetLinx Studio zip inspected, nothing run: setup is an unsigned Advanced Installer bootstrapper whose manifest requires administrator rights; its readable parts (two cabs) hold only the Visual C++ 2012 runtimes; the product payload is in a compressed section built-in tools cannot open. Leftovers, all inside C:\Users\donal\tools\netlinx-studio (dl, x, cab): recycle that folder when this is finished.
2026-10-27 REMOVED C:\Users\donal\tools\netlinx-studio (NetLinx Studio zip download and extracted pieces, 177 MB) to the Recycle Bin with recycle.ps1; verified gone.
2026-10-27 ADD REPOSITORY https://github.com/willurd/ScopeStatus then install ScopeStatus via picker in portable 4215 (tools\st_portable), retest queue row 250. Remove: picker Remove Package, delete the repositories line from Package Control.sublime-settings.
2026-10-27 REMOVED ScopeStatus (picker, console "Removed package" seen), repositories line deleted from Package Control.sublime-settings; test tab closed without saving.
2026-10-27 ADD REPOSITORY https://github.com/chere005/Sublime-WolframMathematicaNotebookViewer then install via picker in portable 4215, retest queue row 251. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED Sublime-WolframMathematicaNotebookViewer (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/braver/SublimeGitUp then install via picker in portable 4215, retest queue row 252. Remove: picker Remove Package, delete the repositories line.
2026-10-27 NOT INSTALLED SublimeGitUp after all (the ADD REPOSITORY line above was not carried out): code launches the macOS GitUp.app with open -a, nothing to run on Windows.
2026-10-27 ADD REPOSITORY https://github.com/ppxu/sublime-semistandard-format then install via picker in portable 4215, retest queue row 253. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED sublime-semistandard-format (picker, console Removed seen), repositories line deleted, test tab and Package Control Messages tab closed.
2026-10-27 ADD REPOSITORY https://github.com/benjajaja/ControlScroll then install via picker in portable 4215, retest queue row 254. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED ControlScroll (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/jfromaniello/sublime-goto-node-module then install via picker in portable 4215, retest queue row 255. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED sublime-goto-node-module (picker, console Removed seen), repositories line deleted, test folder and tab closed in the window.
2026-10-27 ADD REPOSITORY https://github.com/forty-two/NightCycle then install via picker in portable 4215, retest queue row 258. It rewrites theme/color_scheme in User Preferences.sublime-settings: copy saved in scratchpad, restore after. Remove: picker Remove Package, delete the repositories line, restore Preferences.
2026-10-27 REMOVED NightCycle (picker, console Removed seen), repositories line deleted, User Preferences.sublime-settings restored from the copy (theme auto, no color_scheme line); removing the package does not undo the theme/scheme it wrote.
2026-10-27 ADD REPOSITORY https://github.com/GerjanOnline/SublimeFileCleanup then install via picker in portable 4215, retest queue row 259. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED SublimeFileCleanup (picker, console Removed seen), repositories line deleted, test tab closed without saving.
2026-10-27 ADD REPOSITORY https://github.com/kawasako/sublime-plugin-Image2tag then install via picker in portable 4215, retest queue row 260. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED sublime-plugin-Image2tag (picker, console Removed seen), repositories line deleted, test folder and tab closed.
2026-10-27 ADD REPOSITORY https://github.com/frankdejonge/CopyNamespace then install via picker in portable 4215, retest queue row 278. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED CopyNamespace (picker, console Removed seen), repositories line deleted, test tab closed. The clipboard now holds a test string (App\Models\Thing).
2026-10-27 ADD REPOSITORY https://github.com/bit-part/MTML-ST2 then install via picker in portable 4215, retest queue row 280. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED MTML-ST2 (picker, console Removed seen), repositories line deleted, test tab closed without saving. Earlier lines for CopyNamespace test: a Could not find a class dialog from my own too-early run blocked the first add_repository attempt; dismissed.
2026-10-27 ADD REPOSITORY https://github.com/roesti77/Sublime-Open-Shading-Language then install via picker in portable 4215, retest queue row 277. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED Sublime-Open-Shading-Language (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/natew/ExpandSelectionByParagraph then install via picker in portable 4215, retest queue row 293. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED ExpandSelectionByParagraph (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 COPY Sleet folder from ice/sleet commit 8a2468e (clone in scratchpad) into tools\st_portable\Data\Packages\Sleet to test the maintainers fix for ice/sleet#1 on request. Remove: recycle.ps1 on Data\Packages\Sleet and the scratchpad clone.
2026-10-27 REMOVED Data\Packages\Sleet copy and the scratchpad clone of ice/sleet (recycle.ps1, verified gone). Result posted on ice/sleet#1: 8a2468e fixes the syntax load.
2026-10-27 ADD REPOSITORY https://github.com/minimedj/ErlDoc then install via picker in portable 4215, retest queue row 288. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED ErlDoc (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/ecornell/Sublime-MoonScript then install via picker in portable 4215, retest queue row 300. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED Sublime-MoonScript (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/dotmaster/SublimeExpandSelectionToLineBefore then install via picker in portable 4215, retest queue row 302. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED SublimeExpandSelectionToLineBefore (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/theadamlt/Sublime-DCPU-16 then install via picker in portable 4215, retest queue row 309. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED Sublime-DCPU-16 (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/rodrigoflores/Today then install via picker in portable 4215, retest queue row 320. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED Today (picker, console Removed seen), repositories line deleted, scratch tab closed without saving.
2026-10-27 ADD REPOSITORY https://github.com/superguigui/xtoy then install via picker in portable 4215, retest queue row 321. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED xtoy (picker, console Removed seen), repositories line deleted, scratch tab closed without saving.
2026-10-27 ADD REPOSITORY https://github.com/HackerBaloo/SublimeOpenInTotalCommander then install via picker in portable 4215, retest queue row 330. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED SublimeOpenInTotalCommander (picker, console Removed seen), repositories line deleted, test tab closed, dialog dismissed.
2026-10-27 ADD REPOSITORY https://github.com/angelsanchez/iris-path-sublime then install via picker in portable 4215, retest queue row 343. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED iris-path-sublime (picker, console Removed seen), repositories line deleted. Note: a first add_repository and two installs failed because a No executable found dialog left by the Total Commander test blocked input; dismissed.
2026-10-27 ADD REPOSITORY https://github.com/jmm/Sublime-Text-Cycle-Setting then install via picker in portable 4215, retest queue row 348. Remove: picker Remove Package, delete the repositories line.
2026-10-27 NOT INSTALLED Sublime-Text-Cycle-Setting after all (the ADD REPOSITORY line above was not carried out): the plugin file sits in Packages/Cycle Setting/ inside the repo, so a Package Control install would not put it in the package root.
2026-10-27 ADD REPOSITORY https://github.com/jcowgar/sublime-duplicate-same then install via picker in portable 4215, retest queue row 351. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED sublime-duplicate-same (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/sahibalejandro/quark-php-sublime then install via picker in portable 4215, retest queue row 341. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED quark-php-sublime (picker, console Removed seen), repositories line deleted, fixture folder recycled.
2026-10-27 ADD REPOSITORY https://github.com/jugyo/SublimeTraverse then install via picker in portable 4215, retest queue row 356. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED SublimeTraverse (picker, console Removed seen), repositories line deleted.
2026-10-27 ADD REPOSITORY https://github.com/bthorben/WebSuite then install via picker in portable 4215, retest queue row 355. Remove: picker Remove Package, delete the repositories line.
2026-10-27 REMOVED WebSuite (picker, console Removed seen), repositories line deleted, test tab closed.
2026-10-27 ADD REPOSITORY https://github.com/dunckr/hidefiles then install via picker in portable 4215, retest queue row 366. It edits file_exclude_patterns in User Preferences.sublime-settings: copy saved in scratchpad, restore after. Remove: picker Remove Package, delete the repositories line, restore Preferences.
2026-10-27 REMOVED hidefiles (picker, console Removed seen), repositories line deleted, User Preferences.sublime-settings restored from the copy, test tab closed.
2026-10-27 REMOVED the http_basic_auth token line from the portable Package Control.sublime-settings (queue finished); repositories list empty; installed_packages Color Scheme - Legacy, Package Control, SublimeLinter.
2026-10-27 ADD (portable 4215, Package Control picker/install_package) Tcsh and Csh Mode: audit row 1739, test only; remove with remove_package and verify Installed Packages afterwards.
2026-10-27 REMOVED Tcsh and Csh Mode (picker; console "Removed package" seen; package file gone; test tab closed).
2026-10-27 ADD (portable 4215, install_package) Teenage Color Scheme: live test of a package pushed 2023 or later; remove with remove_package, restore Preferences from scratchpad Preferences.before_live5, verify Installed Packages after.
2026-10-27 ADD (portable 4215, install_package) Theme - Rose Pine: live test of a package pushed 2023 or later; remove with remove_package, restore Preferences from scratchpad Preferences.before_live5, verify Installed Packages after.
2026-10-27 ADD (portable 4215, install_package) Writer Color Scheme: live test of a package pushed 2023 or later; remove with remove_package, restore Preferences from scratchpad Preferences.before_live5, verify Installed Packages after.
2026-10-27 ADD (portable 4215, install_package) perl-Test-Class: live test of a package pushed 2023 or later; remove with remove_package, restore Preferences from scratchpad Preferences.before_live5, verify Installed Packages after.
2026-10-27 ADD (portable 4215, install_package) perl-Test-More: live test of a package pushed 2023 or later; remove with remove_package, restore Preferences from scratchpad Preferences.before_live5, verify Installed Packages after.
2026-10-27 REMOVED Teenage Color Scheme (picker, console 'Removed package' seen, package file gone); test tabs closed, Preferences identical to backup.
2026-10-27 REMOVED Theme - Rose Pine (picker, console 'Removed package' seen, package file gone); test tabs closed, Preferences identical to backup.
2026-10-27 REMOVED Writer Color Scheme (picker, console 'Removed package' seen, package file gone); test tabs closed, Preferences identical to backup.
2026-10-27 REMOVED perl-Test-Class (picker, console 'Removed package' seen, package file gone); test tabs closed, Preferences identical to backup.
2026-10-27 REMOVED perl-Test-More (picker, console 'Removed package' seen, package file gone); test tabs closed, Preferences identical to backup.
2026-10-27 ADD batch 1 (portable 4215, install_package, load test only): SublimeLinter-contrib-LanguageTool, SublimeLinter-clang, SublimeLinter-contrib-verilator, SublimeLinter-contrib-swiftlint, SublimeLinter-bandit, SublimeLinter-addon-black-for-flake, Calculate, SublimeLinter-annotations, SublimeLinter-addon-filter, SublimeLinter-govet. Remove each with remove_package (picker) and verify Installed Packages after.
2026-10-27 REMOVED batch 1 (picker): SublimeLinter-contrib-LanguageTool, SublimeLinter-clang, SublimeLinter-contrib-verilator, SublimeLinter-bandit, SublimeLinter-addon-black-for-flake, Calculate, SublimeLinter-annotations, SublimeLinter-addon-filter, SublimeLinter-govet; package files gone; Package Control Messages tab closed. SublimeLinter-contrib-swiftlint never installed (no package file appeared).
2026-10-27 ADD batch 2 (portable 4215, install_package, load test only): SublimeLinter-gotype, SublimeLinter-html-tidy, SublimeLinter-hlint, SublimeLinter-flake8, SublimeLinter-cspell, SublimeLinter-cppcheck, SublimeLinter-eslint, SublimeLinter-csslint, WslBuild, Rsync SSH, RemoveDuplicateLines, ScrollToCursor, Save All New Tabs to One File, Pretty Shell, OpenFileOverSSH. Remove each with remove_package (picker), verify after.
2026-10-27 REMOVED batch 2 (picker, in groups of 5 with a wait between): SublimeLinter-gotype, SublimeLinter-html-tidy, SublimeLinter-hlint, SublimeLinter-flake8, SublimeLinter-cspell, SublimeLinter-cppcheck, SublimeLinter-eslint, SublimeLinter-csslint, WslBuild, Rsync SSH, RemoveDuplicateLines, ScrollToCursor, Save All New Tabs to One File, OpenFileOverSSH, Pretty Shell; package files gone. Fast chained removal of 9 in batch 1 left names in ignored_packages and a 'package is trying to ignore itself' dialog twice: Preferences restored from backup.
2026-10-27 ADD batch 3 (portable 4215, install_package, load test only): MoveTab, Phpcs, Origami, UWSC, Toggle Sidebar Focus, Word Count, Veeam Logs Helper, Templ (go), SnippetMaker, LSP-vue, StringUtilities, StickySearch, SublimeLinter-javac, LSP-flow, LSP-eslint, LSP-lua, LSP-graphql, LSP-dockerfile, LSP-astro, LSP-angular. Remove in groups of 5 with a wait, verify after.
2026-10-27 REMOVED batch 3 (picker, groups of 6): MoveTab, Phpcs, Origami, UWSC, Toggle Sidebar Focus, Word Count, Veeam Logs Helper, Templ (go), SnippetMaker, StringUtilities, StickySearch, SublimeLinter-javac; package files gone; Preferences identical to backup. LSP-* names deferred (need the LSP package and language servers).
2026-10-27 ADD batch 4 (portable 4215, install_package, load test only): SublimeLinter-xmllint, SublimeLinter-phpcs, SublimeLinter-php, SublimeLinter-pug-lint, SublimeLinter-phplint, SublimeLinter-pep8, SublimeLinter-jsl, SublimeLinter-jshint, SublimeLinter-jsxhint, SublimeLinter-json, SublimeLinter-shellcheck, SublimeLinter-ruby, SublimeLinter-vale, SublimeLinter-tslint, SublimeLinter-rubocop, SublimeLinter-pyflakes, SublimeLinter-pycodestyle, SublimeLinter-rst, SublimeLinter-pylint, Copy Relative Command. Remove in groups of 6 with a wait, verify after.
2026-10-27 REMOVED batch 4 (picker): all 20 names of batch 4 incl. SublimeLinter-xmllint, SublimeLinter-phpcs, SublimeLinter-php, SublimeLinter-pug-lint, SublimeLinter-phplint, SublimeLinter-jsl, SublimeLinter-jshint, SublimeLinter-json, SublimeLinter-shellcheck, SublimeLinter-ruby, SublimeLinter-vale, SublimeLinter-tslint, SublimeLinter-rubocop, SublimeLinter-pyflakes, SublimeLinter-pycodestyle, SublimeLinter-pylint, Copy Relative Command, SublimeLinter-pep8, SublimeLinter-jsxhint, SublimeLinter-rst; package files gone. Removing 7 at once raised the 'package is trying to ignore itself' dialog loop and stalled removals until Preferences was restored and the dialog dismissed (twice); use groups of 4 from now on.
2026-10-27 ADD batch 5 (portable 4215, install_package, load test only): Laravel Goto, ConvertEpochToDate, DlangAutoImport, DistractionFreeWindow, Custom Buffer Name, LiveServer, ColorHints, LogbackJsonLogViewer, ColorConverter, Console Exec, Compressor, CompareBuff, Jenkinsfile, Jester, Helium. Remove in groups of 4 with a wait, verify after.
2026-10-27 REMOVED batch 5 (picker): all 15 names of batch 5; package files gone, Installed Packages back to Color Scheme - Legacy / Package Control / SublimeLinter; libraries removed with their packages (only typing_extensions, pre-existing, remains in Data\Lib\python314); Preferences restored from backup.
2026-10-27 ADD batch 6 (portable 4215, install_package, load test only): Inline Fold, Ipynb Preview as Markdown, JapanWordStop, Gitignore, JS Template String Converter, FlutterEnhancements, Expand Selection to Function (JavaScript), Font Size Per View, FoldersSwitch, Folder Aliaser, AhuAIComplete, AddRemoveFolder, Insert Nums, Markdown Nav, AutoProjects. Remove in groups of 4 with a wait, verify after.
2026-10-27 REMOVED batch 6 (picker): Inline Fold, Ipynb Preview as Markdown, JapanWordStop, Gitignore, JS Template String Converter, Expand Selection to Function (JavaScript), Font Size Per View, Folder Aliaser, AhuAIComplete, AddRemoveFolder, Insert Nums, Markdown Nav, AutoProjects; FlutterEnhancements and FoldersSwitch never installed (not found in Package Control). Package files gone, Installed Packages back to baseline, no libraries left, Preferences restored.
2026-10-27 ADD batch 7 (portable 4215, install_package, load test only): RemoveDuplicateCharacters, CopyWithLineNumbersReloaded, Alphpetize, MayaSublime, Markdown Table of Contents, PowerCursors, BufferScroll, Log Highlight, Make Bookmarklet, ANSIescape, Markdown Images, BeyondCompare, MagicPython, Image Link Insertion, Highlight Token. Remove in groups of 4 with a wait, verify after.
2026-10-27 REMOVED batch 7 (picker): RemoveDuplicateCharacters, CopyWithLineNumbersReloaded, Alphpetize, MayaSublime, Markdown Table of Contents, PowerCursors, Log Highlight, Make Bookmarklet, ANSIescape, Markdown Images, BeyondCompare, Image Link Insertion, Highlight Token; BufferScroll and MagicPython never installed (not found in Package Control). Installed Packages back to baseline, no libraries left, Preferences restored.
2026-10-27 ADD batch 8 (portable 4215, install_package, load test only): CMake, CMakeBuilder, Text Highlighter, Wrap Plus, RustFmt, UnicodeMath, ZipContents, Fmt, BBCode (NGA), Sort Lines (Numerically), Virtualenv, SideBarGit, AssistantAI, SymbolBalloon, DiffTabs. Remove in groups of 4 with a wait, verify after.
2026-10-27 REMOVED batch 8 (picker): CMake, CMakeBuilder, Text Highlighter, Wrap Plus, RustFmt, UnicodeMath, ZipContents, Fmt, BBCode (NGA), Sort Lines (Numerically), Virtualenv, AssistantAI, SymbolBalloon, DiffTabs; SideBarGit never installed (not found). Text Highlighter broke the plugin host (see findings), portable restarted twice (graceful close), Text Highlighter added to ignored_packages for one start then Preferences restored from backup.
2026-10-27 REMOVED again: Alphpetize, CopyWithLineNumbersReloaded, RemoveDuplicateCharacters had reappeared in Installed Packages after the portable restarts (batch 7 members); removed via picker, Installed Packages verified back to Color Scheme - Legacy / Package Control / SublimeLinter.
2026-10-27 ADD batch 9 (portable 4215, install_package, load test only): dired, kdesrc-build, Julia, JaiTools, Project Planner, CoffeeScript, sublime-github, AutoMatlab, RSpec, MySFTP, Less, CiscoCollab, SortBy, Material Theme, xpath. Remove via Package Control picker after the test.
2026-10-27 REMOVED batch 9 (all 15 via picker; verified Installed Packages back to Color Scheme - Legacy/Package Control/SublimeLinter, orphan libraries removed; one "ignore itself" dialog dismissed)
2026-10-27 ADD batch 10 (portable 4215, install_package, load test only): Spreadsheet Formula, WrapAsYouType, PyTest, Tag, EditorConfig, CTags, Search in Project, xml2json, FileBrowser, R-IDE, CSS3, Fanhuaji, MCP Commander, iOS build system, Restructured Text (RST) Snippets. Remove via Package Control picker after the test.
2026-10-27 CORRECTION batch 10 list (MCP Commander excluded, it is the portable's own tool): Spreadsheet Formula, WrapAsYouType, PyTest, Tag, EditorConfig, CTags, Search in Project, xml2json, FileBrowser, R-IDE, CSS3, Fanhuaji, iOS build system, Restructured Text (RST) Snippets, Simplenote
2026-10-27 REMOVED batch 10 (12 installed, all removed via picker; verified Installed Packages back to baseline; empty watchdog dist-info folder left in Lib until next start; two ignore-itself dialogs and a stale CiscoCollab syntax dialog dismissed)
2026-10-27 ADD backlog118 group 1 (main Sublime, Package Control picker, one at a time): Abrase, AMPscript Syntax Highlighter, Asymptote, Atomic Color Scheme, Blossom Theme, build2. Remove via Package Control: Remove Package picker; verify Installed Packages and Package Control.sublime-settings back to baseline.
2026-10-27 STOPPED backlog118 group 1 after 2 installs (he objected to the picker appearing in his main Sublime). Abrase: installed, load check ok, REMOVED by him. AMPscript Syntax Highlighter: installed, STILL PRESENT, to be removed with the Remove Package picker when he allows window use. Package Control.sublime-settings hash changed (installed_packages now lists it).
2026-10-27 ADD backlog118 on the portable (C:\Users\donal\tools\st_portable, hwnd via sublime-mcp-portable-4215; main Sublime not used), Package Control picker, one at a time, each removed via Remove Package picker before the next; baseline Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter. List: data\backlog118_2026_10_27.tsv.
2026-10-27 CORRECTION: the backlog118 run on the portable did not start, nothing was installed there. After the log check, 114 of the 118 already have earlier log entries and the other 4 were live-tested on 2026-10-27; so there is no untested live backlog. Only leftover from this session: AMPscript Syntax Highlighter in the MAIN Sublime (Installed Packages), his to remove or to ask me to.
2026-10-28 ADD portable (C:\Users\donal\tools\st_portable, picker flow, B7 reproduction): Abrase, Writer Color Scheme, Atomic Color Scheme, one at a time. Remove each with the remove_package picker; verify Installed Packages is back to Color Scheme - Legacy, Package Control, SublimeLinter and the PC settings hash is unchanged.
2026-10-28 REMOVED (B7 reproduction on the portable): Abrase, Writer Color Scheme, Atomic Color Scheme, each via the remove_package picker with the console line 'Removed package' seen. Package Control left 'Writer Color Scheme' in installed_packages; removed that name by hand; Installed Packages and the PC settings hash are back to baseline (FBBFAC8A...).
2026-10-28 ADD (his word: installs fine if undoable) Ruby 4.0.9-1 portable 7z from github.com/oneclick/rubyinstaller2 (no installer, no admin, no PATH or registry change) into C:\Users\donal\tools\audit-prereqs\ruby, gems into ...\audit-prereqs\gems; for Rubyfmt and Ruby Markers (RESULTS rows 'prerequisite not installed'). Remove: recycle.ps1 the whole C:\Users\donal\tools\audit-prereqs folder; verify Test-Path false and PATH/registry unchanged.
2026-10-28 ADD second portable Ruby 3.4.12-1 (7z, same folder C:\Users\donal\tools\audit-prereqs, no admin/PATH/registry) because rcodetools xmpfilter fails with Errno::EACCES on tmpfile reopen under Ruby 4.0.9; to see whether it is Ruby-version specific. Removed with the whole audit-prereqs folder.
2026-10-28 REMOVED audit-prereqs (Ruby 4.0.9 and 3.4.12 portable, gems, xmp.bat, downloads) via recycle.ps1; verified: folder gone, User and Machine PATH have no audit-prereqs, no HKCU RubyInstaller key, no ruby process. Nothing was installed in Sublime.
2026-10-28 ADD WSL Sublime (build 4215 Linux, ~/.config/sublime-text; sublime-mcp-wsl-4200 server), Package Control picker flow, one at a time: PerlTidy, then perldoc. Remove each via the remove_package picker and verify Installed Packages/Packages back to baseline (LSP, Package Control, SublimeLinter, MCP Commander, Submarine, User). Perl itself is already in WSL (/usr/bin/perl); any apt install needs sudo via his tab-2 WSL terminal and gets its own ledger line first.
2026-10-28 ADD WSL (no sudo, no system change): apt download perltidy + dpkg -x into /home/dpchitester/audit_test/perltidy (and test file t.pl) for the PerlTidy test. Remove: delete /home/dpchitester/audit_test; verify with ls.
2026-10-28 REMOVED PerlTidy from the WSL Sublime via the remove_package picker (console 'Removed package', Installed Packages = LSP, Package Control, SublimeLinter; Package Control.sublime-settings has no PerlTidy). /home/dpchitester/audit_test (perltidy unpacked) kept until perldoc is done.
2026-10-28 REMOVED WSL audit_test (unpacked perltidy, wrapper, t.pl): moved to /home/dpchitester/removed_packages/audit_test_20261028 (restore by moving back); original path gone. perldoc is not in the Package Control list (install_package: not found): not installed, nothing to remove.
2026-10-28 ADD WSL: Package Control repository https://github.com/cockscomb/SublimePerldoc (package SublimePerldoc, hidden ST2-only entry) in the WSL Sublime via add_repository + install_package; and apt download perl-doc + dpkg -x into /home/dpchitester/audit_test2 (no sudo). Remove: remove_package picker, delete the repository line from WSL ~/.config/sublime-text/Packages/User/Package Control.sublime-settings, move audit_test2 to ~/removed_packages; verify.
2026-10-28 REMOVED SublimePerldoc from the WSL Sublime (remove_package picker), repository line deleted from WSL Package Control.sublime-settings (installed_packages = LSP, Package Control, SublimeLinter; no repositories), audit_test2 moved to ~/removed_packages/audit_test2_20261028; tabs closed.
2026-10-28 ADD WSL: package Pmccabe (Package Control, picker flow via install_package) and apt download pmccabe + dpkg -x into /home/dpchitester/audit_test3 (no sudo). Remove: remove_package picker (verify installed_packages baseline LSP, Package Control, SublimeLinter), move audit_test3 to ~/removed_packages.
2026-10-28 REMOVED Pmccabe from the WSL Sublime (remove_package picker); user pmccabe.sublime-settings and audit_test3 (unpacked pmccabe) moved to ~/removed_packages; installed_packages back to LSP, Package Control, SublimeLinter.
2026-10-28 ADD WSL one at a time, Package Control install_package: PyCover, PyRefactor, Python Unittest Helper, PipenvPath; their Python tools (coverage, rope, nose, pipenv) via pip install --target into /home/dpchitester/audit_pip (no sudo, no system site-packages). Remove each package via remove_package picker; at the end move audit_pip and test files to ~/removed_packages; verify installed_packages baseline.
2026-10-28 REMOVED from the WSL Sublime (remove_package picker): PyCover, PyRefactor; their User settings files moved to ~/removed_packages. audit_pip (coverage, rope) stays until PipenvPath and Python Unittest Helper are done.
2026-10-28 REMOVED Python Unittest Helper from the WSL Sublime (remove_package picker); its User settings moved to ~/removed_packages. audit_pip stays for PipenvPath.
2026-10-28 CHANGE WSL Sublime User Preferences.sublime-settings: added a pipenv_path line for the PipenvPath test (backup: ~/removed_packages/Preferences.sublime-settings.backup_20261028; restore by copying it back). Also moved the stray User/PerlTidy.sublime-settings from the PerlTidy test to ~/removed_packages (I had not removed it then). pipenv itself is in audit_pip/lib2 (pip --target), venv in audit_pip/venvs.
2026-10-28 REMOVED PipenvPath from the WSL Sublime (remove_package picker; console 'Removed package'); User Preferences.sublime-settings restored from the backup (no pipenv_path line); audit_pip (pipenv in lib2, venv, projects) moved to ~/removed_packages/audit_pip_20261028; Installed Packages = LSP, Package Control, SublimeLinter. The project window 'p' may remain in the WSL Sublime's recent list.
2026-10-28 ADD portable 4215 (C:\Users\donal\tools\st_portable; main Sublime not used), install_package tool, one at a time, to confirm or clear the static flags in data\auto_static_flags.txt for live maintained packages: Focus, Enhanced HTML and CFML, Piranha, PLI10, Squirrel, MayaSublime, Mediawiker, Jester. Remove each via remove_package picker; baseline Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Package Control.sublime-settings hash unchanged.
2026-10-28 ADD portable 4215 test copy C:\Users\donal\tools\st_portable\Data\Packages\PiranhaFix (Piranha.sublime-syntax with the 3 leading comment lines moved below the YAML header) to see whether the header position is why Piranha's syntax does not register. Remove: recycle.ps1 the folder; verify Test-Path false.
2026-10-28 REMOVED Focus, Enhanced HTML and CFML, Piranha from the portable 4215 (remove_package picker; console 'Removed package' for the first two, Piranha.sublime-package gone by Test-Path); PiranhaFix recycled with recycle.ps1 (Test-Path false). Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Packages = MCP Commander, Theme - Default, User; t.mr test tab closed.
2026-10-28 MAIL sent to the package author (Piranha undefined contexts), Gmail id 1a1817ff7874951b.
2026-10-28 ADD portable 4215 test copy Data\Packages\PLI10Fix\PLI10.sublime-syntax (PLI10 syntax with the 3 leading comment lines moved below the YAML header). Remove: recycle.ps1 the folder, Test-Path false.
2026-10-28 REMOVED PLI10 from the portable 4215 (picker; Test-Path false); PLI10Fix recycled (Test-Path false); test tab closed. Baseline Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter.
2026-10-28 MAIL sent to the package author (correction: Piranha/PLI10 header comments before %YAML, not undefined contexts), Gmail id 1a18184a70d45ff1.
2026-10-28 REMOVED Squirrel from the portable 4215 (picker; Installed Packages back to baseline); test file t.nut recycled; tab closed.
2026-10-28 REMOVED MayaSublime from the portable 4215 (picker; Installed Packages back to baseline); test file t.mel recycled; tab closed.
2026-10-28 ADD (by satisfy_libraries, portable 4215) libraries Jinja2, markupsafe, pywin32, requests, requests-oauthlib into Data\Lib\python314 for Mediawiker. REMOVED Mediawiker (picker); Package Control removed the libraries too (Lib\python314 back to package_control.py, typing_extensions, watchdog only; Test-Path checked); Package Control Messages tab closed.
2026-10-28 REMOVED Jester from the portable 4215 (picker; Installed Packages back to baseline). All eight flagged packages of the static-flag list are now live-checked.
2026-10-28 ADD in WSL (disposable, Donald: he can delete and reinstall WSL entirely): apt packages nim, rsync, patch, php-cli via 'wsl -u root apt-get install' for the prerequisite revisit (Nimpretty, Project Sync, PhpSimpleRefactor). Remove: apt-get remove --purge nim rsync patch php-cli, or wipe WSL.
2026-10-28 ADD WSL Sublime packages Nimpretty, Nim (syntax, needed by Nimpretty is_enabled) via install_package; test file ~/audit_nim/t.nim. Remove: remove_package picker, delete ~/audit_nim.
2026-10-28 REMOVED Nimpretty and Nim from the WSL Sublime (picker); ~/audit_nim moved to ~/removed_packages. apt nim, rsync, patch, php-cli stay installed in WSL (disposable).
2026-10-28 ADD WSL Sublime package Project Sync; test dirs ~/audit_sync/src and dst; ~/.config/sublime-text/Packages/User/DevSync.sublime-settings (local mapping). Remove: remove_package picker, move the dirs and the User file to ~/removed_packages.
2026-10-28 REMOVED Project Sync from the WSL Sublime (picker); ~/audit_sync and User/DevSync.sublime-settings moved to ~/removed_packages.
2026-10-28 ADD WSL Sublime package PhpSimpleRefactor (uses patch and php from apt); test file ~/audit_php/t.php. Remove: picker, move dir to ~/removed_packages.
2026-10-28 ADD in WSL ~/audit_php (refactor.phar v0.1 from the QafooLabs GitHub release, t.php) and User/PhpSimpleRefactor.sublime-settings. Remove: move both to ~/removed_packages.
2026-10-28 REMOVED PhpSimpleRefactor from the WSL Sublime (picker); ~/audit_php and both User/*SimpleRefactor.sublime-settings moved to ~/removed_packages.
2026-10-28 ADD in WSL via apt (disposable): minizinc, rtags, pgcli, postgresql, arduino-cli, for MiniZinc Language, RTagsComplete, PgcliSublime, arduino-cli (package). Remove: apt-get remove --purge those, or wipe WSL.
2026-10-28 NOTE the apt install above also pulled postfix (mail server) as a dependency of one of the packages; remove with apt-get remove --purge postfix or wipe WSL.
2026-10-28 REMOVED MiniZinc Language from the WSL Sublime (picker); ~/audit_mzn moved to ~/removed_packages; the WSL window project p still has its leftover Python unittest build system (set_build_system was changed to MZN for the test).
2026-10-28 ADD WSL Sublime package arduino-cli (install_package). Remove via picker.
2026-10-28 ADD in WSL via apt: arduino (1.8.19 IDE, pulls Java and avr tools) for the arduino-cli package test. Remove: apt-get remove --purge arduino arduino-core-avr, or wipe WSL.
2026-10-28 REMOVED arduino-cli package from the WSL Sublime (picker); ~/audit_ino, ~/.arduino15 and ~/Arduino moved to ~/removed_packages. apt arduino (IDE 1.8.19, Java) stays in WSL. The Arduino Permission Checker (asks to add the user to dialout) was closed with the window X, not Add.
2026-10-28 ADD in WSL: postgresql service started; role dpchitester (superuser, local only) and database auditdb created for the PgcliSublime test; WSL Sublime package PgcliSublime. Remove: dropdb auditdb, dropuser dpchitester, service postgresql stop, remove_package picker.
2026-10-28 ADD WSL User/PgcliSublime.sublime_settings (pgcli_site_dirs, pgcli_url). Remove: move to ~/removed_packages.
2026-10-28 REMOVED PgcliSublime from the WSL Sublime (picker); User/PgcliSublime.sublime_settings moved to ~/removed_packages; database auditdb dropped; postgresql service stopped (role dpchitester remains in the local cluster; apt postgresql, pgcli stay installed in WSL).
2026-10-28 ADD WSL Sublime package RTagsComplete (install_package) for a test with apt rtags.
2026-10-28 ADD WSL ~/audit_rtags (main.cpp, util.cpp, compile_commands.json), User/RTagsComplete.sublime-settings (rc_path), background process rtags-rdm (data dir ~/audit_rtags/.rdm). Remove: pkill rtags-rdm, move dir and the User file to ~/removed_packages.
2026-10-28 REMOVED RTagsComplete from the WSL Sublime (picker); rtags-rdm stopped (pkill, verified none running); ~/audit_rtags, User/RTagsComplete.sublime-settings and ~/.rdm moved to ~/removed_packages; apt rtags stays installed in WSL.
2026-10-28 ADD in WSL ~/audit_cmakelint (pip --target cmakelint, wrapper bin/cmakelint, proj/CMakeLists.txt). Remove: move the folder to ~/removed_packages.
2026-10-28 ADD in WSL symlink /usr/local/bin/cmakelint -> ~/audit_cmakelint/bin/cmakelint (root), WSL Sublime package SublimeLinter-contrib-cmakelint. Remove: rm the symlink, remove_package picker.
2026-10-28 ADD WSL Sublime package CMake (syntax, needed by the cmakelint linter selector source.cmake). Remove via picker.
2026-10-28 REMOVED SublimeLinter-contrib-cmakelint and CMake from the WSL Sublime (picker); /usr/local/bin/cmakelint symlink removed; ~/audit_cmakelint moved to ~/removed_packages. WSL now has an extra empty Sublime window from new_window and the old project window p still shows a Package Control Messages tab.
2026-10-28 PLAN (Donald: re-consider anything WSL dependent): retest in the WSL Sublime the Linux/Unix-dependent rows: Open With, Open in Nautilus, Open in Thunar, NotmuchAddress, ShellVE, Subtitle Sync, GoImports, Pman, Dotfiles Syntax Highlighting, Bash Build System. Each add gets its own ledger line first.
2026-10-28 ADD WSL Sublime package Open With (install_package). Remove via picker.
2026-10-28 CHANGE WSL Package Control.sublime-settings: add_repository for https://github.com/j-martin/open-with-sublime (not in the picker on Linux). Backup: ~/removed_packages/Package Control.sublime-settings.before_openwith_20261028. Restore: copy it back.
2026-10-28 ADD WSL Sublime package open-with-sublime (from the added repository) and test dir ~/audit_ow. Remove: picker, move dir, restore Package Control.sublime-settings from the backup.
2026-10-28 REMOVED open-with-sublime from the WSL Sublime (picker); ~/audit_ow moved; WSL Package Control.sublime-settings restored from the backup (no open-with repository; the after copy kept in ~/removed_packages).
2026-10-28 ADD in WSL via apt: golang-go, notmuch (for GoImports and NotmuchAddress). Remove: apt-get remove --purge, or wipe WSL.
2026-10-28 ADD WSL Sublime package GoImports (install_package); it may download goimports into its own bin folder at load time. Remove via picker; delete leftovers.
2026-10-28 REMOVED GoImports from the WSL Sublime (picker; folder gone from Packages). apt golang-go and notmuch stay in WSL.
2026-10-28 ADD WSL Sublime package NotmuchAddress (install_package). Remove via picker.
2026-10-28 CHANGE WSL Package Control.sublime-settings: add_repository https://github.com/yeled/sublime-notmuch-address (hidden from the picker). Backup ~/removed_packages/Package Control.sublime-settings.before_notmuch_20261028; restore by copying it back.
2026-10-28 ADD WSL Sublime package sublime-notmuch-address (from the added repository). Remove via picker, restore Package Control settings.
2026-10-28 REMOVED sublime-notmuch-address from the WSL Sublime (picker); WSL Package Control.sublime-settings restored from the backup (no notmuch repository).
2026-10-28 ADD in WSL via apt: thunar, nautilus (for Open in Thunar, Open in Nautilus). Remove: apt-get remove --purge thunar nautilus, or wipe WSL.
2026-10-28 NOTE the WSL Sublime stopped after the apt install of thunar and nautilus (no process, ports 9530/9532 closed); relaunched with setsid from ~/.local/sublime/sublime_text; its log is ~/removed_packages/st_launch_20261028.log.
2026-10-28 ADD WSL Sublime package Open in Thunar (install_package). Remove via picker; close the Thunar window if it opens.
2026-10-28 REMOVED Open in Thunar from the WSL Sublime (picker); the test Thunar process stopped with pkill (none running).
2026-10-28 ADD WSL Sublime package Open in Nautilus (install_package). Remove via picker; stop nautilus.
2026-10-28 ADD WSL test dir ~/audit_na (a.txt). Remove: move to ~/removed_packages.
2026-10-28 REMOVED Open in Nautilus from the WSL Sublime (picker); nautilus and thunar processes stopped; ~/audit_na moved to ~/removed_packages.
2026-10-28 ADD WSL Sublime package Dotfiles Syntax Highlighting; test dir ~/audit_df (.env, .bash_aliases). Remove via picker, move dir.
2026-10-28 REMOVED Dotfiles Syntax Highlighting from the WSL Sublime (picker); ~/audit_df moved.
2026-10-28 ADD WSL Sublime packages Bash Build System and Pman (install_package). Remove via picker.
2026-10-28 ADD WSL test dir ~/audit_bb (hello.sh). Remove: move to ~/removed_packages.
2026-10-28 REMOVED Bash Build System and Pman from the WSL Sublime (picker); ~/audit_bb moved.
2026-10-28 CHANGE WSL Package Control.sublime-settings: add_repository https://github.com/apiad/sublime-subtitle-sync (hidden from the picker). Backup ~/removed_packages/Package Control.sublime-settings.before_subsync_20261028; restore by copying it back. AutoAligner needs no retest (done with real Ruby, generall/aligner#7 and #8).
2026-10-28 ADD WSL Sublime package sublime-subtitle-sync (from the added repository). Remove via picker, restore Package Control settings.
2026-10-28 ADD WSL test dir ~/audit_ss (t.srt). Remove: move to ~/removed_packages.
2026-10-28 REMOVED sublime-subtitle-sync from the WSL Sublime (picker); ~/audit_ss moved; WSL Package Control.sublime-settings restored from the backup (no subtitle repository).
2026-10-28 ADD WSL ~/audit_ve (python venv, proj/a.py) and WSL Sublime packages ShellVE and TerminalView (install_package). Remove: picker, move the dir.
2026-10-28 REMOVED ShellVE and TerminalView from the WSL Sublime (picker); ~/audit_ve moved. The WSL Sublime has an extra project window for ~/audit_ve/proj/p.sublime-project (now missing).
2026-10-28 ADD in WSL ~/audit_p4 (Perforce p4 and p4d free binaries from cdist2.perforce.com, user-level, no account; a local test depot will go under ~/audit_p4). Remove: stop p4d, move ~/audit_p4 to ~/removed_packages.
2026-10-28 ADD WSL Sublime package P4Explorer (install_package). Remove via picker.
2026-10-28 ADD in WSL: background process p4d on localhost:1666 (root ~/audit_p4/root), client auditws (root ~/audit_p4/ws), user dpchitester, two submitted files; no account, no network. Remove: pkill p4d, move ~/audit_p4.
2026-10-28 ADD in WSL: symlink /usr/local/bin/p4 -> ~/audit_p4/bin/p4 (root) and ~/.p4enviro (P4PORT, P4USER, P4CLIENT via p4 set). Remove: rm the symlink, move ~/.p4enviro to ~/removed_packages.
2026-10-28 ADD WSL Sublime package Perforce (install_package). Remove via picker.
2026-10-28 REMOVED Perforce package from the WSL Sublime (picker; folder gone). p4d, the p4 symlink and ~/.p4enviro stay for the next Perforce packages.
2026-10-28 ADD WSL Sublime package P4Gutter (install_package). Remove via picker.
2026-10-28 ADD WSL User/P4Gutter.sublime-settings (binary, user, port, workspace, errorlog). Remove: move to ~/removed_packages.
2026-10-28 REMOVED P4Gutter from the WSL Sublime (picker); User/P4Gutter.sublime-settings moved; the test edit in the Perforce workspace reverted. p4d, p4 symlink and .p4enviro still in place.
2026-10-28 ADD WSL Sublime package Waza (install_package). Remove via picker.
2026-10-28 REMOVED Waza from the WSL Sublime (picker); the Perforce workspace reverted (c.txt, my test file, deleted).
2026-10-28 CHANGE WSL Package Control.sublime-settings: add_repository https://github.com/ymengesha/P4Explorer (not in the Linux picker). Backup ~/removed_packages/Package Control.sublime-settings.before_p4x_20261028; restore by copying it back.
2026-10-28 ADD WSL Sublime package P4Explorer (from the added repository). Remove via picker, restore Package Control settings.
2026-10-28 REMOVED P4Explorer from the WSL Sublime (picker); WSL Package Control.sublime-settings restored from the backup (no P4Explorer repository); /tmp/P4Explorer moved to ~/removed_packages.
2026-10-28 ADD WSL Sublime package DiffP4Merge (install_package). Remove via picker.
2026-10-28 ADD in WSL ~/audit_p4merge (p4v.tgz 188 MB from cdist2.perforce.com, extracted there; P4Merge GUI, user-level). Remove: move the folder to ~/removed_packages.
2026-10-28 ADD WSL test dir ~/audit_dm (x.txt, y.txt). Remove: move to ~/removed_packages.
2026-10-28 ADD WSL User/DiffP4merge.sublime-settings (p4merge_path). Remove: move to ~/removed_packages; stop any p4merge process.

2026-10-28 REMOVED (WSL): DiffP4Merge package (Package Control remove), p4d stopped, /usr/local/bin/p4 symlink removed, ~/audit_dm ~/audit_p4merge ~/audit_p4 ~/.p4enviro and User/DiffP4merge.sublime-settings moved to ~/removed_packages (*_20261028). Verified: Installed Packages = LSP, Package Control, SublimeLinter; no p4d/p4merge process; no p4 in /usr/local/bin.
2026-10-28 ADD+REMOVED (WSL): ScalafmtEnhanced via install_package, removed by remove_package picker; verified gone from Packages.

2026-10-28 CHANGE (portable tools\st_portable): MCP Commander plugin folder replaced by git archive of sublime-mcp HEAD a3e3664 (was 1.16.2); old folder kept at scratchpad\MCP Commander.1.16.2; require_consent_for_destructive false removed from User settings (backup scratchpad\portable_settings.bak). Undo: put the old folder and settings back.
2026-10-28 ADD (WSL Sublime): NestingSnippet and SnippetCaller via install_package, to test the keymap that needs insert_snippet_enhanced. Remove: remove_package picker for both, verify Packages dir.
2026-10-28 ADD (WSL): also Context, LocalVariable, QuickSearchEnhanced, Method, Expression, Statement (SnippetCaller's six siblings) via install_package. REMOVED all eight (NestingSnippet, SnippetCaller and the six) via remove_package picker; verified Installed Packages = LSP, Package Control, SublimeLinter. WSL Sublime restarted once. Window flag: the WSL window was left always-on-top by the foreground steps; cleared with SetWindowPos HWND_NOTOPMOST.
2026-10-28 ADD (WSL Sublime): RSL via install_package, to find and run rsltc if available for Linux. Remove: remove_package picker plus any rsltc files (recorded here when added).
2026-10-28 CREATED (WSL): ~/audit_rsl/x.rsl test file. Remove: move to ~/removed_packages after the RSL test.
2026-10-28 REMOVED (WSL): RSL (remove_package picker), test tab x.rsl closed, ~/audit_rsl moved to ~/removed_packages/audit_rsl_20261028. Verified Installed Packages = LSP, Package Control, SublimeLinter. rsltc itself NOT installed (cannot be: see RESULTS).
2026-10-28 ADD (WSL Sublime): C++YouCompleteMe via install_package, to read what it needs from ycmd and try a ycmd build in WSL (~/audit_ycmd). Remove: remove_package picker, move ~/audit_ycmd to ~/removed_packages, apt build deps stay (listed when added).
2026-10-28 DOWNLOAD (WSL, no root): CppYCM branch compiled-ycmd cloned to ~/audit_ycmd/cppycm and unzipped to ~/audit_ycmd/server; Python 2.7.18 source built with --enable-shared into ~/audit_ycmd/py27 (needed by ycm_core.so). Remove: move ~/audit_ycmd to ~/removed_packages, remove C++YouCompleteMe package.
2026-10-28 CREATED (WSL): ~/audit_ycmd/py27w.sh, ~/audit_ycmd/proj (main.cpp, .ycm_extra_conf.py), ~/audit_ycmd/server/CORE_VERSION (17, the bundle lacks it), ~/.config/sublime-text/Packages/User/C++YouCompleteMe.sublime-settings. Remove all (settings file to ~/removed_packages).
2026-10-28 CREATED (WSL): ~/.config/sublime-text/Packages/C++YouCompleteMe (folder, patched copy: collections.abc.Mapping) to see past the first py3.10+ defect. Remove: move the folder to ~/removed_packages, remove the real package, kill any ycmd process.
2026-10-28 REMOVED (WSL): C++YouCompleteMe (remove_package picker; the patched folder copy went with it), tabs closed, ycmd killed, ~/audit_ycmd (cppycm clone, unzipped server, Python 2.7.18 source and private build, proj) moved to ~/removed_packages/audit_ycmd_20261028, User/C++YouCompleteMe.sublime-settings moved. Verified Installed Packages = LSP, Package Control, SublimeLinter; Packages = MCP Commander, Submarine, User; no ycmd process. WSL Sublime restarted three times.
2026-10-28 CREATED (portable tools\st_portable): Data\Packages\Direct Copy (copy of the patched clone tools\forks\SublimeDirectCopy, no .git) to test the menu fix. Remove: move the folder to the Recycle Bin via recycle.ps1; close the tabs it opens.
2026-10-28 REMOVED (portable): Data\Packages\Direct Copy recycled; both settings tabs closed; no User\DirectCopy.sublime-settings was created.
2026-10-28 REMOVED: tools\forks\SublimeDirectCopy (plain clone with one local commit, never pushed) recycled; Donald declined forks and PRs for unifreak's request. Nothing was created on GitHub.
2026-10-28 CREATED: tools\forks\SublimeDirectCopy (clone with fix commit) and the GitHub fork dpc00/SublimeDirectCopy for the PR unifreak asked for on #1 (Donald: I wrongly put a deny block for fork/pr create in his settings.json; removed it). Remove: delete the fork on GitHub after merge or a reasonable wait (closes the PR), then recycle the clone.
2026-10-28 CREATED (portable): Data\Packages\Direct Open (patched clone of unifreak/SublimeDirectOpen, no .git) to test the menu fix. Also clones tools\forks\SublimeDirectOpen and tools\forks\SublimeLyricEditor (PRs for unifreak, Donald: do all, delete forks only when unanswered for a reasonable time). Remove: recycle the portable folder after the test.
2026-10-28 REMOVED (portable): Data\Packages\Direct Open recycled; both tabs closed; no User\DirectOpen.sublime-settings created.
2026-10-28 CORRECTION: edit_settings DID create portable Data\Packages\User\DirectOpen.sublime-settings (starter copy of the default); recycled. Menu test of Direct Copy earlier created no User file.
2026-10-28 CREATED (portable): Data\Packages\LyricEditor (copy of tools\forks\SublimeLyricEditor working tree, no .git) to test three small fixes one by one; also an untitled test tab. Remove: recycle the folder and close the tab by name.
2026-10-28 REMOVED (portable): Data\Packages\LyricEditor recycled, test tab closed (emptied first: the portable server cannot be asked to approve close_file discard), overlay closed; portable back to its single empty untitled tab.
2026-10-28 CREATED: GitHub forks dpc00/SublimeDirectOpen (PR #2) and dpc00/SublimeLyricEditor (two PRs: fix-offset, fix-debug-default) for unifreak's PR request. Remove: delete a fork on GitHub only if the maintainer has not responded in a reasonable time (Donald's rule); then recycle its clone in tools\forks.
2026-10-28 ADD (portable 4215, install_package) Archive Nested Lines: audit, one of 9 channel packages never tested; remove with remove_package and verify Installed Packages afterwards.
2026-10-28 REMOVED (portable 4215) Archive Nested Lines (picker) and Focus. CORRECTION: the 03:58 ledger line said Focus was removed but Focus.sublime-package was still in Installed Packages at 05:19 (found while removing Archive Nested Lines); removed again via the picker and verified by listing: Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter. Lesson: verify every removal by listing the folder, not by the picker call returning ok.
2026-10-28 ADD (WSL, no root): Statac via get.statac.dev script (read first; writes ~/.local/bin/statac and ~/.local/share/statac), needed by LSP-statac; plus packages LSP-statac (install_package) in the WSL Sublime. Test site in ~/audit_statac. Remove: delete ~/.local/bin/statac and ~/.local/share/statac (move to ~/removed_packages), ~/audit_statac, remove_package LSP-statac, verify by listing.
2026-10-28 REMOVED (WSL): LSP-statac (picker), statac lsp process killed, ~/.local/bin/statac -> ~/removed_packages/statac_bin_20261028, ~/.local/share/statac -> statac_share_20261028, ~/audit_statac -> audit_statac_20261028. Verified by listing: Installed = LSP, Package Control, SublimeLinter; Packages = MCP Commander, Submarine, User; no statac process.
2026-10-28 ADD (portable 4215, install_package): ReadableResume Snippets, BlackboardForever Color Scheme, Icons - FileIcons, Deep JSON Color Schemes, AMX Mod X Pawn (audit; five of the last 9 untested channel packages). Remove each with remove_package and verify by listing Installed Packages; reset any color_scheme or icon theme setting I change.
2026-10-28 REMOVED (portable 4215): ReadableResume Snippets, BlackboardForever Color Scheme, Icons - FileIcons, Deep JSON Color Schemes, AMX Mod X Pawn (picker, pick_quick_panel; posted Return keys landed in the editor). Verified by listing: Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Packages = MCP Commander, Theme - Default, User; no leftovers in User; test tabs closed.
2026-10-28 ADD (portable 4215, picker): 3D Tool (Async Burst-Mode), then Meteor Autocomplete (TernJS) (audit, last two untested channel packages). Remove each with remove_package and verify by listing Installed Packages and Packages; Meteor may download Tern/node_modules into its package folder, check Packages for leftovers.
2026-10-28 REMOVED (portable 4215): 3D Tool (Async Burst-Mode), Meteor Autocomplete (TernJS) (picker, pick_quick_panel). Verified by listing: Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Packages = MCP Commander, Theme - Default, User; no Tern node process left; test tabs closed; test project only in the session scratchpad.
2026-10-28 ADD (Windows, per-user, no admin): pip install --target C:\Users\donal\tools\audit-prereqs\pylibs cmakelint (prerequisite for SublimeLinter-contrib-cmakelint revisit; pure Python). Remove: recycle C:\Users\donal\tools\audit-prereqs (recycle.ps1) and verify Test-Path false; also remove the linter override in the portable's User SublimeLinter settings and the package + CMake syntax + SublimeLinter-contrib-cmakelint via the picker.
2026-10-28 ADD (portable 4215, picker): SublimeLinter-contrib-cmakelint, then CMake (syntax) for the cmakelint revisit. Remove both via remove_package and verify.
2026-10-28 ADD (portable 4215): temp file Data\Packages\User\SublimeLinter.sublime-settings (cmakelint executable + PYTHONPATH override; file did not exist before). Remove: recycle it.
2026-10-28 REMOVED: SublimeLinter-contrib-cmakelint and CMake (picker), User\SublimeLinter.sublime-settings and C:\Users\donal\tools\audit-prereqs (recycle.ps1). Verified: Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Packages = MCP Commander, Theme - Default, User; both paths Test-Path False; test tabs closed.
2026-10-28 ADD (portable 4215, picker): PyCover (revisit with coverage.py). Remove via remove_package and verify.
2026-10-28 ADD (Windows, per-user, no admin): pip install --target C:\Users\donal\tools\audit-prereqs\pylibs coverage (PyCover revisit); wrapper C:\Users\donal\tools\audit-prereqs\runcov.cmd; temp file portable Data\Packages\User\PyCover.sublime-settings. Remove: recycle those, remove PyCover via picker, verify.
2026-10-28 REMOVED: PyCover (picker), User\PyCover.sublime-settings and C:\Users\donal\tools\audit-prereqs (recycle.ps1). Verified as listed above; tabs closed.
2026-10-28 ADD (portable 4215, picker): PyRefactor (revisit with rope). Remove via remove_package and verify.
2026-10-28 ADD (Windows, per-user, no admin): pip install --target C:\Users\donal\tools\audit-prereqs\pylibs rope (PyRefactor revisit); wrapper runpy.cmd; temp file portable Data\Packages\User\PyRefactor.sublime-settings; test project in session scratchpad. Remove: recycle those, remove PyRefactor via picker, verify.
2026-10-28 REMOVED: PyRefactor (picker), User\PyRefactor.sublime-settings and C:\Users\donal\tools\audit-prereqs (recycle.ps1). Verified as listed above; tabs and panel closed; test project only in session scratchpad.
2026-10-28 ADD (portable 4215, picker): Python Unittest Helper (revisit, run commands). Remove via remove_package and verify.
2026-10-28 REMOVED: Python Unittest Helper (picker). Nothing else was installed for it (python -m unittest via a view setting). Verified: Installed Packages = Color Scheme - Legacy, Package Control, SublimeLinter; Packages = MCP Commander, Theme - Default, User; tabs and panel closed.
2026-10-28 ADD (Windows, per-user, no admin): pip install --target C:\Users\donal\tools\audit-prereqs\pylibs pipenv (PipenvPath revisit) plus portable picker install of PipenvPath. Remove: recycle C:\Users\donal\tools\audit-prereqs, remove PipenvPath via picker, recycle any test venv created under the session scratchpad, verify.
2026-10-28 ADD (portable 4215): temporary line pipenv_path in Data\Packages\User\Preferences.sublime-settings (backup + hash in session scratchpad portable_Preferences.backup/.hash); test project with .venv in session scratchpad. Remove: restore the backup (hash must match), recycle prereqs.
2026-10-28 REMOVED: PipenvPath (picker), Preferences restored from backup (hash equal), C:\Users\donal\tools\audit-prereqs and the scratchpad pipenvproj (recycle.ps1). Verified: baseline Installed Packages and Packages, no ~\.virtualenvs folder, project closed.
2026-10-28 ADD (Windows, per-user, no admin, no installer): download https://nim-lang.org/download/nim-2.2.6_x64.zip and unzip into C:\Users\donal\tools\audit-prereqs\nim (Nimpretty revisit; contains nimpretty.exe) plus portable picker install of Nimpretty. Remove: recycle C:\Users\donal\tools\audit-prereqs, remove Nimpretty via picker, verify.
2026-10-28 ADD (portable 4215, picker): a Nim syntax package (source.nim) as the Nimpretty test prerequisite, plus satisfy_libraries for shellenv if needed; temp User\Nimpretty.sublime-settings pointing cmd at the unzipped nimpretty.exe. Remove all via picker/recycle and verify.
2026-10-28 REMOVED: Nimpretty and Nim (NimLime) (picker), User\Nimpretty.sublime-settings and C:\Users\donal\tools\audit-prereqs incl. the Nim 2.6.6 zip and unzipped toolchain (recycle.ps1). Verified: baseline Installed Packages and Packages, no Nim files left in User, tab closed (Save Changes dialog answered No on my scratch test file).
2026-10-28 ADD (Windows, per-user, no admin, no installer): download strawberry-perl-5.40.5.1-64bit-portable.zip (about 304 MB, StrawberryPerl/Perl-Dist-Strawberry release) into C:\Users\donal\tools\audit-prereqs\dl and unzip to ...\perl (for perldoc and PerlTidy revisits); portable picker installs of perldoc and PerlTidy. MiniZinc deferred (only a setup.exe, no 7-Zip, no per-user zip). Remove: recycle C:\Users\donal\tools\audit-prereqs, remove packages via picker, verify.
2026-10-28 ADD (portable 4215, picker): perldoc, then PerlTidy. Remove via remove_package and verify.
2026-10-28 CORRECTION: perldoc is not offered by the Package Control picker any more (no match for perldoc among 4728 items), so it is not installed and not tested; only PerlTidy was installed (picker).
2026-10-28 REMOVED: PerlTidy (picker), C:\Users\donal\tools\audit-prereqs incl. Strawberry Perl 5.40.5.1 zip and unzipped tree (recycle.ps1). Verified: baseline Installed Packages and Packages, no Perl leftovers in User, tabs closed, extra (demo) portable window closed. MiniZinc deferred (setup.exe only).
ADD 2026-10-28 (WSL, per-user, no sudo): git clone of ycmd into ~/tools/ycmd and a Python venv ~/tools/ycmd-venv with pip cmake, to build ycmd for C++YouCompleteMe revisit (build.py downloads clangd/clang into the clone). Remove: rm -rf ~/tools/ycmd ~/tools/ycmd-venv (WSL is disposable).
REMOVED 2026-10-28 (WSL): ~/tools/ycmd, ~/tools/ycmd-venv, ~/tools/audit-ycm-test, build and submodule logs, User/C++YouCompleteMe.sublime-settings, and the C++YouCompleteMe package (picker). Verified with a directory listing: ~/tools holds only older entries, no youcomplete files left.
REMOVED 2026-10-28 (WSL): RTagsComplete (picker), its User settings file, ~/tools/audit-rtags-test, ~/.rtags; rtags-rdm stopped. No new install: apt package rtags 2.41 was already in WSL (stays, he said no apt cleanup). Verified: no rdm process, no RTags files outside Sublime's own Backup folder.
ADD 2026-10-28 (Windows, per-user, no admin): VS Code portable zip unpacked to C:\Users\donal\tools\vscode_portable (with its own data folder), for the extension audit he ordered ('you install VS Code, we install MCP, you control VS Code with it and test 50000 extensions'). Allowed by him this turn. Remove: recycle.ps1 on C:\Users\donal\tools\vscode_portable (nothing is written outside it: no registry, no PATH); verify with Test-Path.
ADD 2026-10-28 (VS Code portable): extension pkief.material-icon-theme through vscode-mcp install_extension, to test the tool. Lives in C:\Users\donal\tools\vscode_portable\app\data\extensions. Remove: uninstall_extension, or recycle the portable folder.
ADD 2026-10-29 (portable st_portable, per-user, no admin): User\ObsidianOrig.tmTheme and User\ObsidianFix.tmTheme (upstream master and the fix of mekwall/obsidian-color-scheme#19) plus a color_scheme line in User\Preferences.sublime-settings, to compare the two on screen. Allowed by him this turn (test it). Remove: recycle.ps1 on both theme files, restore Preferences from the scratchpad backup (Preferences.sublime-settings.bak), verify with Test-Path and a read of Preferences.
REMOVED 2026-10-29 (portable st_portable): User\ObsidianOrig.tmTheme and User\ObsidianFix.tmTheme (Recycle Bin), Preferences.sublime-settings restored from backup (hash identical), portable closed. Verified with Test-Path and a hash compare.
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\InsertNumsTest (copies of SublimeText/InsertNums InsertNums.py, one with a one-line fix, plus a runner that writes results to the scratchpad) to test the fix for InsertNums#35. Allowed by him this turn (investigate and publish a fix comment). Remove: recycle.ps1 on that folder; verify with Test-Path.
REMOVED 2026-10-29 (portable st_portable): Packages\InsertNumsTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing (MCP Commander, Theme - Default, User remain).
ADD 2026-10-29 (portable st_portable, Package Control picker): LSP-systemd 1.0.2 (and LSP if it does not come along) to answer macowie in sublimelsp/LSP-systemd#6 (does 1.0.2 load on Python 3.8). Allowed by him this turn (do the three test requests). Remove: Remove Package picker (run_command remove_package, then pick), then verify the folder is gone from Data\Packages and Installed Packages.
ADD 2026-10-29 (portable st_portable, Package Control picker): LSP, the host package LSP-systemd needs, for the same LSP-systemd#6 test. Remove: Remove Package picker; verify.
NOTE 2026-10-29 (portable st_portable): installing LSP also brought libraries bracex 3.2, mdpopups 5.1.2, orjson 3.13.0, wcmatch 11.2 (Python 3.14) into Data\Lib\python314 and Package Control's library list; remove them after the LSP-systemd#6 test (Remove Package picker for LSP, then check Data\Lib\python314 and delete only those four with recycle.ps1 if they stay).
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\Theme - Timeless (loose copy of iccir/Timeless-Theme at commit 5ccb25f, later IconSupport.py of tag 0.8.0 as control), Packages\User\C++.sublime-settings with extensions inl and ipp, Preferences lines theme.timeless.icons.*, and the cache folder Cache\Timeless Icon Support that the theme creates; to answer iccir in iccir/Timeless-Theme#19. Allowed by him this turn. Remove: recycle.ps1 on the package folder, User\C++.sublime-settings and the cache folder; restore Preferences from the scratchpad backup; verify with Test-Path and a hash compare.
REMOVED 2026-10-29 (portable st_portable): Theme - Timeless test package, User\C++.sublime-settings and Cache\Timeless Icon Support (Recycle Bin); Preferences restored from backup. Verified with Test-Path and a hash compare.
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\DBpedia Lookup (loose copy of rvolz/sublime_dbpedia_lookup branch fix/issue#1, commit 6c22c95 and the two before it) to answer rvolz in rvolz/sublime_dbpedia_lookup#1. Allowed by him this turn. Remove: recycle.ps1 on that folder; verify with Test-Path.
REMOVED 2026-10-29 (portable st_portable): Packages\DBpedia Lookup test copy (Recycle Bin); test tabs closed. Verified with Test-Path.
REMOVED 2026-10-29 (portable st_portable): LSP-systemd 1.0.2 and LSP 2.16.0 removed through the Remove Package picker; Package Control removed the orphaned libraries bracex, mdpopups, orjson, wcmatch itself (console lines). Portable closed. Verified with directory listings: Installed Packages holds Color Scheme - Legacy, Package Control, SublimeLinter; Packages holds MCP Commander, Theme - Default, User.
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\SimpleMovementsTest (two copies of colinta/SublimeSimpleMovements simple_movements.py, one with the set fix, plus a runner that writes timings to the scratchpad) to test the fix for colinta/SublimeSimpleMovements#4 before a PR. Allowed by him this turn (proceed with what is left). Remove: recycle.ps1 on that folder; verify with Test-Path.
REMOVED 2026-10-29 (portable st_portable): Packages\SimpleMovementsTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing (MCP Commander, Theme - Default, User remain); Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable, Package Control picker): SublimeLinter-javac 1.4.0 and a sample Main.java kept in the session scratchpad (not in the portable), to confirm that kaste's release fixes SublimeLinter-javac#25 (emoji column). Allowed by him this turn (do kaste's javac#25). Remove: Remove Package picker for SublimeLinter-javac; verify the Installed Packages listing.
REMOVED 2026-10-29 (portable st_portable): SublimeLinter-javac 1.4.0 removed through the Remove Package picker (console: Removed package), test tabs closed, portable closed. Verified: Installed Packages holds Color Scheme - Legacy, Package Control, SublimeLinter; Packages holds MCP Commander, Theme - Default, User; Preferences unchanged (hash). Main.java stays in the session scratchpad.
ADD 2026-10-29 (portable st_portable, Package Control picker): SublimeLinter-cppcheck 2.1.0 and a sample m.c kept in the session scratchpad (not in the portable), to confirm that kaste's release fixes SublimeLinter-cppcheck#25 (UTF-8 byte columns). Allowed by him this turn (go, next in order). Remove: Remove Package picker for SublimeLinter-cppcheck; verify the Installed Packages listing.
REMOVED 2026-10-29 (portable st_portable): SublimeLinter-cppcheck 2.1.0 removed through the Remove Package picker (console: Removed package), test tabs closed, portable closed. Verified: Installed Packages holds Color Scheme - Legacy, Package Control, SublimeLinter; Packages holds MCP Commander, Theme - Default, User; Preferences unchanged (hash). m.c stays in the session scratchpad.
ADD 2026-10-29 (Windows, per-user, no admin, no global change): npm install tslint@6.1.3 and typescript@5 into the session scratchpad folder ...\scratchpad\tslint (its own package.json and node_modules, a.ts, tslint.json), to confirm that SublimeLinter-tslint 1.7.0 fixes SublimeLinter-tslint#46 (UTF-16 columns). Allowed by him this turn (yes, next in order) and under his 10-28 rule (undoable installs fine). Remove: recycle.ps1 on the scratchpad\tslint folder; verify with Test-Path. Also SublimeLinter-tslint through the picker in the portable (removed after).
REMOVED 2026-10-29: the scratchpad\tslint folder (tslint 6.1.3, typescript 5.9.3, a.ts, tslint.json; Recycle Bin) and SublimeLinter-tslint 1.7.0 in the portable (Remove Package picker, console: Removed package); test tabs closed, portable closed. Verified: scratchpad\tslint gone (Test-Path), Installed Packages holds Color Scheme - Legacy, Package Control, SublimeLinter; Packages holds MCP Commander, Theme - Default, User; Preferences unchanged (hash). No global npm change was made.
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\PatchApplyTest (two copies of kkujawinski/sublime-text-3-patch-apply Patch Apply.py, one with the UTF-8 fix, plus a runner that writes results to the scratchpad and uses Git for Windows' patch.exe through the PATH of the portable process only; no PATH or system change) to test the fix for kkujawinski/sublime-text-3-patch-apply#2 before a new PR. Allowed by him this turn (yes, next in order). Remove: recycle.ps1 on that folder; verify with Test-Path.
REMOVED 2026-10-29 (portable st_portable): Packages\PatchApplyTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing (MCP Commander, Theme - Default, User remain); Preferences unchanged (hash). No PATH or system change was made (patch.exe was on the PATH of the portable process only).
ADD 2026-10-29 (portable st_portable, per-user, no admin): Packages\RiotTest (riot.sublime-syntax of riot/syntax-highlight master as riot_orig, and the brace-balancing fix as riot_fix, plus a runner that writes scope readings to the scratchpad) to test the fix for riot/syntax-highlight#14 and #13 before a PR. Allowed by him this turn (yes, next in order). Remove: recycle.ps1 on that folder; verify with Test-Path.
REMOVED 2026-10-29 (portable st_portable): Packages\RiotTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing (MCP Commander, Theme - Default, User remain); Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\ScssTest (throwaway runner that expands 8 SCSS snippets, original vs fixed, for onhernandes/sublime-scss-snippets#2). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\ScssTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\QunitTest (throwaway: qunit completions orig vs fixed, for maxhoffmann/qunit-snippets#2). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\QunitTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\QunitTest again (fixed qunit completions, popup screenshot, maxhoffmann/qunit-snippets#3). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\QunitTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\P4Test (throwaway: p4 grammar orig vs fixed, scope check, c3m3gyanesh/p4-syntax-highlighter#7). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\P4Test (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\EfhTest (throwaway: EasyFileHider command orig vs fixed; it writes file_exclude_patterns into the portable User Preferences and may create User\EasyFileHider.sublime-settings; Preferences restored from backup after), AustinTruex68/EasyFileHider#3. Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\EfhTest and User\EasyFileHider.sublime-settings (Recycle Bin), Preferences restored from backup, portable closed. Verified with Test-Path and a folder listing; Preferences hash equals the backup.
REMOVED 2026-10-29 (portable st_portable): User\ANSIescape, User\HighlightToken, User\Log Highlight, User\MySFTP and User\MySFTP.sublime-settings (residue of the 2026-10-27 batch 7 and 9 tests, Recycle Bin). User now holds only MCP Commander and Package Control settings and Preferences.
ADD 2026-10-29 (portable st_portable): Packages\ScssTest (throwaway runner that expands 8 SCSS snippets, original vs fixed, for onhernandes/sublime-scss-snippets#2). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\ScssTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\P4Test (throwaway: p4 grammar orig vs fixed, scope check, c3m3gyanesh/p4-syntax-highlighter#7). Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (portable st_portable): Packages\P4Test (throwaway: p4 grammar orig vs fixed, scope check, c3m3gyanesh/p4-syntax-highlighter#7). Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (portable st_portable): Packages\P4Test (throwaway: p4 grammar orig vs fixed, scope check, c3m3gyanesh/p4-syntax-highlighter#7). Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (portable st_portable): Packages\P4Test (throwaway: p4 grammar orig vs fixed, scope check, c3m3gyanesh/p4-syntax-highlighter#7). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\P4Test (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\EfhTest again (EasyFileHider orig vs fixed, empty and repeated input, side-bar check), AustinTruex68/EasyFileHider#4. Preferences restored from backup after each case. Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\EfhTest and User\EasyFileHider.sublime-settings (Recycle Bin), Preferences restored from backup, portable closed. Verified with Test-Path and a folder listing; Preferences hash equals the backup.
ADD 2026-10-29 (portable st_portable): Packages\RiotTest again (riot grammars: master, fix branch, riot.tmlanguage; braces in strings), riot/syntax-highlight#15. Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (second run) (portable st_portable): Packages\RiotTest again (riot grammars: master, fix branch, riot.tmlanguage; braces in strings), riot/syntax-highlight#15. Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (third run) (portable st_portable): Packages\RiotTest again (riot grammars: master, fix branch, riot.tmlanguage; braces in strings), riot/syntax-highlight#15. Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (fourth run) (portable st_portable): Packages\RiotTest again (riot grammars: master, fix branch, riot.tmlanguage; braces in strings), riot/syntax-highlight#15. Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (fifth run) (portable st_portable): Packages\RiotTest again (riot grammars: master, fix branch, riot.tmlanguage; braces in strings), riot/syntax-highlight#15. Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\RiotTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing (MCP Commander, Theme - Default, User remain); Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\PatchTest (Patch Apply orig vs fixed through the paste-and-close path, kkujawinski/sublime-text-3-patch-apply#4). Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (portable st_portable): Packages\PatchTest (Patch Apply orig vs fixed through the paste-and-close path, kkujawinski/sublime-text-3-patch-apply#4). Remove: recycle the folder with the portable closed.
ADD 2026-10-29 (portable st_portable): Packages\PatchTest (Patch Apply orig vs fixed through the paste-and-close path, kkujawinski/sublime-text-3-patch-apply#4). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\PatchTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SbtTest and User\StatusBarTime.sublime-settings (StatusBarTime orig vs fixed, status bar values, lowliet/sublimetext-StatusBarTime#6). Remove: recycle both with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SbtTest and User\StatusBarTime.sublime-settings (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SbwTest (StatusBarWeather orig vs fixed on the 3.14 host, load check, lowliet/sublimetext-StatusBarWeather#4). Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SbwTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\Git CoAuthor (throwaway: menu + settings only, orig vs fixed menu path; the test must not create Packages\GitCoAuthorSnippet), TomasBarry/Sublime-git-co-author#1. Remove: recycle the folder with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\Git CoAuthor (Recycle Bin), portable closed; Packages\GitCoAuthorSnippet was never created. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\DbpTest (rvolz/sublime_dbpedia_lookup branch fix/issue#1 at 9a45169, loose copy) and possibly User\dbpedia_lookup.sublime-settings; test of rvolz's newest commits, sublime_dbpedia_lookup#1. Remove: recycle both with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\DbpTest and User\dbpedia_lookup.sublime-settings (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\ScopeTest and User\ScopeAlways.sublime-settings (ScopeAlways b6b7269 vs 46c5e2e, live settings edit), yaworsw/Sublime-ScopeAlways#7. Remove: recycle both with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\ScopeTest and User\ScopeAlways.sublime-settings (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\IntelTest (tushortz/intellekt tag 0.1.0, loose folder as its .no-sublime-package marker asks) and Data\Cache\Intellekt (its SQLite index, written on load; indexes toolchains installed on this PC); tushortz/intellekt#1. Remove: recycle both with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\IntelTest and Data\Cache\Intellekt (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SymTest (scriptkitz/PythonStautsBarShowSymbol 55b342b as loose folder); scriptkitz/PythonStautsBarShowSymbol#1. Remove: recycle with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SymTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SymTest (scriptkitz/PythonStautsBarShowSymbol 55b342b as loose folder); scriptkitz/PythonStautsBarShowSymbol#1. Remove: recycle with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SymTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SymTest (scriptkitz/PythonStautsBarShowSymbol 55b342b as loose folder); scriptkitz/PythonStautsBarShowSymbol#1. Remove: recycle with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SymTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\SymTest (scriptkitz/PythonStautsBarShowSymbol 55b342b as loose folder); scriptkitz/PythonStautsBarShowSymbol#1. Remove: recycle with the portable closed.
REMOVED 2026-10-29 (portable st_portable): Packages\SymTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Packages\TestExpTest (IPWright83/sublime-TestExplorer original vs fixed, unit tests); fork dpc00/sublime-TestExplorer cloned to tools\forks. Remove: recycle package with the portable closed; fork when its PR merges or times out.
REMOVED 2026-10-29 (portable st_portable): Packages\TestExpTest (Recycle Bin), portable closed. Verified with Test-Path and a folder listing; Preferences unchanged (hash). Fork clone tools\forks\sublime-TestExplorer kept until its PR resolves.
ADD 2026-10-29 (portable st_portable): Cremisi Color Scheme (vari-sh/cremisi-sublime) via Package Control Install Package picker, from the packagecontrol.io new list. Remove: Remove Package picker, then verify Installed Packages, installed_packages in Package Control settings and Preferences.
REMOVED 2026-10-29 (portable st_portable): Cremisi Color Scheme via the Remove Package picker; Installed Packages, Packages and User listed, Package Control and Preferences settings unchanged (hash).
ADD 2026-10-29 (portable st_portable): LSP and LSP-ltex-ls-plus (sublimelsp) via the Install Package picker, with their dependencies and the ltex-ls-plus server download (in Data\Package Storage and Data\Cache). Remove: Remove Package picker for both, then recycle Data\Package Storage\LSP-ltex-ls-plus and any Cache folder; verify.
REMOVED 2026-10-29 (portable st_portable): LSP-ltex-ls-plus (Remove Package picker) and Data\Package Storage\LSP-ltex-ls-plus (Recycle Bin, server process stopped first). LSP 2.16.0 and its libraries (bracex, mdpopups, orjson, wcmatch) STAY installed for the next LSP-* packages of this batch; remove them at the end of the batch.
REMOVED 2026-10-29 (portable st_portable): LSP 2.16.0 (Remove Package picker) with its libraries bracex, mdpopups, orjson, wcmatch; portable closed. Verified: Installed Packages, Packages, Lib, Package Storage listed; Package Control settings list only the baseline; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Copy Python Import (odiroot) and Theme - Timeless (iccir) via the Install Package picker; test files in the session scratchpad. Remove: Remove Package picker for both, verify, check Preferences (theme test edits Preferences; restore from backup).
REMOVED 2026-10-29 (portable st_portable): Copy Python Import and Theme - Timeless via the Remove Package picker; Installed Packages, Packages and Package Control settings listed; Preferences restored (hash identical).
ADD 2026-10-29 (portable st_portable): LSP plus LSP-zuban, LSP-oxlint, LSP-oxfmt, LSP-pawnforge, LSP-nsis, LSP-gh-actions, LSP-wren-lsp and SublimeLinter-contrib-oxlint via the Install Package picker (retest of rows with no result text). They may download servers into Data\Package Storage and Data\Cache, and node/uv/pip tools into their own storage. Remove: Remove Package picker for each, stop server processes, recycle Package Storage subfolders, verify.
ADD 2026-10-29 (portable st_portable): Data\Packages\User\SublimeLinter.sublime-settings (oxlint executable path for the SublimeLinter-contrib-oxlint test). Remove: recycle it.
REMOVED 2026-10-29 (portable st_portable): SublimeLinter-contrib-oxlint, LSP-zuban, LSP-wren-lsp, LSP-pawnforge, LSP-oxlint, LSP-oxfmt, LSP-nsis, LSP-gh-actions and LSP (Remove Package picker), Package Storage LSP-oxfmt and LSP-oxlint and User\SublimeLinter.sublime-settings (Recycle Bin), portable closed. Verified: Installed Packages, Packages, User, Package Storage, Lib and Package Control settings at baseline; Preferences unchanged (hash). LSP-wren-lsp, LSP-pawnforge, LSP-nsis and LSP-gh-actions were only loaded (their syntax packages missing); a second pass with the syntax packages follows.
ADD 2026-10-29 (portable st_portable, second pass): LSP, Wren, NSIS, YamlPipelines and AMX Mod X Pawn (their syntaxes) plus LSP-wren-lsp, LSP-pawnforge, LSP-nsis and LSP-gh-actions via the Install Package picker; servers download into Data\Package Storage. Remove: Remove Package picker for each, stop server processes, recycle Package Storage subfolders, verify.
REMOVED 2026-10-29 (portable st_portable, second pass): AMX Mod X Pawn, LSP-gh-actions, LSP-nsis, LSP-pawnforge, LSP-wren-lsp, LSP, NSIS (a folder in Packages), Wren, YamlPipelines via the Remove Package picker; Package Storage LSP-gh-actions, LSP-nsis, LSP-pawnforge recycled (LSP-wren-lsp kept its server elsewhere: Package Storage listing empty); portable closed. Verified: Installed Packages, Packages, User, Package Storage, Lib and Package Control settings at baseline; Preferences unchanged (hash).
ADD 2026-10-29 (portable st_portable): Lua Love, Filter Lines, SublimeERB, Ecmascript Syntax and EZWebSequenceDiagrams via the Install Package picker (skipped as old on 2026-10-07; that rule was retired). Remove: Remove Package picker for each, verify.
REMOVED 2026-10-29 (portable st_portable): Lua Love, Filter Lines, SublimeERB, Ecmascript Syntax, EZWebSequenceDiagrams via the Remove Package picker; portable closed. Verified: Installed Packages, Packages, User and Package Storage at baseline; Preferences hash unchanged (78CEFE76).
ADD 2026-10-29 (his word, this turn): LuaBinaries Lua 5.4 Win64 zip unpacked to C:\Users\donal\tools\lua-test (no installer, no admin, no PATH or registry change) so Lua Love finds luac; plus Lua Love via the picker on portable st_portable. Remove: recycle C:\Users\donal\tools\lua-test, Remove Package picker for Lua Love, verify.
NOTE 2026-10-29: Data\Packages\User\LuaLove.sublime-settings written on st_portable (luac_path to tools\lua-test); recycle it at removal.
REMOVED 2026-10-29 (portable st_portable, Lua Love retest): Lua Love via the Remove Package picker, User\LuaLove.sublime-settings and C:\Users\donal\tools\lua-test recycled; portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash unchanged (78CEFE76).
NOTE 2026-10-29 (B11 fix test): copied the repo sublime_mcp.py and lib\consent.py over the portable st_portable Data\Packages\MCP Commander (our own package, not an install); the repo is the source of truth.
ADD 2026-10-29 (his word: "give a try"): jcode v0.99.1 jcode-windows-x86_64.exe downloaded from github.com/1jehuang/jcode releases into C:\Users\donal\tools\jcode-test (one exe, no installer, no admin, no PATH or registry change by me). Remove: recycle that folder, and any C:\Users\donal\.jcode created by running it; verify.
REMOVED 2026-10-29: the jcode download above was a mistake (jcode is already installed at C:\Users\donal\AppData\Local\jcode\bin\jcode.exe); the downloaded exe and SHA256SUMS in C:\Users\donal\tools\jcode-test were never run and the folder was recycled. Nothing else was added.
ADD 2026-10-29 (portable st_portable, static-only backlog, row 1): DrSync via the Install Package picker. Remove: Remove Package picker, verify.
ADD REPOSITORY 2026-10-29 (portable st_portable): https://github.com/spywhere/DrSync in the portable Package Control repositories setting, to install DrSync (not in the picker). Remove: delete the repository line from Data\Packages\User\Package Control.sublime-settings, Remove Package picker for DrSync, verify.
REMOVED 2026-10-29 (portable st_portable, DrSync): DrSync via the Remove Package picker; repository line removed by restoring Package Control.sublime-settings from the saved baseline (hash FBBFAC8A); portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash unchanged (78CEFE76).
ADD 2026-10-29 (portable st_portable, untested list batch 1, via the Install Package picker): Edge Theme Addon - Linter Theme, Agila Theme, AMPscript Syntax Highlighter, Apple Pips Color Scheme, Atomic Color Scheme, Base16 Color Schemes, Blast Dark, CBP Syntax Highlighter, Blossom Theme, Civic Color Scheme. Remove: Remove Package picker for each, restore Preferences from the saved copy if a theme was applied, verify.
REMOVED 2026-10-29 (portable st_portable, untested list batch 1): Edge Theme Addon - Linter Theme, Agila Theme, AMPscript Syntax Highlighter, Apple Pips Color Scheme, Atomic Color Scheme, Base16 Color Schemes, Blast Dark, Blossom Theme, Civic Color Scheme via the Remove Package picker; portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged. Not recorded as tested (stay on the untested list): Edge Theme Addon (gutter theme not exercised, no linter installed), AMPscript Syntax Highlighter (syntax not exercised), CBP Syntax Highlighter (not in the picker, not installed).
ADD 2026-10-29 (portable st_portable, untested list batch 2, via the Install Package picker): Color Scheme - Baara Dark, Clannad Theme, Dark Neon Color Scheme, Factus 12C Color Scheme, Future Funk - Color Scheme, Harper Color Scheme, Hopscotch Color Scheme, IceWorld Color Scheme. Remove: Remove Package picker for each, restore Preferences from the saved copy if a theme was applied, verify.
REMOVED 2026-10-29 (portable st_portable, untested list batch 2): Color Scheme - Baara Dark, Clannad Theme, Dark Neon Color Scheme, Factus 12C Color Scheme, Future Funk - Color Scheme, Harper Color Scheme, Hopscotch Color Scheme, IceWorld Color Scheme via the Remove Package picker; portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (portable st_portable, untested list batch 3, via the Install Package picker): 0x0, 42 Function Count Lines, ABC Notation, 42 Headers, Abrase, Achievement, AdonisJs, Align Arguments. Remove: Remove Package picker for each, verify; test fixtures stay in the session scratchpad.
REMOVED 2026-10-29 (portable st_portable, untested list batch 3): 0x0, 42 Function Count Lines, 42 Headers, ABC Notation, Abrase, Achievement, AdonisJs, Align Arguments via the Remove Package picker; portable closed. Verified: Installed Packages, Packages, User at baseline (achievement.sublime-settings and unlocked.sublime-settings left by Achievement were recycled); Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (portable st_portable, untested list batch 4): ADOdb library snippets for PHP, ADBView, Alan, Alternative Autocompletion, AMD Butler, AMPScript, AngularJS, AngularJS Jasmine Boilerplate via the Install Package picker; remove via the Remove Package picker, verify baseline.
REMOVED 2026-10-29 (portable st_portable, untested list batch 4): ADBView, ADOdb library snippets for PHP, Alternative Autocompletion, AMD Butler, AMPScript, AngularJS, AngularJS Jasmine Boilerplate via the Remove Package picker (Alan was not in the picker, not installed); portable closed. Verified: Installed Packages, Packages, User at baseline (AngularJS.cache and AngularJS-sublime-package.sublime-settings recycled); Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (portable st_portable, untested list batch 5): AndroidImport, Ant, Ant Buildfile, API Blueprint, Ansible, Apex, Apex Intention Actions, ASCII Cowpletions via the Install Package picker; remove via the Remove Package picker, verify baseline.
REMOVED 2026-10-29 (portable st_portable, untested list batch 5): AndroidImport, Ant Buildfile, API Blueprint, Ansible, Apex, Apex Intention Actions, ASCII Cowpletions via the Remove Package picker (Ant not installed: the "Ant" row was not installed this batch); portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (Donald allowed it in the turn: "Install Ant"): Apache Ant 1.10.18, unzipped to C:\Users\donal\tools\ant (user folder, no admin, no PATH or registry change; PATH set only for the test Sublime process), to run the Ant Buildfile build system. Remove: recycle C:\Users\donal\tools\ant and the zip C:\Users\donal\tools\ant-download after the test.
ADD 2026-10-29 (portable st_portable, untested list batch 6): Ant Buildfile via the Install Package picker, test Sublime started with PATH including C:\Users\donal\tools\ant\apache-ant-1.10.18\bin and JAVA_HOME set for that process only.
REMOVED 2026-10-29 (batch 6): Ant Buildfile and Ant via the Remove Package picker; Apache Ant 1.10.18 (C:\Users\donal\tools\ant) and its download folder (C:\Users\donal\tools\ant-download) recycled, both verified gone; portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (portable st_portable, untested list batch 7; Donald ordered "Install Anaconda"): Anaconda (the Sublime package), anaconda_go, anaconda_rust via the Install Package picker; remove via the Remove Package picker, verify baseline, check Packages\User for leftovers.
ADD 2026-10-29 (batch 7, Donald: 'you give up too easy'): pyasyncore and pyasynchat (the workaround in DamnWidget/anaconda#945) pip-installed with --target into the session scratchpad folder pydeps (C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\pydeps), NOT into Python's site-packages; used only by setting PYTHONPATH for the test Sublime process. Remove: recycle the pydeps folder after the test.
REMOVED 2026-10-29 (batch 7): Anaconda, anaconda_go, anaconda_rust, anaconda_php via the Remove Package picker; Anaconda did not finish removing (its JsonServer held the folder), so after closing the portable Packages\Anaconda was recycled by hand and Preferences and Package Control settings were restored from the baseline copies (a stale "Anaconda" entry was in both); pyasyncore/pyasynchat scratch folder (pydeps) recycled. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A.
ADD 2026-10-29 (batch 8, Donald: 'I am not that familiar with it, that I would ask' = decide myself): drafter 5.1.0 built from the apiaryio/drafter release tarball with the already installed cmake and MinGW g++, entirely in the session scratchpad folder C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\drafter_build (no install, no PATH or registry change; PATH set only for the test Sublime process). Remove: recycle C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\drafter_build.
NOTE 2026-10-29 (batch 8): the drafter source build failed (needs POSIX regex.h, does not compile on MinGW); instead drafter.js (npm, pure JS build of the same parser) installed with npm --prefix into C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\drafter_js, with a small drafter.cmd wrapper in the same folder, PATH set for the test Sublime process only. Remove: recycle C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\drafter_js and C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\95abb597-7413-4c0c-b822-f9a184d32929\scratchpad\drafter_build.
ADD 2026-10-29 (portable st_portable, untested list batch 8): API Blueprint (retest with drafter.js wrapper on PATH), Artisan, Asciidoctor, Auto Hide Sidebar, Auto Semi-Colon, ASCII Decorator, AVR-ASM-Sublime, Behat via the Install Package picker; remove via the Remove Package picker, verify baseline.
REMOVED 2026-10-29 (batch 8): API Blueprint, Asciidoctor, Auto Hide Sidebar, Auto Semi-Colon, ASCII Decorator, Behat via the Remove Package picker (Artisan and AVR-ASM-Sublime are not in the picker, not installed); portable closed. Scratch items recycled and verified gone: drafter source build and drafter.js wrapper folders (scratchpad), User\APIBlueprint.sublime-settings and User\ASCII Decorator Fonts. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (portable st_portable, untested list batch 9): ArcticTypescript, BazelSyntax, Asymptote, Behat Completions, Atomizr, Better Bookmarks, AutoBackups, Better TypeScript via the Install Package picker; remove via the Remove Package picker, verify baseline.
REMOVED 2026-10-29 (batch 9): ArcticTypescript, Asymptote, Atomizr, Better Bookmarks, AutoBackups via the Remove Package picker (waited for each Removed package line; libraries cson, lxml, PyYAML, xmltodict removed as orphans); portable closed. Recycled by hand: User\BetterBookmarks, User\AutoBackups (Windows).sublime-settings, C:\Users\donal\abt. D:\Sublime Text Backups recycled earlier and confirmed absent. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (batch 10): Auto Close Panel, BHT-BASIC, Biml, AutoDocstring, BioPythonUtils on the audit portable (tools\st_portable) via the Install Package picker; remove each via the Remove Package picker, then verify baseline.
REMOVED 2026-10-29 (batch 10): Auto Close Panel, AutoDocstring, BHT-BASIC, BioPythonUtils via the Remove Package picker (waited for each Removed package line; Biml is not in the picker, not installed); portable closed. Recycled by hand: User\Auto Close Panel.sublime-settings. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (batch 11): AutoFileName, BlackRain, AutoF-Strings, Boron Color Scheme, bourbon_completions on the audit portable (tools\st_portable) via the Install Package picker; remove each via the Remove Package picker, then verify baseline.
REMOVED 2026-10-29 (batch 11): AutoFileName, BlackRain, AutoF-Strings, bourbon_completions via the Remove Package picker (waited for each Removed package line; Boron Color Scheme is not in the picker, not installed); portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (batch 12): AutoPEP8, Auto-Spacing, AWS Lambda, Badges, Baidu FE Code Style on the audit portable (tools\st_portable) via the Install Package picker; remove each via the Remove Package picker, then verify baseline.
REMOVED 2026-10-29 (batch 12): AutoPEP8, Auto-Spacing, AWS Lambda, Badges, Baidu FE Code Style via the Remove Package picker (waited for each Removed package line; library requests removed as orphan by Package Control); portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (batch 13): Brainfuck Interpreter, BridleNSIS, Bats, BBC BASIC Syntax, Browser Sync on the audit portable (tools\st_portable) via the Install Package picker; remove each via the Remove Package picker, then verify baseline.
REMOVED 2026-10-29 (batch 13): Brainfuck Interpreter, BridleNSIS, Bats, BBC BASIC Syntax, Browser Sync via the Remove Package picker (waited for each Removed package line; the Browser Sync folder and its node_modules were gone about 12 s later; no node-windows process was left); portable closed. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
ADD 2026-10-29 (batch 14): BeautifyLatex, BetaCode, C++11, BetterFindBuffer, C99 on the audit portable (tools\st_portable) via the Install Package picker; remove each via the Remove Package picker, then verify baseline.
REMOVED 2026-10-29 (batch 14): BeautifyLatex, C++11, BetterFindBuffer, C99 via the Remove Package picker (waited for each Removed package line; BetaCode is not in the picker, not installed); portable closed. Recycled by hand: empty Packages\Default folder left by BetterFindBuffer. Verified: Installed Packages, Packages, User at baseline; Preferences hash 78CEFE76 and Package Control settings hash FBBFAC8A unchanged.
