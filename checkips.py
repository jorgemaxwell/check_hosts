#!/usr/bin/env python3

import nmap
import argparse

parser=argparse.ArgumentParser(description='script to checks for ips in use')
parser.add_argument('ip',help='ip range to check, the information must be the networkID and in CIDR notation. example: 10.10.10.0/24',type=str)
args = parser.parse_args()

ip = args.ip

print('scanning ip {}'.format(ip))
scaner = nmap.PortScanner()
scaner.scan(ip)

print(scaner.all_hosts())