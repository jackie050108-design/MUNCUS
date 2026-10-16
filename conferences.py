"""Per-conference content for the Past Conferences pages. Conferences not listed here show placeholders."""
VSPH = "Vanke School Pudong"
VSPH_IMAGES = ["assets/img/vsph/vsph-logo.png", "assets/img/vsph/stella-vsph.png"]
VSPH_2026_LETTER = [
    "Dear Delegates,",
    "A year ago, MUNCUS x VSPH began its journey with a simple belief: that meaningful dialogue among young people can create a space for understanding, cooperation, and change. Today, as we welcome you to MUNCUS x VSPH 2026, we are honored to continue this journey and build upon the foundation created by our inaugural conference.",
    "The success of a conference is not measured only by the committees held or the resolutions passed, but by the conversations sparked, the perspectives exchanged, and the connections formed between individuals from different backgrounds. With the experience gained from last year, our Secretariat has devoted itself to creating a more engaging, challenging, and meaningful MUN experience for every delegate.",
    "MUNCUS x VSPH 2026 invites you to step into the world of diplomacy, where every discussion requires both strong convictions and the willingness to understand others. Through our committees, delegates will have the opportunity to examine complex global issues, approach challenges from different perspectives, and experience the process of negotiation and cooperation.",
    "In a world where challenges increasingly cross borders, the ability to communicate, compromise, and collaborate has never been more important. Model United Nations is not simply about representing a country or drafting a resolution; it is about discovering how different ideas can come together to address issues that affect us all.",
    "As you participate in this conference, we encourage you to embrace every opportunity to speak, listen, and grow. Challenge yourself to think beyond your own perspective, engage respectfully with others, and make every moment of this conference meaningful.",
    "We sincerely hope that MUNCUS x VSPH 2026 will leave you with unforgettable memories, lasting friendships, and a deeper appreciation for diplomacy and global cooperation. Together, let us continue the journey that began last year and create another remarkable chapter in the history of VSPH Model United Nations.",
    "Welcome to MUNCUS x VSPH 2026.",
    "The future awaits you."
]
CONF = {
"vsph-2026": dict(
  hero_images=["assets/img/vsph/stella-vsph.png"],
  psg=dict(name="Leo Wang", photo="assets/img/vsph/psg-2026.jpg"),
  letter=VSPH_2026_LETTER,
  signoff="Warm regards,<br><b>Leo Wang</b><br>Permanent Secretary-General, MUNCUS x VSPH 2026<br><small>Vanke School Pudong, Class of 2027</small>",
  secretariat=[
    ("Permanent Secretary-General", "Leo Wang", VSPH, "assets/img/vsph/psg-2026.jpg"),
    ("Executive Secretary-General", "Jackie Lin", "WLSA Shanghai Academy"),
    ("Deputy Secretary-General", "Crystal Zhao", VSPH),
    ("Under-Secretary-General, Head of Crisis", "Isaac Zhang", "Shanghai Starriver Bilingual School"),
    ("Under-Secretary-General, Head of Conference Affairs", "Xiaoyu Yang", VSPH),
    ("Under-Secretary-General of Academics", "Timothy Gu", "Shanghai Pinghe School"),
    ("Under-Secretary-General of Academics", "Alfie Flower", "Shanghai High School International Department"),
    ("Under-Secretary-General of Academics", "Andy Wei", "Wenzhou Kean University"),
    ("Under-Secretary-General of Branding", "Rachel Wu", "UWC Atlantic College"),
    ("Under-Secretary-General of Branding", "Ashley He", "Hiba Academy Shanghai"),
  ],
  committees=[
    dict(abbr="USSRGC", name="Soviet Union General Commissariat", topic="End of the War, 1945",
         director=("Isaac Zhang", "Shanghai Starriver Bilingual School"),
         ads=[("Dora Xie", "WLSA Shanghai Academy"), ("Eason Yu", "Shanghai Koller Foreign Language School")]),
    dict(abbr="UNGA", name="United Nations General Assembly", topic="United Nations Partition Plan for Palestine, 1947",
         director=("Eason Wang", VSPH),
         ads=[("Sailing Wang", "Pudong Foreign Languages School"), ("Nathan Yu", "WLSA Shanghai Academy")]),
    dict(abbr="Ad Hoc", name="Zootopia Howling Committee", topic="Emergency Response and Investigation on the Howling Incident",
         director=("Andy Wei", "Wenzhou Kean University"),
         ads=[("Kelina Yang", "Pudong Foreign Languages School"), ("Katherine Yang", "Shanghai Foreign Language School Affiliated to SISU")]),
  ],
  awards=[
    ("USSRGC", "Best Delegate", "Igor Kurchatov", "Zihao Wang", "Shanghai East Foreign Language School Affiliated to SISU"),
    ("USSRGC", "Outstanding Delegate", "Vyacheslav Molotov", "Anzhe Wang", "Ulink College of Shanghai"),
    ("UNGA", "Best Delegate", "United Kingdom", "Jingqi Zou", "Guangzhou Foreign Language School"),
    ("UNGA", "Outstanding Delegate", "Iran", "Shiqi Yuan", VSPH),
    ("Ad Hoc", "Best Delegate", "Captain Felix Firehound", "Qiuyang Zhang", VSPH),
    ("Ad Hoc", "Outstanding Delegate", "Chief Bogo", "Linxuan Xu", "Pudong Foreign Languages School"),
    ("Ad Hoc", "Honorable Mention", "Gideon Grey", "Zihan Yang", "Pudong Foreign Languages School"),
    ("Ad Hoc", "Honorable Mention", "Isabella L. Bexlee", "Lanqi Shan", "Changchun Shiyi High School"),
  ]),
"vsph-2025": dict(hero_images=VSPH_IMAGES),
}
