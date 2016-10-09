# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:44:35 2016

@author: fred
"""
import subprocess
import os
import shlex
import psutil
from flask import Flask, request
from two1.wallet import Wallet
from two1.bitserv.flask import Payment

# Configure the app and wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/fortune', methods=['GET', 'POST'])
@payment.required(3000)
def buy_fortune():

    options = str(request.args.get('options'))
    print(options)
    x = options or ''
    print(x)
    optvalue = 'fortune' + ' ' + options
    print(optvalue)
    args = shlex.split(optvalue)
    print(args)
    fortune = subprocess.check_output(args)
    return fortune

# Initialize and run the server
if __name__ == '__main__':

   import click

   @click.command()
   @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")

   def run(daemon):
            if daemon:
                pid_file = './fortune21-server.pid'
                if os.path.isfile(pid_file):
                    pid = int(open(pid_file).read())
                    os.remove(pid_file)
                    try:
                        p = psutil.Process(pid)
                        p.terminate()
                    except:
                        pass
                try:
                    p = subprocess.Popen(['python3', 'fortune21-server.py'])
                    open(pid_file, 'w').write(str(p.pid))
                except subprocess.CalledProcessError:
                    raise ValueError("error starting fortune21-server.py daemon")
            else:
                print("fortune21 server running...")
                app.run(host='::', port=5011)
   run()
