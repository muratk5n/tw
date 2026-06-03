# Week 22

CNBC: "Software stocks wrap up best month since 2001 as talk of
'SaaSpocalypse' subsides"

---

Politico: "Berlin gives the OK for tougher trade action on China"

---

Politico: "Don’t let Big Tech hide ecological cost of AI, environment
agency chief tells EU.. Brussels must require tech companies to
disclose data centers’ energy and water use [the chief] says."

---

Munee and bidness.. That's what it's all about

Andy O'Brien: "The NY Times' Obsession with Platner's "Working Class"
Cred.. The NY Times story quoted Tony Buxton, a corporate lobbyist
with the Portland firm Preti Flaherty, accusing Platner of lying about
his business. But for some reason it didn’t mention what Buxton does
for work. The Times simply described him as 'a former chairman of the
Maine Democratic Party who had supported Ms. Mills.'..  The Times also
failed to mention that Buxton represents the company seeking to build
a controversial data center in Sanford and successfully lobbied to get
Governor Mills to veto a data center moratorium last month. "

---

2008-2012 has a major fall, then major rise.. The rise is higher than
the previous decline. That means corporations not only reversed their
losses since 2008, they surpassed them. Why wouldn't they? They had
laid off millions of workers bcz of the crisis, frozen hiring, and
closed facilities, extracted more work from the remaining
workforce. When econ began to recover in 2010, every new dollar of
revenue would flow into pure profit, margins expanded to historic
highs, causing the massive, outsized explosion in earnings we see in
the graph bcz corp cost structures were permanently lower (less
workers, deindustrialized and outsourced jobs more). The period as
is known as "jobless recovery" for good reason. 

---

Corp earnings been rising.. 

---

```python
df = pd.read_csv('schiller.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['YoY'] = df['Earnings E'].pct_change(periods=12) * 100
df['PE_Ratio'] = df['S&P Comp P'] / df['Earnings E']
df_recent = df[df['Date'].dt.year >= 2000].copy()
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(df_recent['Date'], df_recent['YoY'], label='YoY Earnings Growth (%)')
ax1.axhline(0, color='black', linestyle='--', linewidth=1.2, alpha=0.7)
ax1.set_title('S&P 500 Year-over-Year (YoY) Earnings Growth Rate (Since 2000)', pad=15)
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Growth Rate (%)', fontsize=12)
ax1.legend(loc='upper left', frameon=True)
ax1.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/116/661/196/470/027/975/original/a3a06163f4f0aeaf.jpg'/>

---

Letz do some corp earnings analysis.. Data at  `https://shillerdata.com`, get
`ie_data.xls`, the data extractor is in `mbl/2026/util.py` under `schiller_conv`.
Outputs to `schiller.csv`. 

---

Hanauer, *Politico*: "[2014] The Pitchforks Are Coming… For Us Plutocrats"

[[-]](https://www.politico.com/magazine/story/2014/06/the-pitchforks-are-coming-for-us-plutocrats-108014/)

---

Hanauer is one of the rare billionaires who consistently speak out on
inequality

---

Nick Hanauer: "This booklet is based on our forthcoming book, *Market
Humanism*. It is a brief guide aimed at policymakers..  *Market
Humanism* and middle-out economics stand in sharp contrast to the
economic theories and policy agenda that dominated the U.S. and much
of the world from the 1970s through the 2010s. We will refer to this
set of ideas as the neoliberal consensus, a political ideology that
integrated free market theories from neoliberal political economy,
neoclassical economics, and libertarian philosophy into a worldview
that shaped the policy agendas of both the Republican and Democratic
parties from Carter and Reagan through Obama...

The neoliberal consensus and trickle-down economics did not emerge by
accident. These ideas were strategically funded, developed, and
promoted by an array of business interests and wealthy individuals who
benefited to the tune of tens of trillions of dollars from the
resulting policies. The neoliberal consensus, however, fractured
during the global financial crisis of 2008, losing both its
intellectual credibility and support from the public...

From the end of World War II until the mid-1970s, during an era of
more regulated capitalism and robust public investment, U.S. GDP
growth averaged approximately 4 percent annually. In contrast, since
adopting neoliberal economic policies starting in the late 1970s and
early 1980s, average GDP growth has fallen significantly, averaging
roughly 2.5 percent annually and declining further in recent
decades. Far from unleashing entrepreneurial dynamism and broad-based
prosperity, neoliberal economics has delivered economic stagnation,
instability, and fragility."

[[-]](https://www.marketsbuiltforhumans.org/flipbook)

---

Space Daily: "The European Commission moved to reserve two-thirds of a
coveted satellite spectrum band for European operators, a decision
that directly threatens SpaceX's direct-to-device plans and Viasat's
existing European Aviation Network while opening a fresh front in the
transatlantic fight over space technology."

---

Cosmology is not science.. It's bunch of harebrained, cockamamie stuff
thrown together that sound scientific. Outside US if something were to
be cut, astrophysics would be the first place to go.

"Someone, somewhere, has taken the decision to defund astrophysics
research in the UK, but no-one seems quite sure who that was, or why."

---

Recommending *Fuze* (2025). Fine work.

---

<img width='340' src='https://cdn.masto.host/frontendsocial/media_attachments/files/116/646/709/883/091/008/original/3c7211cefe4c3a2d.png'/>

---

"We all died in 2020 and this is hell"

---

Reuters: "Starbucks scraps AI inventory tool across North America.. AI
tool miscounted items, leading to errors.. The tool was part of CEO
Brian Niccol's efforts to fix the coffee chain's persistent product
shortages that he has blamed for hurting sales. The app - designed to
improve Starbucks’ visibility into shortages at stores - frequently
miscounted and mislabeled items, such as confusing similar milk types
or ​missing them altogether"

---

You are still a slave, Jew. Just like when they goaded you into those
gas chambers, they goaded you to that f-ing place, Israel, and they
are making money of off you. You are a pawn, a f-ing tool, still
serving the interests of the Aryan race. Is this what you were chosen
for?

---

It's sad MIC making use of Israel in this way. They think they are in
control, but they are being controlled.

---

Garbage Day: "There are.. warning signals across the AI industry that
are flashing bright red right now. Starbucks had to roll back an AI
inventory tool because it kept hallucinating. *The Verge* reported
that Microsoft is rethinking its dependency on Claude Code. And
Duolingo’s stock price has tanked in the last year, after the company
went all-in on AI."

---

England is a cup of tea.<br>
France, a wheel of ripened brie.<br>
Greece, a short, squat olive tree.<br>
America is a gun.<br>

Brazil is football on the sand.<br>
Argentina, Maradona's hand.<br>
Germany, an oompah band.<br>
America is a gun.<br>

Holland is a wooden shoe.<br>
Hungary, a goulash stew.<br>
Australia, a kangaroo.<br>
America is a gun.<br>

Japan is a thermal spring.<br>
Scotland is a highland fling.<br>
Oh, better to be anything<br>
than America as a gun.<br>

*Brian Bilston*

---

Trump Off

[[-]](https://www.youtube.com/shorts/76AKniXhfqM)

---

Turks (the real ones) were assimilated into Anatolia just like any
other migratory moves arriving there. 1920s Republic picked one
ethnicity among many and made it *the* official identity, which was a
mistake. It's like making Irishness the official identity in America:
sure there have been Irish migration, and they are now part of the US
fabric (tomato soup, not melting pot), but not *everyone* is Irish,
surely not in the form they first arrived.

---

\#YannisPappas \#Anatolia

[[-]](https://youtu.be/LM90k5aBPMA?t=525)

---

ANYONE BUT TRUMP BRO

---

BUT DEMS WERE SO MUCH BETTER

---

"@jwilker@wandering.shop

It's amazing how bad medical stuff is still in 2026. Wife went to ER
and 'oh we can't see the stuff your doctor did last week'

Like WTF? With everything we have in tech these days, it's beyond
stupid one medical provider can't see what another has done for the
patient."

---

Suriyak: "The Syrian coast continues to suffer: 🇸🇾 A UN report reveals
an alarming rise in crime rates on the Syrian coast. Despite the
transitional authorities’ denial that these acts are organized,
describing them as isolated incidents or criminal offenses, their
persistence and the manner in which they are carried out confirm the
presence of sectarian motives, among other factors."

---

Gizmodo: "Crypto’s Most Powerful PAC Sends a Warning to Politicians:
Resistance Is Futile.. Rep. Green’s defeat proves that anti-crypto
hostility carries real electoral consequences."

---

E-douche always used space biz to prop up his geek status so he would
come across smarter, more visionary than he actually is on other
unrelated matters, so it's not a surprise the grift will now take its
final corporate form. "Look there is cool space stuff" and "look there
is some other stuff underneath, pay for the cool, get others for
free". That is the sale.

---

The "new" left always wrapped its econ right-wingery with new age,
technobabbly, futuristic glitz... Have to watch for that. Screw labor
rights because we have computers bro, see how shiny they are? Anything
that goes against capital is "old".

It's interesting how two sides sold this freak shit to the
public.. Labour / Dems sold it via futurism, Reps sold it via
nostalgia (they appealed to the old, the rugged, frontiersy America).

---

The Guardian: "The current leadership debate concerning Streeting and
Andy Burnham.. 'has an extraordinarily retro 20th-century feel to it'
[Blair] complains."

---

Zhigge - Rakin' In The Dough \#music

[[-]](https://youtu.be/HSpoilv3N3g?t=168)

---

I see, so that's where this mythical center is.. There is a lot of
dough in that center.

"@GossiTheDog@cyberplace.social

Tony Blair’s son, Euan Blair, is the CEO of a GenAI firm. Tony Blair
lobbies with his own company for GenAI usage in government and
schools, and lax UK AI laws."

---

"@mike_k@mstdn.social

There is something classically AI about headings like:

'A Major Philosophical Shift, Even If Limited'

That’s not how words work."

[[-]](https://www.linuxjournal.com/content/alpine-linux-experiments-systemd-compatibility-while-keeping-its-lightweight-identity)

---

The problem is, center of the past 40 years is screwed up. There was a
time when Eisenhower (a Republican) could embrace the New Deal. Then
the world shifted to a new regime where Bill Clinton (and Blair)
embraced Reaganism. We need a new regime.

---

Do not cede that "center" ground.. 

The Guardian: "Tony Blair has accused Keir Starmer, Andy Burnham and
Wes Streeting of putting Labour’s future at risk by abandoning the
centre ground..His essay, a highly unusual intervention for a past
Labour prime minister, is likely to draw a furious response from
across the party, where Blair’s legacy remains highly contentious. On
Tuesday, one senior source accused him of abandoning social democratic
values to embrace an agenda that had 'no answers'... Blair also
suggested it was a mistake for others in the party to seek to remove
Starmer as prime minister"

"@exchgr@mastodon.world

what you think AI does: cheap code, things break fast but also get
fixed fast

what AI actually does: subsidized code that will become extremely
expensive very soon, things break fast but you don't notice and the
bugs accumulate, losing your customers' trust in your product"

---

"Colorado and California age verification bills exempt open source
operating systems"

---

As stated before, coding harnesses around LLMs, or "agents", are not
improvements of the LLM itself, they are a wrapper around it, to get
over its shortcomings. We can think of it like this: Let's say you
needed to find the minimum of a list of numbers. You have a black box,
a magic algorithmic machine which can (somehow) only return *five*
smallest numbers in that list. So the machine does some work, but it
has its limitations. But we need the one, single minimum number. What
do we do?  Well we write a *wrapper* around the magic black box
machine, we pass a list, get our five numbers which contains the
minimum, and we them run our own little algoritm to find the minimum
within that five.

What's described above is an engineering solution. In IT work, system
integration such things are done all the time. You can't change the
database, the OS itself, so in your "application" layer you do
whatever is necessary to get the functionality you need. Claude Code,
Codex are such applications. When you look in the code for CC (you
can, as it leaked recently) you will see there is nothing AI'ish in
it. It's bunch of manually coded if.. then.. else statements, regex up
the wazoo, for loops and the like. It is a giant handcoded script that
runs LLMs a certain way to provide a more fluent LLM
interaction. That's all it is.

---

CNN: "Mamdani’s ‘tax the rich’ slogan is ‘just as hateful’ as racial
slurs, New York real estate titan [Griffith] says"

---

The Lever: "As support for Israel becomes politically toxic, the
Better Blue Fund is emerging as a quiet new conduit for AIPAC-linked
money in key Democratic primary races."

---

"[A]nger at AI is white hot right now. For a bunch of reasons I've
already discussed. It's particularly and unsurprisingly hot among
young Americans, who can't find jobs, homes, health care, or much of
anything else to give them a leg up in a country hollowed out by
historic levels of corruption...  A few weeks ago a speaker giving a
commencement address at the University of Central Florida was loudly
booed after she proclaimed that improvements in software automation
should be viewed as the 'next industrial revolution.'"

---

\#BenMiles

"Ironically cold weather is a huge instigator of electricle vehicle fire"

[[-]](https://youtu.be/6MIBsuC9REo?t=217)

---

If JEPA works out maybe that will offset the lost momentum in AI. LLMs
have stagnated, they are not improving anymore, but this new approach
can provide the added energy, a new path so stawks will keep going
up. Outsiders will just see "AI has been steadily improving" story
when in fact the methods under-the-hood would have changed.

---

So-called energy based methods are a sound approach (more statistics
within the machinery is better). LeCun's JEPA is said to be using
it. EBM based Kona beats LLMs on reasoning tasks. On Sudoku it will
solve most puzzles where LLMs mostly fail.

---

Seth's Blog: "The real AI.. To quote the great Steve Wozniak, 'Actual
Intelligence.' The kind we’re born with and can develop if we
choose. It’s worth more now than ever before. Alas, it’s rarely taught
in school.

The difficult work of making choices.

The act of curation.

The responsibility of putting your name on it.

The judgment to ask the right questions and skip the other ones."

[[-]](https://seths.blog/2026/05/in-search-of-ai/)

---

"@MikeElgan@mastodon.social

Now you can keep track of how many billions the AI companies are
losing on AI. (Red is spending, green is revenue)"

[[-]](https://files.mastodon.social/media_attachments/files/116/628/155/979/775/964/original/6e8bcc40de33ca03.jpg)

---

SI batteries will be even heavier than lithium ion? Which genius is
betting on this technology?

"[Sodium ion battery] energy density is preventing sodium-ion batteries
from being widely adopted in electric vehicles. Lower energy density
means you need larger cells and that adds significant weight and take
more space."

---

"@mastodonmigration@mastodon.online

In simple terms. SpaceX is a meme stock whose fundamentals in no way
justify inclusion in index funds. NASDAQ rules have been changed so
that it will be included. As a result 401Ks and IRAs will
automatically buy the stock, effectively giving this worthless company
your money. It is the greatest grift of all time."

---

"@GossiTheDog@cyberplace.social

Watching a bunch of people get very excited about the idea of
replacing their staff, when they do not understand the job those staff
do, is particularly eye opening.

Watch the people doing this and remember their names, then enjoy not
working for them.  Inspirational leadership my arse, they’re the
arseholes of Earth."

[[-]](https://cyberplace.social/system/media_attachments/files/116/629/656/614/460/985/original/18f71198c6f31249.jpeg)

---

Power Magazine: "[03/02] China achieved a significant fuel cycle
milestone with its TMSR-LF1 thorium molten-salt reactor—a 2-MWth
prototype built by the Shanghai Institute of Applied Physics.. The
reactor reached first criticality on Oct. 11, 2023, and achieved full
power by June 2024. In October 2024, SINAP scientists performed the
world’s first addition of thorium fuel to a working molten-salt
reactor (MSR), creating a platform for thorium-uranium fuel cycle
research... And one year later, in November 2025, SINAP announced that
TMSR-LF1 had successfully bred uranium-233 from thorium"

---

The Jerusalem Post: "Trump says Netanyahu 'will do whatever I want him
to do,' amid concerns of Iran war restarting"

---

NYT: "Once Trump’s Co-Pilot Against Iran, Netanyahu Is Now a Mere
Passenger.. A partner in the war, Israel has been largely left out of
the peace talks, a humbling setback for its prime minister."

---

"The Next Lina Khan Is Your State Attorney General.. As the White House
eases off antitrust enforcement, states are rushing to seize the power
for themselves."

---

"A map of the thorium content of the lunar surface based on Lunar
Prospector data shows that a large area on the nearside of the Moon,
including the Imbrium basin and Oceanus Procellarum, is enriched in
thorium relative to the rest of the Moon"

<img width='340' src='https://planetary.s3.amazonaws.com/web/assets/pictures/20130922_global_Th.jpg'/>

---

Bloomberg: "SpaceX engineers have been slow to adopt Grok for
technical work because it’s not as effective as rival tools, according
to people familiar with the matter. Within its xAI division, certain
staffers have been using other AI alternatives such as Anthropic PBC’s
Claude for coding instead of Grok, said some of the people, who spoke
on condition of anonymity to discuss internal matters."

---

Business Insider: "SpaceX bought Tesla Megapacks and $131 million
worth of Cybertrucks, its IPO filing shows"

---

\#FullPageAd \#NYT

[[-]](https://media.mastodontech.de/media_attachments/files/116/625/500/303/878/042/original/18ac476c38c72670.jpeg)

---

One scenario goes UAE is told by US to attack Iran, if Iran responds,
that will be the excuse to restart the 60 day period where WH can use
military force again wout congressional approval. Theory goes on, Xi
and US made a deal, US will supply oil to China, and China sold out
Iran... Interesting.. The latter part sounds unlikely though, China
would lose credibility in the global south if they sold out Iran.

---

WSJ: "The U.A.E. Has Been Secretly Carrying Out Attacks on Iran"

---

You are not computing an actual division on $f(x) = x^2 - 1 / x-1$ for
$x=1$ either, and when you use $\lim_{x \to 1} f(x)$ to land you to a
new algebraic statement which you can compute, does that mean you are
using less arithmetic, less math?

---

Sure is. You can sample from the numerator, using hard-core methods of
statistics. It is still within the same realm.

"But you have a normalizer Z bro which you do not compute, that's not
probabilistic"

---

An LLM is a giant, deterministic, feed-forward matrix multiplication
engine that slaps a statistical band-aid on the final output layer (a
cheap softmax calculation at the end of the pipeline).

The so-called energy based models turn a function into a distribution
using a method from statistical mechanics, and they **sample** from it
via well-known statistical methods. Ergo **more** probabilistic.

This terminology caught my attention bcz just the other day I was
using the said approach to turn an optimization problem into a
statistical sampling problem, the approach was fresh in my mind and I
saw this argument, I was like wut?

[geek] You can find the approximate minima of a function by turning it
into a Gibbs distribution, and relying on the (more efficient)
traversal via a sampler to find a approximate minima. The method does
not get stuck in local minimas like a gradient based optimizer are
prone to do. For a final demonstration of the approach I picked the
toughes nut, a 100 dimensional function-from-hell, and applied
parallel particle filters to sample from the posterior running on a
GPU, it found the approximate minima in two seconds [/geek].

Particle filters, MCMC, posteriors, distributions.. no one can tell me
this toolset is not more probabilistic than alternatives.

---

That's a stretch... I would actually say EBMs are *more* probabilistic
compared to LLMs.

"Energy based methods are not probabilistic like LLMs"

---

Reuters: "[02/13] US-led oil sales from Venezuela to bring in $5
billion in months, energy chief Wright tells NBC News"

---
