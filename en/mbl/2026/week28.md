# Week 28

Re-reading the Clinton speech at the signing of the "financial
modernization bill" where they repealed Glass-Steagal.

"We are here today to repeal Glass-Steagall because we have learned
that government is not the answer. We have learned that freedom and
competition are the answers."

Notice the second part. He even used the word "freedom" in that
duplicitous way economic right-wingers use it. After decades of this
shit, do US citizens have freedom, as in from their corporate
overlords, from poverty, and joblessness?

---

No need for optimization. Probabilistic approach can handle every
scenario.

---

Interesting dates found: `2021-03` to `2024-03`. Switch from negative
to positive correlation happened here. In June/July 2022, US CPI
inflation peaked at a 9.1%, the Federal Reserve executed its
75-basis-point interest rate hike, making it clear they were going to
push real rates higher aggressively. Gold prices bottomed later that
Autumn and began their rally despite surging real interest
rates. Confiscating Russian money at Western banks wld have played a
role, CBs were spooked, and the gold rush started. Basel III rules
kicking in 2020 for Europe might have provided a catalyst.

After `2024-03` the systemic changes were priced in, textbook
returned.

---

There are probabilistic programming options. First trick: Running
plain old regression on normalized time series X,Y is the same thing
as computing correlation between X,Y. Another trick, we use "segmented
regression", find pieces of linear fit within blocks, once found, we
run correlation (w/ significance calc) between endpoints. Lines are
connected via a sigmoid, we run Metropolis sampling over the
"posterior".

---

We talked about correlation between real interest rates and gold
price, how they are inversely correlated, but textbook worked
sometimes, not other times. Saw correlation results on two blocks but
that cutoff was chosen via trial-and-error. We can actually estimate
those divisions from the data itself.

---

[Link](https://eigenmagic.net/system/media_attachments/files/116/859/646/222/454/637/original/7f8804db2abcd184.png)

---

"@vampiress@eigenmagic.net

Re-watching Con Air as I work today.

I love how '90s movies so often, no matter how absurd their core
premise or plot got, played it dead serious, without the post-Whedon
wink-and-a-nod to the audience that modern flicks feel obliged to
include out of insecurity."

---

[Very Average Prototypes](https://goodnameforablog.com/posts/very-average-prototypes)

---

Gunn greenlit an average script, realized his mistake later tried to
unf--k things by meddling, probably made things worse.

---

The Holywood Reporter: "Behind the 'Supergirl' Bomb: Competing Cuts,
Creative Differences.. Gunn and [the director] Gillespie had creative
differences over the direction of the movie, numerous sources tell The
Hollywood Reporter, and the film never found its footing in the
post-production process...

[A new writer hired by Gunn, after filming ended] helped write scenes
for a nine-day shoot of additional photography.. [then] the studio
decided to force a bakeoff by creating two cuts, one by Gillespie and
one by the studio... the studio chose its cut as the one to go into
theaters...

The challenge for Gunn, and thus DC Studios, is to navigate the fine
line of being filmmaker friendly while also trusting his strong
artistic point of view that has guided him all his career."

---

Ouch. Domestic opening of *The Marvels* was better than *Supergirl*,
and the former was a bust. SG is set to be a bigger fail than TM

---

```python
u.boxofficemojo("The Marvels")
```

```text
Out[1]: 
{'Domestic Opening': '$46,110,859',
 'Domestic': '$84,500,223',
 'International': '$121,636,602',
 'Worldwide Total': '$206,136,825'}
```

---

```python
u.boxofficemojo("Supergirl")
```

```text
Out[1]: 
{'Domestic Opening': '$37,102,018',
 'Domestic': '$46,570,096',
 'International': '$34,500,000',
 'Worldwide Total': '$81,070,096'}
```

---
