# Single source of truth for the Al Mubin Training website.
# Course codes: AMFC-<CAT><NN>. Fees are per-participant, GST not applicable
# (Al Mubin is not GST-registered as of writing) -- confirm with client before launch.
#
# SWDA / SSG information-disclosure requirement
# ---------------------------------------------
# A Training Provider must disclose, on its website or brochures: course title,
# course training duration, course fees, funding validity period, modes of training,
# course objectives, the names of senior management and trainers, the organisation
# structure, and the facilities & equipment used to conduct training.
#
# Per-course fields below cover title / duration / fees / funding_validity /
# modes / outcomes (objectives) / facilities. Senior management, trainers and the
# organisation structure are NOT yet on the site -- see TODO(client) at the bottom.
#
# TODO(client): funding_validity, modes and facilities below are SAMPLE VALUES
# written to satisfy the disclosure format. Every one must be replaced with the
# client's actual particulars before the site is published. In particular the
# funding validity periods are placeholders -- Al Mubin's courses are in-house and
# are not currently SSG-funded, so the correct disclosure may be "not applicable".

CONTACT = {
    "email": "support@almubin.com.sg",
    "tel_display": "+65 9138 8967",
    "tel_href": "+6591388967",
    # Training team mobile. Digits only, country code first, no "+" -- wa.me link.
    "whatsapp": "6591388967",
    "manager": "Nabisah Begum Binte MD Ibrahim",
    "manager_title": "Training Manager",
    "address_l1": "92 Syed Alwi Road",
    "address_l2": "Singapore 207668",
}

# Google review link shown on each course page.
# TODO(client): replace with the Google Business Profile "write a review" deep link
# once the profile's Place ID is known -- that form is
#   https://search.google.com/local/writereview?placeid=<PLACE_ID>
# and opens the review dialog directly. The search URL below is a stand-in that
# lands on the business listing rather than the review box.
GOOGLE_REVIEW_URL = ("https://www.google.com/search?q=Al+Mubin+Food+Corner"
                     "+92+Syed+Alwi+Road+Singapore")

# Quick-start messages offered in the WhatsApp widget. Each becomes a prefilled
# wa.me message so the enquirer does not have to type one from scratch.
WA_SUGGESTIONS = [
    "I'd like to know the course fees and available dates.",
    "Can you run a course at my outlet?",
    "Is this course eligible for funding?",
    "How many staff can attend one session?",
    "I'd like to speak to someone about a group booking.",
]

# Learner feedback collected from post-course evaluation forms.
TESTIMONIALS = [
    {
        "quote": "The trainer walked our kitchen with us and pointed out hazards we had stopped noticing — the wet patch by the wok station, the way we were stacking the delivery crates. My crew changed how they work the very next shift.",
        "name": "Kitchen Supervisor",
        "role": "Adam Food Corner",
        "course": "Workplace Safety & Accident Prevention",
    },
    {
        "quote": "We thought our halal segregation was already tight. The session showed us where our labelling and supplier records had gaps, and gave us a checklist we now run every week.",
        "name": "Outlet Owner",
        "role": "Zamas",
        "course": "Halal Handling & Internal Halal SOP",
    },
    {
        "quote": "Conducted in both English and Malay, which meant every one of my staff actually followed it. Practical, no long lectures — they were on their feet doing things.",
        "name": "Stall Operator",
        "role": "3 Monkeys",
        "course": "Food Safety and Hygiene",
    },
]

PHOTO = {
    # Malay / halal F&B imagery. Every URL below was verified to return HTTP 200.
    "food": "https://images.unsplash.com/photo-1569058242252-623df46b5025?auto=format&fit=crop&w=1600&q=75",       # nasi lemak w/ egg
    "halal": "https://images.unsplash.com/photo-1755434315388-16387508c1fb?auto=format&fit=crop&w=1600&q=75",      # chicken satay + peanut sauce
    "safety": "https://plus.unsplash.com/premium_photo-1774556295016-a38947d626d3?auto=format&fit=crop&w=1600&q=75",  # chef cooking with wok flames
    "service": "https://plus.unsplash.com/premium_photo-1695297516698-fd7a320a55e5?auto=format&fit=crop&w=1600&q=75",  # halal food stall
    "kitchen": "https://images.unsplash.com/photo-1734018959101-4a9c93b6055d?auto=format&fit=crop&w=1600&q=75",     # chefs working a kitchen line
}
HERO_PHOTO = {
    "main": "https://images.unsplash.com/photo-1755434315388-16387508c1fb?auto=format&fit=crop&w=1200&q=80",       # satay
    "inset": "https://images.unsplash.com/photo-1569058242252-623df46b5025?auto=format&fit=crop&w=900&q=80",       # nasi lemak
}
FLYER_PHOTO = "https://plus.unsplash.com/premium_photo-1669687070821-328b9ef599f5?auto=format&fit=crop&w=1600&q=75"
LABEL = {
    "food": "Food Safety", "halal": "Halal", "safety": "Workplace Safety",
    "service": "Service & Leadership", "kitchen": "Kitchen Operations",
}

COURSES = [
    {
        "slug": "workplace-safety",
        "code": "AMFC-WS01",
        "title": "Workplace Safety & Accident Prevention for the F&B Industry",
        "cat": "safety",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 280,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on in your kitchen"],
        "facilities": [
            "Client's own working kitchen and service area, used as the live training floor",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Demonstration PPE set: heat-resistant gloves, non-slip footwear, aprons",
            "Fire extinguisher and fire blanket (training units) for suppression practice",
            "First-aid kit, spill kit and hazard signage used in the response drills",
        ],
        "lede": "Spot hazards before they become accidents — slips, burns, cuts, fire and manual handling — in a full-day, hands-on session on your own floor.",
        "about": "F&B kitchens concentrate more hazards per square metre than almost any other workplace: hot oil, sharp blades, wet floors, gas lines and heavy stock, all handled at speed during service. This full-day course trains your team to see those hazards before they cause harm, control them with the right technique and equipment, and respond correctly when something does go wrong. Every session is delivered at your own premises using your own equipment and layout, so the risks discussed are the actual risks your crew faces each shift — not classroom photographs. The course closes with your outlet's incident reporting and escalation procedure, so staff know exactly who to tell and what to record.",
        "outcomes": [
            "Identify common F&B workplace hazards: slips and trips, burns and scalds, cuts, fire and gas",
            "Apply safe manual-handling technique for stock, pots and deliveries",
            "Use knives, slicers and hot equipment with the correct guards and technique",
            "Carry out a basic risk assessment and hazard report for their own work area",
            "Respond to accidents correctly: first response, escalation and incident recording",
        ],
        "audience": "All F&B staff. Strongly recommended for kitchen crew and anyone handling hot equipment, sharp tools or deliveries.",
        "schedule": [
            ("24 Jul 2025", "Adam Food Corner", "Completed"),
            ("22 Oct 2025", "Adam Food Corner", "Completed"),
            ("08 Jan 2026", "Adam Food Corner", "Completed"),
            ("19 May 2026", "Adam Food Corner", "Completed"),
        ],
    },
    {
        "slug": "halal-handling-sop",
        "code": "AMFC-HL01",
        "title": "Halal Handling & Internal Halal SOP",
        "cat": "halal",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 280,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on in your kitchen"],
        "facilities": [
            "Client's own storage, preparation and service areas, walked as part of the session",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Segregated halal / non-halal utensil and chopping-board sets for the sorting exercise",
            "Sample supplier halal certificates and delivery documents for the verification drill",
            "Colour-coded labels, chiller shelf tags and the outlet's internal halal SOP checklists",
        ],
        "lede": "Keep your kitchen halal-compliant end to end — sourcing, segregation, storage and service — aligned with your internal halal SOP.",
        "about": "Halal compliance rarely fails at the level of principle; it fails in the details. A shared chopping board, an unlabelled chiller shelf, a delivery accepted without checking the supplier's certificate — any one of these can break the halal chain and put your certification at risk. This full-day course walks your team through the complete halal chain as it runs in your own premises: receiving, storage, preparation, cooking and service. Learners practise the segregation habits your internal halal SOP requires, learn how to verify supplier certification and maintain the supporting records, and rehearse the correct response when a suspected breach occurs.",
        "outcomes": [
            "Explain the halal requirements that apply to sourcing, ingredients and suppliers",
            "Apply segregation of halal and non-halal items across storage, preparation and service",
            "Verify supplier halal certification and maintain the required records",
            "Follow the outlet's internal halal SOP for utensils, equipment and cleaning",
            "Respond correctly when a suspected halal breach occurs, including escalation and record-keeping",
        ],
        "audience": "All kitchen and service staff in halal-certified or halal-practising outlets, including supervisors responsible for compliance records.",
        "schedule": [
            ("11 Sep 2025", "Adam Food Corner", "Completed"),
            ("23 Mar 2026", "Adam Food Corner", "Completed"),
        ],
    },
    {
        "slug": "kitchen-operations-production",
        "code": "AMFC-KO01",
        "title": "Manage Operations and Production Levels in Kitchen",
        "cat": "kitchen",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 380,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on in your kitchen",
                  "Case study and group discussion"],
        "facilities": [
            "Client's own kitchen line and stations, used for the workflow mapping exercise",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Laptops or tablets for the production forecasting and KPI worksheets",
            "Sample production schedules, mise en place templates and wastage logs",
            "Kitchen scales, portioning tools and station timers for the yield exercise",
        ],
        "lede": "Plan workflows, forecast production and hold your kitchen to measurable performance targets — the operational core of a well-run professional kitchen.",
        "about": "This course equips learners with the essential knowledge and practical skills needed to effectively manage kitchen operations and maintain optimal production levels within a professional culinary environment. Participants explore the fundamentals of kitchen operations planning, covering how to design efficient workflows, organise stations, and implement standard operating procedures that drive productivity and uphold service quality at every stage of service. Moving into production management, learners discover how to forecast food production requirements, adjust outputs in response to shifting demand, and apply the principles of mise en place to support consistent, reliable results. Strategies for optimising the use of labour, equipment and ingredients are examined alongside methods for analysing production data to reduce waste and identify opportunities for greater efficiency. The programme concludes by developing learners' capacity to monitor kitchen performance against established targets, interpret key performance indicators, take corrective action where shortfalls arise, and recognise how effective team communication and coordination are central to sustaining high-quality kitchen operations.",
        "outcomes": [
            "Design and implement kitchen operations plans covering workflow management, station organisation and standard operating procedures",
            "Apply food production forecasting techniques and mise en place principles to set and adjust production levels against operational demand",
            "Optimise the use of labour, equipment and ingredients, analysing production data to reduce waste and improve efficiency",
            "Evaluate kitchen performance against production targets by monitoring key performance indicators",
            "Implement corrective actions and continuous improvement strategies supported by effective team communication",
        ],
        "audience": "Aspiring kitchen supervisors, commis and junior chefs seeking career advancement, and hospitality professionals developing stronger operational capabilities. Suitable for beginner to intermediate learners.",
        "schedule": [
            ("Intake forming", "On-site at your premises", "Enquire"),
        ],
    },
]

# Historical runs (2024-2025 track record), kept for the homepage training record.
PAST_RUNS = [
    ("Food Safety and Hygiene (Internal SOP Training)", "3 Monkeys", 4, "08 Jul 2024", "20–45", "food"),
    ("Food Safety and Hygiene (Internal SOP Training)", "Zamas", 4, "22 Jul 2024", "21–45", "food"),
    ("Workplace Safety & Accident Prevention", "3 Monkeys", 8, "12 Aug 2024", "22–45", "safety"),
    ("Supervisor & Team Leadership", "Zamas", 4, "23 Sep 2024", "23–45", "service"),
    ("Halal Handling & Internal Halal SOP", "Zamas", 8, "07 Oct 2024", "24–45", "halal"),
    ("Beverage Handling", "3 Monkeys", 8, "13 Jan 2025", "25–45", "service"),
    ("Workplace Safety & Accident Prevention", "Adam Food Corner", 8, "24 Feb 2025", "26–45", "safety"),
    ("Food Safety and Hygiene (Internal SOP Training)", "Adam Food Corner", 4, "12 Mar 2025", "27–45", "food"),
    ("Halal Handling & Internal Halal SOP", "Adam Food Corner", 4, "24 Mar 2025", "28–45", "halal"),
    ("Takeaway and Counter Services", "Food Court Stalls (Pro-Bono)", 4, "05 May 2025", "29–45", "service"),
    ("Halal Handling & Internal Halal SOP", "Adam Food Corner", 8, "19 May 2025", "30–45", "halal"),
    ("Workplace Safety & Accident Prevention for the F&B Industry", "Adam Food Corner", 8, "24 Jul 2025", "20–45", "safety"),
    ("Halal Handling & Internal Halal SOP", "Adam Food Corner", 8, "11 Sep 2025", "21–45", "halal"),
    ("Workplace Safety & Accident Prevention for the F&B Industry", "Adam Food Corner", 8, "22 Oct 2025", "22–45", "safety"),
    ("Workplace Safety & Accident Prevention for the F&B Industry", "Adam Food Corner", 8, "08 Jan 2026", "23–45", "safety"),
    ("Halal Handling & Internal Halal SOP", "Adam Food Corner", 8, "23 Mar 2026", "24–45", "halal"),
    ("Workplace Safety & Accident Prevention for the F&B Industry", "Adam Food Corner", 8, "19 May 2026", "25–45", "safety"),
]
