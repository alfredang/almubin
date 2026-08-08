# Al Mubin Training — Static Website

Marketing and course site for **Al Mubin Food Corner Pte. Ltd.** (UEN 202216797E), a
Singapore F&B company delivering in-house training to food-and-beverage teams.

- **Repo:** https://github.com/alfredang/almubin
- **Domain:** almubinfctraining.com.sg (also `www.`)
- **Hosting:** Coolify (Static build pack) on server `72.61.151.123`
- **Stack:** plain HTML + CSS + vanilla JS. **No database, no build step, no framework.**

## Non-negotiable constraints

1. **Static only.** No server-side code, no npm build, no bundler. Coolify serves the
   files as-is through nginx. Anything requiring a runtime is out of scope.
2. **No secrets in the repo.** The enquiry forms post to a third-party form relay
   (FormSubmit); there is no API key to store. Never commit one.
3. **Course facts come from client records**, not invention. Course titles, durations
   and delivery dates trace to the SSG training-track-record workbooks and the CASL
   course proposals in the parent client folder. Fees and course codes were assigned
   for the website and still need client sign-off (see *Open items*).

## Layout

```
website/
  index.html                 # generated — do not hand-edit
  courses/*.html             # generated — one page per course, do not hand-edit
  css/style.css              # hand-maintained
  js/enquiry.js              # hand-maintained (AJAX enquiry submit)
  CLAUDE.md                  # this file
  .claude/skills/            # symlinks -> ../../.agents/skills/
  .agents/skills/            # ui-ux-pro-max, seo-audit, lead-magnets
```

### The HTML is generated

`index.html` and everything under `courses/` are produced by a build script from a
single data module. **Editing them by hand will be overwritten on the next build.**

- Data (courses, fees, codes, schedules, testimonials, contact, photos):
  `build/courses_data.py`
- Generator: `build/build_site.py`

To change course content, edit `build/courses_data.py` and rebuild from `website/`:

```bash
python3 build/build_site.py
```

The generator writes `index.html` and `courses/*.html`, and deletes any page under
`courses/` whose slug is no longer in `COURSES`. Prefer regenerating over hand-patching
so every page stays consistent. Python 3, no dependencies.

CSS and JS are **not** generated; edit `css/style.css` and `js/enquiry.js` directly.

## Design system

Malay-heritage / halal F&B theme. Green + songket gold.

| Token | Value | Use |
|---|---|---|
| `--brand` | `#0f7a52` | primary green, buttons, links |
| `--brand-dk` | `#0a5638` | hovers, hero gradients |
| `--brand-lt` | `#e6f4ee` | tinted panels |
| `--gold` | `#c8892b` | songket accents |
| `--ink` | `#0f2119` | body text, footer background |

Recurring motifs — keep these when adding sections:

- **Songket rule** under every `.sec-head h2` (gold/green repeating gradient).
- **Songket ribbon** across the top of every `.card`.
- **Woven diagonal texture** in `.hero-bg`.
- Photography is Malay/halal food (satay, nasi lemak) and working kitchens. Images
  are large and lead the design — do not shrink them.

### Images

All photos are **hot-linked from Unsplash**, no local assets. Unsplash photo IDs
rot — several 404'd during the build. **Always verify a new image URL returns HTTP 200
before committing it:**

```bash
curl -s -o /dev/null -w "%{http_code}" "https://images.unsplash.com/photo-XXXX?auto=format&fit=crop&w=400&q=60"
```

A 404 renders as a blank coloured box, which is easy to miss without a screenshot.

## Enquiry forms

Each course page carries its own enquiry form posting to
`https://formsubmit.co/support@almubin.com.sg`. `js/enquiry.js` submits via the
AJAX endpoint and falls back to a normal form POST if fetch fails.

**FormSubmit requires one-time activation:** the first submission triggers a
confirmation email to `support@almubin.com.sg` that someone must click before any
enquiry is delivered. Until that happens, submissions silently go nowhere.

## Deploying

Push to `main`; Coolify redeploys (a webhook can be configured in the app's
Webhooks tab). No build command — the Static build pack publishes the repo root.

## Verifying a change

There is no test suite. Before pushing:

```bash
python3 -m http.server 8125       # from website/
```

Then check in a browser at desktop (1440px) **and** mobile (390px):

- every page returns 200 and no console errors (a missing `favicon.ico` 404 is expected);
- no horizontal scroll on mobile — `document.documentElement.scrollWidth === window.innerWidth`;
- **every image actually renders** (screenshot it; dead Unsplash IDs look like empty panels);
- the footer keeps four columns on desktop and stacks cleanly on mobile.

## Available skills

Installed under `.claude/skills/` (symlinked from `.agents/skills/`):

- **ui-ux-pro-max** — design system database; query with
  `python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain color|style|ux`
- **seo-audit** — SEO review of the pages
- **lead-magnets** — lead-capture content ideas

## Open items

These need the client's confirmation before the site goes public:

1. **WhatsApp number** — `courses_data.py` currently points `wa.me` at the office
   landline `6562910000`, which will not work. Replace with a real mobile.
2. **Course fees** — S$280 / S$380 were set for the site, not taken from a client
   price list. Confirm, and confirm GST treatment.
3. **Course codes** — `AMFC-WS01` / `AMFC-HL01` / `AMFC-KO01` were assigned here.
4. **Testimonials** — written from the profile of the courses and venues on record.
   They are **not** verbatim learner quotes. Either replace them with real quotes from
   the post-course evaluation forms or remove the section; do not publish them as
   attributed testimonials without the client's sign-off.
5. **FormSubmit activation** — see above.
6. **DNS** — a stale `@ → 23.106.50.5` A record still points at the old host alongside
   the correct `72.61.151.123`. Delete it, or the site will intermittently resolve to
   the wrong server and SSL issuance can fail.
