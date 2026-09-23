# Week 38

Politico: "Anthropic, OpenAI, SpaceXAI, Google sued over call to
'pace' AI development.. The lawsuit alleges comments about need to
'pace the frontier' of AI represent illegal coordination between
competitors."

---

"@cwebber@social.coop

So: you started vibecoding your FOSS project? And now you don't really
understand your codebase anymore *without* asking agents what's
happening? And you basically outsourced all your favorite part of your
passion project to managing a robot that doesn't care? And you're more
burnt out than ever?

I have to say that it's very difficult for me to feel sympathy for
this. I see more people reporting on this, but it feels fairly
predictable. But it also feels like it was clearly where it was going."

---

Time to buy bonds and commodities?

---

YF data goes back only 15 years, but it looks right

```python
# GD=F: Commodities, ^GSPC: SP500
df = u.get_yahoo_tickers(1970, ["GD=F","^GSPC"])
df['Ratio'] = df["GD=F"] / df["^GSPC"]
df['Ratio'].plot()
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/297/628/107/066/756/original/772468feffe8fb24.jpg'/>

---

BigGo Finance: "[08/31] Commodity-to-Equity Ratio Hits 50-Year Low as
Wall Street Sounds Alarm on a 'Perfect Storm' in Hard Assets.. Wall
Street's major institutions are rapidly converging on a rare
consensus: a systemic shortage of physical resources has quietly
begun."

---

Notice yields for stocks is calculated by *inverting* the P/E ratio,
meaning if an equity has price that is wayyy above its earnings, its
yield expectation will go *down*, not up. P/E ratio 20 means 1/20 =
0.05 -> 5% yield. The higher the PE, the lower the yield.

---

Bonds are higher than SP 500 yields, first time in a few decades.. \#RossGivens

```python
pe = u.get_sp500_pe()
df = u.get_fred(1970,['DGS10'])

pe['Yield'] = pe['PE_Ratio'].rdiv(1) * 100
dfc = pe.join(df, how='left',on='Date').interpolate(method='linear')
dfc = dfc.set_index('Date')
dfc = dfc[dfc.index > "1980-01-01"]
dfc[['Yield','DGS10']].plot()
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/301/754/436/649/808/original/dd8adf48c5b35df5.jpg'/>

---

Let's check it out

Investopedia: "Earnings yield, the inverse of the P/E ratio, shows the
return per dollar invested.. Earnings yield helps compare stock
returns to other investment types like bonds."

---

"@dangillmor@mastodon.social

The AI panic looks like an orchestrated con: The bosses of these
rapacious, sleazy, and infinitely sloppy companies are angling for
government permission to be a cartel. This would be followed, as
certain as day follows night, by the bailout they all know they'll
need when their bubble deflates."

---

CNN: " US military had close call after using AI for false
intelligence report.. The intelligence report, circulated across the
US military this spring in the midst of the war with Iran, immediately
set off alarm bells: A Chinese ship in the Middle East was
transporting components of a nuclear weapons program... It was only
just before the planned operation that officials dug deeper into the
report put together by a special operations command analyst and found
it had been generated with the help of artificial intelligence (AI) —
and that a chatbot the analyst had used inaccurately identified the
material the ship was carrying."

---

"@kralcttam@mastodon.social

Oil crisis is moving west.

Saudi Aramco told at least two oil refining customers in Europe that
they will be allocated no crude oil next month.

The decision applies to all European buyers, they said."

---

Motor1: "Toyota just put a number on the hydrogen Hilux, and it is
bigger than anything the electric version can manage. At IAA
Transportation 2026 in Hannover the automaker outlined plans for a
Hilux fuel cell model targeting a 2028 launch for European
professional customers.

The target is 248 miles of WLTP range and 5,512 pounds of towing, plus
roughly a five-minute refuel when a station is operating
normally. That is a work truck pitch built to beat the
battery-electric Hilux on the two numbers that matter most to fleets."

<img width='340' src='https://cdn.motor1.com/images/mgl/pb870v/s1/toyota-hilux-fcev-2028-teaser.webp'/>

---

OpenRouter -> Open Weights LLM -> Code

or

Local Software -> Local Hardware -> OW LLM -> Code

It seems everyone is out to get commercial LLM makers offering cloud
services. The future is not looking too bright for them. Stagnant
product, no moat = trouble

---

I just saw dude running an open weights model on this hardware. 

---

128 GB unified memory. It is a beast

NVidia: "Spark™ is a complete platform for local autonomous
agents. Large local memory, powerful AI compute and the NVIDIA AI
software stack enable agents and large models to run locally, reducing
the need for cloud-based token generation resources"

[[-]](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

---

The Lever: "Big AI’s Favorite Democrats Are Writing The Party’s AI
Plan.. Hakeem Jeffries’ five-member AI commission is stacked with
lawmakers backed by industry super PACs seeking to shape federal
policy."

---

Nadh: "Code is cheap. Show me the talk... The [Linus Torvalds] quip
['Talk is cheap. Show me the code.'] has since become an adage in the
software world. The gist of it back then was that, it was easy to talk
about all the software stuff one would like to do, or could be
hypothetically done, but unless one actually put in the effort and
proved it, talk wasn’t of much value...  All that has now been thrown
out of the window, of course, for better or worse."

---

"@researchfairy@scholar.social

'But the AI will tell us how to fix climate change,' they said, as if
knowing what to do is the problem"

---

"Former Press Secretary of.. Zelensky said that the population in the
region controlled by Kiev is currently only about 20-25 million
people.

In an article published in *The Spectator*, Ms. Mendel said that
Ukraine has lost more than half of its population in 35 years since
declaring independence, separating from the Soviet Union.

The most cautious estimates show that 20-25 million people currently
live in territories controlled by Ukraine, of which about half are of
retirement age... the number of deaths is estimated by her to be about
4 times higher than the number of newborns."

---

TAC: "Given the Chance, Ukrainians Would Give Zelensky the Boot"

---

"@vampiress@eigenmagic.net

'AI' really has made me hate going on the web. I will think of
something obscure I want to learn, quickly discover all search engines
produce no usable results, sigh in frustration and if I truly REALLY
want to know the answer to my abstract question, I will try an LLM.

It will shart out a toxic-reading sycophantic page telling me how
great my question was and sounding like a cross between an
over-enthusiastic school kid and the world's most annoying corpo-fied
co-worker.

Then the icing on the cake - it'll be wrong. Invariably, at least some
part of what dribbles out of its digital orifice is factually
incorrect, stated with the confidence of that asshole down the pub..

It's depressing seeing a useful tool for information becoming absolute
dogshit so fast. I'm slowly looking things up less and less."

---

In one ep of scifi show *Dark Matter*, while traveling "the
multiverse", the characters end up in a version of Earth that has no
computers, no Internet. The scientist among them "finds out why", says
"because JFK lost to Nixon on this Earth, US never went to the Moon,
ergo subsequent related tech stagnated". What a Dem shitlib stupid
thing to say... The space race on US side was energized after Soviet
launch of Sputnik, during D. Eisenhower's term. It was DE who opened
the floodgates on research, education, tech funding, everything
related to space. I've read multiple accounts of uni profs of the
time, they all say the same thing.

Going to the moon was LBJ's idea, who funded the program during his
term.

Nixon did the same and *every successful crewed human US moon landings
happened during his administration*.

JFK just made that one speech got his dumb ass shot. Is this an
achievement? But because the man is an idol for centrist coastal
dimwit shitlibs the sainted fool gets credit.

---

"Shark Tank, but it's just a big tank of sharks and the show is
different billionaires being tossed in periodically"

---

404 Media: "‘Doom Loop’: OpenAI and Microsoft Admits LLMs Are
Destroying the Web and Built on Theft.. Executives working on AI at
Microsoft and OpenAI admitted what its critics have been saying all
along: Large language models are predatory pieces of technology that
have been built on what a Microsoft executive called 'an astonishing
theft of unprecedented proportions,' and the 'largest theft of labor
in human history.' An internal Microsoft document said generative AI
products have created a 'doom loop' that is killing 'the entire web.'

Those statements and a series of other mask-off moments feature
heavily in an unredacted court filing that was unsealed Thursday in
the behemoth New York Times vs OpenAI copyright lawsuit that has been
winding its way through the court system for years."

---

Gullible investor: FOMO!

---

Next headline: QC Companies Say Government Please Stop Us Before We
Invent the Evil Quantum Supercomputer and Become Too Dangerous"

---

Hey I'm fine with projections.. One of the best image segmentation
approaches, level sets, are projections of a 3D shape onto a 2D
dimensions (where the image lives). You manipulate the 3D but the
segmentation occurs in 2D. Fantastic. 

---

The reason quantum computing doesn't work is nature deep down is not
parallel, meaning the deep fabric underneath is not quantum. They are
having problems with QC error correction, that's because quantum
measurements themselves are erroneous. How can you correct the error
of something that is inherently bogus? QC states are a projection of
something else.

---

Snyder wants to come back.. A reminder that ZS actively wanted to make
Batman v Sup movie - a flop. He became obsessed with showing *Man of
Steel*'s hero as a threat, so he too was bitten by the Quantin
Tarantino bug, wanting to show "the ugly side of things". He
frequently cites the *Watchmen* as a favorite, but that too was an
anti-hero movie made in a typical Tarantino fashion. You can't manage
a mainstream franchise that way. 

---

They were abducted and probed on within those two hours

---

The best part of the UFO story below:

"2 hours of missing time with us having know idea where we were.. Two
hours later we were at the same stop sign only coming from another
direction"

They were going one way, then their brain shuts off or something and
when they came to, they were going in the opposite direction. 😂 This
is the best UFO story ever.

[[-]](../2025/week47.html)

---

I had no idea there was more to SS than just big breasteses. She's got
an angle, she's executing on it. Started as anti-Woke warrior, now
serving the Zio. 

---

Bitch is Zio? The fiancee is bad news too.. Mfker is rabid

---

Reverse Canary Mission: "[Sydney] Sweeney is the brand ambassador for
companies of Armani and KÉRASTASE, which are subsidiaries of Zionist
company, L'Oréal, who have factories and stores on occupied
Palestinian land."

---

I don't see a fall in oil prices at the moment.. How much can these
shuttle vessels transport oil anyway? 

[[-]](https://media.mastodontech.de/media_attachments/files/117/287/681/287/264/657/original/8f2a0d01b05d56e0.jpg)

---

These Yemenese are feisty mfkers. Bin Laden was of Yemen descent you
know

---

East-West Pipeline, Sohar Port

```python
import json
jd = json.loads(open("shia2.json").read())
u.map_polys([22, 47.3], polys=jd['regions'],
            poi=jd['poi'],lines=jd["lines"],
            zoom=4,outfile="map05.html")
```

[[-]](map05.html)

---

CNBC: " Oil prices fall as Saudi Arabia reportedly offers more crude
via Hormuz after pipeline attack.. The Saudis are making additional
crude cargoes available to Asian refiners through ship-to-ship
transfers just outside Hormuz near Oman’s Sohar port, sources familiar
with the matter told Reuters.

Shuttle vessels transport crude through Hormuz and then load it onto
tankers waiting outside the strait, which allows these ships to avoid
the risk of Iranian attack while sailing into the Gulf."

---

Firstpost: "Despite signing the Mecca Agreement to manage precisely
the kind of crisis Saudi Arabia is now facing, Crown Prince Mohammed
bin Salman has been forced to seek help from neighbouring states and
European countries to defend the kingdom against Houthi attacks."

---

Anatolian Agency: "US burns through dozens of missile interceptors in
single Iranian attack on Jordan..  US forces fired between 60 and 70
Patriot interceptors against an attack involving about 20 ballistic
missiles, while more than a dozen Terminal High Altitude Area Defense
(THAAD) interceptors were also launched, [WSJ] reported..

Iran reportedly used warheads that separated into multiple projectiles
as they approached their targets, complicating efforts to intercept
them. The defenses did not stop all incoming threats, with Iran
striking fighter jets and other aircraft at Muwaffaq Salti Air Base in
Jordan"

---

IC: "War, What Is It Good For? Absolutely Everything (As Far as
Washington Is Concerned)..  My country is once again fighting a
distant war for reasons that, at best, make no sense whatsoever to me,
and at worst are simply horrific"

---

The Lever: "Weeks before the midterms, the Democrats’ highest-profile
icons are publicly celebrating the AI industry’s revolving-door
corruption aiming to infiltrate the party."

---

It is extremely normal for "tech leaders" not knowing much about the
details of the tech they are "leading". Hands-on on-the-field experts
are not immune to this problem either. The supposed "Godfather of AI"
was clueless about the future of the field he had contributed much
into.

>Fortune: "A decade after the ‘Godfather of AI’ said radiologists were
>obsolete, their salaries are up to $571K and demand is growing
>fast.. In 2016.. Hinton, stood onstage at a machine learning
>conference in Toronto and declared AI would soon kill the radiology
>profession.. 'If you work as a radiologist, you’re like the coyote
>that’s already over the edge of the cliff but hasn’t yet looked down,'
>Hinton said... And yet, despite the doomsday predictions, radiology
>may serve as an example that the warnings of AI-fueled job replacement
>may be oversold.. Over the last 10 years, the number of active
>radiologists in the U.S. has grown by about 10%"

---

"Figures don't lie, but liars figure"

---

"[08/28] Meta scrapped the deepest phase of its AI-agent overhaul
after reading its own output data... Meta’s AI-assisted code changes
rose 220 percent year over year, while the changes that reached users
rose 36 percent."

----

"@baldur@toot.cafe

If the pope released a statement that the world was ending next
Tuesday with the rebirth of the Messiah, the job of a reporter isn't
to schedule an interview with Jesus H. Christ reborn but to figure out
what's wrong with the pope

Media accepting 'AI' millenarianism as fact is genuinely disturbing"

---

The Verge: "Mathematicians are beginning to push back. Many [we] spoke
to, even the most enthusiastic proponents of AI in the field, worried
the companies were having a chilling effect on research, pushing
mathematicians to be more secretive about unfinished work for fear
someone may swoop in and beat them to it...

Resistance is becoming increasingly public. In June, mathematicians
published the Leiden Declaration, a set of principles for the
responsible use of AI in mathematics that has been endorsed by the
International Mathematical Union and signed by nearly 3,900 people, an
increase of nearly 500 people since I last covered it in
mid-August. It urges policymakers, governments, the media, and other
groups to not buy into 'the hype' created by companies who 'overstate
the capabilities of their products.' As the Millennium Prize
controversy raged, OpenAI withdrew its sponsorship of an undergraduate
mathematics hackathon at Caltech following fierce opposition decrying
the intrusion of corporate interests and worries the event would
create a deluge of low-quality 'slop mathematics.'

---

Middle East Monitor: "Norway moves to criminalising trade with Israeli
settlements, other Western countries consider similar steps"

---

Open Insulin Foundation: "We’re a team of biohackers with a variety of
backgrounds, and skills, and relationships to insulin and diabetes,
from many cities and countries around the world.. We’re working to
develop the first practical, small-scale, community-centered model for
insulin production to make insulin accessible to all. This model will
ensure communities in need have local sources of safe, affordable,
high-quality insulin, and that people living with diabetes and their
communities own and govern the organizations that produce the medicine
they depend on to survive...  We are creating an open source (freely
available) model for insulin production built around small-scale
manufacturing and open source techniques for production."

[[-]](https://openinsulin.org/)

---

\#Yemen 09/13 - 09/15

[[-]](ymndata/map03.html)

---

TAC: "As Walls Close In, Zelensky Lashes Out.. Having run out of top
generals to give the boot, the Ukrainian leader is now lashing out
against former officials as he tries to assert control amid a chaotic
corruption crisis...

Balazs Jarabik of the Carnegie Russia Eurasia Center..  said.. that
the accumulating scandals 'are now creating a multicrisis ahead of a
very tough winter where Russia has a much larger destruction
capacity.'"

---

CW: "Type 5 Pressure Vessel, Hydrogen Propulsion Programs Advance..
Strato-V project and NordSpace develop Type 5 composite pressure
vessels while new U.K. government report and NLR report advances
toward hydrogen-powered flight."

[[-]](https://www.compositesworld.com/news/on-the-radar-type-5-pressure-vessel-hydrogen-propulsion-programs-advance)

---

We note the econ dynamics in play: The for-profit "frontline" LLM
companies have a stagnant product, the newcomers are running circles
around them. Given the current tech, you can easily use Openrouter as
the middleman to access a free LLM in the backend, hosted by
whomever. LLM is open weights, the harness is open source, the
programming language used to produce the code is free and open
source. It's all free except the small hosting and routing fee that is
paid to OR. There is no place for the for-profit LLM companies
here. They are **fucked**.

---

In terms of LLM based coding approach, Shopify's method is a good one
to follow. Make the model your bitch, not the other way
around. Seriously constrain the outputs you expect from it, carefully
validate the results at each point on the way.

---

I've read accounts where the open weight model costs were nearly a
quarter of "frontline" models would be (and let's be honest, LLM
innovation has died, soon all LLM models will be frontline).

---

OR can forward the LLM request to any LLM provider in the backend. For
open weight models, eg Kimi, there could be multiple providers, in
that case OR round-robins, or chooses best on cost, or you can force
which provider to use in your API call to OpenRouter. If payment is
required it is made to OpenRouter, OR acts as the middleman. You add
funds to an account balance on OpenRouter by purchasing prepaid
credits. If an agentic harness is needed, you pick one on your end
have the harness talk to OR.

---

"OpenRouter gives you access to hundreds of AI models through a single
API endpoint. It handles fallbacks automatically and picks the most
cost-effective option for each request."

[[-]](https://openrouter.ai/)

---

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/273/618/680/810/550/original/b6dc82ea2a91335c.jpg'/>

---

IC: "The US government continues to double down, even as its
stubbornness costs it dearly—not only in material terms, but also in
geopolitical influence. Washington is rapidly losing power and status
in the Middle East, a decline that could produce a wider domino
effect, reverberating around the world."

---

Wrong response? It was the right response for the MIC.

IC: "25 Years of War Was the Wrong Response to 9/11.. Stop throwing
money at a destructive war machine. Stop threatening and blockading
our neighbors. Close overseas bases and bring our troops home."

---

\#Ukraine 09/05 - 09/15

[[-]](ukrdata/map20.html)

---

Michell Clark: "They made healthcare a commodity, education a debt
trap, and housing a speculation market - then told you that poverty is
a personal failing. They privatized survival and called it freedom."

---

He doesn't have a choice in the matter.. his very existence depends on
the US MIC. If he is not useful in that regard, he will be deposed.
Israel is a tool. The tail does not wag the dog. 

IC: "Does Netanyahu want Israel to be Sparta or to Join US
Military-Industrial Complex?"

---

TAC: ".. I practically had [the Danes] in tears laughing as I tried to
explain how healthcare works in America"

[[-]](https://www.theamericanconservative.com/america-can-learn-from-denmark-on-good-government/)

---

Politico: "Kennedy Center has warned it may close in a matter of days,
unless his name is returned to the building"

---

That might not be all that bad .. if you are transitioning to the
wrong thing. ;) Just because a few dipshits created something and the
world copycatted because the "idea" came from America doesn't mean it
is a worthy goal.

Politico: "‘Slowing things down’: Trade wars hit global
electrification shift.. Tariffs on everything from EVs to grid
components could slow the energy transition."

---

"@scalzi@mastodon.social

Sure, 'AI' might kill us all, but it's rather more likely that the
folks running 'AI' companies are hyping up that fear in order to have
their pet legislators introduce bills that advantage their positions
while kneecapping their competitors and to give them a little more
runway to figure out how to avoid the coming massive economic collapse
they are still in the process of creating. The apocalypse is far more
likely to be caused by the tech CEOs than their spicy autocorrect
programs."

---

Apparently Maxwell had a mechanical model in mind while formulating
electromagnetism. He wasn't like "let me try some algebra and see if
it fits the data bro". We need to understand how the inventors
themselves thought about problems. Variation of his model is still
a hot topic of research today. 

[[-]](https://youtu.be/qIOTPqRjSh4?t=142)

---

MIT Review: "The AI industry’s boldest promise right now is that AI
will soon improve itself, with almost no need for human
oversight. LLMs can already write code, generate synthetic data for
training, and optimize the computer chips they run on. Forecasts of
explosive AI progress predict that what researchers call recursive
self-improvement is on the horizon.

But a new study suggests that it might take a while for us to get
there. The researchers behind it found that AI agents are not yet
capable of conducting open-ended AI research—free-form investigations
that have no clear-cut answers and require judgment and taste"

---

Assads and most Shia in Syria were / are Alewites.

---

Approximate areas with Shia (including variations eg Alevites)
population outside Iran marked in red. The three largest Saudi oil
fields are on the map.

```python
import json
sa_fields = {"Ghawar Field": [25.950246487, 49.669976493],
             "Safaniya Field": [26.42081319, 50.0726183],
             "Khurais Field": [25.27248965, 48.18430747]}
jd = json.loads(open("shia.json").read())
u.map_polys([22, 47.3], jd, poi=sa_fields, zoom=4,outfile="map04.html")
```

[[-]](map04.html)

---

The Shia lives in a lot of key, strategic places..

---
