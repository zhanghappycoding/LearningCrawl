# _*_ coding: UTF-8 _*_

from bottle import request
import urllib2, urllib
import re
from lib.BeautifulSoup import BeautifulSoup

def clawdata(data):
    data = urllib.urlencode(data)
    url = "http://www.powerball.com/powerball/pb_nbr_history.asp"

    response = urllib2.urlopen(url, data)
    soup = BeautifulSoup(response)

    for tag in soup.findAll(valign="middle"):
        csoup = BeautifulSoup(str(tag))
        dictIssue = dict()
        dictIssue["issueDate"] = ""
        dictIssue["luckNum"] = [];
        if csoup.tr != None:
            for tag in csoup.tr.findAll('td'):
                if re.search("[0-9]+\/[0-9]+\/[0-9]{4}", str(tag.text)):
                    dictIssue["issueDate"] = str(tag.text)
                elif str(tag.text) != "&nbsp;":
                    dictIssue["luckNum"].append(int(tag.text))
            print dictIssue
            # store into file

if __name__=="__main__":
    data = {"startDate": '6/4/2016', "endDate": '9/19/2015'}
    clawdata(data)
