# Package lists

These are the lists used from 2026-10-07 on, when the audit moved from a ranked queue to short, purpose-built lists. The earlier queue (September, by install count) is not published here; its results are in `../RESULTS.tsv`.

Each file is tab-separated with a header row (one file has none and is not included). Columns vary a little by file: `installs` / `installs_rank` is the package's place or count on Package Control, `last_push` / `pushed_days_ago` the date of the last push to its repository, `python_kb` the amount of Python it ships, `stars` the repository's stars.

| file | what it holds |
|---|---|
| `audit_list_2026_10_07.tsv` | the first short list of 2026-10-07, by tier |
| `audit_list_2026_10_07_eased4y.tsv` | packages in the top 1000 by installs whose last push is within four years |
| `audit_list_2026_10_07_nopython.tsv` | packages with little or no Python (themes, syntaxes, snippets, schemes) |
| `audit_list_2026_10_08_weakrecords.tsv` | popular, maintained packages whose only record was an incidental install |
| `audit_list_2026_10_09_rebuilt.tsv` | the list rebuilt on 2026-10-09 from repository activity (commits, issues) |
| `audit_list_2026_10_10_top1500.tsv` | next band of the install ranking, up to about rank 1550 |
| `audit_list_2026_10_11_top2000.tsv`, `..._top2500.tsv`, `..._top3100.tsv`, `..._top3650.tsv` | further bands of the install ranking |
| `audit_list_2026_10_11_age3y.tsv`, `..._py1k.tsv`, `..._pyany.tsv` | cuts by age of last push and amount of Python |
| `audit_list_2026_10_11_ai.tsv` | AI-oriented packages (agents, completion, chat) |
| `audit_list_2026_10_11_tail.tsv` | the last 77 rows at the loose end of the ranking, finished on 2026-10-12 |
| `audit_list_2026_10_16_age4_6y.tsv` | packages whose last push was 4 to 6 years ago, not tested before, installable on build 4200 (257 rows) |
