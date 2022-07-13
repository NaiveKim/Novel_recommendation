
# 이거쓰세요

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

df = pd.read_csv('./naver_comments_1404_page.csv')
df.info()

okt = Okt()

df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])
stopwords = stopwords + ['잘볼께요', '굿', '조지는거냐', '레알', '왓더퍽', '고고', '수고', '답글', '음',
                         '와', '인정', '존나', '웅앵웅', '제발','짱개', '시펄', '어머', '으이구', '아이고', '아', '개',
                         '미친', '아놔', '꺄', '퉷', '머지', '으와', '뭐', '홀랭', '웍', '쯧','쯧쯧','올','와우','흐음',
                         '까꿍', '아니', '띠용', '크으', '왤케', '야발', '조땠네', '깐붘', '응앸', '하필', '헐', '굳굳', '꺼억', '어우', '유휴', '흠', '아닉',
                         '시발', '새끼', '큭크크크', '그뇬', '모가지', '아놬', '지것넼', '호오', '어유', '대박', '클린', '부적절하다', '표현', '감지', '댓글',
                         '쓰레기','겨런', '개뿔', '엄꼬', '어웅우루우우', '텐디','안돠', '에이', '진짜', '씨발', '졸라', '멍청이', '브블브클브들벌브',
                         '아악', '베댓', '솔까말', '크크크큭']
count = 0
cleaned_sentences = []
for review in df.comments:
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
df = df[['titles', 'cleaned_sentences']]
df.dropna(inplace=True)

df.to_csv('./naver_comments_(cleaned).csv', index=False)
df.info()