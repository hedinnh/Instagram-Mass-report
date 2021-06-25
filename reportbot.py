import os
def clear_screen():
    os.system('cls')

clear_screen()

from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()

from os import path
from time import sleep 

from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style
import os
import sys

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=91))
PROMPT_COMMAND='echo -en "\033]0;[-] Inspectahs Reporter [-]\a"'

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Enter the link of the video you want to report")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Ticket Opened!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Video mass report complaint is starting!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Ticket Opened!")
        if (k== 5): print()
        i = i + 1

def profile_attack(proxies):
    username = ask_question("Enter the username of the person you want to report")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Ticket Opened!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("user mass report complaint is starting!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Ticket Opened!")
        if (k == 5): print()
        i = i + 1

def main():
    print_success("Successfully loaded all the modules!\n")

    ret = ask_question("Would you like to use a proxy? [Y / N]")

    proxies = []

    if (ret == "Y" or ret == "y"):
        ret = ask_question("Would you like to collect your proxies from the internet? [Y / N]")

        if (ret == "Y" or ret == "y"):
            print_status("Gathering proxy from the Internet! This may take a while.\n")
            proxies = find_proxies()
        elif (ret == "N" or ret == "n"):
            print_status("Please have a maximum of 50 proxies in a file!")
            file_path = ask_question("Enter the path to your proxy list")
            proxies = parse_proxy_file(file_path)
        else:
            sleep(1)
            print_logo()

        print_success(str(len(proxies)) + " Number of proxy found!\n")
    elif (ret == "N" or ret == "n"):
        pass
    else:
        print_error("Not a valid option")
        sleep(1)
        print_logo()

    

    print("")
    print_status("1 - Report a user.")
    print_status("2 - Report a video.")
    report_choice = ask_question("Please select the complaint method")
    print("")

    if (report_choice.isdigit() == False):
        print_error("Not a valid option")
        sleep(1)
        print_logo()
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("Not a valid option")
        sleep(1)
        print_logo()

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[*] Exiting Ig mass report")
        print(Style.RESET_ALL)
        _exit(0)
