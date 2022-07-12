import pandas as pd
from gensim.models import Word2Vec

review_word = pd.read_csv('./cleaned_comment_1480_one.csv')
review_word.info()

cleaned_token_reviews = list(review_word['cleaned_sentences'])
print(cleaned_token_reviews[0])

cleaned_tokens = []
for sentence in cleaned_token_reviews:
    token = sentence.split()
    cleaned_tokens.append(token)
print(cleaned_tokens[0])

embedding_model = Word2Vec(cleaned_tokens, vector_size=100,
                           window=4, min_count=20,
                           workers=6, epochs=100, sg=1)
embedding_model.save('./models/word2vec_comments.model')
print(list(embedding_model.wv.index_to_key))
print(len(embedding_model.wv.index_to_key))

