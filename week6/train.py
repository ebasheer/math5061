import urllib.request as url
import json
import time

COLWIDTH=18

while True:
    septa = url.urlopen('http://www3.septa.org/hackathon/Arrivals/Temple%20U')
    retstr = septa.read().decode(encoding='utf-8')
    js = json.loads(retstr)
    for train in js[next(iter(js.keys()))][1]['Southbound']:
        orig = str(train['origin']).ljust(COLWIDTH)
        dest = str(train['destination']).ljust(COLWIDTH)
        status = str(train['status']).ljust(COLWIDTH)
        sched = str(train['sched_time']).ljust(COLWIDTH)
        track = str(train['track']).ljust(2)
        print(orig, dest, track, status, sched)
    print('*'*5)
    time.sleep(30)
