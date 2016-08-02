# -*- coding: utf-8 -*-
import crawler, twitter, time, database

def main():

    url = 'http://vg.no'
    keywords = ['snegl',
                'kropp',
                'skjer dette',
                'paradise',
                'pladask',
                'miss universe',
                'frøken norge',
                'sex',
                'trikset',
                'pokemon',
                'undertøy',
                'kjendis'
            ]

    old_posts = database.get_posts()
    new_posts = crawler.crawl(url, keywords)

    for k,v in new_posts.items():
        if k not in old_posts.keys():
            print 'POSTING' , v['title']
            print twitter.post_status(v['title'])

            database.add_post(k, v)
            time.sleep(1)


if __name__=='__main__':
    main()
