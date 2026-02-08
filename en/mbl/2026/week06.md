# Week 6


CNBC: "Sweden’s Volvo Cars fell over 22% in its worst trading day
ever. Here’s why.. [its CEO said] the discontinuation of EV incentives
in the U.S. and China [are] contributing to 'a very challenging
external environment.'"

---

\#Mandelson \#Palantir

[[-]](https://www.youtube.com/shorts/wk8FQrk1WS4)

---

*The Wrecking Crew*, the car chase was overdone, but good action
overall.. Then I watched a scene from the show *See*, Momoa and
Bautista played brothers before? 

---

*War Machine*, nice trailer. The name is not symbolic like referring
to a country or an org, the movie is literally about a war machine.

---

There is better jutsu for that, water and beans in a pot, bring to
boil, and turn off the heat. Leave it for one hour. Then drain the
water, beans ready for second stage. 

"With the overnight-soak method, you put water and beans in a pot,
cover the beans with an extra two inches of water, and place in the
refrigerator for eight to 12 hours."

---

"@lfeurope@mastodon.social

Europe is moving from slogans to strategy on #DigitalSovereignty, with
\#opensource increasingly at the core of technological autonomy.

This \#FOSDEM session on global collaboration and Europe’s digital
\#sovereignty goals explores how participation in global open source
communities can strengthen Europe’s strategic autonomy"

[[-]](https://fosdem.org/2026/schedule/event/DNUTXJ-eu-global-digital-sovereignty/)

---

\#Reshare

"@GeofCox@climatejustice.social

About half of all house purchases in the UK now are for 'additional
dwellings' - second homes, buy-to-lets, etc - because 10% of the
population can outbid everybody else, drive up asset prices, and when
it's something people can't live without, like a home, force them to
pay unreasonable rents"

---

Housing becomes about "supply" if too many well-to-do gobble them up,
reducing the said supply.

---

"[Oz] PM’s $4.3m clifftop home earns double rent of typical
landlord.. Mr Albanese has made an array of property investments over
the years. He was reported to have a 5m property portfolio just prior
to getting the nation’s top job"

---

via @Victor@spore.social

ZME Science: "A Radical Climate Proposal Aims to Channel Seawater Into
a Giant Egyptian Desert to Fight Sea Level Rise.. Flooding Egypt’s
vast Qattara Depression with seawater could slightly lower global sea
levels and reshape climate adaptation."

---

"@dantheclamman@scicomm.xyz

Comparing historical hair samples from people from when they were
babies to today, a new study finds a nearly 100-fold decrease in lead
from samples after the EPA's crackdown on leaded gas. Regulation works
and it saves lives!"

[[-]](https://arstechnica.com/science/2026/02/a-century-of-hair-samples-proves-leaded-gas-ban-worked/)

---

"@eb@social.coop

America is not the land of the free, it is the land of the fee"

---

The Lever: "Big Grocery’s Hidden Poverty Tax.. Low-income
neighborhoods face higher food inflation than rich ones, and new
research suggests market consolidation is the culprit."

---

Firstpost: "Russia has said India is free to source crude from any
supplier and dismissed suggestions that New Delhi is moving away from
Russian oil"

---

[Link](https://www.dropbox.com/scl/fi/fppehydj2gg0catok518j/tng_data_1.gif?rlkey=cpea4tuicurz0xmw8w7updkl6&st=8keg2lnc&raw=1)

---

Don't get me started on LLM tech, they are *all* about adjustable
parameters, a modern LLM has over 1.5 *trillion* of them. Imagine the
level of ignorance captured in that design decision. We basically know
next to nothing about intelligence, we just reverse engineered some
parameters from data via a black box, and called it AI.

---

Now we reveal where the data comes from: it is the **SINE FUNCTION**
(with some added noise to make it look like experimental data).

```python
df['ypred'] = np.sin(df.index)
df.plot(grid=True)
```

[Graph](mbl/2026/img/freepar4.jpg)

The sine function, $y = sin(x)$, has no free parameters. It is
simpler, even faster to compute. However it requires the knowledge of
trigonometry. Because the foolish scientist did not know this, his
formulation became parameter heavy. The model with a lot of adjustable
knobs represented his ignorance.

---

But the 7 coefficients tell us nothing in scientific terms because
using the same coefficients / free parameters / "constants" approach I
could turn the curve into a line, I could make it go up, or down. The
structure of my "flexible (too flexible)" formulation doesn't tell me
anything about the phenomena. Those free parameters represent our
*ignorance*, not knowledge.

---

Then the genius says "I can reverse engineer those adjustable knobs
from data!". He uses `polyfit`, and voila

```python
coef = np.polyfit(df.index, df.ydata, degree)
df['ypred'] = np.polyval(coef,df.index)
df.plot(grid=True)
```

[Graph](mbl/2026/img/freepar3.jpg)

That is a good fit

---

He pulls some numbers out of his ass,

$c_0 = -0.00003$,$c_1=-0.00001$,$c_2=0.004$,$c_3=0.0003$,$c_4=-0.12$,
$c_5=-0.005$,$c_6=0.4$,$c_7=0.04$

.. and uses them,

```python
degree = 7
coef = [-0.00003,-0.00001,0.004,0.0003,-0.12,-0.005,0.4,0.04]
df['ypred'] = np.polyval(coef,df.index)
df.plot(grid=True)
```

[Graph](mbl/2026/img/freepar2.jpg)

He obtains the graph above. His "prediction" came close in some
places, though overall not great.

---

I'll give an example. Let's say a scientist is looking at some data
collected from nature,

```python
df = u.data_synth_1()
df.plot(grid=True)
```

[Graph](mbl/2026/img/freepar1.jpg)

And he is asked to find the formulation for this. He looks at the data
and says, "well I can represent this by simply multiplying powers of
$x$ with some coefficients", eg $c_0 x + c_1 x^2 + ... + c_n x^n$. He
thinks he is smart because you can represent any curve with such a
function.

---

Smolin and Unzicker are right.. the "constants" or "free parameters"
represent our ultimate ignorance about the world. Those parameters are
basically knobs you can turn to make our formulas "fit" the
experimental data.  They are reverse engineered from data, they do not
arise from fundamental mathematical deduction.

---

Unzicker: "Cosmology’s 'concordance model' uses six numbers, which are
called 'free parameters' because they cannot be explained within the
model but rather are fitted to the measurements.  The standard model
of particle physics needs not only six of them, but an impressive
17. Why 17?.. In the 1950s, a boom of particle accelerators started
producing hundreds of elementary particles with spectacular
collisions. In the following decades, particle physics has been busy
classifying this zoo and reducing its mathematical description to
'only' 17 parameters. A few Nobel prizes have even been handed out
because of this work. But should we be convinced that we have come to
understand the ultimate structure of matter? In his book *The Trouble
with Physics*, Lee Smolin comments on the 17 free parameters. 'The
fact that there are that many freely specifiable constants in what is
supposed to be a fundamental theory is a tremendous embarrassment.'"

---

"@GeofCox@climatejustice.social

From a European perspective, a central problem with 'liberal middle'
Democrats is that they would simply restore the very conditions that
enabled the rise of the far right in the US - so I don't think it's a
question of the socialist left continuing to be marginalised for
another half-century.  If the Democrats succeed in getting elected, in
their current form, and subsequently in office fail to change key
fundamentals - such as ending American oligarchy and materially
raising working people's living standards - then the far right will
simply flood back again in 5 or 10 years."

---

Politico: "Trump prepares to let go of arms control with Russia"

---

"The expiration of the New START Treaty on 5 February 2026 marks the
end of an era that began in 1969, when the United States and the
Soviet Union launched the SALT I negotiations. For the first time in
decades, there will be no treaty constraining the nuclear arms race."

---

The Guardian: "Fossil fuel firms may have to pay for climate damage
under proposed UN tax.. Framework Convention on International Tax
Cooperation could also force ultra-rich to pay global wealth tax"

---

LBJ, Texas oil interests, and rogue CIA elements - institutionally
they were not involved. Nothing deep, all on the surface

---

Roger Stone, *The Man Who Killed Kennedy*: "The JFK assassination
itself became the most prime example of LBJ’s black magic. Johnson was
within days of not just being dropped from the 1964 Democratic ticket,
but of being politically executed, personally destroyed, and publicly
humiliated by the Kennedys. A Life magazine exposé on LBJ’s corruption
and vast wealth was due to be published within a week. A SWAT team of
reporters was combing through LBJ’s financial transactions in central
Texas. At the very moment when JFK’s Dallas motorcade was slowing on
Elm Street, Don Reynolds was testifying to a closed session of the
Senate Rules Committee about LBJ’s kickbacks and corruption.

Then presto! Magically, mysteriously, and tragically, John Kennedy is
dead. Lyndon Johnson becomes president, and the media exposés and
Senate investigation into LBJ’s corruption are deep-sixed. This was
not without the help of H. L. Hunt and the Texas oil industry, which
helped navigate, fund, and advise Johnson’s career in exchange for
prized government contracts and favorable legislation. The oil magnate
would later be one of the top financiers of the assassination in
Dallas."

---

\#Thorium \#Reshare

[[-]](../../2026/01/thorium.html)

---

The re-release of *Endgame* can help to reclaim "the highest grossing
movie" title, previously lost to Avatar because of [its re-release](https://www.ign.com/articles/avatar-set-to-beat-avengers-endgame-as-highest-grossing-movie-after-re-release).

---

Is Marvel re-releasing *Endgame* with a few added scenes for
*Doomsday* connection? This is your opportunity to digitally remove
Stark's goatee, so VVD can have it.

---

Trek did it best

[[-]](https://www.dropbox.com/scl/fi/f33t77qp6qsu9vizr32ar/trek_evil1.gif?rlkey=r40p9zhqlcvt9sb4mam87dsmm&st=cfq3u1ef&raw=1)

---

How is the reveal going to be? Evil twin reveal needs to have a shock
factor.

"According to the comics, Tony Stark's twin brother is Doctor Doom and
we might see this in live-action as well. Although this is currently
just a normal fact and a rumor, if they make it comic-accurate, this
is what we can expect."

---

King Dollar policy of Volcker wasn't all rainbows and unicorns, it
hurt US trade balance that led to Plaza Accords which then led to real
estate bubble in Japan and that led to other side effects.. 

---

The Motley Fool: "Trump Is Cheering and Potentially Hinting at a Weak
U.S. Dollar"

---

Kevin Warsh: "[2024] Washington writ large [was] trying to design a
set of policies that were good for asset holders, made the stock
market go up every day, [that was] bad for the folks that are living
on their W2 income, that don't own assets, that just have income,
you're taking risks with their paychecks every day...

[I]f the focus from the central bank were on the real economy, the
financial markets will take care of itself. The real economy is
growing strongly, financial markets will be fine. But if the focus is
on financial markets, that doesn't necessarily mean the hard working
people in the real economy will do as well"

---

F24: "Britain on Tuesday unveiled its first national plan to curb
'forever chemicals,' seeking to cut risks to human health and the
environment, the government said. PFAS, used in products from cookware
to food packaging, persist for decades and accumulate in nature,
posing threats likely to endure for hundreds of years."

---

CNBC: "Gold and silver rebound after historic wipeout as analysts say
thematic drivers stay intact"

---

I love it.. Mandelson is a "New Labour" guy, one of those Clintonite
Brits, economic right social left type "progressive". We can enjoy
watching them sink.

CNN: "The latest tranche of documents has revealed that [Peter]
Mandelson appeared to leak sensitive UK government tax plans to
Epstein. They also show that his partner, Reinaldo Avila da Silva,
regularly received undisclosed payments from him."

---

It looks like the Winsdors booted out their troublemaker right on
time.. If he was still a royal he would have been a royal pain in the
ass right now.

---

Corps are your tyrants, America. Their silent opression is worse than
any kind of government can bring to bear.

---

Tubers do this too.. And ppl make fun of China using code words to
bypass censorship.

"It's because the words like die or suicide are often censored on
platforms like Tiktok.. people started saying [unalive] instead."

---

"@GeofCox@climatejustice.social

[W]hile living standards have stagnated for most people.. the wealthy
and privileged have continued to get much wealthier.  About half of
all house purchases in the UK now are for 'additional dwellings' -
second homes, buy-to-lets, etc - because 10% of the population can
outbid everybody else, drive up asset prices, and when it's something
people can't live without, like a home, force them to pay unreasonable
rents - further increasing inequality, both directly and indirectly,
by sucking money out of local economies into elite enclaves."

---

No, Xi is not a minor princeling. Other princelings tend to be sons,
nephews of a Mao general, but generals are dime a dozen. Xi's father
did no one else could, he gave the Red Army refuge when they were down
on their knees, in a bad shape, facing certain ruin. Xi Zhongxun saved
them. IMO that makes his son one of the top princelings.

---

It is interesting China, despite living under a system that enforced
equality for many years, still has an informal pseudo-royalty ranking
system within its party, I am talking about their "princelings".
Basically closeness to Mao in history imbues a man with added
rizz, they get status via that association.

---

We can't blame the banks on the lending capacity issue.. The debacle
demonstrates that fundamental changes need to be systemic not nibbling
around the edges. If banks are to be supplanted, harming everything
*else* done by banks is a risk.

---

The idea was since stablecoins are backed by treasuries which earn
interest, why not pass that interest along to the customer who holds
the coin? That was good choice. But it was too good for the banks'
comfort, they lobbied heavily against the crypto bill and managed to
kill it. They had a clause inserted discouraging yield offerings which
negated a big purpose of the bill.

"[1/15] Bank of America CEO.. warned that interest-bearing stablecoins
could pull as much as $6 trillion out of the US banking system,
arguing that large-scale deposit migration would reduce lending
capacity and push borrowing costs higher."

---

"The Arleigh Burke-class destroyer and Virginia-class submarine are two
of the U.S. Navy’s most sophisticated vessels. The destroyer uses
about 2,600 kg of [rare earth elements], while the submarine demands a
whopping 4,600 kg. These elements support radar, sonar, missile
guidance, and propulsion systems critical for both offensive and
defensive missions.. While these elements are crucial to U.S. defense,
more than 70% of REE imports come from China"

---

Yahoo Finance: "Larry Fink critiqued capitalism during his opening
remarks at the World Economic Forum on Tuesday. 'Capitalism has
focused wealth in the hands of a narrow minority since the end of the
Cold War', said the BlackRock CEO."

---

Ortayli counts Bernard Lewis as one of his influences.. I call him Bernard "[Time for Toppling](https://www.wsj.com/articles/SB1033089910971012713)"
Lewis. Rabid neo. 

---

Yes this is the same University of Chicago that gave rise to "Chicago
School of Economics", basically the neolib, Reaganist agenda. There are
always bizarre things going on over there. 

---

Inalcik found acceptance in the West (esp. Uni. of Chicago); migration
theories that favored [one migration over others](../../2020/07/migrations-anatolia.html)
as an ideology was useful for the Anglo. By placing him on a pedestal
they encouraged an army of followers to continue his
research. Remember the nationalist narrative has an "alien" Turk who
arrives Asia Minor, builds civilisation where non existed, later
backstabbed by bad Arabs (don't like them, stay away from their
region), and always try to reconnect with distant cousins in Asia
(stirring shit up in Russia and China's backyard).

---

Koprulu, Inalcik made a lot of mistakes.. But they were "useful",
that's why they were "state sponsored historians". Inalcik's student
Ortayli, though not as bright as his elders, found some renown in
local nationalist circles. They help advancing the nationalist project
of 1923. But, like Giordano Bruno said "if the first button of a man's
coat is wrongly buttoned, all the rest are sure to be crooked.". That
has always been the problem of the TR project, their initial mistake
created massive intractable problems downstream. One issue alone,
Kurdish seperatism was largely triggered because of the crooked
"Turkish" identity and ended up costing the state 1.8 trillion dollars
over 40+ years. Even if this issue is somehow "solved" today, the
damage has been massive. Anatolians did that to themselves.

---

Lowry: "In one generation the explanation for the question of the
identity of the early Ottomans had been transformed from one which
styled them as an admixture of Islamicized Byzantines and Turks
(Gibbons); to Turks who attracted a large number of Byzantine converts
to their banner due primarily to the heterodox form of Islam they
practiced (Langer/Blake); to an amalgam of Turkish tribes and groups
whose administrative skills were inherited from earlier Turkish states
in Anatolia, the Seljuks, and the Ilhanids (Köprülü); and finally, to
a group of dedicated Muslim gazis who came together for the express
purpose of fighting and converting the Christian infidels in the
border marches of northwest Anatolia (Wittek)...

Somewhat paradoxically, while on one hand denouncing Gibbons’ theory
as 'groundless speculation,' Inalcık seemingly adopted its underlying
argument in 1973, when he stressed (as had Wittek) that a common
background tied together the Byzantine frontier troops with the Muslim
gazis and that this led to assimilation. All this in turn shaped what
he described as: '

>a true 'Frontier Empire,' a cosmopolitan state, treating all creeds
>and races as one, which was to unite the Orthodox Christian Balkans
>and Muslim Anatolia in a single state.

Inalcık leaves unanswered one key question: What were the factors in
the early fourteenth century (prior to the advance into the Balkans)
which had served to unite the Bithynian Christians and Muslims into a
single state? While citing the role played by one Byzantine Greek,
Köse Mihal, who joins forces with the Ottoman rulers Osman and Orhan
'as a famous example of the process of assimilation,' he states that
this Köse (beardless) Mihal was a 'Gazi' and 'a Greek frontier lord
who accepted Islam.' I have encountered no source which alleges that
Mihal was a Muslim prior to the closing years of the reign of Osman
(1299–1324). Less clear are the reasons behind Inalcık’s insistence on
making Köse Mihal a Muslim"

---

via @infobeautiful@vis.social

<img width='340' src='https://cdn.masto.host/vissocial/media_attachments/files/115/989/813/766/901/120/original/6cc87caa3e4f0c1a.png'/>

---

It sounds like 2D trust vectoring (eg up and down) would be more
efficient than 3D. Simplifies design and you can still get 3D
vectoring by additional maneuvering. #J-50

---

They call the Chinese J-50 the "carrier killer"?

---
