
"@chiefsez@threads.net

@jonnolen@threads.net Working Americans paying $1000 per person per
month. Pretty much across the board. For the privilege to pay
thousands more for actual care. They clearly don’t fear us enough. But
they will. This might be the thing that gets us to pitchforks and
torches"

---

"@dgmor85@threads.net

@jonnolen@threads.net Just my wife and I, $32k"

---

"@jonnolen@threads.net

My health insurance premiums are 46,800 but go on and tell me how we
can't fucking afford Universal Single Payer health care. (Family of 4)"

---

"@top_news@mastodon.social

Nvidia live updates: Stock tanks after new affair allegations, board
reportedly preparing to oust Jensen Huang"

---

"@pikesley@mastodon.me.uk

People repeating the phrase Frontier Model like it means something"

---

The Conversation: "Police 'sniffer dogs' are less accurate, and more
harmful, than courts assume.. Research shows that 'sniffer dogs' have
a high rate of false alerts"

---

"@kibblesmith.bsky.social

Maybe the global economy should stop being the eight weirdest men
alive at the same time"

---

It looks like US GDP growth will slow 2027. If that continues in 2028,
and DJT net popularity remains as low as it is now, no Republican
candidate has any chance of winning the next election.

---

After years of electrification talk we get around 20% renewable usage
for most countries. This is abysmal. It mostly has to do with having
chosen the wrong technology. Electrification, batteries were the
inefficient route. Clean gasification / hydrogen and nextgen nuclear
would have worked better.

---

It is hydro (units in TWh)

```python
df[df.iso_code == 'NOR'][['hydro_consumption','primary_energy_consumption']].tail(1)
```

```text
hydro_consumption  primary_energy_consumption
                                          
       340.429                     555.626
```

---

That has to be hydro

---

Norway's is always very high

---

Percentage of low carbon (renewable plus nuclear) consumption per
country

```python
import pandas as pd

df = pd.read_csv('/opt/Downloads/energy-data-master/owid-energy-data.csv')
df = df.set_index('year')

countries = ['NOR','USA','DEU']
fig, axes = plt.subplots(len(countries), 1)
fig.suptitle('Low Carbon Consumption Percentage')

for i,code in enumerate(countries):
   dfm = df.copy()[df.iso_code == code]
   dfm['pct'] = dfm['low_carbon_consumption'] / dfm['primary_energy_consumption'] * 100
   dfm['pct'].plot(ax=axes[i],title=code)
   
plt.tight_layout()   
```

<img width='340' src='https://media.mastodontech.de/media_attachments/files/117/599/041/936/702/038/original/a1c328d88c56af98.jpg'/>

---

BP used to have a usable energy production / consumption dataset,
listed by energy source, now it is dead. The project below seems to
have taken the mantle.

[[-]](https://github.com/owid/energy-data/)

---

VulnCheck: "`curl` [Project] Gives Anthropic's OSS Scanner a Reality
Check..  Three days ago, Daniel Stenberg, who maintains `curl`,
announced that the project had received a batch of 45 vulnerability
reports from Anthropic. Anthropic rated only one as medium severity
and the rest as low. Daniel is moving them over to GitHub at a
deliberate pace "to soften the impact for the team," with plans to
have them all published by the end of the week. This gives us a rare
look at what Anthropic's findings look like once a maintainer actually
validates them.

Of the 34 reports published so far, 19 have been marked as not a
vulnerability, 6 have been confirmed as low severity, and 9 are still
awaiting assessment. That puts the false positive rate at 55.9% so
far, and only 17.6% of findings have been confirmed, all of them low
severity. That's a lot of work dumped on open source maintainers for a
small handful of low-impact bugs, and when a maintainer has to pace
reports just to protect his team, that says plenty about the burden."

---

I did hear execs absolutely disliked the new Gunn movie, *Man of
Tomorrow*, which, some suggest was the real event triggering his
firing. Did he go Tarantino on it like he did for Peacemaker S2?

---

Matalas shined that turd as best as he could, he was handed down a
garbage backstory. And I still don't care about this
character. \#VisionQuest

---

"@GossiTheDog@cyberplace.social

Pass the bong"

>Newsweek: "'I think for most people in this room, the most likely
>reason they will die is because of an AI accident,' OpenAI board
>member Paul Christiano told an audience"

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
    