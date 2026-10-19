#!/usr/bin/env python3
"""Refresh the "Started / Updated" month on each project from real git history.

Usage:  python3 scripts/update_project_dates.py [--check]
  --check   print what would change and exit 1 if anything is stale (no write)

For each project it takes the first and last commit author date across the listed repos
(via the `gh` CLI, so private repos work when you're logged in). Projects with no
verifiable history (the internal AI Suite) are left without dates on purpose. Scholairly's
history comes from a local clone because the repo isn't under this GitHub account.
"""
import re, subprocess, sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / 'index.html'
# project target -> GitHub repos (owner/name). Dates span all of them.
REPOS = {
    'sp': ['moff05/stacking_plan', 'moff05/stacking-planner'],
    'bc': ['moff05/8bit-cre'],
    'pt': ['moff05/stockstarter'],
    'cd': ['moff05/career-dashboard'],
    'hs': ['moff05/hackysack-cv'],
    'sg': ['moff05/signal'],
    'wck': ['moff05/world-cup-kits'],
    'cim': ['moff05/cim423-unity-project', 'moff05/cim423-3d-world'],
}
LOCAL = {'sc': Path.home() / 'Desktop/Claude Projects/ScholAIrly/Scholairly'}
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fmt = lambda ym: f'{MON[int(ym[5:]) - 1]} {ym[:4]}'


def gh_commit_months(repo):
    last = subprocess.run(['gh', 'api', f'repos/{repo}/commits?per_page=1', '-i'], capture_output=True, text=True, check=True).stdout
    m = re.search(r'rel="last"', last) and re.search(r'[?&]page=(\d+)>; rel="last"', last)
    pages = int(m.group(1)) if m else 1
    get = lambda page: subprocess.run(['gh', 'api', f'repos/{repo}/commits?per_page=1&page={page}', '--jq', '.[0].commit.author.date[0:7]'],
                                      capture_output=True, text=True, check=True).stdout.strip()
    return get(pages), get(1)


def local_commit_months(path):
    dates = subprocess.run(['git', '-C', str(path), 'log', '--format=%ad', '--date=format:%Y-%m'], capture_output=True, text=True, check=True).stdout.split()
    return min(dates), max(dates)


def main():
    check = '--check' in sys.argv
    html = SITE.read_text()
    changes = []
    spans = {t: [gh_commit_months(r) for r in repos] for t, repos in REPOS.items()}
    spans.update({t: [local_commit_months(p)] for t, p in LOCAL.items()})
    for target, pairs in spans.items():
        started, updated = min(p[0] for p in pairs), max(p[1] for p in pairs)
        pat = re.compile(r'(data-target="%s" )data-started="[^"]*" data-updated="[^"]*"' % target)
        assert pat.search(html), f'nav item for {target} not found'
        new = pat.sub(rf'\1data-started="{started}" data-updated="{updated}"', html)
        new = re.sub(r'(<div class="proj-nav-item[^"]*" data-target="%s"[^>]*>(?:(?!proj-nav-item).)*?<div class="proj-nav-dates">)[^<]*(</div>)' % target, rf'\1Updated {fmt(updated)}\2', new, count=1, flags=re.S)
        new = re.sub(r'(data-dates-for="%s">)[^<]*(</p>)' % target, rf'\1Started {fmt(started)} · Updated {fmt(updated)}\2', new)
        if new != html:
            changes.append(f'{target}: Started {fmt(started)} · Updated {fmt(updated)}')
        html = new
    print('\n'.join(changes) if changes else 'dates already up to date')
    if check and changes:
        sys.exit(1)
    if not check:
        SITE.write_text(html)


main()
