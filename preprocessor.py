import numpy as np
import pandas as pd
from gensim import models

class PreProcessor:
    def dataset2LBdata(self, dataset, look_back):
        x, y = [], []
        for i in range(len(dataset) - look_back):
            a = i + look_back
            x.append(dataset[i:a])
            y.append(dataset[a])
        return (np.array(x), np.array(y))


    def doc2dic(self, doc):
        from gensim import corpora
        dic = corpora.Dictionary(doc)
        dic.save_as_text('./dic_text.dict')
        return dic

    def dic2bow(self, dic, doc):
        dic.filter_extremes(no_below=0, no_above=1.9)
        return [dic.doc2bow(d) for d in doc]

    def reduct_feature(self, corpus, dic):
        # TF-IDFによる重み付け
        # corpus = models.TfidfModel(corpus)[corpus]
        # # LSIによる次元削減
        # corpus = models.LsiModel(corpus, id2word=dic, num_topics=1)[corpus]
        return corpus

    def bow2vec(self, bow):
        vec = []
        for _, b in enumerate(bow):
            vec.append([d[1] for d in b])
        return vec

    def data2vec(self, values):
        bow_corpus = self.dic2bow(self.dic, values)
        corpus = self.reduct_feature(bow_corpus, self.dic)
        vec = self.bow2vec(corpus)
        return vec

    def data2vec_by_dic(self, values):
        self.dic = self.doc2dic(values)
        bow_corpus = self.dic2bow(self.dic, values)
        corpus = self.reduct_feature(bow_corpus, self.dic)
        vec = self.bow2vec(corpus)
        return vec