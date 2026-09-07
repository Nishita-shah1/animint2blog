# Nishita Shah: GSoC 2026 Animint2 journal

Public engineering journal for my [Google Summer of Code 2026](https://summerofcode.withgoogle.com/) work on [animint2](https://github.com/animint/animint2).

Weekly entries are written from the updates in [animint2#322](https://github.com/animint/animint2/issues/322).

## Local preview

```bash
python build.py
python -m http.server 4173
```

Then open http://127.0.0.1:4173/

## Deploy on Netlify

1. Push this folder to a GitHub repository.
2. In Netlify, create a new site from that repo.
3. Build command: `python build.py`
4. Publish directory: `.`

## Pages

| Page | What it is |
| --- | --- |
| `index.html` | Welcome, week cards, contribution snapshot |
| `journal/` | Community bonding, weeks 1–12, final submission, end term |
| `progress.html` | Timeline of the same entries |
| `about.html` | Profile, mentors, technologies |
| `contact.html` | GitHub and project links |

`build.py` regenerates the HTML from the journal source in that file. Edit `build.py` when you add a new week, then run it again.
