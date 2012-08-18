#!/usr/bin/python

import urllib2
from BeautifulSoup import BeautifulSoup

# Pain to parse but gives more options
islamicFinder="http://www.islamicfinder.org/prayerDetail.php?country=usa&city=Cleveland&state=OH&id=18707&month=&year=&email=&home=2012-7-18&lang=&aversion=&athan=&monthly="

# Easy to parse
ICGC="http://www.iccleveland.org/"

page = urllib2.urlopen(ICGC)
soup = BeautifulSoup(page)


prayer_times_tbl = soup.find('table', attrs={'class':'stripe leftjustify', 'cellspacing':'0'})
info             = soup.find('div', attrs={'class':'info'})

date = info.findAll('b')
cols = prayer_times_tbl.findAll('td')

def print_date():
    '''print date from site '''
    for i in date:
        print i.text
        print '-----------------'


def print_prayer_time():
    '''print prayer times for site'''

    x = 0
    times = []
    prayers = []
    for element in cols:
    
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
    for i in date:
        return i.text


def get_prayer_times():
    ''' gets prayer times from site '''
    x = 0
    times = []
    prayers = []
    prayer_time = []
    for element in cols:
    
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






