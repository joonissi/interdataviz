import pandas as pd
import re

articles_feb = pd.read_csv('NYTArticlesFeb2017.csv')

print articles_feb.keys()

#print articles_feb.keywords
kw = articles_feb.keywords
timestamp = articles_feb.pubDate

f = open('article_keywords_and_dates.csv','w')
f.write('keywords,articleID,timestamp' + '\r\n')

for index, row in articles_feb.iterrows():
  
  #print '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  #line = '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  #f.write(line + '\r\n')

  s = row['keywords'][1:-1].replace('\'','').replace('"','\'')
  ss = [x.strip() for x in s.split(',')]
  #print ss

  for i in ss:
    sss =  i + ',' + row['articleID'] + ',' + row['pubDate']
    print sss
    f.write(sss + '\r\n')

f.close()

#print articles_feb.keys()
