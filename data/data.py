import pandas as pd
import re
import ast

articles_feb = pd.read_csv('NYTArticlesMarch2018.csv')

print articles_feb.keys()

#print articles_feb.keywords
kw = articles_feb.keywords
timestamp = articles_feb.pubDate

f = open('article_keywords_and_dates_march.csv','w')
f.write('keywords,articleID,pubDate' + '\r\n')

for index, row in articles_feb.iterrows():
  
  #print '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  #line = '\"' + row['keywords'][1:-1].replace('\'','').replace('"','\'') + '\"' + ',' + row['pubDate']
  #f.write(line + '\r\n')

  #s = row['keywords'][1:-1].replace('\'','').replace('"','\'')
  s = ast.literal_eval(row['keywords'])
  s = [n.strip() for n in s]
  ss = [n.replace(',', '') for n in s]
  print ss

  for j in ss:
    line = j + ',' + row['articleID'] + ',' + row['pubDate']
    print line
    f.write(line + '\r\n')

  #ss = [x.strip() for x in s.split(',')]
  #print ss

  # for i in ss:
  #   sss =  i + ',' + row['articleID'] + ',' + row['pubDate']
  #   print sss
  #   f.write(sss + '\r\n')

f.close()

#print articles_feb.keys()
