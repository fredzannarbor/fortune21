#!/usr/bin/env python3

import sys
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

print(sys.argv[1:])
# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://[::]:5011/'

#@click.command('cli')
def cli():
   string = sys.argv[1:]
   print(string)
   args = " ".join(string)
   print(args)
   payload = {"options" : args }
   print(payload)
   sel_url = server_url+'fortune'
   response = requests.get(url=sel_url.format(), params=payload)
   print(response.text)

