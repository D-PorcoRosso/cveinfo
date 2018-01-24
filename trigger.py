from cvedetail_parser import CVEDetailSingleParser
from cve_parser import CVESingleParser 
import sys

if len(sys.argv) < 2:
    sys.exit()

cveId = sys.argv[1]

s = CVESingleParser()
result = s.parse(cveId)
d = CVEDetailSingleParser()
result = result + d.parse(cveId)
print result
