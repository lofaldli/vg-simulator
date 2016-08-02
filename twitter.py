# -*- coding: utf-8 -*-
import requests, json
from requests_oauthlib import OAuth1

def get_keys():
    return json.loads(open('SECRETS.json').read())

def get_auth():
    keys = get_keys()
    return OAuth1(keys['consumer_key'], keys['consumer_secret'],
                  keys['access_token'], keys['access_token_secret'])

def post_status(status):
    auth = get_auth()
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    r = requests.post(url, auth=auth, data={'status':status})
    return r.status_code

if __name__=='__main__':
    post_status('test test')
