import requests
from datetime import datetime

hosts = [
    ['ns09', 'ns.coconnect09.ir:2083', 'saeed', 'Sa13733731'],
    ['ns10', 'ns.coconnect10.ir:2053/coconnect/git', 'saeed', 'Sa13733731'],
    ['ns11', 'ns.coconnect11.ir:2083/coco/network', 'saeed', 'Sa13733731'],
    ['ns12', 'ns.coconnect12.ir:2053/coconnect/git', 'saeed', 'Sa13733731'],
    ['ns13', 'ns.coconnect13.ir:2053/coconnect/git', 'saeed', 'Sa13733731']
]
f = open('logs', 'a')
for host in hosts:
    time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    try:
        data = {
            'username': host[2],
            'password': host[3]
        }
        url = 'http://' + host[1] + '/login'

        a = requests.post(url, data)
        b = a.headers['Set-Cookie']
        b = b.split('session=')
        b = b[1].split(';')
        coockie = {'session': b[0]}

        url = 'http://' + host[1] + '/panel/api/inbounds/createbackup'

        get_backup = requests.get(url, cookies=coockie)
        msg = '\n' + time + ' ==> ' + host[0] + ' backup succuss'
        f.write(msg)
        print(msg)

    except:

        msg = '\n' + time + ' ==> ' + host[0] + ' backup failed'
        f.write(msg)
        print(msg)

f.close()
