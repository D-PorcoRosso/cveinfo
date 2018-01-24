from bs4 import BeautifulSoup
import requests
import sys
import csv
import re

class CVESingleParser(object):
    def parse(self, cveId):
        url = 'http://cve.mitre.org/cgi-bin/cvename.cgi?name='
        #cveId = sys.argv[1]
        print cveId
        url = url + cveId
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        #print(response.text)
        tdResult = soup.find_all('td')
        cveId = 'CVE-'+cveId
        descripition = tdResult[10].contents
        references = []
        try:
            for t in tdResult[12].contents[1]:
                if t.name == 'li':
                    references.append(t.text)
        except IndexError:
            print "no references"
        data = [cveId, descripition, len(references), references]

        #f = open("cve.csv","a")
        #w = csv.writer(f)
        #w.writerows(data)
        #f.close()
        return data

#p = CVESingleParser()
#print p.parse("2017-7240")
