from lxml import html
import requests

page = requests.get('http://international.nytimes.com')
htmlFile = html.fromstring(page.text)


stories = htmlFile.xpath('//h3[@class="story-heading"]/text()')
stories2 = htmlFile.xpath('//h2[@class="story-heading"]/text()')

for i in range(0, len(stories)):
    stories_string = str(stories[i])
    stories2_string = str(stories2[i])
    if "\n" in stories_string:
        stories_string.replace("\n", "")
        with open("NYTimesStories.txt", "a") as f:
            f.write(stories_string)
    if "\n" in stories2_string:
        stories2_string.replace("\n", "")
        with open("NYTimesStories.txt", "a") as f:
            f.write(stories2_string)

file.close()
