# Week 22

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

Geek: You can find the approximate minima of a function by turning it
into a Gibbs distribution, and relying of the (more efficient)
traversal via a sampler to find a approximate minima. The method does
not get stuck in local minimas like a gradient based optimizer are
prone to do. For a final demonstration of the approach I picked the
toughes nut, a 100 dimensional function-from-hell, and applied
parallel particle filters to sample from the posterior running on a
GPU, it found the approximate minima in two seconds.

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

