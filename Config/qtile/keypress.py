import threading
import os 
import time

class KeyPress(threading.Thread):
	def run(self):
		os.system(f"mpg123 sounds/press{choice(range(1,4))}.mp3")
