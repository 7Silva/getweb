import requests
import sys
from colorama import Style, Fore, Back

def status(args=None):
    if args is None:
        args = sys.argv

    url = args[2]
    sts = requests.get(url, allow_redirects=False)
    if sts.status_code == 301:
        print(f"[{Fore.YELLOW}-{Fore.RESET}] Status do Servidor/Website: {Style.BRIGHT}{sts.status_code} / Moved Permanently{Style.RESET_ALL} | URL: {Style.BRIGHT}{url}{Style.RESET_ALL}")
    elif sts.status_code == 401:
        print(f"[{Fore.RED}-{Fore.RESET}] Status do Servidor/Website: {Style.BRIGHT}{sts.status_code} / Unauthorized{Style.RESET_ALL} | URL: {Style.BRIGHT}{url}{Style.RESET_ALL}")
    elif sts.status_code == 404:
        print(f"[{Fore.RED}-{Fore.RESET}] Status do Servidor/Website: {Style.BRIGHT}{sts.status_code} / Not Found{Style.RESET_ALL} | URL: {Style.BRIGHT}{url}{Style.RESET_ALL}")
    elif sts.status_code == 500:
        print(f"[{Fore.RED}-{Fore.RESET}] Status do Servidor/Website: {Style.BRIGHT}{sts.status_code} / Internal Server Error{Style.RESET_ALL} | URL: {Style.BRIGHT}{url}{Style.RESET_ALL}")
    else:
        print(f"[{Fore.BLUE}-{Fore.RESET}] Status do Servidor/Website: {Style.BRIGHT}{sts.status_code}{Style.RESET_ALL} | URL: {Style.BRIGHT}{url}{Style.RESET_ALL}")
