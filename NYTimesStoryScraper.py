from lxml import html
import requests

page = requests.get('http://international.nytimes.com')
htmlFile = html.fromstring(page.text)
file = open("NYTimesStories.txt", "w")

stories = htmlFile.xpath('//h3[@class="story-heading"]/text()')

for i in range(0, len(stories)):
    stories_string = str(stories[i])
    if "\n" in stories_string:
        stories_string.replace("\n", "")
        file.write(stories_string)
        print(stories_string)

file.close()
