#!/usr/bin/python

class Clock:
	def __init__(self, time):
		self.time = time
	def print_time(self,time):
		print(time)
		
		
clock = Clock("6:00")
print(clock)


clock.print_time("8:00")