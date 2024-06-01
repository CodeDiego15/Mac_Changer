#!/usr/bin/env python3
# coding=utf-8
import subprocess
from argparse import ArgumentParser  # Use argparse instead of optparse
from colorama import Fore 
import re
__version__ = "0.1.0"

def print_banner():
    # Import colorama within the function

    print(Fore.LIGHTRED_EX + """
          
            
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠇
⠀⠈⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠏⠀
⠀⠀⠈⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣶⣶⣾⣿⣿⣿⣿⣿⣶⣶⣶⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀
⠀⠀⠀⠀⢻⣿⣄⠀⠀⠀⠀⣀⣤⣶⣿⡿⢟⣿⣿⡿⠛⠋⠉⠀⠀⠀⠀⠈⠉⠛⠻⣿⣿⣿⠿⣿⣷⣦⣄⡀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠛⠋⠀⣠⣶⣿⠿⠛⠉⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠈⠙⠻⢿⣷⣦⡀⠈⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⠿⠋⠁⠀⠀⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⠀⠀⠀⠉⠻⢿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⢠⣿⡟⠀⠀⠀⠀⠀⢀⣴⣿⠿⠿⠿⠿⢿⣷⣄⠀⠀⠀⠀⠀⠘⣿⣧⠀⠀⠀⠀⠀⠙⢿⣿⣦⡀⠀⠀
⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠙⢿⣷⡀⠀⠀⠀⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠘⢿⣿⣄⠀
⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣧
⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿
⠀⠘⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⢿⣿⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⢀⣾⡿⠁⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠀
⠀⠀⠀⠙⢿⣷⣄⡀⠀⠀⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠙⠿⣿⣶⣤⣤⣴⣾⣿⠟⠁⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠙⠿⣿⣦⣀⠀⠀⠀⠙⣿⣧⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁⠀⠀⢀⣠⣾⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣦⣄⡀⠘⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠀⣀⣤⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣶⣽⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣵⣾⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 

                    RedEye by DiegoDev. --help si necesita ayuda.

    """ + Fore.RESET)


print_banner()


# Define command-line arguments
parser = ArgumentParser(description= "Change MAC address of a network interface")
parser.add_argument("-i", "--interface", dest="interface", required=True,
                    help="Network interface to change its MAC address")
parser.add_argument("-m", "--mac", dest="new_mac", required=True,
                    help="New MAC address to set")
parser.add_argument("-v", "--version", action="version", version=f"MACMorph {__version__}") 
# Parse arguments
args = parser.parse_args()

if not args.interface:
    parser.error(Fore.LIGHTRED_EX + "[-] Please specify an interface and a new MAC address")
elif not args.new_mac:
    parser.error(Fore.LIGHTRED_EX + "[-] Please specify an interface and a new MAC address")


interface = args.interface
new_mac = args.new_mac


if interface and new_mac:
    print(Fore.LIGHTCYAN_EX + f"[+] Changing MAC address {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface, "ether", new_mac])
else:
    print("Error: Unable to change MAC address")

ifconfig_result = subprocess.check_output(["ifconfig",interface])

mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode("utf-8"))

if mac_address:
    print(Fore.LIGHTGREEN_EX + f"[+] MAC address {mac_address.group(0)} changed successfully")
else:
    print(Fore.LIGHTRED_EX + "[-] MAC address not changed")
    
    
    
