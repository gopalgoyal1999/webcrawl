import bs4

import urllib.request as url

path = "https://www.indeed.co.in/jobs?q="

http_response = url.urlopen(path)

page =bs4.BeautifulSoup(http_response,'lxml')

job = input("enter the type of job u want ")

newpath =path+job

http_response = url.urlopen(newpath)

page1 =bs4.BeautifulSoup(http_response,'lxml')

data=page1.findAll('div',class_="title")
data2=page1.findAll('span',class_="company")
data3=page1.findAll('span',class_="location")
data4=page1.findAll('div',class_="summary")

for i in range(len(data)):
    title=data[i].text
    title=title.replace(" ","")
    title=title.replace("\n","")
    print(f"{i+1}. {title}")
    title1=data2[i].text
    title1=title1.replace(" ","")
    title1=title1.replace("\n","")
    print(f"  {title1}")
    title3=data3[i].text
    title3=title3.replace(" ","")
    title3=title3.replace("\n","")
    print(f"  {title3}")
    title4=data4[i].text
    title4=title4.replace("\n","")
    print(f"  {title4}")
    print(" *"*20)
