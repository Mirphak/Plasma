#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import time
import math

# Prorahn                          ~ 1.39 seconds
# Gorahn           25 prorahn     ~ 34.8  seconds
# Tahvo            25 gorahn      ~ 14.5  minutes
# Gahrtahvo        25 tahvo        ~ 6.05 hours
# Yahr              5 gahrtahvo    ~ 1.26 days
# Vailee           29 yahr         ~ 1    month
# Hahr             10 vailee       ~ 1    year
# Hahrtee fahrah  625 hahr         ~ 6.25 centuries
# 
#  1   Leefo       April 21 - May 27
#  2   Leebro      May 28 - July 3
#  3   Leesahn     July 3 - August 8
#  4   Leetar      August 9 - September 14
#  5   Leevot      September 14 - October 20
#  6   Leevofo     October 21 - November 26
#  7   Leevobro    November 26 - January 1
#  8   Leevosahn   January 2 - February 7
#  9   Leevotar    February 7 - March 15
# 10   Leenovoo    March 16 - April 21


def jday():
	(year, mon, mday, hour, min, sec, wday, yday, isdst) = time.gmtime()

	month1 = mon
	year1 = year
	day1 = mday
	hour1 = hour

	# Algorithm 1. Gregorian Date to Julian Day Number
	if month1 < 3:
		month1 = month1 + 12
		year1 = year1 - 1

	WD = day1 + int(((153 * month1) - 457) / 5) + math.floor(365.25 * year1) - math.floor(0.01 * year1) + math.floor(0.0025 *  year1)
	FD = ((hour1 * 3600) + (min * 60) + sec) / 86400
	JD = WD + FD + 1721118.5
	
	print(JD)

def dnitime():
	dniMonthsOTS = ["Leefo","Leebro","Leesahn","Leetahr","Leevot","Leevofo","Leevobro","Leevosahn","Leevotahr","Leenovoo"]

	(year, mon, mday, hour, min, sec, wday, yday, isdst) = time.gmtime()
	# Baseline conversion date (UTC time), equivalent to 9647 Leefo 1, 00:00:00:00
	#(year, mon, mday, hour, min, sec) = (1991, 4, 21, 16, 54, 00)

	month1 = mon
	year1 = year
	day1 = mday
	hour1 = hour

	# Algorithm 1. Gregorian Date to Julian Day Number
	if month1 < 3:
		month1 = month1 + 12
		year1 = year1 - 1

	WD = day1 + int(((153 * month1) - 457) / 5) + math.floor(365.25 * year1) - math.floor(0.01 * year1) + math.floor(0.0025 *  year1)
	FD = ((hour1 * 3600) + (min * 60) + sec) / 86400
	JD = WD + FD

	# Algorithm 6. Gregorian Date (Julian Day Number) to Cavernian Date
	JDD = JD - 727249.704166666
	AY = JDD * 0.793993705929756 + 1

	# Algorithm 4. Atrian Yahr Number to Cavernian Date
	# (Added the pahrtahvo calculation)
	Z = math.floor(AY)
	G = Z - 0.25
	A = math.floor(G / 290)
	C = Z - (A * 290)
	Z = (AY - math.floor(AY)) * 78125
	vailee = math.floor((C - 0.25) / 29) + 1
	yahr = C - ((vailee - 1) * 29)
	hahr = 9647 + A
	gahrtahvo = int(Z / 15625)
	pt = Z - (gahrtahvo * 15625)
	pahrtahvo = int(Z * 10 / 3125) / 10
	R = Z - (gahrtahvo * 15625)
	tahvo = int(R / 625)
	R1 = R - (tahvo * 625)
	gorahn = int(R1 / 25)
	prorahn = int(R1 - (gorahn * 25))

	# (Modified) Algorithm 3. Cavernian Date to Atrian Yahr Number
	# We determine the current (positive) D'ni century
	dnicent = 0
	while (hahr - dnicent) >= 625 and hahr > 0:
		dnicent += 625
	WY = yahr + ((vailee - 1) * 29) + ((hahr - dnicent) * 290)
	FY = ((gahrtahvo * 15625) + (tahvo * 625) + (gorahn * 25) + prorahn) / 78125
	atrian = int((int(WY + FY) - 0.25) / 290)

	# Display options for vailee names
	vaileeName = dniMonthsOTS[int(vailee)-1]

	# Time format display
	print("%d %s %d, %d:%02d:%02d" % (hahr, vaileeName, yahr, pahrtahvo, gorahn, prorahn))

