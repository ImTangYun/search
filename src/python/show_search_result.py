#!/usr/bin/python
#encodeing=utf-8

import sys
import jieba
import redis

if __name__ == '__main__':

    red = redis.Redis("127.0.0.1", 6379, 1)
    words = jieba.cut(sys.argv[1], True)
    keys = {}
    for word in words:
        try:
            re = red.get(word).split(";")
            keys[word] = re
        except Exception:
            continue
            print "split error"

    for_sort = {}
    for key in keys:
        for link in keys[key]:
            if for_sort.has_key(link):
                for_sort[link] += 1
            else:
                for_sort[link] = 1
    
    sorted_ = {}
    for link in for_sort:
        if sorted_.has_key(for_sort[link]):
            sorted_[for_sort[link]].append(link)
        else:
            l = [link]
            sorted_[for_sort[link]] = l

    red = redis.Redis("127.0.0.1", 6379, 0)
    count = 0
    for i in range(len(sorted_), 0, -1):
        if not sorted_.has_key(i):
            continue
        if not sorted_[i]:
            continue
        for link in sorted_[i]:
	    if link == 5:
		continue
            x = red.get(link)
            if x:
                if count > 10:
                    break
                count +=1
                print '<a href="http://m.byr.cn/article/Job/'+link+'">'+x+'</a><br><br>'














