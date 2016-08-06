# -*- coding: utf-8 -*-
import requests, re
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')

def find_pattern(soup, pattern, name='a'):
    return soup.find_all(name,
                         string=re.compile(pattern.decode('utf-8'),
                                           flags=re.I))

def find_parent(elem):
    parent = None

    # find first div
    for p in elem.parents:
        if p and p.name=='div':
            parent = p
            break

    if not parent:
        raise Exception('could not find parent')
    return parent

def find_title(elem):
    title = ''
    for d in elem.descendants:
        if d.name in ['h1', 'h2', 'h3', 'h4', 'h5']:
            for s in d.find_all('span'):
                if s.string:
                    title += s.string.strip() + ' '
    return title


def find_image_path(elem):
    # find image and title by searching for <img> and <h3>
    image_path = None
    for d in elem.descendants:
        if d.name == 'img' and '.jpg' in d['src']:
            image_path = d['src']

    return image_path

def crawl(url, keywords):
    '''
    finds a sub tree in an html document given by url;
    <div>
        ...
        <img src=image_url ></img>
        ...
        <h3><span>title</span></h3>
        ...
    </div>
    '''
    soup = get_soup(url)

    matches = []
    for k in keywords:
        m = find_pattern(soup, k)
        matches.extend(m)

    posts = {}
    for m in matches:
        parent = find_parent(m)
        id = parent.parent['id']
        if id not in posts.keys():
            posts[id] = {'title': find_title(parent),
                         'image_url': find_image_path(parent)}

    return posts

if __name__=='__main__':
    posts = crawl('http://vg.no', ['kropp', 'snegl', 'slik', 'triks'])
    for p in posts:
        print posts[p]['title']


