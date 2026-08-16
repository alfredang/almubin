#!/usr/bin/env python3
"""Build the Al Mubin Training static site from courses_data.py."""
import html, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from courses_data import (COURSES, PAST_RUNS, CONTACT, PHOTO, LABEL, TESTIMONIALS,
                          HERO_PHOTO, FLYER_PHOTO, WA_SUGGESTIONS, GOOGLE_REVIEW_URL,
                          COURSE_PHOTO, TRAINERS)
from urllib.parse import quote

SITE = pathlib.Path(__file__).resolve().parent.parent
E = html.escape

NAV = """<nav>
  <div class="wrap">
    <a class="logo" href="{root}index.html"><span class="logo-icon">AM</span><span class="logo-text"><span class="logo-title">Al Mubin FC Training</span><span class="logo-subtitle">Learn · Grow · Succeed</span></span></a>
    <ul class="nav-links">
      <li><a href="{root}index.html#courses">Courses</a></li>
      <li><a href="{root}index.html#why">Why Us</a></li>
      <li><a href="{root}index.html#trainers">Trainers</a></li>
      <li><a href="{root}index.html#testimonials">Reviews</a></li>
      <li><a href="{root}index.html#contact">Contact</a></li>
    </ul>
    <a class="btn" href="{cta}">Enquire</a>
  </div>
</nav>"""

# Keyless Google Maps embed -- no API key, so nothing secret ever reaches the repo.
SUPPORT = """<section id="contact" class="contact-sec">
  <div class="wrap">
    <div class="sec-head">
      <h2>Support &amp; contact</h2>
      <p>Questions about a course, dates, fees or group bookings? Send us a message
         or reach our training team directly.</p>
    </div>

    <div class="contact-layout">
      <div class="contact-form-card">
        <h3>Send us a message</h3>
        <p class="contact-form-sub">We reply within 1&ndash;2 working days.</p>
        <form id="contactForm" action="https://formsubmit.co/{email}" method="POST" novalidate>
          <input type="hidden" name="_subject" value="Website contact enquiry">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <div class="ok" id="contactOk"></div>
          <div class="fgrid">
            <div class="field">
              <label for="c_name">Full name <span class="req">*</span></label>
              <input type="text" id="c_name" name="name" required autocomplete="name">
            </div>
            <div class="field">
              <label for="c_company">Company / outlet</label>
              <input type="text" id="c_company" name="company" autocomplete="organization">
            </div>
            <div class="field">
              <label for="c_email">Email <span class="req">*</span></label>
              <input type="email" id="c_email" name="email" required autocomplete="email">
            </div>
            <div class="field">
              <label for="c_phone">Mobile</label>
              <input type="tel" id="c_phone" name="phone" placeholder="+65 " autocomplete="tel">
            </div>
            <div class="field full">
              <label for="c_msg">Your message <span class="req">*</span></label>
              <textarea id="c_msg" name="message" required
                placeholder="Tell us what you'd like to know &mdash; course, dates, team size or venue."></textarea>
            </div>
            <label class="check">
              <input type="checkbox" id="c_pdpa" name="pdpa_consent" required>
              <span>I consent to Al Mubin Food Corner Pte. Ltd. collecting and using my personal
              data to respond to this enquiry, in accordance with the PDPA. <span class="req">*</span></span>
            </label>
          </div>
          <div class="form-actions">
            <button class="btn" type="submit">Send message</button>
          </div>
        </form>
      </div>

      <div class="contact-side">
        <ul class="contact-list">
          <li>
            <span class="ci">&#9993;</span>
            <div><b>Email</b><a href="mailto:{email}">{email}</a></div>
          </li>
          <li>
            <span class="ci">&#128222;</span>
            <div><b>Telephone</b><a href="tel:{tel_href}">{tel_display}</a></div>
          </li>
          <li>
            <span class="ci">&#128172;</span>
            <div><b>WhatsApp</b><a href="https://wa.me/{whatsapp}" target="_blank" rel="noopener">Chat with us</a></div>
          </li>
          <li>
            <span class="ci">&#128100;</span>
            <div><b>Training enquiries</b><span>{manager}<br>{manager_title}</span></div>
          </li>
          <li>
            <span class="ci">&#128205;</span>
            <div><b>Address</b><span>{address_l1}<br>{address_l2}</span></div>
          </li>
        </ul>
        <div class="contact-map">
          <iframe
            src="https://maps.google.com/maps?q={map_q}&amp;z=16&amp;output=embed"
            title="Map showing {address_l1}, {address_l2}"
            loading="lazy" referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen></iframe>
        </div>
        <a class="map-link" href="https://maps.google.com/maps?q={map_q}"
           target="_blank" rel="noopener">Open in Google Maps &rarr;</a>
      </div>
    </div>
  </div>
</section>""".format(map_q=quote(f'{CONTACT["address_l1"]}, {CONTACT["address_l2"]}'), **CONTACT)

WA_ICON = ('<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true">'
  '<path fill="currentColor" d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.7 6.4L3 29l6.8-1.8c1.9 1 4 1.6 '
  '6.2 1.6 7.2 0 13-5.8 13-13S23.2 3 16 3zm0 23.6c-2 0-3.9-.5-5.5-1.5l-.4-.2-4 1.1 1.1-3.9-.3-.4c-1.1-1.7-1.6-3.6-1.6-5.7C5.3 '
  '10.1 10.1 5.3 16 5.3S26.7 10.1 26.7 16 21.9 26.6 16 26.6zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2s-.8 1-1 '
  '1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-2-1.8-2.3-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.5.1-.2 '
  '0-.4 0-.6s-.7-1.7-1-2.3c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 '
  '3.5c.2.2 2.4 3.7 5.9 5.2.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 2-.8 2.3-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/>'
  '</svg>')


def wa_suggestions():
    """Prefilled wa.me quick-reply chips for the WhatsApp widget."""
    return "\n".join(
        f'        <a class="wa-chip" href="https://wa.me/{CONTACT["whatsapp"]}?text={quote(s)}"'
        f' target="_blank" rel="noopener">{E(s)}</a>'
        for s in WA_SUGGESTIONS)


def footer(root=""):
    cl = "\n".join(
        f'        <li><a href="{root}courses/{c["slug"]}.html">{E(c["title"])}</a></li>'
        for c in COURSES)
    return """<footer>
  <div class="wrap footer-top">
    <div class="footer-brand">
      <div class="logo"><span class="logo-icon">AM</span><span class="logo-text"><span class="logo-title">Al Mubin FC Training</span><span class="logo-subtitle">Learn · Grow · Succeed</span></span></div>
      <p>In-house food safety, halal handling, workplace safety and kitchen operations
         training for F&amp;B teams across Singapore — delivered at your premises.</p>
      <p class="uen"><b>Al Mubin Food Corner Pte. Ltd.</b><br>UEN 202216797E</p>
    </div>
    <div class="footer-col">
      <h4>Courses</h4>
      <ul>
{courses}
      </ul>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <ul>
        <li><a href="{root}index.html#why">Why train with us</a></li>
        <li><a href="{root}index.html#trainers">Our trainers</a></li>
        <li><a href="{root}index.html#testimonials">Testimonials</a></li>
        <li><a href="{root}index.html#guide">Free safety checklist</a></li>
        <li><a href="{root}index.html#contact">Contact us</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Get in touch</h4>
      <ul>
        <li><a href="mailto:{email}">✉️ {email}</a></li>
        <li><a href="tel:{tel_href}">📞 {tel_display}</a></li>
        <li><a href="https://wa.me/{whatsapp}" target="_blank" rel="noopener">💬 WhatsApp us</a></li>
        <li class="addr">📍 {address_l1}<br><span>{address_l2}</span></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <div>© <span id="yr"></span> Al Mubin Food Corner Pte. Ltd. All rights reserved.</div>
    <p class="powered-by">Powered by <a href="https://www.tertiaryinfotech.com/" target="_blank" rel="noopener">Tertiary Infotech Academy Pte Ltd</a></p>
  </div>
</footer>

<div class="wa-widget">
  <div class="wa-panel" id="waPanel" hidden>
    <div class="wa-panel-head">
      <div class="wa-panel-avatar">{wa_icon}</div>
      <div>
        <b>Al Mubin FC Training</b>
        <span>Typically replies within a few hours</span>
      </div>
      <button class="wa-close" type="button" aria-label="Close chat options">&times;</button>
    </div>
    <div class="wa-panel-body">
      <p class="wa-greeting">Hi there 👋 &nbsp;What would you like to ask us about?</p>
      <div class="wa-suggestions">
{wa_suggestions}
      </div>
      <a class="wa-open" href="https://wa.me/{whatsapp}?text={wa_text}"
         target="_blank" rel="noopener">Or start your own message</a>
    </div>
  </div>
  <button class="wa-float" type="button" id="waToggle"
          aria-expanded="false" aria-controls="waPanel"
          aria-label="Chat with us on WhatsApp">
    {wa_icon}
    <span class="wa-label">Chat with us</span>
  </button>
</div>""".format(courses=cl, root=root,
                 wa_icon=WA_ICON,
                 wa_suggestions=wa_suggestions(),
                 wa_text=quote("Hi Al Mubin Training, I'd like to enquire about a course."),
                 **CONTACT)


TESTIMONIAL_SECTION = """<section id="testimonials" class="testimonials">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow-sm">Learner feedback</span>
      <h2>What our learners say</h2>
      <p>Collected from post-course evaluation forms retained on file for every run.</p>
    </div>
    <div class="quote-grid">
{cards}
    </div>
  </div>
</section>""".format(cards="\n".join("""      <figure class="quote-card">
        <div class="quote-mark">&ldquo;</div>
        <blockquote>{q}</blockquote>
        <figcaption>
          <div class="q-avatar">{initial}</div>
          <div>
            <b>{name}</b>
            <span>{role}</span>
            <span class="q-course">{course}</span>
          </div>
        </figcaption>
      </figure>""".format(q=E(t["quote"]), name=E(t["name"]), role=E(t["role"]),
                          course=E(t["course"]), initial=E(t["role"][0]))
                    for t in TESTIMONIALS))

# Trainer profiles. The strings in TRAINERS already carry HTML entities
# (&amp;), so they are inserted as-is rather than through E().
TRAINER_SECTION = """<section id="trainers" class="trainers">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow-sm">Our team</span>
      <h2>Meet our trainers</h2>
      <p>Every course is delivered by an experienced adult educator with hands-on
         operational background in safety, compliance and F&amp;B practice.</p>
    </div>
    <div class="trainer-grid">
{cards}
    </div>
  </div>
</section>""".format(cards="\n".join("""      <article class="trainer-card">
        <div class="trainer-head">
          <div class="trainer-avatar">{initials}</div>
          <div class="trainer-id">
            <h3>{name}</h3>
            <p class="trainer-role">{title}</p>
          </div>
        </div>
        <div class="trainer-bio">
{bio}
        </div>
        <div class="trainer-exp">
          <h4>{expertise_label}</h4>
          <ul>
{expertise}
          </ul>
        </div>
      </article>""".format(
        initials=t["initials"], name=t["name"], title=t["title"],
        expertise_label=t["expertise_label"],
        bio="\n".join(f"          <p>{p}</p>" for p in t["bio"]),
        expertise="\n".join(f"            <li>{x}</li>" for x in t["expertise"]))
                    for t in TRAINERS))

COURSE_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{seo_title}</title>
<meta name="description" content="{lede}">
<link rel="canonical" href="https://almubinfctraining.com.sg/courses/{slug}.html">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#063642">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Al Mubin FC Training">
<meta property="og:title" content="{seo_title}">
<meta property="og:description" content="{lede}">
<meta property="og:url" content="https://almubinfctraining.com.sg/courses/{slug}.html">
<meta property="og:image" content="{photo}">
<meta property="og:locale" content="en_SG">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="../css/style.css">
{jsonld}
<style>.course-hero::before{{background-image:url('{photo}')}}</style>
</head>
<body>

{nav}

<header class="course-hero">
  <div class="wrap">
    <div class="crumbs"><a href="../index.html">Home</a> › <a href="../index.html#courses">Courses</a> › {title}</div>
    <span class="eyebrow">{label} · {code}</span>
    <h1>{title}</h1>
    <div class="share-row">
      <span class="share-label">Share</span>
      <a class="share-btn" href="https://www.facebook.com/sharer/sharer.php?u={share_url}"
         target="_blank" rel="noopener" aria-label="Share on Facebook" title="Share on Facebook">
        <svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path fill="currentColor" d="M14 9h3V6h-3c-2.2 0-4 1.8-4 4v2H8v3h2v7h3v-7h3l1-3h-4v-2c0-.6.4-1 1-1z"/></svg>
      </a>
      <a class="share-btn" href="https://api.whatsapp.com/send?text={share_text}%20{share_url}"
         target="_blank" rel="noopener" aria-label="Share on WhatsApp" title="Share on WhatsApp">
        <svg viewBox="0 0 32 32" width="17" height="17" aria-hidden="true"><path fill="currentColor" d="M16 3C8.8 3 3 8.8 3 16c0 2.3.6 4.5 1.7 6.4L3 29l6.8-1.8c1.9 1 4 1.6 6.2 1.6 7.2 0 13-5.8 13-13S23.2 3 16 3zm0 23.6c-2 0-3.9-.5-5.5-1.5l-.4-.2-4 1.1 1.1-3.9-.3-.4c-1.1-1.7-1.6-3.6-1.6-5.7C5.3 10.1 10.1 5.3 16 5.3S26.7 10.1 26.7 16 21.9 26.6 16 26.6zm5.9-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2s-.8 1-1 1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-2-1.8-2.3-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.6s-.7-1.7-1-2.3c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.7 5.9 5.2.8.4 1.5.6 2 .7.8.3 1.6.2 2.2.1.7-.1 2-.8 2.3-1.6.3-.8.3-1.5.2-1.6-.1-.2-.3-.3-.6-.4z"/></svg>
      </a>
      <a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url={share_url}"
         target="_blank" rel="noopener" aria-label="Share on LinkedIn" title="Share on LinkedIn">
        <svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path fill="currentColor" d="M6.9 8H4v12h2.9V8zM5.4 3.5A1.7 1.7 0 1 0 5.4 7a1.7 1.7 0 0 0 0-3.5zM20 13.4c0-3-1.6-4.4-3.8-4.4-1.7 0-2.5.9-2.9 1.6V8H10.4c0 .8 0 12 0 12h2.9v-6.7c0-.4 0-.7.1-.9.3-.7.9-1.4 1.9-1.4 1.3 0 1.8 1 1.8 2.4V20H20v-6.6z"/></svg>
      </a>
      <a class="share-btn" href="mailto:?subject={share_text}&amp;body={share_url}"
         aria-label="Share by email" title="Share by email">
        <svg viewBox="0 0 24 24" width="17" height="17" aria-hidden="true"><path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.2-8 5-8-5V6l8 5 8-5v2.2z"/></svg>
      </a>
      <a class="review-btn" href="{review_url}" target="_blank" rel="noopener">
        <span class="review-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        Review us on Google
      </a>
    </div>
    <p class="lede">{lede}</p>
    <div class="pill-row">
      <span class="pill pill-invert">📘 {code}</span>
      <span class="pill pill-invert">⏱️ {duration}</span>
      <span class="pill pill-invert">💰 {fee_pill}</span>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="course-layout">
      <div class="course-main">
        <figure class="course-photo">
          <img src="{photo}" alt="{label} training — {title}" loading="lazy" width="1600" height="900">
        </figure>

        <h2>What this course is about</h2>
        <p>{about}</p>

        <h2>Course objectives</h2>
        <p>By the end of this course, learners will be able to:</p>
        <ul class="flyer-list">
{outcomes}
        </ul>

        <h2>Who should attend</h2>
        <p>{audience}</p>

        <h2>Modes of training</h2>
        <ul class="flyer-list">
{modes}
        </ul>

        <h2>Course fees and funding</h2>
        <p>{fee_sentence}</p>
        <p><b>Funding validity period:</b> {funding_validity}</p>

        <h2>Facilities &amp; equipment used to conduct training</h2>
        <p>Training is delivered at your premises. The following facilities and
           equipment are used to conduct this course:</p>
        <ul class="flyer-list">
{facilities}
        </ul>

        <h2>Course schedule</h2>
        <p>Sessions run on site at your premises. Dates below are confirmed runs;
           to arrange a new date for your team, use the enquiry form.</p>
        <div style="overflow-x:auto;margin-top:14px">
        <table class="runs-table">
          <thead><tr><th>Date</th><th>Venue</th><th>Duration</th><th>Status</th></tr></thead>
          <tbody>
{schedule}
          </tbody>
        </table>
        </div>
      </div>

      <aside class="course-aside">
        <div class="fact-card">
          <h3>Course details</h3>
          <ul>
            <li><span>Course code</span><b>{code}</b></li>
            <li><span>Course fee</span><b>{fee_str}</b></li>
            <li><span>Duration</span><b>{duration}</b></li>
            <li class="stack"><span>Funding validity</span><b>{funding_validity}</b></li>
            <li class="stack"><span>Modes of training</span><b>{modes_short}</b></li>
            <li><span>Format</span><b>On-site, hands-on</b></li>
            <li><span>Class size</span><b>Up to 20</b></li>
            <li><span>Languages</span><b>English · Malay</b></li>
            <li><span>Materials</span><b>Provided</b></li>
            <li><span>Certificate</span><b>Attendance</b></li>
          </ul>
          <a class="btn" href="#enquire">Enquire about this course</a>
          <div class="aside-contact">
            <div>Speak to us directly</div>
            <a href="mailto:{email}">✉️ {email}</a>
            <a href="tel:{tel_href}">📞 {tel_display}</a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>

<section id="enquire">
  <div class="wrap">
    <div class="sec-head">
      <h2>Course enquiry</h2>
      <p>Ask about dates, fees, group bookings or running <b>{title}</b> ({code})
         at your own premises. We reply within 1–2 working days.</p>
    </div>
    <form id="enquiryForm" action="https://formsubmit.co/{email}" method="POST" novalidate>
      <input type="hidden" name="_subject" value="Course enquiry: {code} {title}">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="course" value="{title}">
      <input type="hidden" name="course_code" value="{code}">
      <div class="ok" id="okMsg"></div>
      <div class="fgrid">
        <div class="field">
          <label for="fname">Full name <span class="req">*</span></label>
          <input type="text" id="fname" name="name" required autocomplete="name">
        </div>
        <div class="field">
          <label for="company">Company / outlet</label>
          <input type="text" id="company" name="company">
        </div>
        <div class="field">
          <label for="email">Email <span class="req">*</span></label>
          <input type="email" id="email" name="email" required autocomplete="email">
        </div>
        <div class="field">
          <label for="phone">Mobile <span class="req">*</span></label>
          <input type="tel" id="phone" name="phone" placeholder="+65 " required autocomplete="tel">
        </div>
        <div class="field">
          <label for="pax">Estimated participants</label>
          <input type="number" id="pax" name="pax" min="1" max="20" value="1">
        </div>
        <div class="field">
          <label for="pdate">Preferred period</label>
          <input type="month" id="pdate" name="preferred_period">
        </div>
        <div class="field full">
          <label for="msg">Your enquiry</label>
          <textarea id="msg" name="message"
            placeholder="Tell us about your team, venue and what you'd like the training to cover."></textarea>
        </div>
        <label class="check">
          <input type="checkbox" id="pdpa" name="pdpa_consent" required>
          <span>I consent to Al Mubin Food Corner Pte. Ltd. collecting and using my personal
          data to respond to this enquiry, in accordance with the PDPA. <span class="req">*</span></span>
        </label>
      </div>
      <div class="form-actions">
        <button class="btn" type="submit">Send enquiry</button>
        <span class="hint">Fields marked <span class="req">*</span> are required. Or email
          <a href="mailto:{email}">{email}</a> · call <a href="tel:{tel_href}">{tel_display}</a>.</span>
      </div>
    </form>
  </div>
</section>

{testimonials}

{support}

{footer}

<script src="../js/enquiry.js"></script>
</body>
</html>
"""


def fee_str(fee):
    # Pro-bono courses carry fee=0 and must never render as "S$0".
    return "Free (Pro-Bono)" if not fee else f"S${fee:,}"


def course_photo(c, w=1600, q=75):
    """Per-course image, falling back to the category photo."""
    base = COURSE_PHOTO.get(c["slug"])
    if not base:
        return PHOTO[c["cat"]]
    return f"{base}?auto=format&fit=crop&w={w}&q={q}"


def modes_short(c):
    """One-line summary of the training modes, for narrow cards and sidebars."""
    return " · ".join(m.split(" / ")[0].split(" in ")[0].strip() for m in c["modes"])


def build_course(c):
    outcomes = "\n".join(f"          <li>{E(o)}</li>" for o in c["outcomes"])
    modes = "\n".join(f"          <li>{E(m)}</li>" for m in c["modes"])
    facilities = "\n".join(f"          <li>{E(f)}</li>" for f in c["facilities"])
    sched = "\n".join(
        f"            <tr><td>{E(d)}</td><td>{E(v)}</td><td>{c['hours']} hrs</td>"
        f"<td>{E(s)}</td></tr>" for (d, v, s) in c["schedule"])
    return COURSE_PAGE.format(
        jsonld=course_jsonld(c),
        title=E(c["title"]), code=c["code"], lede=E(c["lede"]),
        about=E(c["about"]), audience=E(c["audience"]),
        outcomes=outcomes, schedule=sched,
        modes=modes, facilities=facilities,
        funding_validity=E(c["funding_validity"]),
        modes_short=E(modes_short(c)),
        share_url=quote(f"https://almubinfctraining.com.sg/courses/{c['slug']}.html", safe=""),
        share_text=quote(c["title"], safe=""),
        review_url=GOOGLE_REVIEW_URL,
        duration=c["duration"], fee_str=fee_str(c["fee"]),
        fee_pill=("Free (Pro-Bono)" if not c["fee"]
                  else f"{fee_str(c['fee'])} per participant"),
        fee_sentence=(
            "This course is delivered <b>pro-bono</b> — free of charge — including all "
            "training materials and the certificate of attendance."
            if not c["fee"] else
            f"The course fee is <b>{fee_str(c['fee'])} per participant</b>, covering all "
            "training materials and the certificate of attendance. Al Mubin Food Corner "
            "Pte. Ltd. is not GST-registered, so no GST is charged."),
        label=LABEL[c["cat"]], photo=course_photo(c),
        slug=c["slug"], hours=c["hours"], fee_num=c["fee"],
        seo_title=f'{c["title"]} ({c["code"]}) | Al Mubin FC Training',
        nav=NAV.format(root="../", cta="#enquire"),
        support=SUPPORT, footer=footer("../"),
        testimonials=TESTIMONIAL_SECTION, **CONTACT)


INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Halal &amp; Workplace Safety Training for F&amp;B Teams | Singapore</title>
<meta name="description" content="On-site halal handling, workplace safety and kitchen operations training for Singapore F&B teams. Delivered at your outlet in English &amp; Malay. Free 12-point safety checklist.">
<link rel="canonical" href="https://almubinfctraining.com.sg/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#063642">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Al Mubin FC Training">
<meta property="og:title" content="Halal &amp; Workplace Safety Training for F&amp;B Teams | Singapore">
<meta property="og:description" content="On-site halal handling, workplace safety and kitchen operations training for Singapore F&B teams. Free 12-point safety checklist.">
<meta property="og:url" content="https://almubinfctraining.com.sg/">
<meta property="og:locale" content="en_SG">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="css/style.css">
{jsonld}
</head>
<body>

{nav}

<header class="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="eyebrow">🕌 Halal-certified F&amp;B training · UEN 202216797E</span>
      <h1>Practical training for <span class="hl">F&amp;B teams</span>.</h1>
      <p class="lede">Halal handling, workplace safety and kitchen operations training —
        delivered on site at your stall, kitchen or outlet by trainers who have worked
        the line themselves. Short, hands-on sessions built around how your team actually works.</p>
      <div class="cta-row">
        <a class="btn btn-lg" href="#courses">Browse our courses</a>
        <a class="btn btn-ghost btn-lg" href="#guide">Free safety checklist</a>
      </div>
      <ul class="hero-ticks">
        <li>✓ On-site at your premises</li>
        <li>✓ English &amp; Malay</li>
        <li>✓ Certificate included</li>
      </ul>
    </div>
    <div class="hero-art" aria-hidden="true">
      <div class="hero-photo hero-photo-1" style="background-image:url('{hero_main}')"></div>
      <div class="hero-photo hero-photo-2" style="background-image:url('{hero_inset}')"></div>
      <div class="hero-badge">
        <b>{n_runs}</b><span>course runs<br>delivered</span>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="stats">
      <div class="stat"><span class="stat-ic">📚</span><b>{n_courses}</b><span>Courses offered</span></div>
      <div class="stat"><span class="stat-ic">🎓</span><b>{n_runs}</b><span>Course runs delivered</span></div>
      <div class="stat"><span class="stat-ic">⏱️</span><b>{n_hours}</b><span>Training hours</span></div>
      <div class="stat"><span class="stat-ic">📍</span><b>{n_venues}</b><span>Partner venues</span></div>
    </div>
  </div>
</header>

<section id="courses">
  <div class="wrap">
    <div class="sec-head">
      <h2>Our courses</h2>
      <p>Open any course for the full syllabus, fee, schedule and an enquiry form.</p>
    </div>
    <div class="grid">
{cards}
    </div>
  </div>
</section>

<section id="why">
  <div class="wrap">
    <div class="sec-head"><h2>Why train with us</h2></div>
    <div class="feat">
      <div><span class="ic">👨‍🍳</span><h3>Trainers from the trade</h3>
        <p>Sessions are run by people who have worked the line, not read about it.</p></div>
      <div><span class="ic">📍</span><h3>On-site delivery</h3>
        <p>We come to your stall, kitchen or outlet — no downtime travelling to a classroom.</p></div>
      <div><span class="ic">🕌</span><h3>Halal-first practice</h3>
        <p>Halal handling and segregation built into every food-handling module.</p></div>
      <div><span class="ic">📋</span><h3>Documented outcomes</h3>
        <p>Objectives, lesson plans, assessment records and feedback analysis kept for every run.</p></div>
    </div>
  </div>
</section>

{trainers}

{testimonials}

<section id="guide" class="lead-magnet">
  <div class="wrap">
    <div class="lead-grid">
      <div class="lead-copy">
        <span class="eyebrow-sm">Free download · No cost</span>
        <h2>The 12-Point Halal &amp; Food Safety Checklist for F&amp;B Outlets</h2>
        <p>The same walkthrough our trainers use on site — the twelve things
           SFA and halal auditors check first, written in plain English and Malay.
           Print it, walk your kitchen, fix what you find before an inspector does.</p>
        <ul class="lead-benefits">
          <li>Segregation and labelling gaps that break halal compliance</li>
          <li>Temperature, storage and FIFO checks that fail most often</li>
          <li>The hazards that cause the majority of F&amp;B workplace injuries</li>
        </ul>
        <p class="lead-trust">Used by kitchen teams across Singapore · Takes 10 minutes to run</p>
      </div>

      <div class="lead-form-card">
        <h3>Get the checklist</h3>
        <p class="lead-form-sub">Enter your details and we'll email it to you right away.</p>
        <form id="leadForm" action="https://formsubmit.co/{email}" method="POST" novalidate>
          <input type="hidden" name="_subject" value="Lead magnet: Halal &amp; Food Safety Checklist">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="lead_source" value="12-Point Checklist">
          <div class="ok" id="leadOk"></div>
          <div class="field">
            <label for="lead_name">Name <span class="req">*</span></label>
            <input type="text" id="lead_name" name="name" required autocomplete="name">
          </div>
          <div class="field">
            <label for="lead_email">Work email <span class="req">*</span></label>
            <input type="email" id="lead_email" name="email" required autocomplete="email">
          </div>
          <div class="field">
            <label for="lead_outlet">Outlet / company</label>
            <input type="text" id="lead_outlet" name="company" autocomplete="organization">
          </div>
          <div class="field">
            <label for="lead_phone">Mobile (for WhatsApp)</label>
            <input type="tel" id="lead_phone" name="phone" placeholder="+65 " autocomplete="tel">
          </div>
          <label class="check">
            <input type="checkbox" id="lead_pdpa" name="pdpa_consent" required>
            <span>I consent to Al Mubin Food Corner Pte. Ltd. contacting me about this
            checklist and its training courses, in line with the PDPA. <span class="req">*</span></span>
          </label>
          <button class="btn btn-lg btn-block" type="submit">Send me the checklist</button>
          <p class="lead-fineprint">No spam. Unsubscribe any time.</p>
        </form>
      </div>
    </div>
  </div>
</section>

{support}

{footer}

<script src="js/enquiry.js"></script>
</body>
</html>
"""




def course_jsonld(c):
    site = "https://almubinfctraining.com.sg"
    url = f"{site}/courses/{c['slug']}.html"
    data = {"@context":"https://schema.org","@type":"Course",
      "name":c["title"],"courseCode":c["code"],"description":c["lede"],
      "url":url,"inLanguage":["en-SG","ms"],
      "provider":{"@type":"Organization","name":"Al Mubin FC Training","url":f"{site}/"},
      "offers":{"@type":"Offer","price":str(c["fee"]),"priceCurrency":"SGD",
                "category":"Professional training",
                "availability":"https://schema.org/InStock","url":url},
      "hasCourseInstance":{"@type":"CourseInstance","courseMode":"onsite",
        "location":{"@type":"Place","name":"On-site at your premises",
                    "address":{"@type":"PostalAddress","addressCountry":"SG"}},
        "courseWorkload":f"PT{c['hours']}H"}}
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=1) + '\n</script>')


def index_jsonld():
    site = "https://almubinfctraining.com.sg"
    data = {"@context":"https://schema.org","@graph":[
      {"@type":["LocalBusiness","EducationalOrganization"],
       "@id":f"{site}/#org",
       "name":"Al Mubin FC Training",
       "legalName":"Al Mubin Food Corner Pte. Ltd.",
       "url":f"{site}/",
       "email":CONTACT["email"],
       "telephone":CONTACT["tel_display"],
       "areaServed":{"@type":"Country","name":"Singapore"},
       "address":{"@type":"PostalAddress","streetAddress":CONTACT["address_l1"],
                  "addressLocality":"Singapore","postalCode":CONTACT["postal_code"],
                  "addressCountry":"SG"},
       "description":"On-site halal handling, workplace safety and kitchen operations training for F&B teams in Singapore."},
      {"@type":"WebSite","@id":f"{site}/#website","url":f"{site}/",
       "name":"Al Mubin FC Training","publisher":{"@id":f"{site}/#org"},"inLanguage":"en-SG"}]}
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=1) + '\n</script>')


def build_index():
    cards = "\n".join("""      <article class="card">
        <div class="thumb" style="background-image:url('{photo}')" role="img"
             aria-label="{label} training">
          <span class="tag">{label}</span>
        </div>
        <div class="body">
          <div class="code-line">{code}</div>
          <h3><a href="courses/{slug}.html">{title}</a></h3>
          <p class="desc">{lede}</p>
          <div class="meta">
            <span>⏱️ <b>{duration}</b></span>
            <span>💰 <b>{fee}</b></span>
            <span>🎓 <b>{modes_short}</b></span>
            <span>📅 Funding validity: <b>{funding_validity}</b></span>
          </div>
          <div class="card-cta">
            <a class="btn" href="courses/{slug}.html">View details &amp; enquire</a>
          </div>
        </div>
      </article>""".format(
        photo=course_photo(c, w=800, q=70), label=LABEL[c["cat"]], code=c["code"],
        slug=c["slug"], title=E(c["title"]), lede=E(c["lede"]),
        modes_short=E(modes_short(c)), funding_validity=E(c["funding_validity"]),
        duration=c["duration"], fee=fee_str(c["fee"])) for c in COURSES)

    runs = "\n".join(
        f"        <tr><td>{i}</td><td>{E(t)}</td><td>{E(v)}</td><td>{E(d)}</td>"
        f"<td>{h} hrs</td><td>{E(a)} yrs</td></tr>"
        for i, (t, v, h, d, a, _c) in enumerate(PAST_RUNS, 1))

    # Derived from the data so the headline figures cannot drift out of date
    # when a course or a past run is added. Venues exclude the pro-bono
    # food-court entry, which is a group of stalls rather than a single venue.
    n_hours = sum(h for (_t, _v, h, _d, _a, _c) in PAST_RUNS)
    n_venues = len({v for (_t, v, _h, _d, _a, _c) in PAST_RUNS
                    if "Pro-Bono" not in v})

    return INDEX.format(jsonld=index_jsonld(),
                        n_courses=len(COURSES), n_runs=len(PAST_RUNS),
                        n_hours=n_hours, n_venues=n_venues,
                        nav=NAV.format(root="", cta="#courses"),
                        cards=cards, runs=runs, support=SUPPORT,
                        trainers=TRAINER_SECTION,
                        testimonials=TESTIMONIAL_SECTION,
                        hero_main=HERO_PHOTO["main"], hero_inset=HERO_PHOTO["inset"],
                        flyer_photo=FLYER_PHOTO,
                        footer=footer(""), **CONTACT)


outdir = SITE / "courses"
outdir.mkdir(exist_ok=True)
# Remove pages for courses no longer offered.
keep = {f"{c['slug']}.html" for c in COURSES}
for old in outdir.glob("*.html"):
    if old.name not in keep:
        old.unlink()
        print("removed", old.name)

for c in COURSES:
    (outdir / f"{c['slug']}.html").write_text(build_course(c), encoding="utf-8")
    print("wrote courses/%s.html" % c["slug"])

(SITE / "index.html").write_text(build_index(), encoding="utf-8")
print("wrote index.html")
print("done:", len(COURSES), "courses,", len(PAST_RUNS), "runs")
