"""
Iegūt ziņas, izmantojot rss no google.lv.

"""
import feedparser

#norādu RSS plūsmas URL, kas satur google.lv ziņas
rss_url='https://news.google.com/rss?hl=lv&gl=LV&ceid=LV:lv'

# Lejupieladet un iznalizēt RSS plūsmu

feed=feedparser.parse(rss_url)

#japarāda ziņu virsrakstus un saites

for entry in feed.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    print("\n")
