#!/usr/bin/python

# Copyright 2012 Cory Koch
#
# This file is part of PrayerTimes.
#
# PrayerTimes is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PrayerTimes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PrayerTimes. If not, see <http://www.gnu.org/licenses/>.
#
# ********************************************************************
  
import urllib2
from BeautifulSoup import BeautifulSoup
import os

HOME = os.getenv("HOME")
# Pain to parse but gives more options
islamicFinder="http://www.islamicfinder.org/prayerDetail.php?country=usa&city=Cleveland&state=OH&id=18707&month=&year=&email=&home=2012-7-18&lang=&aversion=&athan=&monthly="

# Easy to parse
ICGC="http://www.iccleveland.org/"
PAGE = urllib2.urlopen(ICGC)
#PAGE = check_cache()
SOUP = BeautifulSoup(PAGE)

PRAYER_TIMES_TBL = SOUP.find('table', attrs={'class':'stripe leftjustify', 'cellspacing':'0'})
INFO             = SOUP.find('div', attrs={'class':'info'})

DATE = INFO.findAll('b')
COLS = PRAYER_TIMES_TBL.findAll('td')

# Check to see if a cache exists
# speed up performance/ reduce load on servers.

def open_cache():
    '''open the prayertimes cache'''
    try:
        f = open('HOME/.prayertime', 'r+')
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        
    return f

def write_to_cache(x, f):
    '''write the prayer times to cache'''
    f.write(page)
    

def check_cache():
    f = open_cach()
    if True:#f.readline() == :
        page = f.read()
    
    # cache DNE or is out of date
    else:
        try:
            page = urllib2.urlopen(ICGC)
            write_to_cache(page, f)
        except:
            print "The site must be down..."
    
    return page


def print_date():
    '''print date from site '''
    for i in DATE:
        print i.text
        print '-----------------'


def print_prayer_time():
    '''print prayer times for site'''

    x = 0
    times = []
    prayers = []
    for element in COLS:
    
        x=x+1
        if (x %2 ) == 0:
            times.append(element.text)
        else:
            prayers.append(element.text)


    for prayer, time in zip(prayers, times):
    
        prayerp = list(prayer)
        timep = list(time)
        for i in prayerp:
            if i == ':':
                n = prayerp.index(':')
                prayerp[n] = '|'
        
        for j in timep:
            if j == 'a':
                timep.append('m')
            if j == 'p':
                timep.append('m')

            

        print '%8s %s' % ("".join(prayerp),"".join(timep))

    print '-----------------'
    

def get_date():
    ''' gets date from site '''
    for i in DATE:
        return i.text


def get_prayer_times():
    ''' gets prayer times from site '''
    x = 0
    times = []
    prayers = []
    prayer_time = []
    for element in COLS:
    
        x=x+1
        if (x %2 ) == 0:
            times.append(element.text)
        else:
            prayers.append(element.text)

    
    for prayer, time in zip(prayers, times):
    
        prayerp = list(prayer)
        timep = list(time)
        for i in prayerp:
            if i == ':':
                n = prayerp.index(':')
                prayerp[n] = '|'
        
        for j in timep:
            if j == 'a':
                timep.append('m')
            if j == 'p':
                timep.append('m')
    
        prayer_time.append('%8s %s' % ("".join(prayerp),"".join(timep)))

    return prayer_time

if __name__=="__main__":
    print_date()
    print_prayer_time()



#table = soup.find({"table" : True, "width" : "330", "cellspacing" : "1","align" : "center", "bgcolor" : "#a9c6f7"})

#cols = rows.findAll('td')

#print cols






