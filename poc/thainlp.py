
# coding: utf-8

# ### make is-a tuples according to wordnet

# In[ ]:


from pythainlp.corpus import wordnet as wn

import codecs

LANG = "tha"
OUTPUT_V = "relationship_{}-v.csv".format(LANG)
OUTPUT_N = "relationship_{}-n.csv".format(LANG)

import logging
logging.basicConfig(level=logging.INFO) # to see logs from gensim


# #### get all word relationship

# In[ ]:


def write_all_rel(pos, fp):
    for i, synset in enumerate(list(wn.all_synsets(pos))):
        if i%100 == 0:
            print("{} -> {}".format(synset.name(), str(synset.hyponyms())))

        for synset_sub in synset.hyponyms():
            for word_parent in synset.lemma_names(lang=LANG):
                for word_child in synset.lemma_names(lang=LANG):
                    fp.write("{},{}\n".format(word_parent, word_child))

with codecs.open(OUTPUT_V, "w", "utf-8") as fp:
    write_all_rel("v", fp)
with codecs.open(OUTPUT_N, "w", "utf-8") as fp:
    write_all_rel("n", fp)


# #### unique relationship

# In[ ]:


def unique_rel(filename):
    rel = {}
    for line in codecs.open(filename, "r", "utf-8"):
        tokens = line.strip().split(",")
        if tokens[0] not in rel:
            rel[tokens[0]] = []
        if tokens[1] not in rel[tokens[0]]:
            rel[tokens[0]] += [tokens[1]]

    print("{}: {} words".format(filename, len(rel)))

    with codecs.open(filename, "w", "utf-8") as f:
        for word1 in rel:
            for word2 in rel[word1]:
                f.write("{},{}\n".format(word1, word2))

unique_rel(OUTPUT_V)
unique_rel(OUTPUT_N)


# #### learn poincare embedding

# In[ ]:


from gensim.models.poincare import PoincareModel


# In[ ]:


def build_relationship(name_file="relationship_tha.csv"):
    relations = []
    for line in codecs.open(name_file, "r", "utf-8"):
        tokens = line.strip().split(",")
        relations += [(tokens[0], tokens[1])]
    return relations

rels_v = build_relationship(name_file=OUTPUT_V)
rels_n = build_relationship(name_file=OUTPUT_N)


# In[ ]:


VALUE_DEFAULT_EPOCHS = 100
VALUE_DEFAULT_SIZE = 50
VALUE_DEFAULT_NEGATIVE = 10
VALUE_DEFAULT_MEMO = ""
VALUE_DEFAULT_BURNIN = 10
VALUE_DEFAULT_REG = 1.0

def make_filename_model(lang=LANG, 
                        epochs=VALUE_DEFAULT_EPOCHS,
                        size=VALUE_DEFAULT_SIZE,
                        negative=VALUE_DEFAULT_NEGATIVE,
                        memo=VALUE_DEFAULT_MEMO,
                        burnin=None,
                        reg=None
                       ):
    if burnin != None and reg != None:
        return "poincare_{}_{}e_{}d_{}n_{}b_{}r_{}.h5".format(lang, epochs, size, negative, burnin, reg, memo)
    else:
        return "poincare_{}_{}e_{}d_{}n_{}.h5".format(lang, epochs, size, negative, memo)

def train(rels, 
          lang=LANG, 
          epochs=VALUE_DEFAULT_EPOCHS,
          epochs_load=0,
          size=VALUE_DEFAULT_SIZE, 
          negative=VALUE_DEFAULT_NEGATIVE,
          memo=VALUE_DEFAULT_MEMO,
          burnin=None,
          reg=None,
          resume=False):
    try:
        if resume:
            filename = make_filename_model(lang, epochs_load, size, negative, memo, burnin, reg)
            model = PoincareModel.load(filename)
            print("resume {}".format(filename))
        else:
            print("first training")
            raise ValueError()
    except:
        if resume:
            print("file not found")
        model = PoincareModel(rels, burn_in=0, regularization_coeff=0, negative=negative, size=size)
    
    model.train(epochs=epochs, print_every=1500)
    model.save(make_filename_model(lang, epochs+epochs_load, size, negative, memo, burnin, reg))
    
    return model


# #### train recipes

# In[ ]:


# train only nouns (first 1000 epochs, 50dims)
model = train(rels_n, epochs=1000, size=50, negative=50, memo="n")


# In[ ]:


# train more
model = train(rels_n, epochs=1000, size=50, negative=50, memo="n", epochs_load=1000, resume=True)


# In[ ]:


# train only nouns (first 100 epochs, 2dims)
model = train(rels_n, epochs=100, size=2, memo="n")


# In[ ]:


# train only nouns (first 200 epochs, 200dims, burnin and reg = 0)
# these settings seem to work better,
# according to https://rare-technologies.com/implementing-poincare-embeddings/
model = train(rels_n, epochs=200, size=200, memo="n", burnin=0, reg=0)


# In[ ]:


# train more (200 epochs, 200dims, burnin and reg = 0)
model = train(rels_n, epochs=200, size=200, memo="n", epochs_load=200, resume=True, burnin=0, reg=0)


# #### some attemptions

# In[ ]:


model = PoincareModel.load(make_filename_model(LANG, 400, 200, 10, "n", 0, 0))


# In[ ]:


model.kv.descendants("ไก่")


# *Cleaning the structure or separating it seems to be needed*

# ### visualize sample hypernyms (synsets)

# In[ ]:


from gensim.test.utils import datapath
from gensim.models.poincare import PoincareRelations

file_path = datapath("poincare_hypernyms_large.tsv")
rels = PoincareRelations(file_path)

for epochs in [5, 10, 20, 50, 100, 1000]:
    model = PoincareModel(rels, size=2)
    model.train(epochs=epochs)

    import plotly
    import gensim.viz.poincare

    plotly.offline.init_notebook_mode(connected=False)
    prefecutre_map = gensim.viz.poincare.poincare_2d_visualization(model=model,
                                                                   tree=rels,
                                                                   figure_title="{} epochs".format(epochs),
                                                                   show_node_labels=model.kv.vocab.keys())
    plotly.offline.iplot(prefecutre_map)


# ### visualize thai hypernyms

# In[ ]:


import random
from gensim.viz.poincare import poincare_2d_visualization
from IPython import display
from plotly.offline import init_notebook_mode, iplot

init_notebook_mode(connected=True)


# In[ ]:


rels_show = random.sample(rels_n, 100)
rels_labeled = random.sample(rels_show, 50)


# In[ ]:


figure_title = "visualize embedding poincare 100 epochs"
model = PoincareModel.load(make_filename_model(LANG, 100, 2, 10, "n"))
iplot(poincare_2d_visualization(model, set(rels_show), figure_title, num_nodes=10, show_node_labels=rels_show))


# In[ ]:


figure_title = "visualize embedding poincare 1000 epochs"
model = PoincareModel.load(make_filename_model(LANG, 1000, 2, 10, "n"))
iplot(poincare_2d_visualization(model, set(rels_show), figure_title, num_nodes=10, show_node_labels=rels_show))


# In[ ]:


figure_title = "visualize embedding poincare 3000 epochs"
model = PoincareModel.load(make_filename_model(LANG, 3000, 2, 10, "n"))
iplot(poincare_2d_visualization(model, set(rels_show), figure_title, num_nodes=10, show_node_labels=rels_show))


# # tests

# In[ ]:


import pythainlp as ptn


# In[ ]:


words = ptn.tokenize.word_tokenize("สวัสดีครับ")
words


# In[ ]:


ptn.tag.pos_tag(words, engine="perceptron")


# ### get all Thai words defined in wordnet

# In[ ]:


from pythainlp.corpus import wordnet as wn


# In[ ]:


class ThaiWords():
    def __init__(self):
        self.vocab = set()
        for synset in list(wn.all_synsets("n")):
            self._traverse(synset)
    
    def _traverse(self, synset):
        for word in synset.lemma_names("tha"):
            self.vocab.add(word)
        for synset_sub in list(synset.hyponyms()):
            print(synset_sub)
            self._traverse(synset_sub)


# In[ ]:


len(wn.all_lemma_names(pos="n", lang="tha"))


# In[ ]:


wn.synset("object.n.01").lemma_names(lang="jpn")


# In[ ]:


x = list(wn.all_synsets("n"))


# In[ ]:


x[0].lemma_names(lang="tha")


# In[ ]:


wn.synsets("親", lang="jpn")


# In[ ]:


wn.synset("gray.a.01").lemma_names(lang="eng")

