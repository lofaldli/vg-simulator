# -*- coding: utf-8 -*-
import crawler, twitter, time, database, requests

def main():

    url = 'http://vg.no'
    keywords = ['snegl',
                'kropp',
                'dette',
                'paradise',
                'pladask',
                'miss universe',
                'frøken norge',
                'sex',
                'triks',
                'pokemon',
                'undertøy',
                'hollywood',
                'kjendis',
                'øvelse',
                'slik',
                'slank',
                'digg'
            ]

    old_posts = database.get_posts()

    try:

        new_posts = crawler.crawl(url, keywords)

        new = 0

        for k,v in new_posts.items():
            if k not in old_posts.keys():
                title = v['title'].encode('utf-8')
                print 'POSTING' , title
                print twitter.post_status(title)

                database.add_post(k, v)
                new += 1
                time.sleep(1)

        if new == 0:
            print 'no new posts found'
        elif new == 1:
            print 'one new post found'
        else:
            print str(new) + ' new posts found'

    except requests.exceptions.ConnectionError:
        print 'could not connect'



if __name__=='__main__':
    main()
