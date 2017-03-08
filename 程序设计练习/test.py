# coding:utf-8

import json

x = []


q2 = json.loads(open('1.json', 'r').read())
q1 = json.loads(open('user_list.txt', 'r').read())

q = q1 + q2

for i in q:
    w = i
    if w not in x:
        x.append(w)

print len(x)

e = open('55.json', 'w')
e.write(json.dumps(x))
e.close()
