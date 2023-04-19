#!/usr/bin/env python3
# checkips.py
# Purpose: this script will scan for available hosts in a given network using nmap library
# USAGE: ./checkips.py
# Author: Jorge Barcasnegras
# Date: *19-04-2023

import nmap
import argparse
from tqdm import tqdm

# using argparse to ask to receive the IP through the terminal
parser = argparse.ArgumentParser(description='script to checks for ips in use')
parser.add_argument('ip', help='ip range to check, the information must be the networkID and in CIDR notation. example: 10.10.10.0/24', type=str)
args = parser.parse_args()

# saves the IP input by the user
ip = args.ip

print('scanning IP {}:'.format(ip))
scanner = nmap.PortScanner()

# Define a function to update the progress bar
def update_progress_bar(hosts_scanned, total_hosts):
    progress = int((hosts_scanned / total_hosts) * 100)
    tqdm.write('Scanning: {}% ({}/{})'.format(progress, hosts_scanned, total_hosts))

# Start the scan and display a progress bar
hosts = scanner.scan(hosts=ip, arguments='-sn')['scan']
total_hosts = len(hosts)
with tqdm(total=total_hosts) as pbar:
    for i, host in enumerate(hosts):
        update_progress_bar(i+1, total_hosts)
        pbar.update(1)

# Print the available hosts

print('\n Available hosts: {}'.format(scanner.all_hosts()))
