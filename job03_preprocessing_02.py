### 기존 작성

# import pandas as pd
# from konlpy.tag import Okt
# import re
#
# df = pd.read_csv('./crawling_data/reviews_2017_2022.csv')
# df.info()
#
# okt = Okt()
#
# df_stopwords = pd.read_csv('./stopwords.csv')
# stopwords = list(df_stopwords['stopword'])
#
# count = 0
# cleaned_sentences = []
# for review in df.reviews:
#     count += 1
#     # if count % 10 == 0:
#     #     print('.', end='')
#     # if count % 100 == 0:
#     #     print()
#     # review = re.sub('[^가-힣 ]', ' ', review)
#     # review = review.split()
#     # words = []
#     for word in review:
#         if len(word) > 20:
#             word = ' '
#         words.append(word)
#     review = ' '.join(words)
#     token = okt.pos(review, stem=True)
#
#     df_token = pd.DataFrame(token, columns=['word', 'class'])
#     df_token = df_token[(df_token['class'] == 'Noun') |
#                         (df_token['class'] == 'Verb') |
#                         (df_token['class'] == 'Adjective')]
#     words = []
#     for word in df_token.word:
#
#         if 1 < len(word):
#             if word not in stopwords:
#                 words.append(word)
#     cleaned_sentence = ' '.join(words)
#     cleaned_sentences.append(cleaned_sentence)
#
# df['cleaned_sentences'] = cleaned_sentences
# df = df[['title', 'cleaned_sentences']]
# df.dropna(inplace=True)
#
# df.to_csv('./crawling_data/cleaned_review_2018.csv', index=False)
# df.info()

import pandas as pd
from konlpy.tag import Okt
import re

df = pd.read_csv('./crawling_data/reviews_2017_2022.csv')
df.info()

okt = Okt()

df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])
stopwords = stopwords + ['잘볼께요', '굿', '조지는거냐', '레알', '왓더퍽', '고고', '수고', '답글', '음',
                         '와', '인정', '존나', '웅앵웅', '제발','짱개', '시펄', '어머', '으이구', '아이고', '아', '개',
                         '미친', '아놔', '꺄', '퉷', '머지', '으와', '뭐', '홀랭', '웍', '쯧','쯧쯧','올','와우','흐음',
                         '까꿍', '아니', '띠용', '크으', '왤케', '야발', '조땠네', '깐붘', '응앸', '하필', '헐', '굳굳', '꺼억', '어우', '유휴', '흠', '아닉']
count = 0
cleaned_sentences = []
for review in df.reviews:
    count += 1
    if count % 10 == 0:
        print('.', end='')
    if count % 100 == 0:
        print()
    review = re.sub('[^가-힣 ]', ' ', review)
    review = review.split()
    words = []
    for word in review:
        if len(word) > 20:
            word = ' '
        words.append(word)
    review = ' '.join(words)
    token = okt.pos(review, stem=True)

    df_token = pd.DataFrame(token, columns=['word', 'class'])
    df_token = df_token[(df_token['class'] == 'Noun') |
                        (df_token['class'] == 'Verb') |
                        (df_token['class'] == 'Adjective')]
    words = []
    for word in df_token.word:

        if 1 < len(word):
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_sentences'] = cleaned_sentences
df = df[['title', 'cleaned_sentences']]
df.dropna(inplace=True)

df.to_csv('./crawling_data/review_2017_2022(cleaned).csv', index=False)
df.info()