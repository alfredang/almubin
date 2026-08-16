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
    "email": "admin@almubinfctraining.com.sg",
    "tel_display": "+65 9138 8967",
    "tel_href": "+6591388967",
    # Training team mobile. Digits only, country code first, no "+" -- wa.me link.
    "whatsapp": "6591388967",
    "manager": "Nabisah Begum Binte MD Ibrahim",
    "manager_title": "Training Manager",
    "address_l1": "18 Sin Ming Lane #07-29",
    "address_l2": "Midview City, Singapore 573960",
    # Kept separate from address_l2 so the JSON-LD PostalAddress stays accurate.
    "postal_code": "573960",
}

# Google review link shown on each course page.
# TODO(client): replace with the Google Business Profile "write a review" deep link
# once the profile's Place ID is known -- that form is
#   https://search.google.com/local/writereview?placeid=<PLACE_ID>
# and opens the review dialog directly. The search URL below is a stand-in that
# lands on the business listing rather than the review box.
GOOGLE_REVIEW_URL = ("https://www.google.com/search?q=Al+Mubin+Food+Corner"
                     "+18+Sin+Ming+Lane+Midview+City+Singapore")

# Trainer profiles. Source: the trainer profile PDFs filed under
#   course_application/ATO Supporting Document/5. SOP/
# These also satisfy the SWDA disclosure requirement to publish the names of
# the trainers. Do not embellish -- every claim below traces to those profiles.
TRAINERS = [
    {
        "name": "Kasmani Bin Dollah",
        "initials": "KD",
        "title": "Adult Educator | Professional Trainer | Consultant",
        # Short profile -- the version shown on the site. The longer "bio"
        # below is retained as the source record behind it.
        "summary": (
            "An adult educator and professional trainer with nearly three decades of "
            "experience across training, workplace operations and professional "
            "development. An early career in the Singapore Police Force gave him a "
            "strong grounding in operational discipline, workplace safety, risk "
            "awareness and accident prevention — which he brings to workplace-based "
            "training through real scenarios and hands-on discussion."
        ),
        "bio": [
            "Kasmani Bin Dollah is an experienced adult educator, professional trainer and "
            "consultant with nearly three decades of professional experience spanning training, "
            "technology, workplace operations, leadership and professional development.",

            "With an early career in the Singapore Police Force, Kasmani developed a strong "
            "foundation in operational discipline, workplace and public safety, risk awareness, "
            "accident prevention, incident management and adherence to established procedures. "
            "These experiences have contributed to his practical approach when facilitating "
            "workplace-based training.",

            "Over the years, Kasmani has transitioned into adult education and professional "
            "training, designing and delivering programmes for learners from diverse backgrounds. "
            "His training experience covers workplace safety and accident prevention, operational "
            "procedures and SOP awareness, Halal handling and internal Halal SOP practices, as "
            "well as digital technology, AI, e-commerce and professional development.",

            "As a trainer, Kasmani adopts a practical and learner-centred approach, using "
            "workplace scenarios, real-world examples and interactive discussions to help adult "
            "learners understand how concepts can be applied in their day-to-day work.",
        ],
        "expertise_label": "Areas of Training Expertise",
        "expertise": [
            "Workplace Safety &amp; Accident Prevention for the F&amp;B Industry",
            "Halal Handling &amp; Internal Halal SOP",
            "Digital Technology &amp; Workplace Productivity",
            "AI &amp; Prompt Engineering",
            "E-Commerce &amp; Digital Marketing",
            "Leadership &amp; Professional Development",
        ],
    },
    {
        "name": "Koh Leong Sim (Sam Koh)",
        "initials": "SK",
        "title": "Adult Educator | WSQ Trainer | Learning &amp; Development Specialist",
        "summary": (
            "An ACTA-certified adult educator with over 15 years in training, curriculum "
            "development and workforce capability building. He holds a WSQ Diploma in "
            "Design and Development of Learning for Performance and the WSQ competency "
            "in Food and Beverage Safety and Hygiene, and has held training roles with "
            "the Land Transport Authority, Ministry of Manpower, People's Association "
            "and the Institute of Technical Education."
        ),
        "bio": [
            "Koh Leong Sim (Sam Koh) is an experienced Adult Educator and Learning &amp; "
            "Development Specialist with over 15 years of experience in training, curriculum "
            "development and workforce capability building across public and private sector "
            "organisations in Singapore.",

            "An ACTA-certified trainer, Sam also holds a WSQ Diploma in Design and Development "
            "of Learning for Performance (DDDLP), providing him with a strong foundation in adult "
            "learning, competency-based training, curriculum development and assessment.",

            "Sam has attained the WSQ competency Follow Food and Beverage Safety and Hygiene "
            "Policies and Procedures, strengthening his knowledge of safety, hygiene and "
            "operational procedures within the F&amp;B environment. His professional background "
            "includes leadership and training roles with the Land Transport Authority, Ministry "
            "of Manpower, People's Association and Institute of Technical Education.",

            "Known for his practical and learner-centred facilitation style, Sam combines "
            "real-world operational experience with structured adult-learning methodologies to "
            "help learners translate knowledge into practical workplace application.",
        ],
        "expertise_label": "Relevant Training &amp; Professional Expertise",
        "expertise": [
            "Workplace Safety &amp; Accident Prevention for the F&amp;B Industry",
            "Food &amp; Beverage Safety and Hygiene Policies &amp; Procedures",
            "Workplace Safety, Compliance &amp; SOP Implementation",
            "Crisis Management &amp; Business Continuity",
            "Service Leadership &amp; Workplace Communication",
            "Digital Transformation &amp; Artificial Intelligence",
            "Curriculum Development &amp; WSQ Training",
        ],
    },
]

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

# Per-course product images, keyed by slug. Several courses share a category
# (three are "service"), so the photo cannot be derived from `cat` alone --
# without these they would all show the same picture. A course with no entry
# here falls back to PHOTO[cat]. Every URL below was verified HTTP 200 and the
# image was opened and checked for subject matter before being added.
# NOTE: prefer free-tier images.unsplash.com URLs. Some plus.unsplash.com
# ("Unsplash+") photos are served to browsers with a repeating "Unsplash+"
# watermark even though a direct curl of the same URL comes back clean -- so a
# 200 check is NOT enough. Always open the page in a browser and look at the
# image before committing a plus.unsplash.com URL.
COURSE_PHOTO = {
    # chef in uniform prepping vegetables in a commercial kitchen
    "food-safety-hygiene":
        "https://images.unsplash.com/photo-1574966740793-953ad374e8fe",
    # uniformed kitchen brigade working a service line
    "supervisor-team-leadership":
        "https://images.unsplash.com/photo-1776142519748-2b897acaecd7",
    # staff preparing drinks behind a beverage counter
    "beverage-handling":
        "https://images.unsplash.com/photo-1513663580958-665b7ef55d1b",
    # packed takeaway meal trays lined up in a production kitchen
    "takeaway-counter-services":
        "https://images.unsplash.com/photo-1675647699232-76b8f533b006",
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
    {
        "slug": "food-safety-hygiene",
        "code": "AMFC-FS01",
        "title": "Food Safety and Hygiene (Internal SOP Training)",
        "cat": "food",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 280,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on in your kitchen"],
        "facilities": [
            "Client's own preparation, storage and service areas, walked as part of the session",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Calibrated probe thermometers and chiller/freezer logs for the temperature checks",
            "Handwashing station, sanitiser and colour-coded cleaning cloths for the hygiene drill",
            "The outlet's own internal food safety SOP and record templates",
        ],
        "lede": "Keep food safe from delivery to service — personal hygiene, temperature control, storage and cleaning — run against your own internal SOP.",
        "about": "Most food safety failures are ordinary lapses repeated under pressure: a probe that is never calibrated, a chiller that is never logged, a cloth that wipes both the board and the bench. This full-day course works through the food safety chain exactly as it runs in your own premises — receiving, storage, preparation, cooking, holding and service — and ties each step back to your outlet's internal SOP. Learners practise the checks that matter most in a busy kitchen: personal hygiene and handwashing discipline, temperature control and the records that evidence it, separation of raw and ready-to-eat foods, stock rotation, and the cleaning and sanitising routine. The session closes on what to do when something is out of specification, who to tell, and what to write down.",
        "outcomes": [
            "Apply personal hygiene and handwashing standards required of a food handler",
            "Control time and temperature across receiving, storage, cooking, holding and service",
            "Separate raw and ready-to-eat foods to prevent cross-contamination",
            "Apply stock rotation, labelling and date-marking in line with the outlet's SOP",
            "Carry out the cleaning and sanitising routine, and complete the supporting records",
            "Respond correctly when food is out of specification, including escalation and record-keeping",
        ],
        "audience": "All food handlers, kitchen crew and service staff, including supervisors responsible for food safety records.",
        "schedule": [
            ("08 Jul 2024", "3 Monkeys", "Completed"),
            ("22 Jul 2024", "Zamas", "Completed"),
            ("12 Mar 2025", "Adam Food Corner", "Completed"),
            ("Intake forming", "On-site at your premises", "Enquire"),
        ],
    },
    {
        "slug": "supervisor-team-leadership",
        "code": "AMFC-SL01",
        "title": "Supervisor & Team Leadership",
        "cat": "service",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 380,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Role-play and group discussion",
                  "Case study"],
        "facilities": [
            "Client's own outlet or a meeting space on site for the discussion segments",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Role-play scenario cards drawn from real F&B shift situations",
            "Sample duty rosters, briefing templates and performance record forms",
        ],
        "lede": "Run a shift, brief a team and handle the difficult conversations — practical supervisory skills for F&B floor and kitchen leaders.",
        "about": "Most F&B supervisors are promoted for being good at the work, not for being trained to lead it. This full-day course fills that gap with the everyday skills a shift leader actually needs: planning and briefing a shift, allocating work across a mixed team, giving instructions that survive a busy service, and holding people to standard without losing them. Learners practise the conversations supervisors avoid — correcting a repeat mistake, handling a complaint in front of customers, resolving friction between crew members — through role-play built on situations from their own outlets. The course also covers the supervisor's compliance role: enforcing hygiene, halal and safety standards on the floor, and keeping the records that show it was done.",
        "outcomes": [
            "Plan and brief a shift, allocating work across the team against the day's demand",
            "Give clear instructions and delegate effectively during a busy service",
            "Give feedback, correct performance and handle difficult conversations constructively",
            "Resolve conflict within the team and de-escalate customer complaints",
            "Motivate and develop crew members, including new and part-time staff",
            "Uphold hygiene, halal and safety standards on the floor and maintain the supporting records",
        ],
        "audience": "Supervisors, team leaders, senior crew and anyone stepping up into a shift-leading role in an F&B outlet.",
        "schedule": [
            ("23 Sep 2024", "Zamas", "Completed"),
            ("Intake forming", "On-site at your premises", "Enquire"),
        ],
    },
    {
        "slug": "beverage-handling",
        "code": "AMFC-BH01",
        "title": "Beverage Handling",
        "cat": "service",
        "hours": 8,
        "duration": "8 hours (1 day)",
        "fee": 280,
        "funding_validity": "1 Jan 2026 – 31 Dec 2027",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on at your beverage station"],
        "facilities": [
            "Client's own beverage counter, station and equipment, used as the training floor",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Blenders, dispensers, shakers, jiggers and ice wells for the preparation practice",
            "Measuring jugs, portioning scoops and recipe cards for the consistency exercise",
            "Cleaning and sanitising materials for the equipment hygiene routine",
        ],
        "lede": "Prepare, serve and store beverages safely and consistently — hygiene, recipe accuracy and equipment care at a busy counter.",
        "about": "Beverages are prepared fast, handled by many hands and often overlooked in food safety training — yet ice, dispensers, blenders and syrups are all common contamination points. This full-day course covers the beverage operation end to end as it runs at your own counter: receiving and storing ingredients, ice handling, preparing hot and cold drinks to a consistent recipe, and serving at speed without cutting hygiene corners. Learners practise portioning and recipe accuracy so that the same drink tastes the same on every shift, and work through the cleaning and sanitising schedule for each piece of equipment — the step most often skipped when the queue is long. Halal considerations for ingredients, syrups and shared equipment are built into the session.",
        "outcomes": [
            "Store and handle beverage ingredients, ice and garnishes hygienically",
            "Prepare hot and cold beverages to a consistent recipe and portion standard",
            "Operate and clean beverage equipment safely, including blenders and dispensers",
            "Apply the cleaning and sanitising schedule for the beverage station",
            "Verify that ingredients and shared equipment meet the outlet's halal requirements",
            "Serve beverages at speed while maintaining hygiene and presentation standards",
        ],
        "audience": "Beverage crew, counter staff and kitchen crew who prepare or serve drinks, including new hires and part-timers.",
        "schedule": [
            ("13 Jan 2025", "3 Monkeys", "Completed"),
            ("Intake forming", "On-site at your premises", "Enquire"),
        ],
    },
    {
        "slug": "takeaway-counter-services",
        "code": "AMFC-TC01",
        "title": "Takeaway and Counter Services",
        "cat": "service",
        "hours": 8,
        "duration": "8 hours (1 day)",
        # Pro-bono: delivered free of charge to food court stalls. fee=0 renders as
        # "Free (Pro-Bono)" rather than a dollar amount.
        "fee": 0,
        "pro_bono": True,
        "funding_validity": "Not applicable — delivered pro-bono",
        "modes": ["Classroom / on-site facilitated", "Practical hands-on at your counter"],
        "facilities": [
            "Client's own service counter and takeaway station, used as the training floor",
            "Portable projector, screen and laptop brought on site for the theory segment",
            "Flip chart, whiteboard and printed learner guides for each participant",
            "Takeaway containers, lids, bags and labels for the packing practice",
            "Sample order tickets and delivery-platform labels for the accuracy exercise",
            "Handwashing station, sanitiser and glove stock for the hygiene segment",
        ],
        "lede": "Serve, pack and hand over takeaway orders accurately and hygienically — counter service, packing standards and queue handling.",
        "about": "Takeaway and counter service is where most customers actually meet the business, and where mistakes are most visible: the wrong order, a leaking container, a cold meal, a queue that stops moving. This full-day course is delivered pro-bono to food court stalls and small operators, and covers the counter operation end to end at your own premises. Learners work on order taking and accuracy, packing standards that keep food at temperature and intact in transit, correct labelling for both walk-in and delivery-platform orders, and hygienic handling at the point of handover. The session also covers the customer-facing side — greeting, handling a queue under pressure, and dealing with a complaint without escalating it — plus the halal segregation that packing and shared utensils must respect.",
        "outcomes": [
            "Take and confirm orders accurately, including delivery-platform orders",
            "Pack takeaway orders to keep food at temperature, intact and correctly separated",
            "Label orders correctly, including allergen, halal and delivery information",
            "Handle food hygienically at the counter and point of handover",
            "Manage a queue under pressure while maintaining service standards",
            "Handle customer complaints and order errors calmly and correctly",
        ],
        "audience": "Counter and takeaway crew at food court stalls, kiosks and small outlets, including part-time and new service staff.",
        "schedule": [
            ("05 May 2025", "Food Court Stalls (Pro-Bono)", "Completed"),
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
