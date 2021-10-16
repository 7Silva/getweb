import requests
import sys
import os

def html(args=None):
    if args is None:
        args = sys.argv

    url = args[2]
    sts = requests.get(url)
    
    print(sts.text)

    if args[3] == '--export':
        url2 = url.split('https://')
        resolve = url2[1]

        print(os.listdir('./src/export/'))

        with open(f'./src/export/{resolve}.txt', 'wb') as writer:
            writer.write(sts.text.encode("utf-8"))
