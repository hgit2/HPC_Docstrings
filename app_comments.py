#!/usr/bin/env python3
# coding: utf-8

from flask import Flask
from flask import abort, request, make_response
from flask import render_template, redirect, url_for

from data import USERS
# Set API dev in an another file
from api import SITE_API

app = Flask(__name__)
# Add the API
app.register_blueprint(SITE_API)


@app.route('/hello_world')
def hello_world():
    app.logger.debug('Hello world')    
    # instantiate a Response object
    resp = make_response("Hi! world !!")
    # add headers
    resp.headers['Content-Type']= 'text/plain'
    resp.headers['Content-language'] = 'fr'
    resp.headers['X-Parachutes'] = 'parachutes are cool'
    
    # check if accept-language is the same as content language
    if 'Accept-language' in request.headers:
        if resp.headers['Content-language'] in request.headers['Accept-language']:
            #resp.headers['Content-language'] = 'fr'
            resp.data="Bonjour le monde"
            return resp, 200
        else:
            #then return in englixh
            return resp, 200
    #return 'Hello, World!', 200



def find_user(username):
    for i in USERS:
        if i["name"]==username:
            return [i["id"],i["name"],i["wikipageid"],i["birth"], i["gender"], i["fields"] ]


@app.route('/users/')
@app.route('/users/<username>/')
def users(username=None):
    if not username:
        return render_template('users.html', users=USERS)
    else:
        return render_template('users.html', user=find_user(username))
    

@app.route('/adduser/', methods=['POST'])
def adduser():
    # Get the form content
#    form = request.form
#    app.logger.debug(dict(form))
    name=request.form["name"]
    iduser=request.form["id"]
    wikipageid=request.form["wikipageid"]
    birth=request.form["birth"]
    gender=request.form["gender"]
    fields=request.form["fields"]
    newuser=dict(id=iduser, name=name, wikipageid=wikipageid, birth=birth, gender=gender, fields=fields)
    USERS.append(newuser)
    return 'Hello, World! You posted {}'.format(dict(request.form.items())), 201

# Script starts here
if __name__ == '__main__':
    from os import environ
    DEBUG = environ.get('DEBUG')
    app.run(port=8000, debug=DEBUG)


