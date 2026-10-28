# Week 43


"@skyglowberlin@fediscience.org

Half of the electricity consumed by Dublin is now used by data centers"

---

"@hembrow@todon.eu

So today some of the worst people on earth using the most
environmentally destructive tools on earth brought down a huge part of
the internet by exploiting a potential problem found many years ago in
PHP which was previously not practical for anyone to exploit.

It only became 'practical' to exploit this problem because 'AI' came
along to automate the boring and repetitive work required to do
so. Absurd amounts of computing power were applied specifically to
break into other peoples' websites.

Now the same people who are behind this are trying to pretend that
they're heroes for finding an exploit.

'AI uncovers critical vulnerabilities', their headline reads. But the
vulnerability was only made to be critical by the very same people as
hide behind that headline.

Many thousands of websites are offline, many people are losing money,
many thousands of people are working hard to try to patch or work
around the problem, many small guys are finding it almost impossible
to patch, and we're all supposed to be thankful to OpenAI and others
involved? Nah. Fuck off.

Everything about 'AI' involves a lot of externalized costs, but I've
still yet to see even a single positive thing that has been achieved
by 'AI'. That has definitely not changed today.

\#php2shell \#php \#fuckai \#openai"

---

"@GossiTheDog@cyberplace.social

OpenAI ambulance chasing the PHP vulnerabilities and pretending they
found and disclosed them (they did not) is disgusting. It’s a media
play and it’s really gross, and says a lot about OpenAI."

---

I would not teach LLM internals / coding at universities, I would
teach hands-on, very detailed neural machine translation (NMT) which
use the same base techniques, then briefly mention "you can turn this
approach into a hallucinating stochastic parrot slop generating
machine" and roughly cover the extensions required for that, that's
it.

---

"@tante@tldr.nettime.org

[It passed](https://codeberg.org/Codeberg/org/pulls/1253#issuecomment-19820434).

Codeberg bans vibe coded slop"

---

That's funny.. bcz it was his idea

"@magnusmanske@wikis.world

Ok, seriously, whose bright idea was it to write Wikipedia software
and much of the ecosystem in PHP of all things?!?

Oh wait..."

---

ABC News: "Nearly 70% of the internet is estimated to use PHP,
including WordPress, which is used for more than 40% of websites."  "

---

Everyone likes free stuff, especially those high-flying capitalist
jagoffs

---

PHP is FOSS. It is used by many. Facebook started out with PHP (later
modified its runtime, and some other aspects).  Many sites use PHP.

---

The Internet runs on free software, held up by freely contributing
people to said free and open software. Help them help you until more
"systemic changes" arrive.

---

"@dvk@toot.re

I just sponsored [oerdnj](https://github.com/sponsors/oerdnj).
Go sponsor your open source dependencies!"

---

"@dvk@toot.re

[FOSS developer] Ondrej backported the PHP patch to PHP 7.4 while on
vacation.

Can't think of anything more impactful today."

---

"eniko@mastodon.gamedev.place

'Not every billionaire is a policy failure,' argues an opinion piece
in the FT.

Comrades, we're winning the argument. They've conceded the broad
principle and are reduced to haggling over details."

---

Russiagate was all about shoring up support for the
military-industrial complex, its supporters and its goals. Politically
it aimed to help an MIC stooge, Hillary Clinton, that was the bonus.

---

TAC: "Remember Russiagate?... The trick was to link this project with
the political passions stirred up by Donald Trump. It worked like a
charm. There is now an army of liberals who are almost as obsessed
with Russian President Vladimir Putin as they are with President
Trump...

The evidence suggests there will be a second attempt at Russiagate
after the midterms. The immediate goal will no doubt be to shore up
support for the Ukraine war. But smarter operators behind the scenes
may also understand that the situation on the Ukrainian frontline is
hopeless, and that it is highly unlikely that the conflict will still
be raging by the time Trump leaves office. They are therefore looking
for new places to continue their pressure campaign against Russia—the
Balkans, the South Caucasus, anywhere Kremlin influence can be
plausibly alleged."

---

"@jonny@neuromatch.social

By the way, everyone already knew this, but 'Muse was written with
Claude' confirmed by the sourcemap comments. If i was a meta engineer
i would be a liquid composed primarily of shame by volume, attempting
to mop myself up off the floor but being continuously juiced back out
by having to live the lie that i am not merely a cog in the machine of
the company at the top of a single leaderboard: burning the most money
on that fuckin boondoggle."

---

We need to socialize capitalism

---

It appears crisis happens right after peak or during a bottom of PEGY.
We are getting there.. PE is falling, dividends flat, earning growth
rising.. Why does that lead to crisis? Capitalism is a fight between
labor and capital, the rich get richer keeping more of the profits,
nothing trickles down which pisses off the rest, their demands become
more vocal. Eventually, crisis. On the streets or in the markets.

---

Yes we can

```python
window=3
df = u.get_pd().read_csv("schiller.csv", index_col='Date', parse_dates=['Date']).sort_index()
df = df.resample('YE').last()
df['PE'] = df['S&P Comp P'] / df['Earnings E']
df['Div Yield %'] = (df['Dividends D'] / df['S&P Comp P']) * 100
df['E Growth'] = df['Earnings E'].pct_change().rolling(window).mean() * 100
denom = df['E Growth'] + df['Div Yield %']
df['PEGY'] = df['PE'] / denom

df[df.index > '1980-01-01']['PEGY'].plot(ylim=(0,5))
plt.axvspan('1990-09-01', '1991-07-01', color='y', alpha=0.5, lw=0)
plt.axvspan('2001-03-01', '2002-01-01', color='y', alpha=0.5, lw=0)
plt.axvspan('2007-12-22', '2009-05-09', color='y', alpha=0.5, lw=0)
plt.axvspan('2020-02-01', '2021-02-01', color='y', alpha=0.5, lw=0)

cols = ['S&P Comp P','Div Yield %','E Growth','PE','PEGY']
df[cols].tail(4)
```

```text
Out[1]: 
             S&P Comp P  Div Yield %   E Growth         PE      PEGY
Date                                                                
2023-12-31  4685.051500     1.500596  36.302089  24.346783  0.644049
2024-12-31  6010.908571     1.244941   2.638639  28.600222  7.364396
2025-12-31  6853.025455     1.160363  11.702018  28.479041  2.214134
2026-12-31  7450.032857     1.096682  15.489323  25.221168  1.520629
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/478/053/881/309/278/original/7314ec34c3cd6fdf.jpg'/>

---

Schiller data contains total SP 500 dividend values too.. Can we do
PEGY calculation at SP 500 level in that case?

---

Reuters: "The developers of the widely used PHP programming language
said on Wednesday they would release patches for two critical
vulnerabilities, as EU cybersecurity officials warned organisations
unable to apply the fixes should take affected websites offline... PHP
is used across large parts of the internet, and speculation has
circulated ​over the past day that websites running the software could
be exposed to serious cyber intrusions."

---

Why do they still call the now-gone Orban government a "regime"? There
was an election, power changed hands. Clearly there was democracy,
clearly there wasn't an everlasting "regime".

---


If NMT and LLM tech share the same basis, would NMT also suffer from
halucination issues? Yes.. but likely NMT suffers less. LLMs are
trained on massive amounts of text trying to predict that next word,
LLM inputs within the chat session are open-ended... A neural
translation system on the other hand is trained on clear-cut sentence
*pairs*. For a given sentence in one language, there is always the
*right answer*, as label, inside the other pair. IMO there is less of
a chance of going wrong during inference after that type of training /
input compared to LLM's.

---

\#BlockBlast \#Ads

[[-]](https://www.instagram.com/p/DecfvksvHiW/)

---

"toxi@mastodon.thi.ng

Ken Thompson, 1983: wouldn't it be awful if someone snuck secret code
into a compiler that broke our ability to trust the output of a
computer

AI Guy, 2026: wouldn't it be cool if we stuck something we know can't
be trusted into every part of the computer"

---

The Lever: "Ken Salazar Is Campaigning Against A Tax On People Like
Ken Salazar.. Obama’s former interior secretary is using workers and
right-wing spin to attack a tax measure that could cost someone
earning his former salary an extra $111,000 a year."

---

*Dissenting POWs: From Vietnam`s Hoa Lo Prison to America Today* by
Tom Wilber and Jerry Lembcke

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/474/558/543/412/821/original/eedbb62f209802a3.jpg'/>

---

First use of GPUs for general purpose sci computation tasks appears to
have started around 2003, thanks to researchers at Technical
University Munich and independently at Caltech. 

---

For the first time I saw Ecosia beating Google Search - found what I
was looking for on the first page \#Ecosia

---

"@futurebird@sauropods.win

How the heck is a girl supposed to write a creepy SF micro fiction
when these goobers keep just literally doing the thing that I wanted
to be ominous and portend dark futures about???"

---

\#TheNewMiddleEast \#AlJazeera

[[-]](https://youtu.be/qRrtN8YSoVQ?t=685)

---

\#Yemen 10/07 - 10/20

[[-]](ymndata/map09.html)

---

Seymour Hersh, *The Dark Side of Camalot*: "The crisis worsened later
that afternoon, when it was learned that a Soviet surface-to-air
missile had shot down an American U-2 spy plane during an
intelligence-gathering overflight of the island... [RFK wrote] 'There
was the realization that the Soviet Union and Cuba apparently were
preparing to do battle. And there was the feeling that the noose was
tightening on all of us, on Americans, on mankind, and that the
bridges to escape were crumbling.'.. Kennedy was losing control..

In *Kennedy*, his 1965 insider's memoir, Ted Sorensen described what
happened next.. Sorensen wrote, the Kremlin announced that 'Kennedy's
terms were being accepted.. I [was] hardly able to believe
it'.. Sorensen's published account was a half-truth. As he knew, and
would not reveal for twenty-seven years, the crisis was resolved when
Bobby Kennedy, on behalf of his brother, held a last-minute meeting
with Dobrynin and made a secret arrangement to give Nikita Khrushchev
the trade he wanted - Jupiter missiles removed from Turkey in exchange
for withdrawal of Soviet missiles from Cuba."

---

Noam Chomsky, *Rethinking Camalot*: "Another favored idea is that JFK
had become a demon to the military-industrial complex because he was
going to end the Cold War. To assess the thesis, we may turn again to
the speech he was to give in Dallas on the day of the assassination,
with its proud boast about his vast increases in Polaris submarines,
Minuteman missiles, strategic bombers on 15-minute alert, nuclear
weapons in strategic alert forces, readiness of conventional forces,
procurement, naval construction and modernization, tactical aircraft,
and special forces. JFK military Keynesianism had raised Pentagon
spending from $45.3 billion in 1960 to 52.1 billion in 1962"

---

"@bridget@beige.party

The only death penalty i support is a corporate death
penalty. dissolve corporations that egregiously break the law"

---

"@GossiTheDog@cyberplace.social

The FBI say they suspect a ransomware negotiator at a cyber firm - no,
not one of the prior arrested cyber vendor people - ran ShinyHunters
extortion site.

I've been saying this for years - the cybersecurity industry has many
people who their hands directly in the pie.

The status quo sucks and governments really need to legislate around
cyber ransom and extortion payments.  Lots of cybersecurity things at
vendors have become normalised which are not normal."

---

Britain's rivers are polluted by shit, and political sphere is
polluted by Zionists. I see a parallel.

---

Al-Jazeera: "UK PM adviser’s wife expresses ‘support’ for Palestine
Action.. Police reviewing social media post by writer Sarah Helm, wife
of Burnham’s National Security Adviser Jonathan Powell. [She wrote]
'God help us authors who support Palestine and Palestine Action'..

The UK government outlawed Palestine Action in July 2025, after
activists from the group broke into a Royal Air Force base and sprayed
red paint on two aircraft to protest against UK military support for
Israel’s genocidal war on Gaza. Being a member or a supporter is
punishable by up to 14 years in prison."

---

"Eating London’s sewage vegetables.. Tomato plants are sprouting on
London’s polluted rivers. You don’t want to know how they got there.
When life gives you vegetables, make chutney"

---

Politico: "Maybe There Was an Egg Cartel After All.. For years,
economists dismissed collusion as crankery and blamed bird flu for
high prices. Then the feds found evidence that could prove the cranks
right, and almost nobody noticed...

Investigators found what they considered evidence of a scheme in which
three of the country’s largest egg producers coordinated inflated bids
to a central price clearinghouse so as to artificially drive up prices
in ways immediately felt by consumers, as the U.S. Justice Department
and 17 state attorneys general outlined in a lawsuit"

---

"I’ve decided to archive the source code of my [programming language]
Ruby [packaged code] gems to make it clear that I’m no longer working
on them.. I no longer feel inspired to contribute to a commons that’s
being strip-mined by massive corporations to feed the very machines
whose unthinking output pollutes it."

---

Politico: "'Little of it was constructive’: GOP bemoans a distracted
Trump in midterms’ final stretch"

---

Warren Buffett: "Don't ask the barber whether you need a haircut"

---

By now everyone knows George Noble is a protege of Peter Lynch. Whenever
this guy is on a show they repeat it ad nauseam.

---

NVidia is calculated to be underpriced.. Well if you agree with the
current growth projections, yes, that makes sense. Apple looks about
right.. it's a known stock, no NVidia, there is a bubble in everything
tech, so the stock is likely overbought.

---

```python
u.yf_pegy("NVDA")
```

```text
PEGY: 0.21
```

```python
u.yf_pegy("AAPL")
```

```text
PEGY: 1.36
```

---

So it goes like this?

$$
PEGY = \frac{P/E}{Growth + DivYield}
$$

Values under 1 would signal underpriced, greater than 1 overpriced

---

"The PEGY ratio was popularized by legendary investor Peter
Lynch.. [he] originally championed the PEG ratio (P/E divided by
Growth Rate) as a way to find growth stocks trading at reasonable
valuations. However, he recognized that the PEG ratio unfairly
penalized dividend-paying stocks. The PEGY ratio solves this by adding
dividend yield to the growth rate, giving credit to companies that
return cash to shareholders"

---

"@mhoye@cosocial.ca

'Accenture decides to spend less on AI per employee per month than
they spend on coffee and snacks' seems like a signal."

---

Fortune: "Accenture Clarifies Claude Spending Limits As AI Cost
Questions Grow"

---

The Onion: "Protestors Criticized For Looting Businesses Without
Forming Private Equity Firm First"

---

Gibbs, *Corporate Power and Globalization in US Foreign Policy*: "The
need to contain the European quest for foreign policy independence
also entailed an economic dimension...In seeking to avoid the trading
bloc scenario, American officials sought to use NATO as a means of
binding Europe to the United States, and maintaining US access to
European markets. True, NATO was officially a military, not an
economic organization. But the alliance also had a vital economic
function..

[NATO commander Wesley Clark said] 'As a result of.. [economic]
interests, we have continued to maintain a strong military presence in
Europe.' .. US investors, both in the military and nonmilitary
sectors, expressed strong support for maintaining the military
alliance with Europe. During the lead-­up to NATO’s fiftieth
anniversary celebrations in 1999, support for continuing NATO was
expressed by both military-oriented corporations including Boeing,
Motorola, TRW, and United Technologies; as well as nonmilitary ones
such as Eastman-Kodak, Ford, and General Motors (Smart 1999). Once
again, we see that military action and globalization are not at all
incompatible, and indeed militarism in this case went hand in hand
with globalization...

[1999] was a period of great anxiety, regarding the stability of the
world economy. Policymakers were preoccupied with international
economic turmoil, in the aftermath of the 1997–1998 international
economic crisis. A major US hedge fund collapsed in 1998, and there
was a brief though widespread fear that this was a harbinger of even
greater instability (a danger that was surely increased by the
misguided policies of the Clinton administration itself, which
supported austerity measures in the most economically unstable
countries)...

In short, the military–industrial complex model outlined above fits
the facts of the Kosovo case in several important respects: As we have
seen, the military procurement companies appear to have supported the
war and they clearly benefited from its effects, both in terms of the
increase in military spending that resulted from the intervention, as
well as the way that the intervention helped to preserve the NATO
military alliance. Many nonmilitary investors also supported the
intervention, in order to showcase US power and thus intimidate
radical governments or insurgent groups who might threaten valuable
capital assets. And intervention was viewed as a means to ensure
macroeconomic stability after the 1997–1998 economic crisis."

---

"Microsoft admits Windows 11 has a GDID tracker with no off switch,
first documented publicly in an FBI hacker complaint"

---

NYT: "Wall Street investors have been bidding up the price
of.. instruments that insure corporate debt against default, such as
those insuring SoftBank, the Japanese technology colossus that has
borrowed heavily to bet its future on a partnership with OpenAI.

The recent market moves could spell losses for investors that own the
companies’ existing bonds and could mean the companies will be forced
to pay higher interest rates when they borrow again, raising the costs
of their already wildly expensive A.I. projects."

---

Maybe Linus is getting softer at older age. Back in 2000 [someone](http://xancatos.org/debuggers)
asked him to include a debugger in the Linux kernel codebase. He
doesn't want the tool, and goes further, doesn't want the *person* who
would need such a thing, ie the exclusion of the debugger is almost
like a filter that will keep a "certain type" of programmer out of the
project. LLMs could be seen that way, but their output is accepted.

---

Allowing LLM for Linux development can be a PR problem. Kernel coding
was always seen as the pinnacle of programming pizazz, skill. Now some
dipshit with LLM can send some code, and that will be perceived as
quality has been lowered. 

---

"@exchgr@mastodon.world

Getting the fediverse to turn on linux is quite the achievement. great
job, linus! 🎉"

---

MIC didn't even bother with JFK, he was a tool, useful for
them. Another part of the private complex / surface state did him in,
the MIC would have stayed neutral, tentatively okay'ed the move, bcz
the incoming president would be fine for them too.

---

Clintons were "cleared" before their WH run, they were *allowed* to
reach the Presidency because it was clear they would play ball within
the constraints of the system. How did they know? There are many
signs.. Nixon was toppled via a military-industrial complex plot, he
was set up, and [look](https://media.mastodontech.de/media_attachments/files/117/466/138/426/081/300/original/73fe506b18b5abfb.webp)
who is on the impeachment unquiery team. These are all signals that
you were on the "right team", "right side" of things.

---

Don't be mad at Kaya Callas. Be mad at the dynamic which put her
there.

---

If the EU was cucked by US during the Balkan Wars per D. Gibbs how
come they oppose US now when WH disagrees w/ Ukraine? Europe back then
was cucked by the US military-industrial complex - via their stooges
in the White House, the Clintons - who wanted to continue the war,
involve NATO. After Europe's humiliation their entire elite structure
was shaped by that state of affairs, the new power dynamic of the
world. Now the same US MIC wants the war in Ukraine to continue, and
the top echelons of EU play along with that, they are by now staffed
by the sort of people who are totally in sync with it. There is no
discrepancy here.

---

NBC News: "Brazil’s Lula wins electoral court challenge against Meta
for alleged pro-Bolsonaro algorithm bias"

---

"@FranceskAlbs@mastox.eu

.. Neither Cartier-Bresson, Banksy nor Cold War Steve could have come
up with such an image. Absolutely perfect composition and lighting
(even the road signs are perfect)! 😍"

<img width='340' src='https://static.mastox.eu/media_attachments/files/117/448/854/027/416/631/original/01c64bf3b78d4531.jpeg'/>

---

"@toxi@mastodon.thi.ng

If the three+ decades of free (ab)use and lack of participation /
reciprocation (financially or otherwise) of commercial players and
governments have not killed FLOSS software projects / culture, it very
much feels like LLMs and their euphoric adoption are finally
succeeding with that by now, in some sense even in a suicidal manner"

---

NBC News: "Hormuz ship attacks hit record high as Iran escalates
strikes"

---

"@carnage4life@mas.to

The past week, and yesterday in particular, were brutal for chip
stocks.

Anthropic’s slowing revenue growth has added to investors’ fears that
AI companies won’t generate enough revenue to justify the trillions
being committed to data centers.

A very dotcom bubble shaped pattern is forming 🫧"

---

"@eniko@mastodon.gamedev.place

Ah, yep, the pivot to the next Big Tech Thing™ is starting now, with
it being quantum computing just like many people predicted.. AI is
fucking done for lmao"

---

"@gabrielesvelto@mas.to

Alright folks, taking bets now, who gets to be the Lehman Brothers of
tech?

- Oracle
- CoreWeave
- SpaceX
- Nebius"

---

D. Gibbs says William Perry *himself* commented back in the 90s
(Clinton era) that the Russians were "losers, and we do not need to
honor our agreements with losers". The Borger excerpt below suggests
Perry "asked around" and the response he got *from others* was "who
cares what [Russians] think, they’re third-rate". Which side is
correct? Perry could be re-writing history here, but he sounds like he
is regretful now US expanded NATO borders eastward. He should be.

---

Borger, *The Guardian*: "[2016] William Perry says US contempt toward
Russia as 'third-rate power' after end of Cold War played a big role
[in rising Russian hostility]... Perry said the decision reflected a
contemptuous attitude among US officials towards the troubled former
superpower.

'It wasn’t that we listened to their argument and said he don’t agree
with that argument,' he said. 'Basically the people I was arguing with
when I tried to put the Russian point ... the response that I got was
really: "Who cares what they think? They’re a third-rate power." And
of course that point of view got across to the Russians as well. That
was when we started sliding down that path'"

---

There are a lot of gems in that talk, how US torpedoed early deals in
Bosnia, Kosovo, how the EU was cucked, and how military-industrial
complex works. They make wars to make wars, and the strategery in the
traditional IR sense is only an afterthought, shaped around that
primary business interest.

---

\#DavidGibbs \#MIC \#NeutralityStudies

[[-]](https://youtu.be/EcHX_2v_yyM?t=713)

---
