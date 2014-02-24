import urllib2 as ur
from bs4 import BeautifulSoup as sp

#url = "http://gucky.uni-muenster.de/cgi-bin/rgbtab-en"
url = "http://cvsweb.xfree86.org/cvsweb/*checkout*/xc/programs/rgb/rgb.txt?rev=1.1"

page = ur.urlopen(url).read()
soup = sp(page)

colors = soup.body.string
import re

pattern = re.compile('(\d+ \d+ \d+)')
rgb_colors = pattern.findall(colors)
rgb_uniq = []
for color in rgb_colors:
  if color not in rgb_uniq: rgb_uniq.append(color)
