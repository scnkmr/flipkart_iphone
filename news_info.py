'''www.sachinthakur.in'''
import requests
from bs4 import BeautifulSoup as bs

page=requests.request("GET","https://www.marketingmind.in/category/startup/")
content=bs(page.content,"html.parser")
#print(content.prettify())
title=content.find_all("a",class_="post_name")
date=content.find_all("li",class_="post-meta-author-date")
img=content.find_all("img",class_="jw-responsive-img")

post_title=[x.get_text().replace(",","") for x in title]
post_link=[x["href"] for x in title]
post_date=[x.get_text().replace(",","") for x in date]
post_img=[x["src"] for x in img]

f=open("iphone_from_flipkart.csv","w",encoding="utf-8")
f.write("Post Title, Post Date, Post Image link, Post Link \n")
for x in range(len(post_title)):
    f.write(post_title[x]+","+post_date[x]+","+post_img[x]+","+post_link[x]+"\n")

f.close()

