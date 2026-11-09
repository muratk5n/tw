# Week 45

The Lever: "Big Tech Lost The Election. Now Comes The Gaslighting. As
Democrats prepare to investigate Silicon Valley, its liberal-branded
lobby is scrambling to erase voters’ resounding rejection of Big Tech."

---

CNBC: "Top Democrats call to rein in AI buildout after midterms sweep:
'National data center moratorium now'"

---

CNBC: "Nasdaq sell-off batters Asian chip stocks as SK Hynix, Samsung,
Softbank, TSMC tumble"

---

Sheeee-iiiit

```python
u.get_yahoo_ticker(2026,"^GSPC").tail(100).plot(grid=True,title="SP 500")
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/569/947/666/669/118/original/fb6bc9837545413d.jpg'/>

---

"@MAKS23@mastodon.social

🇺🇸👀 Shares of American technology companies, especially AI players,
have plummeted. Almost $3 trillion has evaporated from the market in a
matter of minutes, and NASDAQ index has fallen by ~5%.

Cryptocurrency is also falling."

---

What's in a name? 

The Verge: "OpenAI is quietly renaming data centers 'compute
campuses'.. People hate data centers. They’re loud, resource-hungry
eyesores that are so profoundly unpopular they have managed to achieve
the near-impossible in today’s polarized political landscape: genuine
bipartisan opposition. But what about 'compute campuses'? Those sound
lovely, right?

OpenAI seems to be gambling that a quiet rebrand could be all it takes
to defuse the growing political backlash that threatens to derail the
infrastructure fueling the AI boom."

---

"@howelloneill@infosec.exchange

Crypto and AI spent $250m in the midterms 'in hopes of picking the
lawmakers who will decide how — or whether — their industries will be
regulated ...  nearly three-quarters of their money went to the
competitive races, and there, they got clobbered'"

---

Business is not a good background for politics. Enterpreneurship is a
necessary evil the society tolerates for that *last mile* of
service. They do not innovate at a fundamental level, nor bring
positive change to people by default. The work attracts a certain type
of personality, by and large such people should be discriminated
against, filtered out from public service.

---

Newsweek: "Ramaswamy’s Concession to Amy Acton Went to Voicemail"

---

"This software team will charge you $10,000 a week to remove all
AI-generated code from your systems.. The three man team is known as
'Slopfix'. It claims to be able to reduce AI generated codebases by up
to 65% in size. They aim to 'refactor vibecoded codebases back to
maintainability'"

---

Coulter, *TAC*: "The American Israel Public Affairs Committee (AIPAC)
and the closely affiliated United Democracy Project (UDP) spent in the
neighborhood of an estimated $45 million to defeat Abdul El-Sayed in
Michigan—who famously refused to answer whether Israel or Iran was a
bigger threat to the U.S. That money became toxic, driving support for
El-Sayed. He will now be America’s first Muslim senator...

Iran War zealots used a blowtorch to kill a spider and burned the
house down. Unfortunately, it was our house, too.. Virtually every
poll shows that the top election issues were the Iran War, gas prices,
and the cost of living. And the reason gas prices are high is because
of the war; the reason the cost of living is high is because of gas
prices."

---

Yahoo News: "Donald Trump Jr. has weighed in on the midterms with a
dig at his own dad. Don Jr., 48, gave a full-throated endorsement of
Vice President JD Vance's surprisingly candid assessment of where the
Republican Party went wrong after a humiliating defeat in the midterm
elections on Tuesday... 'The reason we lost is the war,' Vance
wrote. 'The president himself said so last night.'... 'Every word of
this is 💯💯💯,' the president's son said."

---

Jacobin: "Abdul El-Sayed becomes the first left insurgent to win a
statewide race with a purple electorate. And he did it on a platform
of Medicare-for-All, taxing the rich, and ending arms sales to
Israel. The facade that Democratic voters must choose more 'moderate'
candidates is gone."

---

Al-Monitor: "Israel faces new era of sinking US support after election"

---

TAC: "The actually forward-looking point is that America First -
immigration sanity, trade and economic realism, and foreign-policy
restraint - has not in fact been tried in any serious, dedicated
way. What the current management and its ministers have delivered is
Bushism without all the personal decency and intellectual
seriousness. It turns out, based on yesterday’s midterm results, that
'Bushism, but even more evil and retarded' is not enormously popular
outside the 30 percent of the country that will vote for anything with
an R next to it.

This is basically the stuff of optimism. That is to say, immigration
sanity, trade and economic realism, and foreign-policy restraint all
still have a politically viable lane. Trump the candidate beats Trump
the president."

---

Hey, they tried, gave it a good college try and failed. This is not
intelligence. Another path must be tried now.

---

The glorified search engine parallel still works for LLMs. When you
query it, the response is like a search result, an amalgamation of a
page that would've answered your query had it existed. But of course,
"textual thinking" has its limits. 

---

"@GossiTheDog@cyberplace.social

If you're wondering why the UK government recently advised people to
stockpile some limited essentials recently, this thread [below] was
part of the reason."

---

"@GossiTheDog@cyberplace.social

If ransomware groups (and a big if so far) focus on UK food
production, warehousing and logistics they could cripple UK retailers
within days.

I’ve worked both production (Crabbers) and retailer (Co-op)
and.. well, yeah - it’s risky biz.

For food and soft drinks production, margins have been squeezed by
retailers heavily - at Crabbers we made next to no money, despite
being the biggest supplier in most sections.

Heavy IT digitalisation happened across industry to cut cost.

There’s a handful of orgs - Culina and the like - who are absolutely
central to UK food and drink supply. Combating ransomware groups isn’t
in their budget range."

---

"@JulianOliver@mastodon.social

All these metals that we're spraying into the atmosphere on reentry
burn are even worse than PFAS in the hydrosphere, in that unlike PFAS
(which after 1000's of years do eventually decay) they are pretty much
permanent, never cycled out of the atmosphere.

Space junk burn may prove to become our most indelible mark on this planet."

---

TAC: "Iran More Likely to Strike Europe if Trump Attacks.. Germany and
the UK have facilitated the U.S. military campaign."

---

The Lever: "Democrats Won. Let’s Make Sure They Don’t F#*k It
Up... The voters delivered a mandate for change. Our explosive new
series asks whether Democrats have the guts to deliver...

Will they take on the billionaire donor class and the corruption
poisoning Washington? Can they actually lower costs — from housing and
groceries to health care?.. Can they end America’s endless wars
and reform a Congress designed to block change?"

---

Crysis was an FPS game

---

I think a combination of *real* exchange rates, current account,
exports could work as leading indicator for crysis. I'd compute RER
diy - CPI, official exch rates needed for the calc are all there. The
idea would be RER captures purchasing power parity, so compare two
CPIs.

---

```python
df = u.get_gmd()
df = df[(df.ISO3 == "ARG") & (df.year > 1970) & (df.year < 2027)].set_index("year")

df.CA_GDP.plot()
crisis_years = df[df['CurrencyCrisis'] == 1].index
for cy in crisis_years:
  plt.axvline(x=cy,color='red',linestyle='--',alpha=0.7)
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/556/531/730/957/699/original/3c8e1b178e329fb2.jpg'/>

---

`cons` and `cons_GDP` for consumption

---

`CA_GDP` current account as a percentage of GDP.. nice

---

Global Macro Database is like an all you can eat buffet.. What can I
*not* do with that...

---

CNBC: "Treasury yields fall as investors crowd into bonds for safety
amid election stock sell-off"

---

CNBC: "AI stocks slide as Texas governor result raises data center
risks.. Democrat Gina Hinojosa won the Texas governor’s race after
campaigning for tougher limits on data center development."

---

Intentional or not warmongering was placed on the ballot, and the MIC,
the private complex lost. They killed Charlie Kirk, took aim at Trump
in Butler PA, finally had their war, and now they got their
answer. This should serve as the impetus to defang them.

---

"Vice President JD Vance is blaming Republicans' abysmal midterm
performance directly on the Iran war."

---

HTW: "Democrat Troy Jackson pulls off historic upset in Maine, ends
Susan Collins' three-decade Senate run"

---

F24: "Midterms 2026: Democrats win control of House and Senate as
Republican strongholds fall"

---

\#Yemen 10/20 - 11/04

[[-]](mbl/2026/ymndata/map10.html)

---

LLM travel planning is still in shambles. The reason likely is because
LLM does not think algorithmically, it thinks textually. Whatever
connections, crumbs of thoughts it can glean from what people wrote,
becomes what it knows, (albeit in its "latent space" form). Sure
applied to even pure math, it can "crank out" formulas, bcz math
contains a lot of written symbols. But planning trips require real
world understanding, a grasp of space which LLM does not have. I
notice they are oblivious to forming blocks of know-how / knowledge
about ways of doing things, competences (which the Japanese call
"jutsu"). Humans naturally collect such tidbits throughout their
lives, but LLM is not made to learn such structures. This is a
failing, and a major reason why LLM tech is stagnant now, since 2023.

---

Good dataset... Highly recommended. It combines all the usual
variables for all countries, along with exports, imports, debt related
ones. Money base, interest rates, all there. They also label crisis
occurence per year (0/1), analysts developing predictive formulas can
find the data useful.

"Global Macro Database.. The world's most comprehensive macroeconomic
dataset."

[[-]](https://www.globalmacrodata.com/)

---

Using nationalization to bring down the debt.. It clearly worked for
post WWII Britain.

Economist Pettifor: "In 1945 here in Britain public debt was 250% of
GDP. That was because we had had six years of economic destruction
where we [took] our young men [out of the work force]..  had them
killed essentially. At home we were unable to produce. We were unable
to manufacture.. The government [was] pouring money into the economy
in order to generate food for the people and weapons for the soldiers.
But there was not income coming back in the form of tax revenues
because they were people were not employed in that sense...

Post war we've got 250% GDP debt-to-income and immediately the Labor
government began spending. It spent on the national health service, it
nationalized the health service, nationalized the education system
nationalized housing to a large extent. Nationalized the coal mines
for God's sake, and spent all that money and that generated
employment, and employment generated income, and .. quite quickly the
debt went down from 250% to about 20% of GDP and it stayed at 20% of
GDP, until the 1970s I'm afraid until Mrs. Thatcher came onto the
scene when the public debt began to rise relative to income."

---

"@toxi@mastodon.thi.ng

Happy 10th anniversary to this era-defining quote & prediction! 🎉

'Brexit means Brexit and we are going to make a Titanic success of it'

Boris Johnson"

---

Reuters: " Americans went to the polls on Tuesday in midterm
elections.. Voters rebuked Trump and his agenda, blaming him for
stubbornly high prices, with a large ‌majority unhappy about the
direction of the country, according to voter exit polls"

---

AP News: "[10/06] US has given at least $21.7 billion in military aid
to Israel since war in Gaza began, report says"

---

"@Lana@beige.party

This shit cost 2 trillion dollars btw."

[[-]](https://beige.party/@Lana/117548066946330957)

---

Mother Jones: "Using AI to Plan Backcountry Trips Is Getting People
Into Big Trouble.. By the time the three hikers called for help from a
rocky face on Mount Shasta in Northern California, they’d made a
series of bad decisions... Their lack of preparation and poor
planning, as they admitted later, came partly from relying on Google’s
artificial intelligence chatbot Gemini. By morning, they were lost on
a gnarly part of the mountain, and one hiker had banged up his knee...

The three 20-year-olds aren’t the only ones making missteps in wild
spaces with the help of artificial intelligence. Another Mount Shasta
visitor pitched her tent near a 'No Camping' sign, insisting she had a
right to do so because AI told her she could.. His team also
encountered a man wandering around at a trailhead with an AI-generated
map that showed prominent features on the wrong side of a nearby
mountain"

---

The Lever: "Big AI’s $140 Million Election Machine Stalls Out.. A
super PAC network became so politically toxic that it stopped donating
in the most competitive Congressional races."

---

"Serbia’s Political Tsunami Won’t Bring Geopolitical Transformation..
Serbia’s 'multivector' foreign policy has kept Belgrade reasonably
close to Beijing, Moscow, Brussels, and Washington. This 'four
pillars' strategy of balancing these partnerships—which dates back to
Boris Tadić’s presidency (2004–12)—will continue to shape Serbia’s
geopolitical orientation, experts told [TAC]"

---

This is what you get after decades of thinking electrification + solar
+ batteries would be enough to fix energy pollution, when in fact
nextgen nuclear + hydrogen was the silver bullet. People were caught
unprepared when the new energy demand hit and now even the pro climate
types are begging for energy from polluting sources.

Futurism: "New Data Centers in the US Set to Wipe Out 15 Years of
Greenhouse Gas Reductions. If the AI industry has its way, US carbon
emissions will rise 42 percent by 2030, a new Sierra Club analysis
found."

---

"@GossiTheDog@cyberplace.social

Danfoss are back in the news today over freezers defrosting in Europe
again, e.g. in Sweden. In Sweden, loads of the devices are directly
internet attached using 4G modems...  I've confirmed the freezers in
the countries impacted today are all mgmt interface facing internet,
same issue and vuln as last time. Many of the freezers are end of life
and have no patch available, they've just been left online to quite
literally rot."

---

BusinessInsider: Dozens of grocery stores across Europe have reported
rising temperatures in some of their refrigeration systems, with some
retailers calling it a cyberattack while another called it an 'IT
incident.' The incidents in Sweden, Belgium, and Estonia unfolded on
Sunday night and come weeks after a hack on fridges and freezers in
France that forced supermarkets to throw away food.

---

Consitutional Courts are becoming a problem in many countries.. When
power changes hands the new admin can find itself at odds with the
court whose members are left-overs from previous administrations. I'd
change the system so after every election the court gets wiped out,
out of 9 members 5 could be appointed by the majority in the
parliament, the rest by the opposition parties. That one person
majority gives enough room for the new gov to enact reforms, and allow
any one judge to "surprise" either side, stick to the law when
necessary, rather than the latest political hot topic.

---

Wired: "An underground activist group says it plans to start openly
doxing billionaires as part of a phased campaign against what it calls
the American oligarch.. They call themselves 'Capytistas,' a play on
Zapatistas, the Indigenous insurgents of southern Mexico."

---

It's tough to associate "Russia Russia Russia" with one side on this
one. People usually tie right-wing parties like LAJ to Russian
influence. But in the Polish case LAJ hates Russia (it probably has to
do with Poland's deep seated animosity against its one-time
neighbor). The party was founded by the Kaczynski twin brothers, one
of them, Lech, died in a plane crash, and surviving brother Jaroslaw
straight up blamed Moscow, Putin directly claiming he killed his
brother.

Tusk is not your usual pencil pusher centrist dumb ass either. There
are nuances on this one. But Tusk is solidly pro EU, ppl against the
EU won't like him.

---

Tusk is the current Polish PM, the President is an ally of the
previous government of Law and Justice party. Tusk's gov kept sending
judges to court, president refused to swear them in. It is
ridiculous. Tusk is right on this one.

---

Le Monde: "The refusal by the [Polish] president to swear in new court
judges, who were nominated by parliament, has spawned a constitutional
crisis in the country."

---

That is funny

But UK should return to EU

"@pikesley@mastodon.me.uk

Yeah but she also believes that Quantum exists Within AI"

>BBC News
>
>Reeves says UK's future should be inside the EU

---

I wonder chatbot recommends them because their site name has the word
404 in it, associated with web page failure. Who knows the bizarre
ways LLMs can halucinate.

404 Media: "ChatGPT Keeps Telling People 404 Media Can Solve Their
Tech Support Problems.. Because big tech platforms essentially do not
have customer support and make it impossible for their users to
contact a human, many people experiencing run-of-the-mill tech
problems have turned to ChatGPT. And, increasingly, ChatGPT is telling
people that have normal tech support problems that they have
discovered something journalistically notable and that 404 Media,
specifically, can help them.

Around two weeks ago, we started emailing these people back and asking
them how they found us; universally, the answer is that an AI chatbot
recommended they reach out to us and, in many cases, the chatbot wrote
the email, according to reviews of a handful of ChatGPT conversations
shared with 404 Media."


---

For *Young Washington* they picked a good actor. To play GW you need
size, like Liam Neeson level or, well, David Morse (who did play
Washington in the miniseries *John Adams*). All accounts talk about
that, Washington was an imposing figure, which probably helped him as
general.

And GW was a grinder, they got that right too. He wanted nothing
more than climbing the "career ladder", that is the British military,
he wanted to rise up in that system. But he was discriminated against,
they didn't want him because he was American born. Then they gave him
a militia command (outside the usual military chain), he displayed
bravery, skill in command during a battle (against the French
ironically), his fate was automatically decided by all these factors.
Once there was enough unrest against the Brits, here is the local
American general at the ready who was already commanding a local
militia. The Brits had created their own rebel leader. 

---

"@dougbinks@mastodon.gamedev.place

It is telling that the Proton engineering manifesto states::

'Why has productivity not increased dramatically if everyone is using
LLMs all the time already?'

Followed by a number of theories as to what needs to change to improve
productivity with LLM use. The most obvious answer is ignored - that
LLMs are not dramatically helping productivity and that their direct
and indirect costs should be more keenly considered against any gains."

---

A compliment to every progressive

Fox News: "Nancy Pelosi criticizes progressive Democrats' Israel stance"

---

Obama is supporting left-wing candidates these days all of whom
support Medicare for All, they are indirectly saying ACA was a
failure. BHO is clearly fine with that otherwise he would not be on
the campaign trail with them.

---

Current Affairs: "The ACA Marketplace Is a Scam Covered With the Veneer of 'Choice'"

[[-]](https://www.currentaffairs.org/news/2022/07/the-aca-marketplace-is-a-scam-covered-with-the-veneer-of-choice)

---

"@jonny@neuromatch.social

NSF requested 500 million dollars, total, for math AND physics, next
year:

Simply funding basic research is an absolute bargain compared to LLMs
brute forcing results for press releases"

---

Reuters: "Apple's new CEO is a product perfectionist taking on the AI
age.. While software rivals.. are spending hundreds of billions to
push artificial intelligence into every corner of their businesses,
the man set to lead one of the world's most iconic ​companies appears
to treat AI with a deliberate, almost stubborn pragmatism...

'We never think about shipping a technology,' Ternus.. said in a
recent interview.. 'We always think about how can we leverage
technology to ship amazing products'"

---

😂 😂 😂 

The Times: "Tech founders think AI will cure cancer — so they’ve
started smoking"

---

The OG of French protests, the French Revolution happened because of
too much debt. France overspent fighting its biggest rival abroad,
Britain, in the Americas, whose settlers eventually got their freedom
thanks to France, but the French got the bill. The king raised taxes
to pay, people revolted. He got the guillotine.

---

TechCrunch: "Anthropic expected to receive high ‘junk’ rating from
credit agencies following IPO, FT report says"

---

Reuters: "S&P Global [Ratings] revises Meta's outlook to 'negative' on
AI spending, cash flow worries"

---

We are seeing some positive moves from BHO

"Obama Endorses Socialist-Aligned Senate Candidates in Midterm
Push.. Former President Barack Obama campaigned in Michigan for Abdul
El-Sayed and supported Angie Nixon in Florida"

---

Barron's: "Voters in Los Angeles will settle a surprisingly
competitive mayoral race in Tuesday's midterm vote, a bitter showdown
between two progressive women of color who were once allies. Nithya
Raman, an 11th-hour entrant against Democratic incumbent Karen Bass,
has generated significant momentum..

Observers have drawn obvious comparisons between Raman and Mamdani:
both millennials, both South Asian, both born abroad and both
DSA-affiliated. But the similarities end there..  while Mamdani came
up through the DSA ranks as both an activist and a legislator, Raman's
affiliation has been far shakier"

---

Their fears became true. DJT is not spending for them. Reps are
complaining, that's the word 

WaPo: "[9/3] Republicans fear Trump will keep super PAC money and not
spend on the midterms. Some people around Trump have concluded that he
has little interest in spending the bulk of his super PAC funds on
this year's midterm races"

---

\#LLM \#Accuracy

[[-]](https://youtu.be/hxikiaOJ-_Y?t=1481)

---

CNBC: "[10/15] CoreWeave credit default swaps hit distress levels as
investors sour on AI debt"

---

Russia Derangement Syndrome

Politico: "Putin’s potential G20 comeback risks normalizing Russian
war crimes, says Kallas"

---

This is looking increasingly like World War 3. Romania is NATO.

Reuters: "[10/18] Romanian F-16 fighter jets shot ‌down two drones over
the country's territorial waters on Saturday, the defence ministry
said...  Defence Minister Radu Miruta said on Sunday the drones were
likely latest generation Russian drones, flying at speeds similar to
fighter jets.. The drones ⁠were brought down days after two chemical
tankers were hit by drones near Romania's Black Sea coast, the latest
​in a series of attacks highlighting risks to commercial shipping on
NATO's eastern flank."

---

A talk show with two Trek alumni Frakes and Spiner - *Dropping
Names*. Too bad Stewart passed away before he could become a guest.

---

