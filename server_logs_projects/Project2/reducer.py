#!/usr/bin/env python

from datetime import datetime
import sys


def reducer():

	dayList = dict()
	old_day = None
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 3:
			continue

		this_day, this_date, _ = data

		if old_day and old_day != this_day:
			#date_str = datetime.fromordinal(int(this_date)).date()
			print("{}\t{}".format(old_day, sum(dayList.values())/len(dayList.keys())))
			#print("{}\t{}\t{}".format(old_day, sum(dayList.values()), len(dayList.keys())))
			#for i in dayList:
			#	print i, dayList[i]
			#print("{}\t{}".format(old_date, count))
			dayList = dict()

		old_day = this_day
		dayList[this_date] = dayList.get(this_date, 0) + 1


	if old_day:
        	print("{}\t{}".format(old_day, sum(dayList.values())/len(dayList.keys())))
		#print("{}\t{}\t{}".format(old_day, sum(dayList.values()), len(dayList.keys())))
		#for i in dayList:
		#	print i, dayList[i]



if __name__ == "__main__":
	reducer()
