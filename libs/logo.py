import os
from colorama import Fore, Back, Style
from random import choice

logo = """

        ██╗ ██████╗     ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
        ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
        ██║██║  ███╗    ██╔████╔██║███████║███████╗███████╗    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
        ██║██║   ██║    ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
        ██║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║███████║    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
        ╚═╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                                                                          """.replace('█', f'{Fore.WHITE}█{Fore.BLACK}')


def print_logo():
    os.system(f"title Instagram Mass Report Bot Made by Rdimo#6969")
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.YELLOW + "[#] Made by Rdimo#6969"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)