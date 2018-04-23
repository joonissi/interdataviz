import pandas as pd

#Import data from csv
input_file = 'article_keywords_and_dates_march_2018.csv'
df = pd.read_csv(input_file, delimiter=',')


counts = df['keywords'].value_counts().reset_index().to_csv('article_keywords_counts_march_2018.csv')
#counts = df.groupby('keywords').count()

#print counts