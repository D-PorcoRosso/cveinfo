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
        if "Unknown CVE ID" in response.text:
            return []
        soup = BeautifulSoup(response.text, 'lxml')
        CVSS = soup.find('div', attrs={'class':'cvssbox'})
        vType = soup.find('span', attrs={'class':'vt_ec'})
        data = [CVSS.contents[0],vType.contents[0]]
        return data
        
#p = CVEDetailSingleParser()
#print p.parse("2017-6334")

