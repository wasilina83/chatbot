from bs4 import BeautifulSoup
import requests

# Data from https://www.picoauto.com/support/ https://www.picoauto.com/support/topic22842.html
# Tutorial from https://www.youtube.com/watch?v=Zp417bPfvN0

sites_el = [""]
for elementes in range(-425, 0, 25):
    sites_el.append(str(elementes))

for el in sites_el: 
    url = f'https://www.picoauto.com/support/forum2{el}.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #row-item topic_read
    boddy = soup.find('ul', attrs={'class':'topiclist topics'})
    topics = boddy.find_all('li')

    for point in range(0,len(topics),1):
        point_data = topics[point].text.split('\n')
        point_data = list(filter(len,point_data))
        print(point_data)

        



#     print(soup)
#<body id="phpbb" class="notouch section-viewforum/forum2.html ltr hasjs">


    # url = f'https://www.picoauto.com/support/forum2.html'
    # page = requests.get(url)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # #row-item topic_read
    # boddy = soup.find('div', attrs={'class':'inner'})
    # print(boddy)
    # #print(soup)