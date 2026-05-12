# Week 20

[GINI calculation](../../2021/01/stats.html#gini) shows some of the same
patterns as the compute below. How? GINI looks at wealth distribution,
its data is wealth of key percentiles. Living standard index uses
income for *one* group, and looks at what they would spend their money
on. Why would the rich getting richer effect the median price of your
house? Well.. it does. When all assets become investment vehicles for
the rich, the price of *your* house will rise, *your* living standard
will fall.

---

Failed the litmus test

---

[Zeteo News](https://pbs.twimg.com/media/HGhKD7FW4AAGMf2.jpg)

---

Bains is hitting Valadao on the Medi-Cal thing but she's got some
problems on her own.

---

David Hogg: "Follow the money, and it's clear that big business,
special interests, and the political status quo are backing Jasmeet
Bains.

We need Randy @villegas_ca22 in Congress."

---

Cal Matters: "California Rep. David Valadao has some explaining to
do... Nearly two-thirds of constituents in his Central Valley district
— approximately 527,000 Californians — are enrolled in Medi-Cal, the
state Medicaid program that provides health care coverage to
low-income Americans and those with disabilities. At 64%, Valadao’s
district has the highest Medicaid enrollment rate of any Republican
seat in the country.

Yet last year, the Republican cast what would become the decisive vote
to pass President Donald Trump’s domestic policy megabill, a law that
slashed more than $1 trillion from Medicaid and other programs that
help the poorest Americans to pay for tax cuts that will mostly
benefit the country’s richest."

---

Things have been going badly ever since 1992, 92-00 looks flat with
some gains, but that era laid the groundwork for all the fail that was
to follow (deregulation, NAFTA, oligapolies in various sectors). Then
the catastrophe started and lasted until 2016, gains afterwards. After
2020 decrease, some increase later, not much difference before/after
(Biden). Post 2024, FRED does not have incomes for 2025/6, I used
linear interpolation, the results do not look good. There is a stupid
war, US is spending money for all the wrong things. GINI confirms
this.

---

```python
targets = ['MSPUS','HLTHSCPCHCSA','CUSR0000SEEB','CPIAUCSL']
income = ['MEHOINUSA646N']
df = u.get_fred(1992, income + targets)
df['MEHOINUSA646N'] = df['MEHOINUSA646N'].interpolate(method='linear')
df = df.interpolate(method='linear')
ratios_df = df.copy()
for col in targets:
    ratios_df[col] = ratios_df[income[0]] / ratios_df[col]
normalized_df = ratios_df[targets] / ratios_df[targets].iloc[0]
ratios_df['super_index'] = normalized_df.mean(axis=1)
ratios_df['super_index'].plot(title='Living Standards Index', grid=True)
```

![](https://media.mastodontech.de/media_attachments/files/116/550/552/141/911/973/original/d473818a033d1c10.jpg)

---

From FRED (econ indicator database)

`MEHOINUSA646N` - Median Household Income in the US

`MSPUS` - Median Sales Price of Houses Sold 

`HLTHSCPCHCSA` - Health Expenditures per Capita

`CUSR0000SEEB` - Tuition

`CPIAUCSL` Consumer Price Index, for regular items

If you divide household income by each of these measures, you would
get "units of that measure that can be bought by a regular person". If
median income in 2010 is 100, education is 10, I could buy 10 units of
education for that year, same for housing etc. The result might not
make sense on its own but comparatively the measures can point to some
trends.

CPI has a housing component too, but I wanted a seperate measure for
that and have all combined equally, groceries, health, education, real
estate.

---

It's time to develop a living standards index

---

Is this what the seasteading movement turned into? At least before
they were thinking about building livable structures on water, there
could be interesting engineering there.. Now they just want to hole up
in some giant steel cage like a rat.

---

Another libertard bizarro experiment.. it was a nice read

The Guardian: "[2021] The disastrous voyage of Satoshi, the world’s
first cryptocurrency cruise ship.. Last year, three cryptocurrency
enthusiasts bought a cruise ship. They named it the Satoshi, and
dreamed of starting a floating libertarian utopia. It didn’t work out"

[[-]](https://www.theguardian.com/news/2021/sep/07/disastrous-voyage-satoshi-cryptocurrency-cruise-ship-seassteading)

---

There is a story in the book *Titan*, the J. D. Rockefeller
biography. They are discussing a business issue, and a debt related
subject comes up, certain amt of interest needs to be paid,
Rockefeller does the calculation in his head really fast, and gives
the answer. Then he silently pats himself in the back because he
calculated it faster than the Jew banker sitting at that table. He is
like "I beat a Jew calculating interest". Why would that person be
different, better on this matter though..? The calculation is just
another aspect of computation, arithmetic.

---

Jews *learned* modern finance from Europeans. I've seen some yield
chasing mfkers in Europe that would run circles around the finance
guru Jew.

---

The 1992 event of shorting the British pound and "breaking the Bank of
England" is usually attributed to Soros, when in fact the idea and the
execution of it was Druckenmiller's. Is it because Soros is Jew and
it is assumed they are good at "money stuff"?

---

There are words like "pressure", "tackling the challenge" in the
article because a massive trade deficit is not a good thing. Even
globalisation-friendly EU does not enjoy trade deficits.

---

"China recorded its largest-ever trade surplus with the European Union
in the first quarter of 2026...  China’s industrial production has
been growing faster than both its GDP and its domestic demand. This
reflects a broader pattern of supply-side expansion that continues to
seek global outlets, regardless of US policy. Even a significant
rollback of US tariffs would not by itself relieve the structural
pressure this creates for European markets...  Meanwhile, subdued
Chinese domestic demand limits the scope for offsetting the deficit
with an increase in Chinese consumption of European goods."

---

Schuller's idea sill does not explain why there is gravity. The
$G,\Lambda$ are free parameters. You could set $G=0$ then there is no
gravitational pull. The theory does not say what the value is supposed
to be causing the actions we observe around us.

But it is an improvement of sorts, it shows a clear transition from
Maxwell to Einstein with minimal assumptions.

---

🤣 🤣 🤣 

Me: "Could you summarize Frederic Schullers theory on gravity? How is
gravity derived from electromagnetism?"

LLM: "This is not part of Schuller's framework. Gravity is not derived
from electromagnetism in GR or in Schuller's lectures."

Me: "I am literally looking at a Youtube video right now with title
'Frederic Schuller: The Physicist Who Derived Gravity From
Electromagnetism'"

LLM: "You're right to push back, and I appreciate the correction! Let
me look that up rather than speculate.... [searches] My apologies for
the confident but wrong answer earlier! Now I can give you a real
summary."

---

You muck with people's oil they muck with your oil. US has been
engaged in some shady biz as of late.. 

AP: "[There was] an explosion and a fire at a refinery in the New
Orleans area on Friday"

---

Mastodon User: "Boy I was wrong about the Fediverse.. See I had
forgotten the one golden rule of capitalism. To thrive in capitalism
one must be amoral. Now you can be wildly sickeningly successful with
morals but you cannot reach that absolute zenith of shareholder
value. Either you accept a lower share price and don’t commit
atrocities or you become evil. There is no third option.

So of course media corporations became bargaining chips for the
oligarchs' actual businesses. Why fight a defamation suit when you can
settle it by running favorable coverage and maybe bankrupting the
media outlet you bought as a stocking stuffer? Suddenly I couldn’t
find any reliable reporting about anything in the US...

It was somewhere in the middle of DMing with someone who had forgotten
more about Greenland than I would ever know and someone who lived
close to an RAF base in the UK that it clicked. This was what they had
been talking about. Actual human beings were able to find each other
and ask direct questions without this giant mountain of bullshit
engagement piled on top of it. Meta or Oracle or whoever owns TikTok
this week couldn't stop me.

I never expected to find my news from strangers on a federated social
network that half the internet has never heard of. I never expected a
lot of things. But there's something quietly beautiful about a place
where people just... share what they know. No brand deals, no
engagement metrics, no algorithm nudging you toward rage. Just someone
who spent twenty years studying Arctic policy posting a thread at 2 AM
because they think you should understand what's happening. It's the
internet I was promised in 1996. It only took thirty years and the
complete collapse of American journalism to get here."

---

[Link](https://media.mastodontech.de/media_attachments/files/116/548/180/377/594/970/original/d93d58e84de745ad.jpg)

---

NYT: "[2023] The Return of Tony Blair.. Blair is suddenly, and rather
remarkably, back in favor. For Mr. Starmer, embracing Mr. Blair sends
a political message"

---

Starmer was Blair's boy, they conspired against Corbyn.. The latest
election is a major blow to them both.

---

\#Taken

[[-]](https://sinceyouarrived.world/taken)

---

Paul Graham: “[2007] Eventually the open source world won, by
producing Javascript libraries that grew over the brokenness of
Explorer the way a tree grows over barbed wire.”

---

Israel is gnawing on your country bit by bit and you are condemning
Iran?

---

???

"Syria condemns Iranian attacks on UAE"

---

Greens did well. The message, overall campaign clicked with the voters.

<img width='340' src='https://ichef.bbci.co.uk/ace/standard/800/cpsprodpb/vivo/live/images/2026/5/8/ac0184a3-f9c3-4aa9-8cb1-1b2a39a14e82.png.webp'/>

---

Following the same worn out centrist playbook will not work. The
electorate will keep choosing "the other" at every election if their
well-being does not improve. UK corporate interests caused this. They
attacked Miliband with their "Red Ed" attacks... They attacked Corbyn
with antisemitism charges... Now this is what they get - Reform is
surging.

---

CNBC: "UK PM Starmer says he plans to remain in office despite
crushing local elections defeat"

---

IC: "Labour Suffers Heavy Election Losses, Reform UK Soars"

---

Le Monde: "Inequality reaches record levels in the UK.. Britons now
live in one of the most unequal countries in the world, according to a
new report based on six years of research. These disparities are
evident both geographically and in terms of public health."

---
