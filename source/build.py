# -*- coding: utf-8 -*-
"""Builds the Resilient Collaborative multi-page site into this folder.
index.html is the artifact's main page (no doctype: the host wraps it); every other page is a full document.
Shared look and behaviour live in site.css and site.js."""
import html, os, shutil
OUT = "public"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
shutil.copytree("../img" if os.path.isdir("../img") else "img", f"{OUT}/img")
for f in ("site.css", "site.js"):
    shutil.copy(f, OUT)
DOMAIN = "resilientcollaborative.com.np"
open(f"{OUT}/CNAME", "w").write(DOMAIN + "\n")
e = html.escape

FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">'
NAV = [("about.html", "About"), ("services.html", "Services"), ("work.html", "Work"), ("people.html", "People")]
EMAIL = "resilientcollaborativenepal@gmail.com"
ADDRESS = "Koteshwar, Kathmandu Metropolitan City, Ward 32, Bagmati Province, Nepal"


def header(active):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site"><div class="wrap nav">
<a class="brand" href="./" aria-label="Resilient Collaborative, home"><svg data-ring aria-hidden="true"></svg><span class="wm">resilient<br>c<span class="dot"></span>llaborative</span></a>
<ul class="links">{links}</ul>
<a class="btn" href="contact.html">Get in touch <span class="arr" aria-hidden="true">→</span></a>
<button class="menu-btn" aria-expanded="false">Menu</button>
</div></header>'''


FOOTER = f'''<footer class="site"><div class="wrap">
<div class="row">
<div><a class="brand" href="./" aria-label="Home"><svg data-ring="light" aria-hidden="true"></svg><span class="wm">resilient<br>c<span class="dot"></span>llaborative</span></a>
<p class="tl">People. Places. Possibilities.<span>For a better tomorrow.</span></p></div>
<nav aria-label="Footer"><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}<li><a href="contact.html">Contact</a></li></ul></nav>
</div>
<small>© 2026 Resilient Collaborative (P) Ltd. · Reg. No. 135445/71/072 · {e(ADDRESS)} · {DOMAIN}</small>
</div></footer>'''

CTA = f'''<section class="cta band"><canvas data-topo='{{"c":"#F4F2EE","a":0.18,"x":0.85,"y":0.3,"n":12,"s":2.2,"acc":-1}}' aria-hidden="true"></canvas>
<div class="wrap inner"><div class="rv"><p class="label" style="margin-bottom:18px">Contact</p><h2>work<br>with us.</h2></div>
<div class="rv"><p>Tell us about the project you have in mind. We reply within two working days.</p>
<p style="margin-top:22px"><a class="btn light" href="contact.html">Contact us <span class="arr" aria-hidden="true">→</span></a></p></div></div></section>'''


ICON = "data:image/svg+xml," + ('<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><g transform=%22translate(50 50) scale(.84) translate(-50 -50)%22 fill=%22none%22 stroke-width=%2222%22>'
        '<circle cx=%2250%22 cy=%2250%22 r=%2239%22 stroke=%22%23151515%22 transform=%22rotate(-84 50 50)%22 stroke-dasharray=%220 40.84 32 8.84 32 8.84 32 8.84 32 8.84 32 8.84%22/>'
        '<circle cx=%2250%22 cy=%2250%22 r=%2239%22 stroke=%22%23B5452B%22 transform=%22translate(3.7 -6.55) rotate(-84 50 50)%22 stroke-dasharray=%2232 213.04%22/></g></svg>')
DESC = "Resilient Collaborative is a planning, design and engineering practice in Kathmandu, Nepal, working with governments, municipalities and development partners."


def page(slug, title, active, body, main=False):
    url = f"https://{DOMAIN}/" + ("" if slug == "index.html" else slug)
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
           f'<title>{e(title)}</title><meta name="description" content="{e(DESC)}"><link rel="canonical" href="{url}"><link rel="icon" href="{ICON}">'
           f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(DESC)}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://{DOMAIN}/img/lake2.jpg">'
           f'{FONT}<link rel="stylesheet" href="site.css"></head><body>{header(active)}<main>{body}</main>{FOOTER}<script src="site.js"></script></body></html>')
    open(f"{OUT}/{slug}", "w").write(doc)


def phead(label, h1, lede, h1_style=""):
    return (f'<section class="phead"><canvas data-topo=\'{{"c":"#B9B4AA","a":0.4,"x":0.86,"y":0.55,"n":12,"s":0.9,"acc":4}}\' aria-hidden="true"></canvas>'
            f'<div class="wrap"><p class="label">{e(label)}</p><h1 style="{h1_style}">{h1}</h1><p class="lede">{lede}</p></div></section>')


# ------------------------------------------------------------------ projects
PROJECTS = [
    dict(slug="work-landslide.html", img="idrmp", tags="risk", sector="Disaster risk",
         title="Landslide and flood mitigation in Birendranagar and Dullu", where="Surkhet and Dailekh · 2021",
         lede="Civil works and bio-engineering to stabilise slopes and riverbanks affected by monsoon landslides and flooding.",
         facts=[("Client", "Tayar Nepal"), ("Programme", "Improved Disaster Risk Management Project"), ("Location", "Birendranagar, Surkhet and Dullu, Dailekh"), ("Period", "June to December 2021"), ("Role", "Sub-consultant, technical experts"), ("Value", "NPR 19.07 million (US$ 144,388)")],
         body=["Birendranagar and Dullu live with recurring landslides and river flooding. Under the Improved Disaster Risk Management Project, Tayar Nepal engaged us to provide the technical experts for mitigation works in both municipalities.",
               "Our design paired civil engineering with bio-engineering. Gabion walls, embankments and drainage hold the slopes and riverbanks in place. Crib walls, brush layering, fascines, palisades, bamboo fencing and planting help the slopes stabilise naturally in the seasons that follow.",
               "Alongside the works we ran training for communities and municipal staff and supported local enterprise, so that local people can maintain the works."],
         did=["Site survey and assessment", "Flood and landslide mitigation design support", "Slope stabilisation and riverbank protection", "Gabion, stone masonry and drainage structures", "Bio-engineering: crib walls, brush layering, fascines, palisades, bamboo fencing and planting", "Construction supervision, quantity checks and quality control", "Community training and enterprise development support"],
         experts=["Urban Planner", "Bio-engineering Expert", "Geotechnical Engineer", "Hydrologist", "Landslide Expert", "Enterprise Development Expert", "Curriculum Development Expert", "Site Engineer"],
         gallery=[]),
    dict(slug="work-energy.html", img="map", contain=True, tags="research", sector="Research and data",
         title="Baseline study of building energy use in Nepal", where="Twelve sites, Terai to Himalaya · 2023",
         lede="Field data on how buildings use energy across four climate zones, collected to inform passive design guidelines.",
         facts=[("Programme", "Building Energy Efficiency in Nepal (BEEN), EU SWITCH-Asia"), ("Coverage", "Twelve sites across four bioclimatic zones"), ("Period", "February to August 2023"), ("Role", "Sub-consultant, technical experts"), ("Value", "NPR 2.98 million (US$ 22,359)")],
         body=["BEEN was a four-year, EU-funded initiative under the SWITCH-Asia Programme to improve energy efficiency in Nepal’s building sector. Before anyone could write guidelines, the project needed to know how buildings in Nepal actually use energy.",
               "We provided the Team Leader, the Statistics Head and the Project Coordinator for the field study. The team trained more than 40 enumerators and surveyed homes, hotels and resorts, and offices from the plains of the Terai to high mountain settlements such as Chame and Muktichhetra.",
               "The data on building design, construction materials and energy use now informs passive design guidelines, technical standards and energy-efficiency tools for the country."],
         did=["Literature review and case studies", "Coordination with partner municipalities", "Training of more than 40 enumerators", "Field data collection", "Cleaning and sorting data by building typology", "Analysis and final report"],
         experts=["Team Leader", "Statistician", "Project and District Coordinator"],
         gallery=[("been1", "Stone house surveyed in a high mountain settlement"), ("been2", "Timber guesthouse surveyed in a mountain settlement")]),
    dict(slug="work-lake.html", img="lake2", tags="public-space", sector="Public space",
         title="Bethauli-Kaparkatti Lake and Park, Butwal", where="Butwal, Rupandehi · 2020",
         lede="A detailed project report to open the lake to the public while protecting its water source and ecology.",
         facts=[("Assignment", "Detailed project report"), ("Location", "Butwal, Rupandehi"), ("Period", "December 2020"), ("Role", "Sub-consultant, technical experts"), ("Value", "NPR 3.5 million (US$ 19,750)")],
         body=["Bethauli-Kaparkatti Lake is one of Butwal’s key natural assets. The brief was to open it to the public while protecting its water source and ecology.",
               "We kept building to a minimum. The design protects the lake’s water source, softens the edges with planting, and adds pedestrian paths, a footbridge and low-level lighting. Every route is accessible.",
               "The result is a public space for boating, fishing, cycling, walking and community events."],
         did=["Landscape planning and design", "Urban design and accessibility planning", "Recreational infrastructure design", "Footbridge design coordination", "Lighting design", "Environmental conservation measures and assessment", "Cost estimate and construction documents"],
         experts=["Urban Planner", "Senior Architect", "Bio-engineering Expert", "Geotechnical Engineer", "Hydrologist", "Site Engineer"],
         gallery=[("lake1", "Lakeside pavilions"), ("lake4", "Footbridge across the lake"), ("lake3", "Planted lake edge")]),
    dict(slug="work-park.html", img="park", contain=True, tags="public-space", sector="Public space",
         title="Shahid Lakhan Park renovation, Dang", where="Dang · 2019",
         lede="A renovation plan for a public park, based on consultation with the people who use it.",
         facts=[("Assignment", "Detailed project report"), ("Location", "Dang"), ("Period", "2019"), ("Role", "Design consultant"), ("Value", "NPR 2.5 million (US$ 16,500)")],
         body=["The park needed better facilities for nearby residents while keeping its trees and open space.",
               "We reviewed the existing master plan and consulted residents, park users and the municipality. Environmental screening came next. The new plan organises the park into activity pockets, among them a play area, a performance space, a café beside a water feature and new public toilets, joined by an accessible loop.",
               "Improved access, lighting and amenities sit alongside the existing trees and lawns."],
         did=["Existing master plan review", "Site survey and assessment", "Stakeholder consultation", "Environmental screening and assessment", "Park, amenity and lighting design", "Accessibility planning", "Cost estimate, BOQ, specifications and tender documents"],
         experts=["Team Leader and Senior Landscape Architect", "Urban Planner", "Landscape Architect", "Architect", "Civil Engineer", "Environmental Specialist", "Social Development Specialist"],
         gallery=[]),
    dict(slug="work-rapti.html", img="rapti", tags="health", sector="Health infrastructure",
         title="Rapti Hospital, Dang: detailed engineering design", where="Dang · 2020 to 2022",
         lede="Design and supervision for a 100-bed hospital in a seismically active region.",
         facts=[("Assignment", "Detailed engineering design and supervision"), ("Location", "Dang"), ("Period", "2020 to 2022"), ("Role", "Design and supervision consultant"), ("Value", "NPR 3.5 million (US$ 23,000)")],
         body=["A hospital in an earthquake-prone region needs to remain operational after a disaster.",
               "We designed architecture and engineering together from the start: a seismic-resistant structure, barrier-free and patient-centred planning, and mechanical, electrical and plumbing services coordinated with both. An environmental assessment and a full tender package followed, and we stayed on to supervise construction."],
         did=["Site survey and soil investigation", "Architectural, structural, electrical and sanitary design", "Environmental assessment", "Cost estimate and BOQ", "Technical specifications and tender documents", "Construction supervision"],
         experts=["Team Leader and Senior Architect", "Architect", "Structural Engineer", "Electrical Engineer", "Sanitary Engineer", "Geotechnical Engineer", "Environmental Specialist", "Survey Engineer", "Quantity Surveyor", "CAD Draftsperson"],
         gallery=[]),
    dict(slug="work-tulsi.html", img="tulsi", tags="health", sector="Health infrastructure",
         title="Tulsi Hospital, Dang: detailed engineering design", where="Dang · 2019 to 2021",
         lede="Design and supervision for our first 100-bed hospital.",
         facts=[("Assignment", "Detailed engineering design and supervision"), ("Location", "Dang"), ("Period", "2019 to 2021"), ("Role", "Design and supervision consultant"), ("Value", "NPR 2.5 million (US$ 16,500)")],
         body=["Tulsi Hospital was our first 100-bed health facility, and the approach we developed here still guides our health infrastructure work.",
               "Architecture and engineering were designed together: a seismic-resistant structural system, barrier-free layouts that follow how patients and staff move, and coordinated services. We prepared the environmental assessment and a complete tender package, then supervised construction."],
         did=["Site survey and soil investigation", "Architectural, structural, electrical and sanitary design", "Environmental assessment", "Cost estimate and BOQ", "Technical specifications and tender documents", "Construction supervision"],
         experts=["Team Leader and Senior Architect", "Architect", "Structural Engineer", "Electrical Engineer", "Sanitary Engineer", "Geotechnical Engineer", "Environmental Specialist", "Survey Engineer", "Quantity Surveyor", "CAD Draftsperson"],
         gallery=[]),
]
ALT = {"idrmp": "Aerial view of slope stabilisation works on a hillside", "map": "Map of Nepal with the survey sites marked",
       "lake2": "Rendering of the lake at dusk with lit paths", "park": "Site plan of the renewed park",
       "rapti": "Rendering of Rapti Hospital at dusk", "tulsi": "Aerial rendering of Tulsi Hospital and its street"}


def card(p, wide=False):
    cls = "card rv" + (" wide" if wide else "") + (" contain" if p.get("contain") else "")
    return (f'<a class="{cls}" href="{p["slug"]}" data-tags="{p["tags"]}"><img src="img/{p["img"]}.jpg" alt="{e(ALT[p["img"]])}" loading="lazy">'
            f'<div class="meta"><span class="sector">{e(p["sector"])}</span><h3>{e(p["title"])}</h3><span class="where">{e(p["where"])}</span></div></a>')


PRACTICES = [
    ("planning", 0, "Planning and urban design",
     ["A plan starts with how people use a place today and what the land will allow, and only then sets out where growth, open space and services should go.",
      "We test options with the people affected before anything is fixed, and we draw plans that municipal staff can read, use and defend long after we have left."],
     ["Master and concept planning", "Strategic land use planning", "Public space, parks and landscape", "Heritage and cultural preservation", "Smart city solutions"],
     ["work-lake.html", "work-park.html"]),
    ("risk", 1, "Disaster risk and resilience",
     ["We treat risk as part of planning from the start. Hazard mapping draws on local knowledge of where water flows and which slopes are unstable.",
      "Where it fits, we pair engineering with nature-based measures such as bio-engineering, and we design public facilities, health facilities above all, to stay open when they are needed most."],
     ["Disaster risk reduction planning", "Landslide and flood mitigation", "Bio-engineering for slopes and riverbanks", "Climate-resilient health facilities", "Resettlement planning"],
     ["work-landslide.html", "work-rapti.html"]),
    ("design", 2, "Design and engineering",
     ["We take projects from concept to construction. Our detailed project reports and engineering designs are written to be built: clear drawings, honest estimates and tender documents a contractor can price.",
      "Architecture, structure and services are designed together rather than handed from desk to desk, and we stay involved on site through supervision."],
     ["Detailed project reports (DPR)", "Architecture, structure, electrical and sanitary design", "Cost estimates, BOQ and specifications", "Tender documents", "Construction supervision and quality control"],
     ["work-rapti.html", "work-tulsi.html"]),
    ("research", 3, "Research, data and economics",
     ["Our recommendations rest on field evidence. Surveys, well-trained enumerators and careful data cleaning give clients data they can present to ministries and funders.",
      "Our research on how communities recover after disasters in Nepal and Sri Lanka feeds directly into this work, and economic analysis shows what each option costs and what it returns."],
     ["Feasibility studies", "Baseline surveys and enumerator training", "Data cleaning, analysis and reporting", "Economic development studies", "Economic impact and cost-benefit assessment"],
     ["work-energy.html"]),
]

APPROACH = [("Context Understanding", "Grounded in people, places and realities."),
            ("Collaborative Design", "Bring diverse knowledge together."),
            ("Practical Implementation", "From plans to action."),
            ("Lasting Impact", "Stronger, more inclusive and resilient futures.")]
VISION = "Places that work for the people who live in them, now and for generations to come."
MISSION = "We plan, design and engineer public places and infrastructure with governments, communities and development partners across Nepal and South Asia. Our plans rest on field evidence and local knowledge. We design them to withstand disasters and a changing climate, and we stay involved until they are built."


def approach_row(label="Our approach"):
    items = "".join(f'<li><span class="num">0{i+1}</span><h3>{e(t).replace(" ", "<br>", 1)}</h3><p>{e(d)}</p></li>' for i, (t, d) in enumerate(APPROACH))
    return f'<div class="split va-row rv"><div><p class="label">{label}</p><span class="tick" aria-hidden="true"></span></div><ol class="approach4">{items}</ol></div>'


def vision_approach(mission=True, more=False):
    m = f'<p class="lede">{e(MISSION)}</p>' if mission else ""
    link = '<p><a class="more" href="about.html">About us <span class="arr" aria-hidden="true">→</span></a></p>' if more else ""
    return (f'<section class="band va"><div class="wrap stack" style="gap:clamp(48px,6vw,88px)">'
            f'<div class="split rv"><div><p class="label">Our vision</p><span class="tick" aria-hidden="true"></span></div>'
            f'<div class="stack"><p class="vision">{e(VISION)}</p>{m}{link}</div></div>'
            f'{approach_row()}</div></section>')


MARQ = ["Urban planning", "Disaster risk reduction", "Detailed project reports", "Landscape and public space", "Resilient health infrastructure", "Bio-engineering", "Baseline research", "Construction supervision"]

TEAM = [("apil", "Apil KC", "Chief Executive Officer and Managing Director", True),
]


def team_cards(link=True):
    out = []
    for pid, name, role, real in TEAM:
        tag = "a" if link else "div"
        href = f' href="people.html#{pid}"' if link else ""
        out.append(f'<{tag} class="person rv" id="{"" if link else pid}"{href}><div class="ph"><span class="ini">{"".join(w[0] for w in name.split())}</span></div>'
                   f'<b>{e(name)}</b><span>{e(role)}</span></{tag}>')
    return "".join(out).replace(' id=""', "")


# ------------------------------------------------------------------ home
rows = "".join(f'<li><a href="services.html#{sid}"><h3>{e(t)}</h3><p>{e(how[0])}</p><span class="arr" aria-hidden="true">→</span></a></li>' for sid, i, t, how, _, _ in PRACTICES)
home = f'''
<section class="hero"><canvas data-topo='{{"c":"#B9B4AA","a":0.45,"x":0.78,"y":0.5,"n":14,"s":0.4,"acc":5}}' aria-hidden="true"></canvas>
<div class="wrap hero-grid"><div>
<p class="label" style="margin-bottom:22px">Planning · Design · Disaster risk · Research</p>
<h1><span class="w"><span>people.</span></span><span class="w"><span>places.</span></span><span class="w"><span>possibilities.</span></span></h1>
<p class="tomorrow">For a better tomorrow.</p>
<p class="lede">Resilient Collaborative is a planning, design and engineering practice in Kathmandu. We work with governments, municipalities and development partners on planning, design, engineering and research for public places and infrastructure.</p>
<div class="ctas"><a class="btn" href="work.html">See our work <span class="arr" aria-hidden="true">→</span></a><a class="btn ghost" href="about.html">About us</a></div>
</div><div class="hero-mark"><svg id="heroRing" viewBox="0 0 100 100" role="img" aria-label="The Resilient Collaborative ring"></svg></div></div></section>
<div class="marquee" aria-hidden="true"><div class="track">{"".join(f"<span>{m}</span>" for m in MARQ*2)}</div></div>

<section class="band white"><div class="wrap split rv"><p class="label">Who we are</p>
<div class="stack"><h2 class="h2">planning, design and engineering, based in Kathmandu.</h2>
<div class="prose"><p>We started in 2014 as a small design studio in Dang, western Nepal. Our work has since grown from single buildings to larger places and systems, including hospitals, public parks, a city lake, landslide mitigation and a national study of building energy use.</p>
<p>Today we bring planners, engineers, environmental and social specialists to one table, so that clients receive one coordinated piece of work.</p></div>
<p><a class="more" href="about.html">Our story <span class="arr" aria-hidden="true">→</span></a></p></div></div>
</section>

<section class="band"><div class="wrap stack"><div class="split rv"><p class="label">What we do</p><h2 class="h2">what we do.</h2></div>
<ul class="rows rv">{rows}</ul></div></section>

<section class="band white"><div class="wrap stack"><div class="split rv"><p class="label">Selected work</p><div class="stack"><h2 class="h2">recent projects.</h2><p><a class="more" href="work.html">All projects <span class="arr" aria-hidden="true">→</span></a></p></div></div>
<div class="grid">{card(PROJECTS[0], True)}{card(PROJECTS[2])}{card(PROJECTS[4])}{card(PROJECTS[1], True)}</div></div></section>

{vision_approach(mission=False, more=True)}
{CTA}'''
page("index.html", "Resilient Collaborative", "", home, main=True)

# ------------------------------------------------------------------ about
about = phead("About", "our <span>story.</span>",
              "We began as an architecture studio and moved, project by project, into planning, disaster risk and research. We still work close to the site and to the people who use it.") + f'''
<section class="band white"><div class="wrap split"><p class="label rv">Our story</p>
<ol class="timeline rv">
<li><span class="yr">2014</span><h3>A design studio in Dang</h3><p>A small architecture practice in western Nepal, making buildings that worked well and fitted their place.</p></li>
<li><span class="yr">2015</span><h3>Incorporated</h3><p>Registered on 27 May 2015 as Ingenious Design Solution Pvt. Ltd.</p></li>
<li><span class="yr">2019 to 2022</span><h3>Hospitals, parks and a lake</h3><p>Two 100-bed hospitals in Dang, and detailed project reports for a public park in Dang and a lake and park in Butwal.</p></li>
<li><span class="yr">2021</span><h3>Landslide and flood mitigation</h3><p>Landslide and flood mitigation in Birendranagar and Dullu, combining civil works with bio-engineering.</p></li>
<li class="mark"><span class="yr">2023</span><h3>A new name and a Kathmandu office</h3><p>We became Resilient Collaborative and moved our registered office to Kathmandu. The same year we fielded the survey team for a national baseline on building energy use.</p></li>
<li><span class="yr">Today</span><h3>Today</h3><p>A multi-disciplinary practice working for governments, municipalities and development partners, with research feeding into planning and engineering.</p></li>
</ol></div></section>

{vision_approach()}

<section class="band"><div class="wrap split"><p class="label rv">Principles</p>
<div class="prose rv">
<p><strong>Plans should still work after the next disaster.</strong> We design with floods and earthquakes in mind, and with the budgets that will be available to maintain what is built.</p>
<p><strong>We work in mixed teams and with local partners.</strong> Engineers hear from social specialists, and communities see drawings before they are final.</p>
<p><strong>We consult before we design.</strong> Ideas are tested with the people who will use the result.</p>
<p><strong>We are open about uncertainty.</strong> Our figures can be traced to their sources, and our advice is independent.</p>
<p><strong>We carry lessons forward.</strong> What we learn on one assignment informs the next.</p>
</div></div></section>
<section class="band white"><div class="wrap split"><p class="label rv">Company</p>
<dl class="dl rv"><dt>Legal name</dt><dd>Resilient Collaborative (P) Ltd.</dd>
<dt>Former name</dt><dd>Ingenious Design Solution Pvt. Ltd., until July 2023</dd>
<dt>Registration</dt><dd>No. 135445/71/072, Office of the Company Registrar, Government of Nepal</dd>
<dt>Registered office</dt><dd>{e(ADDRESS)}</dd></dl></div></section>
{CTA}'''
page("about.html", "About · Resilient Collaborative", "about.html", about)

# ------------------------------------------------------------------ services
TITLE = {p["slug"]: p["title"] for p in PROJECTS}
sections = "".join(
    f'''<article class="practice" id="{sid}"><div class="rv"><svg class="seg" data-seg="{i}" aria-hidden="true"></svg><h2>{e(t)}</h2><div class="prose">{"".join(f"<p>{e(x)}</p>" for x in how)}</div></div>
<div class="rv"><h3>In practice</h3><ul class="ticks">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul><h3>Related work</h3><div class="related">{"".join(f'<a class="chip" href="{r}">{e(TITLE[r])}</a>' for r in rel)}</div></div></article>'''
    for sid, i, t, how, items, rel in PRACTICES)
services = phead("Services", "<span>services.</span>",
                 "Each assignment is different, but our approach is consistent. We start from the place and the people who use it, involve the relevant disciplines early, and deliver plans that can be built and maintained.") + \
    f'<section class="band" style="padding-block:24px 40px"><div class="wrap">{sections}</div></section>' + f'<section class="band white"><div class="wrap">{approach_row()}</div></section>' + CTA
page("services.html", "Services · Resilient Collaborative", "services.html", services)

# ------------------------------------------------------------------ work
FILTERS = [("all", "All work"), ("risk", "Disaster risk"), ("public-space", "Public space"), ("health", "Health infrastructure"), ("research", "Research and data")]
work = phead("Projects", "<span>projects.</span>",
             "Completed assignments for government, municipalities and development programmes. Select a project to read more.") + f'''
<section class="band" style="padding-top:56px"><div class="wrap">
<div class="filters" role="group" aria-label="Filter projects">{"".join(f'<button type="button" class="filter" data-f="{k}" aria-pressed="{str(k=="all").lower()}">{t}</button>' for k, t in FILTERS)}</div>
<div class="grid">{card(PROJECTS[0], True)}{card(PROJECTS[1])}{card(PROJECTS[2])}{card(PROJECTS[3])}{card(PROJECTS[4])}{card(PROJECTS[5], True)}</div>
<p class="note">Assignments completed before July 2023 were delivered under the company’s former name, Ingenious Design Solution Pvt. Ltd. The company and its registration are unchanged.</p>
</div></section>{CTA}'''
page("work.html", "Work · Resilient Collaborative", "work.html", work)

# ------------------------------------------------------------------ project pages
for i, p in enumerate(PROJECTS):
    prev, nxt = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    gal = ("<div class=\"gallery rv\">" + "".join(f'<figure style="margin:0"><img src="img/{k}.jpg" alt="{e(c)}" loading="lazy"><figcaption class="note" style="margin-top:8px">{e(c)}</figcaption></figure>' for k, c in p["gallery"]) + "</div>") if p["gallery"] else ""
    body = phead(f'Work · {p["sector"]}', e(p["title"]), e(p["lede"]), "font-size:clamp(36px,5.4vw,72px);max-width:20ch") + f'''
<div class="pimg{' contain' if p.get('contain') else ''}" style="margin-top:0"><img src="img/{p["img"]}.jpg" alt="{e(ALT[p["img"]])}"></div>
<section class="band" style="padding-top:56px"><div class="wrap stack" style="gap:56px">
<div class="facts rv">{"".join(f'<div><span>{e(k)}</span><b>{e(v)}</b></div>' for k, v in p["facts"])}</div>
<div class="pbody"><div class="prose rv">{"".join(f"<p>{e(x)}</p>" for x in p["body"])}
<h3 class="label" style="margin-top:20px">What we did</h3><ul class="ticks">{"".join(f"<li>{e(x)}</li>" for x in p["did"])}</ul></div>
<aside class="side rv"><div class="box"><h3>Experts mobilised</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in p["experts"])}</ul></div></aside></div>
{gal}
<nav class="pager rv" aria-label="More projects"><a href="{prev["slug"]}"><span>← Previous</span><b>{e(prev["title"])}</b></a><a href="{nxt["slug"]}"><span>Next →</span><b>{e(nxt["title"])}</b></a></nav>
</div></section>{CTA}'''
    page(p["slug"], f'{p["title"]} · Resilient Collaborative', "work.html", body)

# ------------------------------------------------------------------ people
DISC = ["Urban Planner", "Landscape Architect", "Architect", "Structural Engineer", "Civil Engineer", "Geotechnical Engineer", "Electrical Engineer", "Sanitary Engineer", "Hydrologist", "Landslide Expert", "Bio-engineering Expert", "Environmental Specialist", "Social Development Specialist", "Enterprise Development Expert", "Statistician", "Survey Engineer", "Quantity Surveyor", "Site Engineer"]
people = phead("People", "who you will <span>work with.</span>",
               "A core team and a network of specialists we have worked with in the field. Each assignment is staffed with the expertise it requires.") + f'''
<section class="band white" id="apil-profile"><div class="wrap founder">
<div class="portrait rv"><span class="ini">AK</span></div>
<div class="stack rv"><div><h2>Apil KC</h2><p class="role">Chief Executive Officer and Managing Director</p></div>
<div class="prose"><p>Apil leads the firm’s strategy and its work on disaster recovery, resilient infrastructure and urban planning. He is a PhD candidate in Urban and Regional Planning at the University of Michigan’s Taubman College, where he studies how recovery is governed after disasters in Nepal and Sri Lanka.</p>
<p>Alongside the firm, he advises Nepal’s Ministry of Health and Population on climate-resilient health facilities as a Climate Resilient Infrastructure Expert under the SAMARTHA programme. His research has appeared in the International Journal of Disaster Risk Reduction.</p></div>
<p class="notebox">The advisory and research roles above are Apil’s individual experience, separate from the firm’s own assignments.</p></div>
</div></section>
<section class="band white"><div class="wrap split"><p class="label rv">How we build teams</p>
<div class="stack rv"><div class="prose"><p>Our projects need several disciplines at once. For each assignment we bring together the people the work needs, from our core staff and from associates we have worked beside in the field. These are disciplines we have mobilised on completed projects.</p></div>
<div class="chips">{"".join(f'<span class="chip">{d}</span>' for d in DISC)}</div></div></div></section>
<section class="band white"><div class="wrap split"><p class="label rv">Join us</p>
<div class="stack rv"><h2 class="h2">careers.</h2>
<div class="prose"><p>We welcome applications from planners, engineers, environmental and social specialists, and researchers. Send a short note and your CV, and tell us what kind of work interests you.</p></div>
<div class="copy"><code id="mailP">{EMAIL}</code><button class="btn" type="button" data-copy="#mailP">Copy email</button><span class="ok" aria-live="polite"></span></div></div></div></section>{CTA}'''
page("people.html", "People · Resilient Collaborative", "people.html", people)

# ------------------------------------------------------------------ programs
programs = phead("Programs and insights", "programs and <span>insights.</span>",
                 "Talks, trainings and short articles on planning, disaster recovery and research.") + '''
<section class="band"><div class="wrap stack"><div class="split rv"><p class="label">Upcoming</p><h2 class="h2">events.</h2></div>
<ul class="events rv">
<li><span class="d">[Date]</span><div><h3>[Talk or workshop title]</h3><p class="t">[Format] · [Venue], Kathmandu</p></div><span class="tag">Event</span></li>
<li><span class="d">[Date]</span><div><h3>[Training or field program]</h3><p class="t">[Format] · [Location]</p></div><span class="tag">Training</span></li>
</ul></div></section>
<section class="band white"><div class="wrap stack"><div class="split rv"><p class="label">Insights</p><h2 class="h2">insights.</h2></div>
<ul class="events rv">
<li><span class="d">[Month]</span><div><h3>[Article or research brief title]</h3><p class="t">[Short description]</p></div><span class="tag">Insight</span></li>
<li><span class="d">[Month]</span><div><h3>[Article or research brief title]</h3><p class="t">[Short description]</p></div><span class="tag">Insight</span></li>
</ul></div></section>''' + CTA
# page("programs.html", ...) returns when there are real events and articles

# ------------------------------------------------------------------ contact
contact = phead("Contact", "<span>contact.</span>",
                "Tell us about the project you have in mind. We reply to every enquiry within two working days.") + f'''
<section class="band white"><div class="wrap split"><p class="label rv">Reach us</p>
<div class="stack rv">
<dl class="dl"><dt>Email</dt><dd><div class="copy" style="margin:0"><code id="mailC">{EMAIL}</code><button class="btn" type="button" data-copy="#mailC">Copy email</button><span class="ok" aria-live="polite"></span></div></dd>
<dt>Office</dt><dd>{e(ADDRESS)}</dd>
<dt>Website</dt><dd>{DOMAIN}</dd></dl></div></div></section>
<section class="band"><div class="wrap split"><p class="label rv">Before you write</p>
<div class="prose rv"><p>It helps us reply well if your note says where the place is, what decision or problem sits behind the request, and roughly when you need answers. If there is a terms of reference or a request for proposals, attach it.</p>
<p>For partnerships on proposals, tell us the lead firm, the client and the expertise you are looking for.</p></div></div></section>'''
page("contact.html", "Contact · Resilient Collaborative", "contact.html", contact)
pages = sorted(f for f in os.listdir(OUT) if f.endswith(".html"))
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'<url><loc>https://{DOMAIN}/{"" if p == "index.html" else p}</loc></url>\n' for p in pages) + "</urlset>\n")
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: https://{DOMAIN}/sitemap.xml\n")
print("built", len(pages), "pages into", OUT)
