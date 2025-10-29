import requests
import xml.etree.ElementTree as ET


response=requests.get("https://www.ynet.co.il/Integration/StoryRss2.xml")
print(response)
data= ET.fromstring(response.content)
items = data.findall(".//item")

# Extract and print titles
for item in items:
    title = item.find("title").text
    print(title)