"""Generates the static pages. Edit content below, then run: python3 build.py"""
NAV=[("index.html","Home"),("about.html","About"),("conference.html","Conference"),("committees.html","Committees"),("past.html","Past Conferences"),("members.html","Member Clubs"),("resources.html","Resources"),("news.html","News"),("contact.html","Contact")]
# Past conferences, newest first: (slug, short name, dates, venue)
PAST=[("vsph-2026","MUNCUS x VSPH 2026","Oct 4–6, 2026","Vanke School Pudong"),
("wlsa-2026","MUNCUS x WLSA 2026","Aug 18–20, 2026","WLSA Shanghai Academy"),
("shph-2026","MUNCUS x SHPH 2026","Jun 27–29, 2026","Shanghai Pinghe School"),
("skfls-2026","MUNCUS x SKFLS 2026","Feb 25–27, 2026","Shanghai Koller Foreign Language School"),
("wlsa-2025","MUNCUS x WLSA 2025","Aug 15–17, 2025","WLSA Shanghai Academy"),
("vsph-2025","MUNCUS x VSPH 2025","Aug 5–7, 2025","Vanke School Pudong"),
("shph-2025","MUNCUS x SHPH 2025","Jun 21–22, 2025","Shanghai Pinghe School"),
("ypbs-2025","MUNCUS x YPBS 2025","Jan 18–19, 2025","Shanghai Yangpu Bilingual School")]
# Top-level menu groups: (label, landing page, [(page, label), ...])
MENU=[("About","about.html",[("about.html","About MUNCUS"),("members.html","Member Clubs"),("news.html","News"),("contact.html","Contact")]),
("Conference","conference.html",[("conference.html","Overview"),("committees.html","Committees"),("resources.html","Delegate Resources")]),
("Past Conferences","past.html",None)]
def page(fn,title,body,desc="Model United Nations Club Union of Shanghai",theme=""):
    items=[]
    for label,land,subs in MENU:
        if subs is None: subs=[(f"past-{p[0]}.html",p[1]) for p in PAST]
        on=fn==land or any(fn==h for h,_ in subs)
        sub="".join(f'<li><a href="{h}">{t}</a></li>' for h,t in subs)
        items.append(f'<li class="dropdown"><a href="{land}"{" class=\"active\"" if on else ""}>{label}<span class="caret"></span></a><ul class="sub">{sub}</ul></li>')
    nav="".join(items)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | MUNCUS</title><meta name="description" content="{desc}">
<link rel="canonical" href="https://muncus.org/{"" if fn=="index.html" else fn}"><link rel="icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Montserrat:wght@700;800&family=Noto+Sans+SC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css"></head><body{f' class="theme-{theme}"' if theme else ""}>
<header class="site"><div class="container"><a class="brand" href="index.html"><img src="assets/img/emblem.png" alt="MUNCUS emblem"><span><b>MUNCUS</b><small>上海模拟联合国社团联盟</small></span></a>
<button class="burger" aria-label="Menu">☰</button><nav class="main"><ul>{nav}<li><a class="cta" href="register.html">Register</a></li></ul></nav></div></header>
<main>{body}</main>
<footer class="site"><div class="container"><div class="grid g4">
<div><img src="assets/img/emblem.png" alt="" style="height:60px;filter:brightness(0) invert(1);margin-bottom:12px"><p>Connecting Model UN clubs across Shanghai since 2024.</p></div>
<div><h4>Explore</h4><ul><li><a href="about.html">About Us</a></li><li><a href="conference.html">Conference</a></li><li><a href="committees.html">Committees</a></li><li><a href="members.html">Member Clubs</a></li></ul></div>
<div><h4>Participate</h4><ul><li><a href="register.html">Register</a></li><li><a href="resources.html">Delegate Resources</a></li><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Connect</h4><ul><li><a href="mailto:info@muncus.org">info@muncus.org</a></li><li>WeChat: MUNCUS</li><li><a href="https://www.instagram.com/muncus_off/" target="_blank" rel="noopener">Instagram: @muncus_off</a></li><li>Shanghai, China</li></ul></div>
</div><div class="foot-bottom">© <span data-year></span> MUNCUS · Model United Nations Club Union of Shanghai · muncus.org</div></div></footer>
<script src="assets/js/main.js"></script></body></html>'''
def hero(t,s): return f'<section class="page-hero"><div class="container"><h1>{t}</h1><p>{s}</p></div></section>'
P={}
P["index.html"]=("Home",'''
<section class="hero"><div class="container"><div class="zh">上海模拟联合国社团联盟</div><h1>MUNCUS</h1>
<p>The Model United Nations Club Union of Shanghai — uniting student diplomats across the city to debate, collaborate and lead.</p>
<a class="btn btn-primary" href="register.html">Register for MUNCUS [YEAR]</a><a class="btn btn-ghost" href="about.html">Learn More</a></div></section>
<div class="stats"><div class="container grid g4"><div><b>[XX]</b>Member Clubs</div><div><b>[XXX]</b>Delegates</div><div><b>[XX]</b>Committees</div><div><b>[XX]</b>Years</div></div></div>
<section><div class="container split"><div><div class="eyebrow">Welcome</div><h2>A Union of Shanghai's MUN Community</h2>
<p>[Welcome message / mission summary placeholder. Describe who MUNCUS is, how it brings together Model UN clubs from schools across Shanghai, and what makes it unique.]</p>
<a class="btn btn-blue" href="about.html">About MUNCUS</a></div><div class="ph">[Photo: conference opening ceremony]</div></div></section>
<section class="soft"><div class="container"><div class="eyebrow">Get Involved</div><h2>Explore MUNCUS</h2><div class="grid g3" style="margin-top:28px">
<div class="card"><span class="tag">Conference</span><h3>Annual Conference</h3><p>[Dates & venue placeholder] — our flagship conference for delegates across Shanghai.</p><a href="conference.html">Conference details →</a></div>
<div class="card"><span class="tag">Committees</span><h3>Committees</h3><p>From General Assembly bodies to crisis committees, explore this year's topics.</p><a href="committees.html">View committees →</a></div>
<div class="card"><span class="tag">Community</span><h3>Member Clubs</h3><p>Meet the school MUN clubs that make up the union, and learn how to join.</p><a href="members.html">See members →</a></div>
</div></div></section>
<section><div class="container"><div class="eyebrow">Latest</div><h2>News & Announcements</h2><div class="grid g3" style="margin-top:28px">
<div class="card"><span class="tag">[Date]</span><h3>[Announcement title]</h3><p>[Short summary of the announcement.]</p></div>
<div class="card"><span class="tag">[Date]</span><h3>[Announcement title]</h3><p>[Short summary of the announcement.]</p></div>
<div class="card"><span class="tag">[Date]</span><h3>[Announcement title]</h3><p>[Short summary of the announcement.]</p></div></div></div></section>
<section class="cta-band"><div class="container"><h2>Ready to Take the Floor?</h2><p>Registration for MUNCUS [YEAR] is [opening soon / open now].</p><a class="btn btn-primary" href="register.html">Register Now</a></div></section>''')
P["about.html"]=("About",hero("About MUNCUS","Who we are, what we stand for, and the people who lead us.")+'''
<section><div class="container split"><div><div class="eyebrow">Our Mission</div><h2>Mission</h2><p>[Mission statement placeholder.]</p><h3>Vision</h3><p>[Vision placeholder.]</p></div><div class="ph">[Photo]</div></div></section>
<section class="soft"><div class="container"><div class="eyebrow">History</div><h2>Our Story</h2><div class="timeline" style="margin-top:24px">
<div><b>[Year]</b> — [MUNCUS founded …]</div><div><b>[Year]</b> — [First annual conference …]</div><div><b>[Year]</b> — [Milestone …]</div></div></div></section>
<section><div class="container"><div class="eyebrow">Leadership</div><h2>Secretariat</h2><div class="grid secretariat" style="margin-top:28px">
'''+"".join(f'<div class="card"><div class="ph" style="min-height:180px">[Photo]</div><h3 style="margin-top:14px">[Name]</h3><p>{r}<br><small>[School]</small></p></div>' for r in ["Secretary-General","Deputy Secretary-General","Director of Academics","Director of Operations"])+'''</div></div></section>''')
P["conference.html"]=("Conference",hero("MUNCUS [YEAR] Conference","Everything delegates, advisors and schools need to know.")+'''
<section><div class="container grid g3"><div class="card"><span class="tag">When</span><h3>[Dates]</h3><p>[Day 1 – Day 3]</p></div><div class="card"><span class="tag">Where</span><h3>[Venue]</h3><p>[Address, Shanghai]</p></div><div class="card"><span class="tag">Fees</span><h3>[Fee]</h3><p>[Delegate / school fee details]</p></div></div></section>
<section class="soft"><div class="container"><h2>Schedule</h2><div class="grid g3" style="margin-top:24px">
'''+"".join(f'<div class="card"><h3>Day {d}</h3><p>[Time] — [Session]<br>[Time] — [Session]<br>[Time] — [Session]</p></div>' for d in (1,2,3))+'''</div></div></section>
<section><div class="container"><h2>Key Dates</h2><div class="timeline" style="margin-top:20px"><div><b>[Date]</b> — Registration opens</div><div><b>[Date]</b> — Country assignments released</div><div><b>[Date]</b> — Position papers due</div><div><b>[Date]</b> — Conference</div></div></div></section>''')
P["committees.html"]=("Committees",hero("Committees","Explore this year's committees and topics. Background guides will be posted here.")+'''
<section><div class="container"><div class="grid g3">'''+"".join(f'<div class="card"><span class="tag">{c}</span><h3>[Committee Name]</h3><p><b>Topic:</b> [Topic]<br><b>Chair:</b> [Name]</p><a href="#">Background Guide (coming soon) →</a></div>' for c in ["General Assembly"]*2+["Specialized Agency"]*2+["Crisis"]*2)+'''</div></div></section>''')
P["members.html"]=("Member Clubs",hero("Member Clubs","The school Model UN clubs that make up the union.")+'''
<section><div class="container"><div class="grid g4">'''+"".join('<div class="card" style="text-align:center"><div class="ph" style="min-height:120px">[Club logo]</div><h3 style="margin-top:12px;font-size:1.05rem">[School MUN Club]</h3></div>' for _ in range(8))+'''</div></div></section>
<section class="cta-band"><div class="container"><h2>Join the Union</h2><p>[How a school club can become a MUNCUS member.]</p><a class="btn btn-primary" href="contact.html">Apply for Membership</a></div></section>''')
P["resources.html"]=("Resources",hero("Delegate Resources","Guides and documents to help you prepare.")+'''
<section><div class="container grid g3">'''+"".join(f'<div class="card"><h3>{t}</h3><p>[Description placeholder]</p><a href="#">Download →</a></div>' for t in ["Rules of Procedure","Position Paper Guide","Beginner's Guide to MUN","Dress Code & Conduct","Advisor Handbook","Awards Policy"])+'''</div></section>''')
P["news.html"]=("News",hero("News","Announcements and updates from MUNCUS.")+'''
<section><div class="container grid g3">'''+"".join('<div class="card"><div class="ph" style="min-height:160px">[Image]</div><span class="tag" style="margin-top:14px">[Date]</span><h3>[Article title]</h3><p>[Summary]</p></div>' for _ in range(6))+'''</div></section>''')
P["register.html"]=("Register",hero("Registration","Register your delegation for MUNCUS [YEAR].")+'''
<section><div class="container" style="max-width:720px"><div class="note">Placeholder form — not yet connected to a backend. Registration details coming soon.</div>
<form><div class="field"><label>School / Club</label><input></div><div class="field"><label>Head Delegate / Advisor Name</label><input></div><div class="field"><label>Email</label><input type="email"></div>
<div class="field"><label>Number of Delegates</label><input type="number" min="1"></div><div class="field"><label>Registration Type</label><select><option>Delegation</option><option>Individual Delegate</option></select></div>
<button class="btn btn-blue" type="button">Submit (coming soon)</button></form></div></section>''')
P["contact.html"]=("Contact",hero("Contact Us","Questions about the conference or membership? Get in touch.")+'''
<section><div class="container split"><div><h2>Reach the Secretariat</h2><p><b>Email:</b> <a href="mailto:info@muncus.org">info@muncus.org</a><br><b>WeChat:</b> MUNCUS<br><b>Instagram:</b> <a href="https://www.instagram.com/muncus_off/" target="_blank" rel="noopener">@muncus_off</a><br><b>Location:</b> Shanghai, China</p></div>
<form><div class="field"><label>Name</label><input></div><div class="field"><label>Email</label><input type="email"></div><div class="field"><label>Message</label><textarea rows="5"></textarea></div><a class="btn btn-blue" href="mailto:info@muncus.org">Send via Email</a></form></div></section>''')
P["past.html"]=("Past Conferences",hero("Past Conferences","A look back at every MUNCUS conference.")+'<section><div class="container grid g3">'+"".join(f'<a class="card" style="text-decoration:none;color:inherit" href="past-{p[0]}.html"><div class="ph" style="min-height:160px">[Cover photo]</div><span class="tag" style="margin-top:14px">{p[2]}</span><h3>{p[1]}</h3><p>{p[3]}</p><span style="color:var(--blue-dark)">View conference →</span></a>' for p in PAST)+'</div></section>')
from conferences import CONF
SEC=["Permanent Secretary-General","Secretary-General","Deputy Secretary-General","Deputy Secretary-General","Director of Academics","Director of Operations","Director of Logistics","Director of Media"]
THEMED=("vsph",)
def esc(x): return x.replace("&","&amp;").replace("<","&lt;")
def person(r,n,sch="",ph=None):
    if ph: return f'<figure class="poster"><img src="{ph}" alt="{n}, {r}, {sch}" loading="lazy"></figure>'
    av=f'<img class="avatar" src="{ph}" alt="{n}">' if ph else f'<div class="ph avatar">{"[Photo]" if n.startswith("[") else "".join(w[0] for w in n.split()[:2])}</div>'
    return f'<div class="card person">{av}<h3>{n}</h3><p>{r}</p>{f"<small>{sch}</small>" if sch else ""}</div>'
def comm(m):
    ads="".join(f"<li>{n}<small>{sch}</small></li>" for n,sch in m.get("ads",[]))
    d=m["director"]
    return (f'<div class="card committee"><span class="tag">{m["abbr"]}</span><h3>{m["name"]}</h3><p><b>Topic:</b> {m["topic"]}</p>'
            f'<p class="muted">{m.get("desc") or "[Topic description]"}</p><div class="staff"><div><b>Director</b><ul><li>{d[0]}<small>{d[1]}</small></li></ul></div>'
            + (f'<div><b>Assistant Directors</b><ul>{ads}</ul></div>' if ads else "") + '</div></div>')
for slug,name,date,venue in PAST:
    c=CONF.get(slug,{})
    theme=slug.split("-")[0] if slug.split("-")[0] in THEMED else ""
    psg=c.get("psg",{})
    photo=f'<img class="psg" src="{psg["photo"]}" alt="{psg["name"]}">' if psg.get("photo") else '<div class="ph psg">[Large photo: Permanent Secretary-General]</div>'
    letter="".join(f"<p>{esc(p)}</p>" for p in c.get("letter",["Dear Delegates,","[Letter paragraph 1]","[Letter paragraph 2]","[Letter paragraph 3]"]))
    sign=c.get("signoff","Sincerely,<br><b>[Name]</b><br>Permanent Secretary-General")
    badges="".join(f'<img src="{x}" alt="">' for x in c.get("hero_images",[]))
    secr=c.get("secretariat",[(r,"[Name]") for r in SEC])
    comms=c.get("committees",[dict(abbr="[ABBR]",name="[Committee Full Name]",topic="[Topic]",director=("[Name]","[School]"),ads=[])]*3)
    awards=c.get("awards",[("[ABBR]",a,"[Country / Role]","[Name]","[School]") for a in ("Best Delegate","Outstanding Delegate","Honorable Mention")])
    def ctitle(cm):
        m=next((m for m in comms if m["abbr"]==cm),None)
        if not m: return cm
        return f'{m["abbr"]}: {m["name"]}' if m["abbr"]=="Ad Hoc" else f'{m["name"]} ({m["abbr"]})'
    arows=""
    for cm in dict.fromkeys(a[0] for a in awards):
        arows+=f'<tr class="group"><th colspan="4">{ctitle(cm)}</th></tr>'+"".join(f'<tr><td>{aw}</td><td>{role}</td><td><b>{n}</b></td><td>{sch}</td></tr>' for c2,aw,role,n,sch in awards if c2==cm)
    aph=c.get("award_photos",[])
    award_car=('<div class="carousel photo-car" data-interval="3000"><div class="track">'+"".join(f'<div class="slide"><img src="{x}" alt="{name} award recipients and dais" loading="lazy"></div>' for x in aph)+'</div><button class="prev" aria-label="Previous">‹</button><button class="next" aria-label="Next">›</button><div class="dots"></div></div>') if aph else ''
    slides="".join(f'<div class="slide ph">[Highlight photo {i}]</div>' for i in range(1,7))
    b=(f'<section class="page-hero conf-hero"><div class="container"><div><h1>{name}</h1><p>{date} · {venue}</p></div><div class="hero-badges">{badges}</div></div></section>'
       f'<section><div class="container split letter">{photo}<div><h2>Welcome to {name}</h2>{letter}<p class="sign">{sign}</p></div></div></section>'
       '<section class="soft"><div class="container"><h2>Secretariat</h2><div class="grid secretariat" style="margin-top:28px">'+"".join(person(*p) for p in secr)+'</div></div></section>'
       '<section><div class="container"><h2>Committees</h2><div class="grid g3" style="margin-top:28px">'+"".join(comm(m) for m in comms)+'</div></div></section>'
       f'<section class="soft"><div class="container"><h2>Photo Highlights</h2><div class="carousel"><div class="track">{slides}</div><button class="prev" aria-label="Previous">‹</button><button class="next" aria-label="Next">›</button><div class="dots"></div></div></div></section>'
       '<section><div class="container wide"><h2>Awards</h2><div class="awards-layout'+(' has-photos' if aph else '')+'"><div class="table-wrap"><table class="awards"><tbody>'+arows+'</tbody></table></div>'+award_car+'</div><p style="margin-top:30px"><a href="past.html">← All past conferences</a></p></div></section>')
    P[f"past-{slug}.html"]=(name,b,theme)
for fn,v in P.items(): open(fn,"w").write(page(fn,v[0],v[1],theme=v[2] if len(v)>2 else ""))
print("built",len(P),"pages")
