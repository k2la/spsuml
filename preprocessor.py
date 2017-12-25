import numpy as np
import pandas as pd
from gensim import models

def dataset2LBdata(dataset, look_back):
    x, y = [], []
    for i in range(len(dataset) - look_back):
        a = i + look_back
        x.append(dataset[i:a])
        y.append(dataset[a])
    return (np.array(x), np.array(y))


def doc2dic(doc):
    from gensim import corpora
    dic = corpora.Dictionary(doc)
    dic.save_as_text('./dic_text.dict')
    return dic

def dic2bow(dic, doc):
    dic.filter_extremes(no_below=0, no_above=1.9)
    return [dic.doc2bow(d) for d in doc]

def reduct_feature(corpus, dic):
    # TF-IDFによる重み付け
    # corpus = models.TfidfModel(corpus)[corpus]
    # # LSIによる次元削減
    # corpus = models.LsiModel(corpus, id2word=dic, num_topics=1)[corpus]
    return corpus

def bow2vec(bow):
    vec = []
    for _, b in enumerate(bow):
        vec.append([d[1] for d in b])
    return vec

def data2vec(values):
    dic = doc2dic(values)
    bow_corpus = dic2bow(dic, values)
    corpus = reduct_feature(bow_corpus, dic)
    vec = bow2vec(corpus)
    return vec
