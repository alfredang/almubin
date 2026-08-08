# almubin

Static marketing and course website for **Al Mubin Food Corner Pte. Ltd.** (UEN 202216797E) —
in-house halal handling, workplace safety and kitchen operations training for F&B teams in Singapore.

**Live:** https://almubinfctraining.com.sg

## Stack

Plain HTML + CSS + vanilla JavaScript. No database, no framework, no build step at deploy time.
Hosted on Coolify using the **Static** build pack.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | Homepage — hero, courses, testimonials, training record, flyer, contact |
| `courses/` | One detail page per course (generated) |
| `css/style.css` | Design system: Malay-heritage green + songket gold |
| `js/enquiry.js` | Enquiry form submission |
| `build/` | Page generator — `courses_data.py` (content) + `build_site.py` |

`index.html` and `courses/*.html` are **generated**. To change course content, edit
`build/courses_data.py` and run:

```bash
python3 build/build_site.py
```

## Local preview

```bash
python3 -m http.server 8125
```

Then open http://localhost:8125.

## Notes

See [CLAUDE.md](CLAUDE.md) for the design system, image-verification rule, and the list of
items still needing client sign-off (WhatsApp number, fees, course codes, testimonials).
