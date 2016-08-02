# -*- coding: utf-8 -*-
import sqlite3, os

DATABASE = 'posts.db'
sqlite_db = None

def connect_db():
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    global sqlite_db
    if not sqlite_db:
        sqlite_db = connect_db()
    return sqlite_db

def close_db():
    if sqlite_db:
        sqlite_db.close()

def init_db():
    print 'initialising database...'
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print 'done'

def add_post(id, post):
    db = get_db()
    db.execute('insert into entries (article_id, title, image_url) values (?, ?, ?)',
               [id, post['title'], post['image_url']])
    db.commit()

def get_entries():
    db = get_db()
    cur = db.execute('select article_id, title, image_url from entries order by id desc')
    entries = cur.fetchall()
    return entries

def get_posts():
    entries = get_entries()
    posts = {}
    for e in entries:
        posts[e[0]] = {'title': e[1], 'image_url': e[2]}
    return posts

if __name__=='__main__':
    init_db()
    add_post('0', {'title':'test', 'image_url': 'example.com/test.jpg'})
    add_post('1', {'title':'test', 'image_url': 'example.com/test.jpg'})
    print get_posts()
