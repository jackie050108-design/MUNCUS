"""News articles. Newest first. Each becomes news-<slug>.html and a card on the News page and homepage.

An article either uses the conference-results layout (intro/photos/awards) or a list of `blocks`:
  ("img", src[, caption])   ("h2", text)   ("p", text)   ("closed", text)
  ("letter", conf_slug)     ("schedule",)  ("location",) ("registration", with_note)
  ("committees", conf_slug) ("dais",)      ("affairs",)
"""
D = "assets/img/news/vsph-2026/"
VSPH_SCHEDULE = [
  ("October 4", "Day 1", [("Conference Registration","09:00 – 11:00"),("Lunch Break","11:00 – 13:00"),("Opening Ceremony","13:00 – 14:00"),("Committee Session 1","14:00 – 17:00"),("Dinner Break","17:00 – 19:00"),("Committee Session 2","19:00 – 21:00")]),
  ("October 5", "Day 2", [("Delegate Workshop","09:00 – 11:00"),("Lunch Break","11:00 – 13:00"),("Committee Session 3","13:00 – 17:00"),("Dinner Break","17:00 – 19:00"),("Gala Night","19:00 – 21:00")]),
  ("October 6", "Day 3", [("Committee Session 4","09:00 – 11:00"),("Lunch Break","11:00 – 13:00"),("Committee Session 5","13:00 – 16:00"),("Closing Ceremony & Awards","16:00 – 17:00"),("Delegate See-off","After 17:00")]),
]
VSPH_LOCATION = dict(photo=D+"campus.jpg", name_zh="上海浦东新区民办万科学校", name="Vanke School Pudong",
  address_zh="上海市浦东新区康桥路1700弄2-4号", address="No. 2-4, Lane 1700, Kangqiao Road, Pudong New Area, Shanghai")
VSPH_DAIS = [
  ("Soviet Union General Commissariat (USSRGC)", ["isaac-zhang","dora-xie","eason-yu"]),
  ("United Nations General Assembly (UNGA)", ["eason-wang","nathan-yu","sailing-wang"]),
  ("Ad Hoc: Zootopia Howling Committee", ["andy-wei","kelina-yang","katherine-yang"]),
]
CLOSED = "Registration for MUNCUS x VSPH 2026 has closed. This article is kept here as a record of the conference."
NEWS = [
  dict(
    slug="vsph-2026-concludes",
    date="October 8, 2026",
    title="MUNCUS x VSPH 2026 Concludes: Award Winners Announced",
    title_zh="MUNCUS x VSPH 2026｜会议圆满落幕，获奖名单公布！",
    summary="Three days of debate at Vanke School Pudong came to a close with awards across USSRGC, UNGA and the Ad Hoc Zootopia Howling Committee.",
    cover="assets/img/news/vsph-2026/cover.jpg",
    conference="vsph-2026",
    wechat="https://mp.weixin.qq.com/s/q6PYsmTPtxhRlaSfH9HWxQ",
    intro=[
      "From October 4 to 6, 2026, delegates from schools across Shanghai and beyond gathered at Vanke School Pudong for MUNCUS x VSPH 2026, the second edition of the conference co-hosted by the Model United Nations Club Union of Shanghai and Vanke School Pudong.",
      "Across three committees, the Soviet Union General Commissariat (USSRGC), the United Nations General Assembly (UNGA) and the Ad Hoc: Zootopia Howling Committee, delegates negotiated, drafted and responded to crisis over three days. At the closing ceremony, the dais teams recognized the delegates below.",
    ],
    photos=["assets/img/news/vsph-2026/group-2026-full.jpg"],
    closing_image="assets/img/news/vsph-2026/thanks.jpg",
  ),
  dict(
    slug="vsph-2026-dais-announced",
    date="September 30, 2026",
    title="Countdown to MUNCUS x VSPH 2026: Dais Team Announced",
    title_zh="MUNCUS x VSPH 2026｜会议开幕倒计时！主席团阵容公布，我们万科见！",
    summary="Meet the nine directors and assistant directors leading USSRGC, UNGA and the Ad Hoc Zootopia Howling Committee, plus the schedule and conference affairs.",
    cover=D+"dais-collage.jpg",
    wechat="https://mp.weixin.qq.com/s/naKyotnKJ66BVq3ckzKjzQ",
    blocks=[("img",D+"cover.jpg"),
      ("p","With MUNCUS x VSPH 2026 just days away, we are proud to introduce the dais teams who will lead this year's three committees at Vanke School Pudong from October 4 to 6."),
      ("h2","Dais Team"),("dais",),("h2","Conference Location"),("location",),("h2","Conference Schedule"),("schedule",),
      ("h2","Conference Affairs"),("affairs",)],
  ),
  dict(
    slug="vsph-2026-registration-in-progress",
    date="September 11, 2026",
    title="MUNCUS x VSPH 2026 Registration in Progress: No Conference Is Quite Like This",
    title_zh="MUNCUS x VSPH 2026｜会议报名进行中！No Conference Is Quite Like This. Come See For Yourself.",
    summary="The three committees and their topics are revealed, from the end of the war in 1945 to the Partition Plan for Palestine and a crisis in Zootopia.",
    cover=D+"cover.jpg",
    wechat="https://mp.weixin.qq.com/s/TCIsYfPpaFieYCn52t-ABQ",
    blocks=[("img",D+"cover.jpg"),("h2","Committees & Topics"),("committees","vsph-2026"),
      ("h2","Conference Location"),("location",),("h2","Conference Schedule"),("schedule",),
      ("h2","Registration Info"),("registration",False),("closed",CLOSED)],
  ),
  dict(
    slug="vsph-2026-dais-recruitment",
    date="August 29, 2026",
    title="Dais Recruitment Opens for MUNCUS x VSPH 2026: Who's Behind the Dais? You Could Be.",
    title_zh="MUNCUS x VSPH 2026｜主席团招募开启：Who's Behind the Dais? You Could Be.",
    summary="Applications open for Committee Directors and Assistant Directors for MUNCUS x VSPH 2026 at Vanke School Pudong.",
    cover=D+"director-recruitment.jpg",
    wechat="https://mp.weixin.qq.com/s/rY3rBr7Du8m-3n4mgEfINg",
    blocks=[
      ("p","<b>Conference Time:</b> October 4 – 6, 2026　大会时间：2026年10月4日 – 2026年10月6日"),
      ("p","<b>Conference Location:</b> Vanke School Pudong　会议地点：上海浦东新区民办万科学校（上海市浦东新区康桥路1700弄2-4号）"),
      ("h2","Committee Director Recruitment"),
      ("p","If you are willing to join us as a Committee Director at this year's MUNCUS x VSPH 2026, apply and the Secretariat will reach out to you shortly."),
      ("p","若您希望以委员会主席的身份加入本次 MUNCUS x VSPH 2026 模拟联合国大会，欢迎报名，大会秘书处将尽快联系您。"),
      ("img",D+"director-recruitment.jpg"),
      ("h2","Assistant Director Recruitment"),
      ("p","If you are willing to join us as an Assistant Director at this year's MUNCUS x VSPH 2026, apply and the Secretariat will reach out to you shortly."),
      ("p","若您希望以主席助理的身份加入本次 MUNCUS x VSPH 2026 模拟联合国大会，欢迎报名，大会秘书处将尽快联系您。"),
      ("img",D+"ad-recruitment.jpg"),
      ("closed","Dais recruitment for MUNCUS x VSPH 2026 has closed. Meet the selected dais team in our September 30 announcement.")],
  ),
  dict(
    slug="vsph-2026-registration-opens",
    date="August 28, 2026",
    title="MUNCUS x VSPH 2026 Registration Opens: Autumn Is Back, and So Are We in Vanke!",
    title_zh="MUNCUS x VSPH 2026｜报名通道开启！Autumn is Back - and So Are We in Vanke!",
    summary="The first announcement for MUNCUS x VSPH 2026: the Permanent Secretary-General's welcome letter, venue, schedule and free admission for all delegates.",
    cover=D+"campus.jpg",
    wechat="https://mp.weixin.qq.com/s/qyvJz48by9OuKbegs9NzOw",
    blocks=[("img",D+"cover.jpg"),("h2","Welcome Letter"),("letter","vsph-2026"),
      ("h2","Conference Location"),("location",),("h2","Conference Schedule"),("schedule",),
      ("h2","Registration Info"),("registration",True),("closed",CLOSED)],
  ),
]
