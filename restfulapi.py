import pickle
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask,jsonify,render_template,request 

app = Flask(__name__)
model = pickle.load(open('D:\\python_virtual\\enthire\\airline_model.sav','rb'))
vocab = pickle.load(open('D:\python_virtual\enthire\\vocab.sav','rb'))

@app.route('/',methods = ['POST'])
#@app.route('/api_call',methods = ['POST'])
def api_call():
    data = request.get_json(force = True)
    data = [data['sentence']]
    cv_test = CountVectorizer(vocabulary = vocab.vocabulary_)
    test_text = cv_test.transform(data)
    op = ['positive','negative']
    res = [op[int(model.predict(test_text))]]

    return  jsonify(sentiment=res)

if __name__ == "__main__":
    app.run(port=5000,debug=True)
