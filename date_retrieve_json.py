import urllib
import json
import re


print "The script provides current date and time in Nairobi and saves it to file in JSON format"
url = 'http://www.timeanddate.com/worldclock/kenya/nairobi'
content = urllib.urlopen(url).read()
date = re.findall(r'<span .*?ctdat>(.*?)</span>', str(content))

data = []
data.append({'Nairobi date and time:': date})

with open("data.json", "w") as file:
        json.dump(data, file)