import operator
import pickle
import string
import time
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_dict():
    d = []
    f = open('./dict.txt')
    for line in f:
        d.append(line.replace('\n', ''))
    return d

def get_tfidf():
    f = open('./tf_idf_no.pickle','rb')
    object_file = pickle.load(f)
    f.close()
    return object_file

def get_words_idf():
    f = open('./words_idf.pickle','rb')
    object_file = pickle.load(f)
    f.close()
    return object_file

def get_law(text):
    use_this_dict_to_cut_and_build_matix = get_dict()
    tfidf_per_NO = get_tfidf()
    words_idf = get_words_idf()

    w_indoc = {}
    ll = 0

    for w in use_this_dict_to_cut_and_build_matix:
        if w in text:
            if w in w_indoc:
                w_indoc[w] += text.count(w)
            else:
                w_indoc[w] = text.count(w)
            ll += text.count(w)
    
    xx = {}
    for w in words_idf:
        if w in w_indoc:
            xx[w] = words_idf[w] * w_indoc[w]
        else:
            xx[w] = 0
    
    r_NO = {}
    for no in tfidf_per_NO:
        s = 0
        for x in tfidf_per_NO[no]:
            s += tfidf_per_NO[no][x] * xx[x]
        r_NO[no] = s
    sorted_r_NO = sorted(r_NO.items(), key=operator.itemgetter(1))
    sorted_r_NO = sorted_r_NO[::-1]
    
    return sorted_r_NO

@app.route('/test')
def test():
    return 'Test service success'

@app.route('/', methods=['POST'])
def process():
    text = request.args.get('text', default='')
    # text = request.form.get('text', default='')
    result = get_law(text)
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)