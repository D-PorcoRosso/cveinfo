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
        data = [[cveId, descripition, len(references), references]]

        f = open("cve.csv","a")
        w = csv.writer(f)
        w.writerows(data)
        f.close()

p = CVESingleParser()
p.parse("2017-7240")
p.parse("2017-6334")
p.parse("2017-6077")
p.parse("2017-3881")
p.parse("2016-6435")
p.parse("2016-6433")
p.parse("2014-9583")
p.parse("2014-8243")
p.parse("2014-1635")
p.parse("2013-7030")
p.parse("2013-3568")
p.parse("2012-2765")
p.parse("2011-3315")
p.parse("2008-0403")


