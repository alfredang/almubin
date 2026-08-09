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

Deep teal ground + amber accent, taken from the client's holding page.

| Token | Value | Use |
|---|---|---|
| `--brand` | `#08535b` | primary teal, buttons, WhatsApp widget |
| `--brand-dk` | `#063642` | hovers, hero gradients, panel headers |
| `--brand-lt` | `#e6f1f3` | tinted panels |
| `--amber` / `--gold` | `#f6bd3c` | accents, logo badge, CTA buttons |
| `--ink` | `#062b36` | body text |
| `--teal-dk` | `#042634` | footer background |

The WhatsApp widget deliberately uses brand teal rather than WhatsApp green so it
sits inside the palette; keep it that way if you restyle it.

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

**A 200 is not sufficient on its own.** Some `plus.unsplash.com` ("Unsplash+") photos are
served to *browsers* with a repeating "Unsplash+" watermark, even though `curl` of the same
URL returns a clean image. Always load the page in a browser and look at the picture before
committing a `plus.unsplash.com` URL. Free-tier `images.unsplash.com` URLs are never
watermarked, so prefer them. (Three `plus.` URLs currently in use were checked in-browser
and are clean.)

Per-course product images live in `COURSE_PHOTO` in `courses_data.py`, keyed by slug, and
fall back to `PHOTO[cat]`. They cannot be derived from `cat` alone — three courses share
the `service` category and would otherwise all show the same picture.

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

1. **Course fees** — S$280 / S$380 were set for the site, not taken from a client
   price list. Confirm, and confirm GST treatment.
2. **Google review link** — `GOOGLE_REVIEW_URL` in `courses_data.py` currently points at
   a Google *search* for the business, not the review box. Replace with the Business
   Profile deep link `https://search.google.com/local/writereview?placeid=<PLACE_ID>`
   once the Place ID is known, so the button opens the review dialog directly.
3. **SWDA disclosure fields** — `funding_validity`, `modes` and `facilities` in
   `courses_data.py` are SAMPLE values written to satisfy the SWDA information-
   disclosure format. All must be replaced with the client's actual particulars.
   The funding validity periods in particular are placeholders: these are in-house
   courses and are not currently SSG-funded, so the honest disclosure may be
   "not applicable". The disclosure list also requires the **names of senior
   management and trainers** and the **organisation structure**, which are not yet
   anywhere on the site.
4. **Course codes** — `AMFC-WS01` / `AMFC-HL01` / `AMFC-KO01` were assigned here.
5. **Testimonials** — written from the profile of the courses and venues on record.
   They are **not** verbatim learner quotes. Either replace them with real quotes from
   the post-course evaluation forms or remove the section; do not publish them as
   attributed testimonials without the client's sign-off.
6. **FormSubmit activation** — see above.
7. **DNS** — a stale `@ → 23.106.50.5` A record still points at the old host alongside
   the correct `72.61.151.123`. Delete it, or the site will intermittently resolve to
   the wrong server and SSL issuance can fail.
