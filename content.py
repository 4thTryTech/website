"""All page copy for the site. Edit here, then run build.py.

Entries marked sample=True are invented placeholders that show the layout. They carry a visible "Sample" tag on the
site. Replace them with real write-ups and drop the flag.
Body blocks: a plain string is a paragraph; ("h2", text) is a heading; ("note", text) is a highlighted placeholder note;
("try", number, held, heading, text) is one step of a project's route (held=True marks the try that worked).
"""

SITE = {
    "name": "4th Try Tech",
    "tagline": "When the 3rd try wasn’t enough, keep going.",
    "description": "A working log of technology projects, experiments, and misadventures.",
    "url": "https://4thtrytech.github.io/website/",   # change to https://4thtry.tech/ when the domain points here
    "domain": "",                                       # set to "4thtry.tech" to write a CNAME file for GitHub Pages
}

PAGES = {
    "home": {
        "what": [
            "Good projects rarely go in a straight line. 4th Try Tech follows the route they actually take: the idea, the first build, the detours, the rethink, and the version that finally holds.",
            "I write about architecture, tools, automation and home-built infrastructure. Come for the project, stay for the journey, and borrow whatever saves you a lap.",
        ],
        "steps": [
            ("The idea", "What I wanted and why it seemed simple."),
            ("The first build", "What I tried first, with the versions and the numbers."),
            ("The detours", "What broke, what I changed, and what each try cost."),
            ("The version that holds", "What is running now, and what I would skip next time."),
        ],
    },
    "story": {
        "title": "Story",
        "description": "Why it is called 4th Try Tech, and who is behind it.",
        "body": [
            ("h2", "Why “4th Try”"),
            "The name is the brand. Three tries that do not take, and a fourth that does.",
            "I have shipped enough systems to know the first plan never survives contact with the hardware, the second fixes the wrong thing, and the third almost works. The fourth is the one built on what the first three taught. That is not failure, it is the route. This site keeps the route in view instead of hiding it.",
            ("h2", "What you will find here"),
            "Projects and lab notes on architecture, tools, automation and home-built infrastructure. Each one shows the path it actually took: what I set out to do, what I tried, what I changed and why, and what is running now. Versions, numbers and configs are included, because “it got faster” helps nobody.",
            "If something here saves you a lap, it has done its job.",
            ("h2", "Who is behind it"),
            ("note", "Draft wording, to be confirmed before launch."),
            "I am Michael Lehman, a solutions architect. I design tooling and automation for large managed infrastructure by day, and I run a homelab that gets rebuilt more often than it strictly needs. 4th Try Tech is my personal project, separate from my employer, and the opinions are my own.",
            ("h2", "The mark"),
            "The rocket carries a 4 because it is the fourth try that flies. Coral marks a try that did not take. Green is kept for the one that did, and for nothing else.",
        ],
    },
    "contact": {
        "title": "Contact",
        "description": "How to reach 4th Try Tech.",
        "body": [
            "Found a mistake, have a better way, or tried the same thing and got a different result? I would like to hear it.",
            ("note", "Placeholder: the contact channel has not been chosen yet. An email address, a form, or links such as GitHub or LinkedIn will go here."),
        ],
    },
    "projects_intro": "Longer write-ups. Each one shows the whole route: the idea, every try, and the version that finally held.",
    "notes_intro": "Shorter, dated entries written while the work is happening.",
}

PROJECTS = [
    {
        "slug": "sample-homelab-storage", "sample": True, "try": 4, "held": True, "date": "2026-09-12",
        "title": "Homelab storage that survives a dead node",
        "summary": "Three tries at replication before one held through a pulled cable.",
        "body": [
            ("h2", "The idea"),
            "Keep one copy of everything that matters on three small servers in three places, so that losing any one of them is an inconvenience and not an event.",
            ("try", 1, False, "Mirror everything, everywhere", "Simple to reason about and far too slow over a home uplink. The first full sync never finished."),
            ("try", 2, False, "Sync on a schedule", "Finished, but a node that was offline at the wrong hour came back with stale data and quietly won."),
            ("try", 3, False, "Snapshots shipped in order", "Almost. Ordering held, but a pulled network cable mid-transfer left a snapshot half applied."),
            ("try", 4, True, "Snapshots, resumable, verified before they count", "A transfer only becomes the new truth after it is complete and checked. Pulling the cable now costs minutes, not data."),
            ("h2", "What I would skip next time"),
            "Try 2. A schedule hides the question of which copy is newer, and that question always comes back.",
        ],
    },
    {
        "slug": "sample-alert-noise", "sample": True, "try": 2, "held": False, "date": "2026-09-18",
        "title": "Alert noise, cut down to what matters",
        "summary": "Second pass at grouping alerts so a bad night is five pages, not fifty.",
        "body": [
            ("h2", "The idea"),
            "Group alerts by the thing that is actually broken, not by the check that noticed it.",
            ("try", 1, False, "Group by host", "Better than nothing, but one bad switch still paged once per server behind it."),
            ("try", 2, False, "Group by dependency", "In progress. Needs a dependency map I trust, which turns out to be its own project."),
        ],
    },
]

NOTES = [
    {
        "slug": "sample-why-the-third-try-failed", "sample": True, "date": "2026-09-18",
        "title": "Why the third try failed on Tuesday",
        "summary": "The config was right. The assumption about the network was not.",
        "body": [
            "Everything passed in the lab. In place, the replication link dropped every few minutes and the transfer restarted from zero each time.",
            "The fix was not in the storage layer at all. More on that in the project write-up.",
        ],
    },
    {
        "slug": "sample-picking-a-time-series-database", "sample": True, "date": "2026-09-05",
        "title": "Notes on picking a time-series database",
        "summary": "What I compared, what I measured, and the one number that decided it.",
        "body": [
            "Three candidates, one week of real metrics replayed into each, the same queries against all three.",
            "The deciding number was not ingest rate. It was how long the dashboard I open most took to load.",
        ],
    },
]
