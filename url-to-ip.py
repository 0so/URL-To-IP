import socket
from urllib.parse import urlparse
from colorama import init, Fore, Style

init(autoreset=True) # colorama

def get_ip(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.scheme:
            domain = parsed_url.netloc 
        else:
            domain = url

        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print(Fore.RED + "No se pudo resolver el nombre de dominio" + Style.RESET_ALL)
        return None



banner = """
             ____  ____   _______   ___           ___________  ______         __       _______   
            ("  _||_ " | /"      \ |"  |         ("     _   ")/    " \       |" \     |   __ "\  
            |   (  ) : ||:        |||  |          )__/  \\__/// ____  \      ||  |    (. |__) :) 
            (:  |  | . )|_____/   )|:  |             \\_ /  /  /    ) :)     |:  |    |:  ____/  
             \\ \__/ //  //      /  \  |___          |.  | (: (____/ //      |.  |    (|  /      
             /\\ __ //\ |:  __   \ ( \_|:  \         \:  |  \        /       /\  |\  /|__/ \     
            (__________)|__|  \___) \_______)         \__|   \"_____/       (__\_|_)(_______)    
"""
print(Fore.YELLOW + banner + Style.RESET_ALL)
print(Fore.MAGENTA + "BY @0SO -> (https://github.com/0so)" + Style.RESET_ALL + "\n")
url = input(Fore.CYAN + "URL:" + Style.RESET_ALL + " ")
ip = get_ip(url)
if ip:
    print(Fore.CYAN + "IP:" + Style.RESET_ALL, Fore.GREEN + ip + Style.RESET_ALL)

