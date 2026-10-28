"""Find commands referenced by a package's palette/menu/keymap resources that no class of that package defines."""
import ast
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
REPOS = os.path.join(BASE, 'repos')
served = set(json.load(open(os.path.join(BASE, 'served_idx.json'))))
Q = json.load(open(r'C:\Users\donal\AppData\Local\Temp\claude\C--Users-donal-projects-sublime-mcp\165e315a-efcb-49b3-8b31-7320fbdb0c43\scratchpad\campaign\queue.json'))
known = set(json.load(open(os.path.join(BASE, 'st_known_commands.json'))))
CORE = set('''show_panel hide_panel toggle_comment open_file exec insert insert_snippet move move_to set_setting toggle_setting
run_macro_file next_view prev_view close close_file new_file save save_all undo redo copy cut paste select_all
left_delete right_delete find_all find_under find_next prev_result next_result build show_overlay toggle_side_bar
open_url reindent indent unindent swap_line_up swap_line_down duplicate_line delete_line join_lines sort_lines
upper_case lower_case title_case toggle_bookmark next_bookmark prev_bookmark clear_bookmarks select_all_bookmarks
toggle_record_macro run_macro fold unfold unfold_all fold_all scroll_lines goto_line goto_symbol context_menu
prompt_open_file prompt_save_as prompt_select_project open_dir open_recent_file new_window close_window exit
reveal_in_side_bar toggle_full_screen toggle_distraction_free set_layout focus_group move_to_group
transpose set_mark select_to_mark swap_with_mark delete_to_mark yank clear_fields insert_best_completion
auto_complete hide_auto_complete replace_completion_with_auto_complete commit_completion expand_selection
single_selection select_lines split_selection_into_lines slurp_find_string slurp_replace_string
wrap_lines decrease_font_size increase_font_size reset_font_size pane_toggle_menu
paste_and_indent reveal_in_side_bar open_terminal_in_project
'''.split())


def cmd_name(cn):
    name = cn[0].lower()
    last = False
    for ch in cn[1:]:
        if ch.isupper() and not last:
            name += '_' + ch.lower()
        else:
            name += ch
        last = ch.isupper()
    if name.endswith('_command'):
        name = name[:-8]
    return name


def strip_json(t):
    t = re.sub(r'/\*.*?\*/', '', t, flags=re.S)
    t = re.sub(r'(?m)^\s*//.*$', '', t)
    t = re.sub(r'(?m)(?<=[,\[{\s"\d])//[^"\n]*$', '', t) if False else t
    t = re.sub(r',(\s*[\]}])', r'\1', t)
    return t


def walk(x, out):
    if isinstance(x, dict):
        c = x.get('command')
        if isinstance(c, str):
            out.add(c)
        for v in x.values():
            walk(v, out)
    elif isinstance(x, list):
        for v in x:
            walk(v, out)


SKIP = ('/tests/', '/test/', '/node_modules/', '/docs/', '/examples/', '/demo/', '/.github/')
report = []
for d in sorted(os.listdir(REPOS)):
    idx = int(d[:4])
    if idx not in served:
        continue
    root = os.path.join(REPOS, d)
    defined = set()
    dynamic = False
    refs = {}
    for dp, dn, fn in os.walk(root):
        if os.sep + '.git' in dp:
            continue
        rel = dp[len(root):].replace(os.sep, '/') + '/'
        if any(s in rel.lower() for s in SKIP):
            continue
        for f in fn:
            p = os.path.join(dp, f)
            if f.endswith('.py'):
                try:
                    tree = ast.parse(open(p, encoding='utf8', errors='replace').read())
                except Exception:
                    continue
                for n in ast.walk(tree):
                    if isinstance(n, ast.ClassDef):
                        bases = [ast.unparse(b) if hasattr(ast, 'unparse') else '' for b in n.bases]
                        if any('Command' in b for b in bases) or n.name.endswith('Command'):
                            defined.add(cmd_name(n.name))
                            for b in n.body:
                                if isinstance(b, ast.FunctionDef) and b.name == 'name':
                                    for r in ast.walk(b):
                                        if isinstance(r, ast.Return) and isinstance(r.value, ast.Constant) and isinstance(r.value.value, str):
                                            defined.add(r.value.value)
                                        elif isinstance(r, ast.Return):
                                            dynamic = True
            elif f.endswith(('.sublime-commands', '.sublime-menu', '.sublime-keymap', '.sublime-macro', '.sublime-mousemap')):
                try:
                    data = json.loads(strip_json(open(p, encoding='utf-8-sig', errors='replace').read()))
                except Exception:
                    continue
                s = set()
                walk(data, s)
                for c in s:
                    refs.setdefault(c, set()).add(os.path.relpath(p, root).replace(os.sep, '/'))
    if dynamic:
        continue
    missing = {c: sorted(v)[:2] for c, v in refs.items() if c not in defined and c not in known and c not in CORE}
    if missing:
        report.append((idx, Q[idx]['name'], missing))

json.dump(report, open(os.path.join(BASE, 'cmd_missing.json'), 'w'))
print(len(report), 'packages reference commands they do not define')
for idx, name, m in report[:120]:
    print(idx, name, '|', dict(list(m.items())[:4]))
