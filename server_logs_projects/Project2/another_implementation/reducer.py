#!/usr/bin/env python

from __future__ import division
from collections import defaultdict
from datetime import datetime
import sys

def reducer():
    counts = defaultdict(list)
    count = 0
    old_date = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        this_date, _ = data

	#print this_date
        if old_date and this_date != old_date:
            day = datetime.strptime(old_date, '%Y-%m-%d').weekday()
            counts[day].append(count)
            #print('{}\t{}\t{}'.format(old_date, sum(counts[day]), len(counts[day])))
            count = 0


        #day = datetime.strptime(this_date, '%Y-%m-%d').weekday()
        count += 1
        old_date = this_date


    for each in counts:
        print('{}\t{}'.format(each, sum(counts[each])/len(counts[each])))

if __name__ == "__main__":
    reducer()
