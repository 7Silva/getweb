import sys
import os
from time import time

def main(args=None):
    try:
        if args is None:
            args = sys.argv
        def clear():
            os.system('cls')
        
        clear()

        if args[1].lower() == "help":
            print(f'Para obter mais informações sobre um comando específico, digite nome_do_comando --help')
            print(f'-STATUS   [url]            Retorna os Status code do Servidor/Website.')
            print(f'-HEADERS  [url]            Retorna a headers do Website.')
            print(f'-HTML     [url]            Retorna o codigo HTML do Website.')
            print()
        elif args[1].lower() == "-status":
            if args[2] == '--help':
                from src.help.statush import statush
                statush()
                exit()
            from src.status import status
            status()
        elif args[1].lower() == "-headers":
            if args[2] == '--help':
                from src.help.headersh import headersh
                headersh()
                exit()
            from src.headers import headers
            headers()
        elif args[1].lower() == "-html":
            if args[2] == '--help':
                from src.help.htmlh import htmlh
                htmlh()
                exit()
            from src.html import html
            html()
        

        return 0
    except KeyboardInterrupt:
        exit()
 
if __name__ == '__main__':
    sys.exit(main())