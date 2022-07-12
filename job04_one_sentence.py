import pandas as pd

df = pd.read_csv('./naver_comments_(cleaned).csv')
df.dropna(inplace=True)
df.info()
one_sentences = []
for title in df['titles'].unique():
    temp = df[df['titles'] == title]
    if len(temp) > 30:
        temp = temp.iloc[:30, :]
    one_sentence = ' '.join(temp['cleaned_sentences'])
    one_sentences.append(one_sentence)
df_one = pd.DataFrame({'titles':df['titles'].unique(), 'reviews':one_sentences})
print(df_one.head())
df_one.to_csv('./cleaned_naver_comments_one.csv', index=False)