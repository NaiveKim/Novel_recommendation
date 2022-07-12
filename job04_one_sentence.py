import pandas as pd

df = pd.read_csv('./cleaned_comment_1480.csv')
df.dropna(inplace=True)
df.info()
one_sentences = []
for title in df['cleaned_titles'].unique():
    temp = df[df['cleaned_titles'] == title]
    if len(temp) > 30:
        temp = temp.iloc[:30, :]
    one_sentence = ' '.join(temp['cleaned_sentences'])
    one_sentences.append(one_sentence)
df_one = pd.DataFrame({'cleaned_titles':df['cleaned_titles'].unique(), 'cleaned_sentences':one_sentences})
print(df_one.head())
df_one.to_csv('./cleaned_comment_1480_one.csv', index=False)