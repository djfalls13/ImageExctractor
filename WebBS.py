

#!/usr/bin/env python3

import os

def clearsreen():
    os.system('cls' if os.name == 'nt' else 'clear')

clearsreen()


#Import Modules

from bs4 import BeautifulSoup

import requests

import urllib.request

import urllib3

from urllib.parse import urljoin

http = urllib3.PoolManager()  # Create Instance of Urlllib


#Get the link with Requests and create Soup

websiteurl = input('Enter a full http:// website address:  ')

html_doc = requests.get(websiteurl) #Creates object

soup = BeautifulSoup(html_doc.text, 'html.parser')  #use object.text to get text content


'''
# If Input ends with 'index.html' this must trim it off

if websiteurl.endswith('index.html'):

    websiteurl = websiteurl[:-10]        # Treats the string like a List removing last 10 characters
    print('\n\ntest trim right side: ' , websiteurl)
else:
    pass
'''


print(' \n\n\n  Resolving:   \n\n\n')

for i in soup.find_all('img'):
    y = websiteurl

    z = i.get('src')

    xyz = urljoin(y, z)

    print(y)

    print(z)

    print(' ')

    print(xyz)

    #urllib.request.urlretrieve(xyz, z)



print('\n')

wait = input("PRESS ENTER TO CONTINUE.")

clearsreen()

print('Attempting Image Download')




http = urllib3.PoolManager()  # Create Instance of Urlllib


os.system('rm -rf images')

os.system('mkdir images')




file = open('images/urllist.txt', 'w')


for i in soup.find_all('img'):
    y = websiteurl

    z = i.get('src')

    xyz = urljoin(y, z) + '\n '

    #print(y)

    #print(z)

    print(xyz)

    file.write(xyz)

file.close()


os.system('wget -i images/urllist.txt -P images/')





'''
This code needs to be debugged
Keep getting File Not Found errors
will try WGET as a workaround


    if xyz.endswith('.jpg') or xyz.endswith('.gif') or xyz.endswith('.png'):
        url1 = xyz
        response = http.request('GET', url1)
        with open(z, 'wb') as f:
            f.write(response.data)
'''















