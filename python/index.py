from flask import Flask, render_template, request, make_response, jsonify
from flask.helpers import url_for
import requests
import sapcai

app=Flask(__name__)

#token d475521f36a9539e5e4d673bf807c3f4
build=sapcai.Build('d475521f36a9539e5e4d673bf807c3f4', 'en')


@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.method=='POST'):
        question=request.form['question']
        print(question)
        response=build.dialog({'type':'text', 'content':question}, 'CONVERSATIONAL_ID')
        #print(response) #DialogResponse
        messages=response.messages
        l=[]
        for message in messages:
            l.append({'type':message.type,'content':message.content})
        print(l)
        return jsonify(results=l)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)