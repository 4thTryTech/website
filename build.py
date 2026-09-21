#!/usr/bin/env python3
"""Builds the 4th Try Tech site into docs/ (GitHub Pages serves that folder).

usage: python3 build.py [path to a checkout of the brand repo, default ../brand]

Plain Python 3, no dependencies. Brand files (tokens, fonts, icons, lockups, animated heroes) are copied from the
brand repo at build time, so the brand repo stays the single source of truth. Page copy lives in content.py,
styles in src/site.css, behavior in src/site.js. All links are relative, so the site works at a project URL
(user.github.io/website/) and at a custom domain alike.
"""
import html, os, shutil, sys
from content import PAGES, PROJECTS, NOTES, SITE

BRAND = sys.argv[1] if len(sys.argv) > 1 else "../brand"
OUT = "docs"
HERE = os.path.dirname(os.path.abspath(__file__))

COPY = {  # brand repo path -> site path
    "tokens/colors.css": "assets/brand/colors.css",
    "fonts/web": "assets/fonts",
    "animation/splash-animated-light.svg": "assets/brand/splash-animated-light.svg", "animation/splash-animated-dark.svg": "assets/brand/splash-animated-dark.svg",
    "animation/hero-tablet-animated-light.svg": "assets/brand/hero-tablet-animated-light.svg", "animation/hero-tablet-animated-dark.svg": "assets/brand/hero-tablet-animated-dark.svg",
    "animation/hero-desktop-animated-light.svg": "assets/brand/hero-desktop-animated-light.svg", "animation/hero-desktop-animated-dark.svg": "assets/brand/hero-desktop-animated-dark.svg",
    "logo/lockup-horizontal-small-light.svg": "assets/brand/lockup-light.svg", "logo/lockup-horizontal-mono-reversed.svg": "assets/brand/lockup-dark.svg",
    "logo/lockup-stacked-light.svg": "assets/brand/lockup-stacked-light.svg", "logo/lockup-stacked-dark.svg": "assets/brand/lockup-stacked-dark.svg",
    "elements/rocket-light.svg": "assets/brand/rocket-light.svg", "elements/rocket-dark.svg": "assets/brand/rocket-dark.svg",
    "icons/favicon.ico": "favicon.ico", "icons/favicon.svg": "favicon.svg", "icons/apple-touch-icon.png": "apple-touch-icon.png",
    "icons/icon-192.png": "icon-192.png", "icons/icon-512.png": "icon-512.png", "icons/icon-maskable-512.png": "icon-maskable-512.png",
    "icons/site.webmanifest": "site.webmanifest",
}
e = html.escape


def pair(root, name, cls="", alt=""):
    """Light and dark versions of one brand image; CSS shows the one that matches the theme."""
    return (f'<img class="{cls} t-light" src="{root}assets/brand/{name}-light.svg" alt="{e(alt)}">'
            f'<img class="{cls} t-dark" src="{root}assets/brand/{name}-dark.svg" alt="{e(alt)}">')


def layout(path, title, description, body, body_class=""):
    depth = 0 if path == "" else path.strip("/").count("/") + 1
    root = "../" * depth
    nav = "".join(f'<a href="{root}{href}"{" aria-current=page" if path.startswith(href) and href else ""}>{label}</a>'
                  for label, href in (("Projects", "projects/"), ("Lab notes", "notes/"), ("Story", "story/"), ("Contact", "contact/")))
    full = f"{title} · {SITE['name']}" if title else SITE["name"]
    url = SITE["url"] + path
    return f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(full)}</title>
<meta name="description" content="{e(description)}">
<script>try{{if(localStorage.getItem("theme")==="dark")document.documentElement.dataset.theme="dark"}}catch(e){{}}</script>
<link rel="stylesheet" href="{root}assets/fonts/fonts.css">
<link rel="stylesheet" href="{root}assets/brand/colors.css">
<link rel="stylesheet" href="{root}assets/site.css">
<link rel="icon" href="{root}favicon.ico" sizes="48x48">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<meta name="theme-color" content="#46607A">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE['name'])}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{e(url)}">
<meta property="og:image" content="{e(SITE['url'])}assets/og.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
<a class="logo" href="{root or './'}" aria-label="4th Try Tech, home">{pair(root, "lockup")}</a>
<nav class="main" id="nav" aria-label="Main">{nav}</nav>
<div class="tools">
<button class="theme" id="theme" type="button" aria-pressed="false" aria-label="Dark mode"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="t-light" fill="currentColor" d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/><g class="t-dark" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2" fill="currentColor"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/></g></svg><span class="t-light">Dark</span><span class="t-dark">Light</span></button>
<button class="menu" id="menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
</div></div></header>
<main id="main">
{body}
</main>
<footer class="site"><div class="band" aria-hidden="true"></div><div class="wrap">
<span class="tag">{e(SITE['tagline'])}</span>
<nav aria-label="Footer">{nav}<a href="https://michaellehman.me/">About Michael</a></nav>
</div></footer>
<script src="{root}assets/site.js"></script>
</body>
</html>
"""


def pill(n, ok):
    return f'<span class="pill{" ok" if ok else ""}" title="Try {n}{", the one that held" if ok else ""}">{n}</span>'


def card(root, kind, item):
    folder = "projects" if kind == "Project" else "notes"
    sample = '<span class="sample">Sample</span>' if item.get("sample") else ""
    badge = pill(item["try"], item.get("held", False)) if "try" in item else ""
    return (f'<a class="card" href="{root}{folder}/{item["slug"]}/"><div class="meta">{badge}<span>{kind}</span><span>{item["date"]}</span>{sample}</div>'
            f'<h3>{e(item["title"])}</h3><p>{e(item["summary"])}</p></a>')


def prose(blocks):
    out = []
    for b in blocks:
        if isinstance(b, tuple) and b[0] == "h2":
            out.append(f"<h2>{e(b[1])}</h2>")
        elif isinstance(b, tuple) and b[0] == "try":
            _, n, held, heading, text = b
            out.append(f'<div class="try"><div class="try-h">{pill(n, held)}<h2>{e(heading)}</h2></div><p>{e(text)}</p></div>')
        elif isinstance(b, tuple) and b[0] == "link":
            out.append(f'<p>{e(b[1])}<a href="{e(b[3])}">{e(b[2])}</a>.</p>')
        elif isinstance(b, tuple) and b[0] == "note":
            out.append(f'<p class="placeholder">{e(b[1])}</p>')
        else:
            out.append(f"<p>{e(b)}</p>")
    return "\n".join(out)


def page_home():
    latest = sorted([("Project", p) for p in PROJECTS] + [("Lab note", n) for n in NOTES], key=lambda x: x[1]["date"], reverse=True)[:3]
    steps = "".join(f'<li>{pill(i + 1, i == 3)}<div><h3>{e(h)}</h3><p>{e(t)}</p></div></li>' for i, (h, t) in enumerate(PAGES["home"]["steps"]))
    body = f"""<div class="hero" role="img" aria-label="4th Try Tech. {e(SITE['tagline'])} A rocket with a 4 on its hull lifts off in front of a sun.">
{pair("", "splash-animated", "phone")}{pair("", "hero-tablet-animated", "tab")}{pair("", "hero-desktop-animated", "desk")}</div>
<div class="wrap lead"><p>{e(SITE['description'])}</p>
<div class="btns"><a class="btn" href="notes/">Read the latest</a><a class="more" href="story/">How this started</a></div></div>
<section class="block"><div class="wrap two"><h2>What this is</h2><div class="text">{prose(PAGES['home']['what'])}</div></div></section>
<section class="block"><div class="wrap"><h2>How a project reads here</h2><ol class="tries">{steps}</ol></div></section>
<section class="block"><div class="wrap"><h2>Latest from the lab</h2><div class="cards">{"".join(card("", k, i) for k, i in latest)}</div>
<div class="links"><a href="projects/">All projects</a><a href="notes/">All lab notes</a></div></div></section>"""
    return layout("", "", SITE["description"], body, "home")


def page_simple(path, key):
    p = PAGES[key]
    body = f'<div class="wrap page"><h1>{e(p["title"])}</h1><div class="text">{prose(p["body"])}</div></div>'
    return layout(path, p["title"], p["description"], body)


def page_index(path, title, description, intro, kind, items):
    cards = "".join(card("../", kind, i) for i in sorted(items, key=lambda i: i["date"], reverse=True))
    body = f'<div class="wrap page"><h1>{e(title)}</h1><div class="text"><p>{e(intro)}</p></div><div class="cards">{cards}</div></div>'
    return layout(path, title, description, body)


def page_entry(folder, kind, item):
    sample = '<p class="placeholder">This is a sample entry. It shows the layout and is not a real write-up.</p>' if item.get("sample") else ""
    badge = pill(item["try"], item.get("held", False)) if "try" in item else ""
    body = (f'<article class="wrap page"><div class="meta">{badge}<span>{kind}</span><span>{item["date"]}</span></div>'
            f'<h1>{e(item["title"])}</h1>{sample}<div class="text">{prose(item["body"])}</div>'
            f'<p class="back"><a href="../">All {"projects" if kind == "Project" else "lab notes"}</a></p></article>')
    return layout(f"{folder}/{item['slug']}/", item["title"], item["summary"], body)


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    os.chdir(HERE)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT, ignore_errors=True)   # some environments cannot delete; files are then overwritten in place
    for src, dst in COPY.items():
        s, d = os.path.join(BRAND, src), os.path.join(OUT, dst)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copytree(s, d, dirs_exist_ok=True) if os.path.isdir(s) else shutil.copyfile(s, d)
    for folder in ("src", "static"):                       # our own styles, script and images
        for name in os.listdir(folder):
            shutil.copyfile(os.path.join(folder, name), os.path.join(OUT, "assets", name))
    write(".nojekyll", "")
    if SITE.get("domain"):
        write("CNAME", SITE["domain"] + "\n")
    write("index.html", page_home())
    write("story/index.html", page_simple("story/", "story"))
    write("contact/index.html", page_simple("contact/", "contact"))
    write("projects/index.html", page_index("projects/", "Projects", "Projects, each shown with the route it actually took.", PAGES["projects_intro"], "Project", PROJECTS))
    write("notes/index.html", page_index("notes/", "Lab notes", "Shorter, dated entries written while the work happens.", PAGES["notes_intro"], "Lab note", NOTES))
    for p in PROJECTS:
        write(f"projects/{p['slug']}/index.html", page_entry("projects", "Project", p))
    for n in NOTES:
        write(f"notes/{n['slug']}/index.html", page_entry("notes", "Lab note", n))
    nf = layout("", "Page not found", "That page is not here.", '<div class="wrap page"><h1>That try did not take</h1><div class="text"><p>The page you were after is not here. Head back to the start and try again.</p><p><a class="btn" href="' + SITE['url'] + '">Back to the home page</a></p></div></div>')
    write("404.html", nf)
    n = sum(len(f) for _, _, f in os.walk(OUT))
    print(f"built {n} files into {OUT}/")


if __name__ == "__main__":
    main()
