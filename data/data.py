import pandas as pd

articles_feb = pd.read_csv('NYTArticlesFeb2017.csv')

print articles_feb.keys()

#print articles_feb.keywords
kw = articles_feb.keywords
timestamp = articles_feb.pubDate

f = open('article_keywords_and_dates.csv','w')
f.write('keywords,timestamp' + '\r\n')

for index, row in articles_feb.iterrows():
  
  print '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  line = '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  f.write(line + '\r\n')

f.close()
