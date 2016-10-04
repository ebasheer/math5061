import urllib.request as url
import json
import time

while True:
    septa = url.urlopen('http://www3.septa.org/hackathon/Arrivals/Temple%20U')
    retstr = septa.read().decode(encoding='utf-8')
    js = json.loads(retstr)
    for train in js[next(iter(js.keys()))][1]['Southbound']:
        orig = str(train['origin']).ljust(20)
        dest = str(train['destination']).ljust(20)
        status = str(train['status']).ljust(20)
        sched = str(train['sched_time']).ljust(20)
        track = str(train['track']).ljust(20)
        print(orig, dest, track, status, sched)
    print('*'*5)
    time.sleep(30)
