import bs4

import urllib.request as url

path="https://www.indiatvnews.com/"

http_response=url.urlopen(path)

webpage1=bs4.BeautifulSoup(http_response,'lxml')

print(" HELLO ")
print(" NEWS => FYI,INDIA,WORLD,BUSINESS,SPORTS,SCIENCE,CRIME,JOB,POLITICS,ENTERTAINMENT,EDUCATION,LIFESTYLE ")

news=['fyi','india','world','science','politics','education','business','jobs']

c= True

def dip(data):
    for i in range(0,len(data)):
        print(i+1,data[i].text)
        print("  "*20)
    print("*"*20)
    
  
while c:

    News_name=input(" Enter the news type :   ")

    News_name=News_name.lower()

    if News_name=='bye':
        print("      THANKS      ")
        c=False
        break

    newpath=path+News_name

    http_response=url.urlopen(newpath)

    webpage2=bs4.BeautifulSoup(http_response,'lxml')
    
        
    if News_name in news :

        page=webpage2.find('div',class_="big-news-list")

        data=page.findAll('a')

        print(News_name+"  News  ")
        dip(data)

    print("  LATEST NEWS  ")
    page1=webpage2.findAll('ul',class_="list")
    for i in range(0,len(page1)):
        data=page1[i].findAll('p',class_="titel")
        dip(data)
    print("*"*20)


    data=webpage2.findAll('p',class_="title")
    dip(data)
    
    print(" MORE NEWS")
    page2=webpage2.findAll('div',class_="content")
    for i in range(0,len(page2)):
        data=page2[i].find('a',)
        print(i+1,data.text)
        print("  "*20)
    print("*"*20)

    print(" TOP NEWS ")
    page1=webpage2.find('ul',class_="rhs_story")
    data=page1.findAll('p',class_="title")
    dip(data)
   
