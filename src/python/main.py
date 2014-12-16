#!/usr/bin/python
#encoding=utf-8
from download_and_parse import *
import redis
import jieba
jieba.load_userdict("/home/candy/test/pachong/crawler/test/dict.txt")
def download_all(red, page_num):
    s = catch_a_page("http://m.byr.cn/board/Job")
    result = parse_page(s)
    for key in result:
        r.set(key.split("/")[3], result[key])
    for i in xrange(2, page_num):
        s = catch_a_page("http://m.byr.cn/board/Job?p=" + str(i))
        result = parse_page(s)
        for key in result:
            red.set(key.split("/")[3], result[key])

def query_words(red):
    all_key = red.keys()
    query = {}
    for key in all_key:
        ll = jieba.cut(r.get(key).split("====")[0])
        for words in ll:
            if query.has_key(words):
                query[words].add(key)
            else:
                query[words] = set(key)
    return query

def insert_query(red, query):
    for keys in query:
        value = ""
        for link in query[keys]:
            value += link + ";"
        red.set(keys, value)

def print_all(red):
    keyss = red.keys()
    for key in keyss:
        print key

def delete_all(red):
    red.flushdb()

if __name__ == "__main__":

    print "this is main function"
    jieba.load_userdict("/home/candy/test/pachong/crawler/test/dict.txt")
    r = redis.Redis("127.0.0.1", 6379, 0)
    download_all(r, 400)
    query = query_words(r)
    r = redis.Redis("127.0.0.1", 6379, 1)
    insert_query(r, query)
    print_all(r)
    #delete_all(r)
    '''
    result = parse_page(s)
    all_key = r.keys()
    query = {}
    for key in all_key:
        ll = jieba.cut(r.get(key).split("====")[0])
        for words in ll:
            if query.has_key(words):
                query[words].add(key)
            else:
                query[words] = set(key)
    for key in query:
        print key
        for link in query[key]:
            print link
        print ""
    '''






