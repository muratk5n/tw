
<img width='340' src='https://media.mastodontech.de/media_attachments/files/116/718/757/134/706/302/original/32965af464417335.jpg'/>

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

"@pikesley@mastodon.me.uk

Formulating an #EMFCamp policy: if I'm in your talk and your slides
have #LLM slop on them, I'm walking out. No ifs no buts. You couldn't
be bothered making them, I'm not interested in looking at them, and I
have to presume that whatever you're saying has had the same amount of
thought put into it"

---

LLM complemented me for catching the error 😂 

---

When I confronted it, it said this:

"You're right, I was sloppy there... LLMs generate text token by
token, and math is particularly dangerous because a
plausible-*looking* intermediate step is easy to produce without
actually checking it. I filled in a step confidently that I hadn't
carefully verified..

Even when the source material is right there in the context.. I'm
still generating tokens based on what seems likely to follow, so my
own learned patterns can override what's literally in the provided
text.

In this case the telescoping idea was in [textbook] derivation, but
the specific intermediate algebraic steps weren't spelled out [wants
to be spoonfed?]  explicitly even there — so I had to generate them,
and that's where my pattern-completion drifted from correct algebra.

It's a fundamental limitation to be aware of.. I'm not doing symbol
manipulation [basically math the way humans do it], I'm doing
sophisticated pattern matching that usually looks like symbol
manipulation."

---

Oh boy, "frontier" LLM made a massive algebraic mistake..

Now I'm not even sure they can be used for ed assist.

---

There were some other reports too saying Palantir software isn't that
good. But Focker somehow created an aura of greatness about the
product. Focker is always in the circle of trust 👌.

---

"@ChrisMayLA6@mastodon.me.uk

You may recall I posted recently on the highly focussed character of
the claimed productivity benefits of Palantir's technology in the NHS
(mostly happening in one London hospital); now NHS England has quietly
admitted that it actually does not have robust evidence to link any
wider rises in efficacy & performance to Palantir's software....

So, just to be clear; their claims are just than, claims unsupported
by evidence - which further suggests political interference!"

---

## Reference

[Nations and Nationalism, Culture, Narratives](0119/2013/02/nations-and-nationalism.html)

[Education, Workplace](0119/2017/09/education-workplace.html)

[Science and Technology](0119/2018/09/science-technology.html)

[Democracy, Parties](0119/2016/11/democracy.html)

[Economy](2021/01/economy.html)

[Globalization](0119/2018/09/globalization.html)

[Rome, The First Wave, Religion](0119/2017/12/rome.html)

[Human Nature & Health](2020/07/human-nature.html)

[Climate Change](2022/01/climate.html)

[Reports](2021/01/reports.html)

[The Middle East](0119/2019/07/middleeast.html)

[TR](../tr/index.html)

## Browse

[By Year](years.html)

[Search](search.html)

[Microblog Archive](mbl/index.html)

[PDF](https://www.dropbox.com/scl/fi/8kl0sla1booo83zeb28dn/tw-all.pdf?rlkey=p9r319p8jbzak5du3dasju05y&st=28wknfsp&raw=1)

Also on 
[Mastodon](https://mastodontech.de/@muratk5n),
[Codeberg](https://muratk5n.codeberg.page/tw/en/),
[Github](https://muratk5n.github.io/tw/en/)
