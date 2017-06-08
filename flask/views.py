import os
import json
import pprint
from bson.json_util import dumps
import logging
from pymongo import MongoClient
from flask import request, render_template, Response
from app import app
from models import Post
client = MongoClient('db')
db = client.usda

@app.route('/api', methods=['GET'])
def api():
    a = db.pie.find_one()
    app.logger.info(a['data'])
    json_response = dumps(a['data'])
    return Response(json_response,
                    status=200,
                    mimetype='application/json')

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text=text).save()
    posts = Post.objects.all()
    '''
    posts = db.foodgroups.find();
    #app.logger.info(dumps(_items))
    # posts = [item for item in _items]
    return render_template('index.html', posts=posts)
