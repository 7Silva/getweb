import requests
import sys
from time import sleep
from colorama import Style, Fore, Back

def headers(args=None):
    if args is None:
        args = sys.argv

    url = args[2]
    sts = requests.get(url, allow_redirects=False)
    if sts.status_code == 301:
        print(f'[{Fore.YELLOW}-{Fore.RESET}] Redirect!')
        sleep(1)
        print()
        print(sts.headers)
    elif sts.status_code == 401:
        print(f'[{Fore.RED}-{Fore.RESET}] Unauthorized!')
        sleep(1)
        print()
        print(sts.headers)
    elif sts.status_code == 404:
        print(f'[{Fore.RED}-{Fore.RESET}] Not Found!')
        sleep(1)
        print()
        print(sts.headers)
    elif sts.status_code == 500:
        print(f'[{Fore.RED}-{Fore.RESET}] Internal Server Error!')
        sleep(1)
        print()
        print(sts.headers)
    else:
        print(sts.headers)