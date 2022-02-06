#Internet Archive Website
#Example code taken from the Introducing Python Book page. 11

import webbrowser
import requests


print("Let's find n old website")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url= "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()

try:
    old_site = data["archived_snapshots"]["closets"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)    