from bs4 import BeautifulSoup
import requests
import sys
import csv
import re

class CVEDetailSingleParser(object):
    def parse(self, cveId):
        url = 'https://www.cvedetails.com/cve/CVE-'
        #cveId = sys.argv[1]
        print cveId
        url = url + cveId
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        CVSS = soup.find('div', attrs={'class':'cvssbox'})
        print CVSS.contents[0]
        vType = soup.find('span', attrs={'class':'vt_ec'})
        print vType.contents[0]

p = CVEDetailSingleParser()
p.parse("2017-6334")

