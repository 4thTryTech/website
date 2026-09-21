# website

4th Try Tech primary website. Static HTML, built by a small Python script and served by GitHub Pages from `docs/`.

## Layout

| Path | What it is |
| --- | --- |
| `content.py` | All page copy: site name and URL, Home, Story, Contact, and the project and lab-note entries. Edit this to change words |
| `src/site.css`, `src/site.js` | Styles, and the script for the light and dark toggle and the phone menu |
| `static/` | Our own images, such as `og.png`, the link-preview picture |
| `build.py` | Builds everything into `docs/` |
| `docs/` | The built site. Do not edit by hand; it is replaced on every build |

Brand files (color tokens, fonts, icons, lockups, animated heroes) are not kept here. `build.py` copies them from a checkout of the `brand` repo, so that repo stays the single source of truth.

## Build

```
python3 build.py            # expects the brand repo next to this one, at ../brand
python3 build.py /path/to/brand
```

Plain Python 3, no packages to install. To preview, run `python3 -m http.server` inside `docs/` and open http://localhost:8000.

## Publish

GitHub Pages: Settings, Pages, deploy from branch `main`, folder `/docs`. All links are relative, so the site works at `https://4thtrytech.github.io/website/` and at a custom domain. When the domain is ready, set `url` and `domain` in `content.py` and rebuild; that writes the `CNAME` file.

## Rules of the house

- The site opens in light mode. Visitors can switch to dark with the button in the header, and their choice is remembered.
- Entries flagged `sample: True` in `content.py` are invented placeholders and show a "Sample" tag. Replace them with real write-ups and remove the flag.
- Placeholder notes (dashed boxes) mark things still to decide: the contact channel and the final bio wording.
- Copy follows the brand voice in the `brand` repo: candid, practical, wry; the journey is the subject.
