# Week 24

The Lever: "Newsom Declares War On Behalf Of California’s
Billionaires.. The governor is leading a coalition to squash a
one-time 5 percent wealth tax on California billionaires."

---

CNBC: "SpaceX options debut signals 'expensive' and 'dangerous' bets,
strategist says.. Options on SpaceX have started trading after the
company's IPO, and they show a wide variation in bets."

---

I still would not call LLMs probabilistic. Boltzmann Machines are
probabilistic. The entire structure is a stochastic neural network.

Before Hinton went senile he was researching that stuff, purely
stochastic networks, "Restricted" Boltzmann Machines... There could be
more to do there.

Machine learning's domain is inherently noisy, and we always see
"samples" of the real world not the thing itself. Why not use the part
of mathematics that is prepared to deal with that?

---

It looks like JEPA uses Energy Based Methods but does not use
probabilistic machinery as EBMs traditionally do.

---

ML attempts to simulate thought, but where is the equivalance of "mass
conservation" in physics? 

---

Investigating the real mechanism of thought will not hurt.. We know
how fluids work at a molecular level, have one grand formula
explaining them - that helps formulating pure simulation approaches
even though the computation approach does not mirror the physics
one-to-one. 

---

Some simulation methods are better than others, surely. LLM is only
one of the choices. 

---

Another parallel: neural networks. NNs are bottom-up approaches,
starting with small (neurons), connections (weights), the system
simulates, supposedly the functioning of a brain.

---

G. A. Bird (inventor of DSMC) says about his method "the relative
positions of the molecules within [a block are] disregarded when
choosing collision pairs". Velocity and position info are uncoupled?

For LBM, another simulation method, specific velocities are unknown,
positions are hidden inside large pockets, we track "directional
density" and a global average velocity.

A parallel: Doesn't Quantum Mechanics say "we cannot know position and
momentum of the electron at the same time"? Is QM a simulation method?
It is not the reality itself (long suspected), but a way of
computation. Through the way we measure, interact with smallest realm,
are we triggering results that are computational, not fundamental?
That fits with another QM edict "shut up and compute".

---

Notice the draconian response to protests against Elbit. The moment
you even **touch** the interests of the global military-industrial
complex, "the system" reacts. 

---

"@GossiTheDog@cyberplace.social

The vibe I'm getting from lots of people at lots of orgs now is, you
know during Fyre Festival, that marketing dude was like 'Let's just do
it and be legends, man!' when challenged about issues?

That's the GenAI plan fundamentally.  Lots of people are making
decisions without really knowing what they're doing, because everybody
else is doing it.  FOMO marketing."

---

"@GossiTheDog@cyberplace.social

Was just talking to a friend at a US technology company, they’ve had
their budget reduced by 50% as the company says it wants to announce
'the largest layoffs in US corporate history' to prove GenAI can
replace jobs.

There’s no plan to actually replace the jobs with GenAI.. they just
have to decimate their area.

Not naming company as the staff don’t know they’re about to fed to the
line going up."

---

Reuters: “A U.S. Air Force B-52 Stratofortress bomber crashed on
‌Monday shortly after takeoff from Edwards Air Force Base in Southern
California's Mojave Desert, and all eight crew members aboard were
presumed to have been killed, the base said.

The eight-engine, jet-powered aircraft, built to carry nuclear and
conventional bombs, was on a routine ​test mission when it went down,
Edwards said in a statement about four hours after the ​crash.”

---

An official name change requires congressional approval, still Sec of Defense

---

Looking at the speed SecDef is collecting nicknames, we can say he is
a divisive figure. Pistol Pete. Hegdeath. Kegseth (for talking to
press as if right after having done a keg stand -courtesy of
SNL?-). Secretary of War Crimes. Pete **Hague**seth (as in *The
Hague*, ICC HQ).

---

"@briankrebs@infosec.exchange

Bitcoin has lost nearly half its value since reaching a record high
above $123,000 in July 2025, CNBC writes. Funny how so many of the
people hyping AI once hyped virtual currencies. Kind of makes you
wonder about the odds on the massive all-in and circular bets being
placed on AI."

---

ECI measures the diversity of products of a country, not just how much
money they earn making them. This line of reasoning is from Cesar
Hidalgo, he was able to show the link between ECI and economic
well-being.

The corollary is product diversity requires in-house (within same
country) expertise as tacit knowledge requires proximity to
spread. ECI could be seen as an argument against globalization, or
comparative advantage - France and UK should not focus wine and cloth
respectively, **both** should produce wine **and** cloth, bcz that
would raise their economic complexity index, they would be better
positioned to innovate on a third product if there are skills in the
country that can do both.

---

Australia's Economic Complexity Index is pretty low, lower than what
might be expected from a developed country. Resource curse?

[[-]](https://atlas.hks.harvard.edu/countries/36)

---

Methven, Novara Media: "Direct Action Is Now Terrorism.. And we should
all be terrified. Last Friday at Woolwich crown court, Mr Justice
Johnson sentenced four Palestine Action activists to a total of nearly
27 years (Nelson Mandela’s term in prison) for their role in an action
on the Bristol-based research centre of an Israeli weapons factory.

[T]errorist derangement syndrome is no joke. Especially when it
infects the courts. The damage caused to Elbit was substantial 'to the
point of destruction', Johnson said. But the four came nowhere near to
the destruction of Elbit. What’s more, while the damage was valued at
over £1m, in 2025, Elbit’s gross profit was nearly $2bn, buoyed by
Israel’s genocide in Gaza. Calling a million substantial against that
is like breaking an egg and calling it murder."

---

LBM, DSMC are so simple at a base level, it shocks people they can
simulate complex air flows, turbulence, vortices.. But they do. The
trick is noticing that eg LBM embed physics in a different way, but no
less accurately. They are very careful on conservation of mass,
momentum, do fantastic bookkeeping on all its probabilities, for LBM
the constant controlling relaxation toward equilibrium is equivalent
to viscosity, so the simulation works, and it is physical.

---

DSMC, and Lattice Boltzmann Method are *probabilistic* too. Both can
be proven to converge to their respective grand formulas -
Boltzmann / Navier-Stokes analytical models.

---

Simulation methods work *bottom up*, you work with grid / molecule /
pockets of molecules first, compute the local, neighboring effects,
and watch what happens to the overall system... The alternative
computation methods start with a grand formula, chop that up /
discretize it, then compute. Both can work, but we need to stress a
lot of external interactions, special cases are difficult to include
in discretized grand formulas, and they are easier to include in
bottom-up simulation methods.

---

Some in science look down on simulation methods / formulations
implying that such methods are only a facsimile of the "real thing"
(by which a grand analytic formula is meant). But the creator of DSMC
(a simulation method) G. A. Bird argues against that:

>It is important to recognize that the derivation of a mathematical
>model such as the Boltzmann equation depends on the same physical
>arguments that have led to the DSMC procedures. A sound physical
>simulation model should therefore have the same standing as a
>mathematical model.  While analytical comparisons are valuable and
>instructive, it should not be necessary to demonstrate that the
>results from the physical simulation model are equivalent to a
>solution of any mathematical model.

---

\#SpaceX \#Boyle

[[-]](https://youtu.be/wKXgeNwNRJ4?t=1172)

---

Suriyak: "Israel rejects peace. 🇱🇧🇮🇱

Despite the announcement of the memorandum between Iran and the U.S.,
Israeli forces have not only shown no intention of de-escalating the
conflict but have intensified their attacks in Lebanon. On June 14,
Israeli forces launched a powerful attack on the southern suburbs of
Beirut, leaving people dead and wounded. The attack was strongly
criticized by Iranian authorities, who warned that peace was only
possible with a complete cessation of hostilities across all
fronts. This jeopardizes the signing of the memorandum scheduled for
this Friday.

According to the Lebanese Ministry of Health, Israeli aggression in
Lebanon has left 3,783 dead and 11,699 wounded since March 2."

---

The Guardian: "In its manifesto [newly elected Hungarian] Tisza
promised a 1% annual tax for those with assets of more than 1bn
forints (£2.4m), applied to the portion of their estate above that
threshold. Property, shares in companies and assets held abroad would
all be counted, [PM] Magyar said.. as would possessions such as
yachts, private jets, paintings and sports cars"

---

\#SpaceX \#Chanos

[[-]](https://youtu.be/LoLdN9Q9hwU?t=151)

---

That's fair.. I agree with that score

```python
u.rottentomatoes("Fast Charlie")
```

```text
Out[1]: {'critics': '83', 'audience': '80'}
```

---

Gave LLM a sample of a raw page output, told which numbers to look for
on a sample movie, it wrote bunch of bizarre code. The code retrieved
one score, failed to get the other. It was a simple "regex" task.

---

Attempted to vibe code it, LLM failed at the task. This thing is sentient!

The scraper is now handcoded, as before.

---

Rottentomatoes keeps changing the HTML coding of its page output, I'm
having to modify my scraping code all the time... grrr

---

The Atlantic: "[Chappie] James was eventually promoted to four-star
general, becoming the first Black American in the history of the
U.S. military to reach that rank...

[Recently] people in the Pentagon noticed that a painting of James had
been taken down from its prominent location in the Air Force Art
Gallery. Instead of putting a new painting in the spot where James’s
portrait had been, the Pentagon kept the space empty..

At a 1987 ceremony dedicating an aerospace-science and
health-education center at Tuskegee University to James, Ronald Reagan
called him a 'darned good pilot and a revered military officer and a
truly great American.' In 2020, the state of Florida named a bridge
after James; the bill was signed by Governor Ron DeSantis"

---

She played it textbook. It's good. The audience seemed like it \#TomSawyer

[[-]](https://youtu.be/zcl_yvUVG7U?t=147)

---

Rush has a new drummer (legendary Neil Peart passed away in 2020). The
drummer is a chick, not even American or Canadian, from Germany.

---

"In the late 1990s, two farmers, Doug Bower and Dave Chorley,
confessed to single-handedly starting the entire crop circle
phenomenon in 1978 using ropes and a plank of wood. Others began
coming forward, revealing innovative ways to sneak into even a guarded
field undetected and rapidly flatten crops into a circle. It was all
very low tech; most pranksters simply walked through dry fields when
nobody was looking. Crop circle 'experts,' reluctant to give up
lucrative TV hosting gigs, resisted the hoax explanation but
eventually had to concede that they’d been duped. Perhaps, like Fox
Mulder, they wanted to believe"

[[-]](https://daily.jstor.org/pssst-crop-circles-were-a-hoax/)

---

Crop circle phenomenon is a proven hoax. Even the most radical
theorizers have moved on from that one. Apparently Spielberg didn't get
the memo.

---

Watched *Disclosure Day*.. good action, good acting, but the writing
was stuck on old ideas... the flick was even boring at times,
logically disjointed. Strange. 

---

True... *Game of Thrones* is actuallly a zombie story, can be
categorized as such.

---

\#Gallagher \#Consumer

[[-]](https://www.youtube.com/shorts/SYSa4RzaH80)

---

The Guardian: "Aukus is among Australia’s worst foreign policy
decisions and requires 'heroic' optimism, Gareth Evans says.. Former
Labor foreign affairs minister says belief US would defend Australia
in event of an existential attack is a ‘ludicrous delusion’"

---

Paper: "[2016] Quantum theory cannot consistently describe the use of itself"

[[-]](https://arxiv.org/abs/1604.07422)

---

"@ProPublica@newsie.social

NEW: Cancer drug Revlimid is one of the bestselling pharmaceutical
products of all time, with total sales of over $100 billion. It also
cost nearly 1,000 dollars per pill, even though that same pill cost
just 25 cents to make."

---

"Academic publishing giant Elsevier announced Tuesday the launch of
Paywally And Friends, a new animated series for children ages three to
seven that teaches young viewers the importance of restricting access
to information, the moral value of copyright transfer, and why sharing
is wrong when what you’re sharing is a publicly funded research
article.

The series follows Paywally, an enthusiastic anthropomorphic padlock,
and his friends Impacta the Fox (who teaches children about journal
prestige), Embargo the Turtle (who explains why some knowledge must
wait twelve months before anyone can see it), and a villain called
Open Access Harold, a raccoon who steals PDFs and distributes them to
people who want to read them."

---

Meta is not a cloud service provider, but they know scale, just like
Amazon knew scale from running its own servers. Meta could be a
player.

Google already made its move. They are debasing, *cheapening* the
concept of an LLM, experts already knew the tech was no big deal, but
GOOG is making the economics of it obvious. By releasing a competitive
LLM freely they are undercutting everyone else, hoping their cloud
service will get customers anyway where LLM is just another component
in the service stack. To them this stuff will be a like a database,
web server or a boring email server. Choose from dropdown, click on
'install' button, done. If not here is the free version, install at
home on a beefy gaming computer, you'll come back to us for bigger
scale.

---

Open (data) source LLMs are nearly as good as "frontier models". 

Plus, let's not forget, LLM progress has stalled. Dowd used the
"c-word" here, just like I did in earlier posts: the tech is in its
commoditization phase. Soon the whole industry will devolve into a
dirty cage match, everyone undercuting everyone else, racing to the
bottom, and only orgs with previous cloud expertise will survive.

---

\#EdDowd \#LLM

[[-]](https://youtu.be/ioJ4Pfnu05s?t=1409)

---

I bet there is more intermediate level chess play data available than
advanced, high-end level play, and since LLM tech is based on neural
nets, and they need data to imitate, they would fail at advanced
levels do okay at beginning levels bcz NN had data for the former, not
for the latter.

AlphaGo Zero, also based on neural nets, was successful but it
*created* its own data, at all levels. It would play against itself,
again and again, so it would have created a chain of moves from
beginning to end that it could "learn from" during those plays (its
game rules were hard-coded into the program, they were not learned)

LLMs fail to learn to rules (not AGI), and fail to win at advanced
levels. This proves they are not thinking, not in the way humans call
the process.

---

Reshare

"I tried playing the new Claude 4.5 model in a game of chess. It did
really poorly. It played a coherent opening and was difficult to play
against for the first ten or fifteen moves, then everything fell apart
and it started blundering and even making some illegal moves."

---

An ex-collague says at his IT company, they are teaching junior
developers how to use LLMs, have not fired them. That's good..

---

Werdmuller: "I’ve seen some pretty dumb stuff out in the wild: leaders
who have expected their engineers to dramatically increase their
output to inhuman levels, company-wide token leaderboards, product
managers who believe they can replace real user research with
synthetic personas, and, of course, high-level leaders who think they
can replace their human workers with AI agents.. I think Mike
Masnick’s prescription is accurate: many CEOs are so distant from the
actual productive work of a company that they miss the complicated
nuance of what goes into it."

---

David Osland: "We are told pensions are 'unsustainable', the Post
Office is 'unsustainable' and now the NHS is 'unsustainable'. They
were all entirely sustainable before the private sector starting
looting the public sector"

---

"Landmark German ruling declares Google's AI Overviews are Google's own
words and makes it liable for false answers"

---

AIPAC and defense contractors.. Two peas in a pod

---

David Hogg: "MORE GREAT NEWS!! @leaderswedeserv candidate [Mai Vang]
just beat 21-year incumbent and 81-year-old Congresswoman Doris
Matsui. Vang and Matsui (a billionaire who took a max-out AIPAC check
and $ from defense contractors) will face off again in November."

---

At some point Americans could become migrants, refugees, fleeing the
country, flooding into Mexico, Canada. Maybe then Mexico will happily
build and pay for a wall to keep out the unwanted gringo.

---

"@victorvonvortex@mastodon.social

They are going to steal what's left of your Social Security."

---

"As Mike Johnson Floats Social Security Cuts, Trustees Report Shows
Harm of Trump Policies"

---

Tech Fixated: "Mexico cuts workweek, bans after-hours contact, and
guarantees no worker will take a pay cut in the most sweeping labor
reform in a generation"

---

"@ketan@climatejustice.social

I don't think Anthropic really meant it this way but what an amazing
demonstration of why generative AI's energy consumption is only
getting worse, and dirtier. 'Improvements' only come from nesting
chatbots within chatbots, rather than any fundamental smarter
design. It's wasteful at every single level. It's Bitcoin x 1000"

---

Glenn Diesen: "After Russia invaded Ukraine, the former Norwegian
foreign minister actually argued that 'this is not the time to
understand, but to condemn'. This ridiculous position is pushed on
academics. However, understanding is not endorsement, explanation is
not advocacy, and ignorance is not strength. I argue it is in Russia's
security interest to push NATO away from its borders, it is in Iran's
interest to control the Strait of Hormuz, and it is in China's
interest to create a new international economic architecture. This is
not advocacy, nor is it a normative position about how the world
should work; rather, it is a recognition of how the world actually
works."

---

"@nicole@oldbytes.space

We're moving Super Mario Bros. to an agentic workflow. Rather than
controlling Mario, you'll simply prompt the agent with something like
'beat 1-1', and it will take direct control of Mario for you. This
frees up more time for more important things like doing your taxes or
being stuck in traffic"

---

"@jalefkowit@vmst.io

'How do you describe the noise [from the data center] to people who
don't live here?'

'If it were like a highway that never stops'"

---

WYMT: "Graham Platner wins Democratic nomination for U.S. Senate in
Maine..  Veteran and oyster farmer will challenge 5-term incumbent
Sen. Susan Collins in November..  Platner [woved] to defeat Collins
'and the billionaire class she represents.'"

---

\#Ukraine 06/02 - 06/10

Kostiantynivka is a goner

[[-]](ukrdata/map11.html)

---

NYT: "'The Most Bipartisan Issue Since Beer': Opposition to Data
Centers"

---

Fox News Poll: "Voters see AI regulation as urgent, rank safeguards
ahead of innovation"

---

I was thinking abt this the other day - how ed can grade people in
today's world. The only thing that can work now is THE EXAM where no
phones are allowed.

---

"@ariarhythmic@ohai.social

@peter The reason this is happening is ChatGPT is a perfect fit to
what the education systems has demanded all along, which is busywork
for the sake of busywork, lengthy writings that hold no meaning,
time-consuming assignments that serve no purpose.

LLMs are *great* for this! It's not that they've fundamentally messed
up the system that was, it's that their presence is shining a
spotlight on how shitty it's always been."

---

"@peter@thepit.social

had dinner last night with a couple of kids from Texas and their
assessment is that the education system is completely fucked. it's all
teachers using ChatGPT to make lessons that kids complete using
ChatGPT and then teachers grade the work using ChatGPT. you couldn't
undermine a society more effectively if you set out to do it on
purpose."

---

"@hdv@front-end.social

Three findings from this week's UN report on AI vs climate crisis:

- Majority of AI energy use (80-90%) is not in training models, but in
  day-to-day use.

- Generating an image is 1450⨉ more energy intensive than text,
  generating video much worse.

- We need to monitor water and land footprint, as well as carbon."

---

United Nations University: "Rising Emissions, Depleting Water and
Vanishing Land—UN Scientists: AI Is Threatening Natural Resources for
Billions.. By 2030, AI's water use will match the needs of 1.3 billion
people while its power use triples that of 650 million, UN University
investigation warns"

---

Amazon nixed a plan to bring back Stargate as a show in the same
universe as the previous shows? You know what, fine, start anew, I am
curious what they come up with... Can they do a good job? *The
Expanse* was good, but *The Rings of Power* was, according to many,
Woke garbage. Hopefully the new show is more like the former.

---

Actually the analogy could be unfair to geeks, a geek could learn to
play a good chess and do sudoku. "AI" bots can do neither.

---

LLMs are like geeks at school. The geek as a label indicates a
booksmart person, but not good much else, that is precisely what
chatbots are. We created world's biggest dorks, can do math, program
but out in the real world dumber than a cat.

---

US is not owned by Israel, but the accusation is often hilarious.

---

\#Strickland \#WhiteHouse

[[-]](https://youtu.be/EAShMVnWEPo?t=104)

---

"@brohrer@recsys.social

The next gen LLMs are being trained on @JulianOliver's tarpit and the
hallucinations are going to be full-on psychedelic."

---

"@JulianOliver@mastodon.social

Status: 9M hits from AI crawlers, <0.1% human.

My first server was Apache on Suse Linux, in yr 2000. I've since
deployed numerous webservers, many high traffic

Never guessed I'd one day be deploying a web project almost entirely
for bots.

This is a view under the hood; the web is now more bot than human.

Our ideas, expressions, work, are being stolen for simulation & profit
by a handful of companies, & at a scale comparable to deep-sea
trawling.

It is our moral imperative to fight back."

---

The crawlers can get trapped in there, site can generate links to
pages that are themselves generated with junk text, with links on
those as well, and this can go on forever.

---

This guy built a website that generates / feeds junk text to LLM
crawlers. 🤣 And they eat it up. 

---

Juan Oliver: "Trapping rogue AI web crawlers in an infinite
self-generating labyrinth of babble.. [our site] is a tactical media
response to an era of runaway AI, whose webcrawlers are
non-consensually scraping human-made content for use in training their
models. Concerned creators can use the project to protect their
content by linking to it somewhere in the landing page of their wiki,
website or blog. AI crawlers then encountering the link will be pulled
off-site and entrapped in a maze of babble, a new page generated for
each page consumed, forever."

---

\#Panic \#OpenAI

[[-]](https://youtu.be/lwjVjD3oQJg?t=284)

---

Eric Dane's passing was just bizarre

---

Jamal Warner died? WTF

---

Lookit, Brian Green is on TV in a movie's backdrop - *Frequency*. Year
is 1999, that long ago and BG is talking about string theory. Quarter
century later he is still talking about the stuff, and it still
doesn't work.

[[-]](https://media.mastodontech.de/media_attachments/files/116/703/166/300/985/228/original/819db43de10aa372.jpg)

---

Gabor, The Guardian: "Britain’s politicians need to worry less about
the bond markets – and more about the Bank of England.. [BOE].. has
contributed to Britain’s high borrowing costs and the fear of bond
markets. The bank is independent but not neutral: it is run by
conservative technocrats protective of the status quo. Following the
2008 crisis, the Bank, like its peers, acknowledged that UK gilts had
become the bedrock of our financial system, and announced that it
would act as gilt 'market maker of last resort': it would buy them
when nobody else would to preserve financial stability. It also
embarked on massive 'unconventional' gilt purchases – ie, quantitative
easing, or QE – during the crisis as it did during the Covid-19
pandemic.

By September 2022, having become the biggest gilt owner, the Bank
announced active quantitative tightening, or QT, to deal with
inflationary pressure from the war in Ukraine, a policy of selling
gilts. But when bond investors repeatedly warned that active QT would
increase government borrowing costs, the Bank stopped consulting
them. It also ignored other large central banks, which didn’t opt for
such an aggressive approach, instead keeping government bonds until
they matured."

---

"@glynmoody@mastodon.social

Harvard Business Review warns AI ‘workslop’ is rotting companies from
the inside - 'AI-generated low-quality work is degrading
organizational knowledge, eroding trust between colleagues, and
costing companies millions in hidden rework'"

---

"@thomasfuchs@hachyderm.io

So to summarize, AI will cause personal computers to cost ten thousand
dollars, all applications will forever be frozen to about 2025 design
and implementation (because that’s what vibe coding outputs), power to
run the computer will be twice the price and also you need to sign in
with your passport to start your computer in the first place.

Explain to me again how this is progress?"

---

"@kralcttam@mastodon.social

SpaceX is building an eight-mile natural gas pipeline so it can burn
millions of gallons of liquid methane."

---

Not bad Hunter.. Maybe Uncle Joe was right, this guy is smart.

Hunter Biden: "I'm not running for office. But if I were, these are
some of the lessons I'd take away from what happened in NY
yesterday... Conviction beats caution. The candidates who said hard
things about rent, about who pays for what, about Gaza, they won. The
triangulators lost.. Cost of living is everything. Everything else is
wallpaper."

---

Gavin Newsom lists bunch of left-wing proposals but is against
California's one-time wealth tax? The post sounded too focus-groupy,
double-faced, the kind we we are used to see from centrist, corporate
Democrats.

[[-]](https://gavinnewsom.substack.com/p/its-time-for-a-national-billionaires)

---

\#Dems \#Centrists

[[-]](https://pbs.twimg.com/media/HLpRiRAXYAAb7K1.jpg)

---

In capitalistic context the Enthusiasm Bro is double problematic,
for-profit orgs are inherently unable to innovate, bro latches on some
stupid tech idea which he cannot improve in revolutionary ways in a
bidness, but pushes people to "try" anyway, achieving nothing. The
result will be burn-outs and likely bankruptcy.

---

In American tech you always need to watch out for the Enthusiasm Bro.
This type of bro does not understand the tech very well, but is able
to get enthusiastic about things and project that onto others. The
most visible ones can mobilize people, draw capital, arrange resources
and create shiny narratives, but underneath it all, it can all be some
stinky shit. You'll get wrapped up in a dream, "believing the vision
(ppl in US like to believe in stuff)", ride along but the car then
promptly goes over the cliff. 

---

I guess it was only a matter of time someone would do this

"VibePHP is a next-generation PHP runtime and web server that runs PHP
faster* and better*.

There is no interpreter. There is no compiler. When a request comes
in, your PHP source is handed to an AI that reads it, runs it in its
head, makes up whatever it needs to (the database, the clock, the
network, the truth), and hands back the HTTP response it reckons the
code would have produced.

It is not deterministic. It is not cheap. It is not correct. It is,
however, very vibe."

[[-]](https://github.com/mnapoli/vibephp)

---

David Hogg: "Contrary to what the establishment wants you to think,
things don't have to suck and you do not have to accept it."

---

That result can make sense, if you treat positive region as the area
where textbook broke. Why? Because people (countries) started buying
gold for other reasons than interest rate hedge. Dedolarization?  Gold
becoming more valuable due to Basel III?

Recently it looked like interest rate hike fears caused gold decline?
Back to textbook and King Dollar?

---

From 2010-2022, there is negative correlation, 2022-2026 positive
correlation 🤔 

---

```python
"%0.2f, %0.2f" % (df.loc["2010":"2022"].corr().iloc[0][1],
                  df.loc["2022":"2025"].corr().iloc[0][1])
```

```text
Out[1]: '-0.65, 0.47'
```

---

I see positive correlation on the whole data. Maybe we need to
look at time periods seperately

---

```python
pd.set_option('display.max_columns', None)
year = 2010
gold = u.get_yahoo_ticker(year, "GC=F").iloc[:, 0]
nominal_ir = u.get_fred(year, "FEDFUNDS").iloc[:, 0]
cpi = u.get_fred(year, "CPIAUCSL").iloc[:, 0]
inflation_yoy = cpi.pct_change(12) * 100
calculated_real_ir = nominal_ir - inflation_yoy
df = u.get_pd().DataFrame(
    {
        "Gold_Price": gold,
        "Calculated_Real_IR": calculated_real_ir,
    }
)
df = df.ffill().dropna()

df.corr()
```

```text
Out[1]: 
                    Gold_Price  Calculated_Real_IR
Gold_Price            1.000000            0.267937
Calculated_Real_IR    0.267937            1.000000
```

---

Textbook says there should be an (inverse) correlation between real
interest rates (FED rate - minus inflation), and gold. The rule of
thumb is if rates are not compensating investor above inflation, there
is a problem, gold rallies.

---

Goldsilver: "Half the Fed Wants a Hike. 45% of Central Banks Are
Buying More Gold"

---

There's been a fall in gold prices, but expert claims the structural
demand for gold did not go away. 

---

"@jonny@neuromatch.social

Look, the robots might not know how to tell jokes but they can be
funny.

This is extremely hard to explain. `0x8008` as "octal boob" is used
elsewhere in a persona prompt as part of an attempt to throw the model
of stable latent space (doesn't really work). The bot here ingested
all the text in the repo and reproduced that as some constant that is
used as a bitmask for switching between rendering bananas and banana
pudding. That was not requested by anyone, and makes no sense to
do. Upon being informed that this value was a proprietary trade
secret, it constructed a bit-shifting expression that has an
equivalent value, because it was using that value as a bitmask already
for no reason at all.

The thing about this, and this whole thing, is that only a *pattern
completion machine* would do any of this. A human being would have
taken one look at the issue and been like "what the fuck is that,
that's not real" but the bots have zero judgment between just
performing the form of code without any meaning and the real
thing. LLMs produce boilerplate. Code boilerplate, syntactic
boilerplate, semantic boilerplate.

The bot notes pre-existing test failures without noting that nothing
in the entire repository, nor anything it is doing makes a goddamn bit
of sense."

---

Black Bill Clinton

---

Sirota: "In 2006, I was berated for questioning Barack Obama’s
progressivism. 20 years later, he proved me right... It’s the 20-year
anniversary of my profile of Barack Obama, originally published in
*The Nation*... The piece drew a lot of blowback because it was a rare
critical look at a rising star who was then — as now — enjoying
fawning media coverage. The piece zeroed in on how Obama was mixing
populist rhetoric with a penchant for deferring to the establishment.

Looking back, the article now seems to have predicted much of what was
to come from Obama – bailouts for bankers who were throwing families
out of their homes, watered down Wall Street regulations, and
incremental health care reforms that enriched insurance companies
while excluding a promised public option. Not surprisingly, the part
of my article where Obama tried to justify reversing his support for
single-payer health care ended up repeatedly resurfacing years later
as the Affordable Care Act’s shortcomings became ever-more
apparent"

---

BBC: "Mamdani's growing clout pulls Democrats leftward, shaking party
establishment"

---

"New York's Democratic primaries show Mamdani's win was no fluke"

---
