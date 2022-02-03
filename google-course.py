# Copy right 
# Change list


from lxml import html
import requests
from dotenv import load_dotenv
import os 

load_dotenv()  # take environment variables from .env.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--string", type=str, required=True)

args = parser.parse_args()    
print (args.string)

currentcourseurl = args.string
#currentcourseurl = 'https://partner.cloudskillsboost.google/course_sessions/607180/video/115093'

baseurl = 'https://partner.cloudskillsboost.google'

import requests
nexticon = [1]

while  len(nexticon)>0:

    headers = {
        'authority': 'partner.cloudskillsboost.google',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'upgrade-insecure-requests': '1',
        'origin': 'https://partner.cloudskillsboost.google',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://partner.cloudskillsboost.google/course_sessions/747946/video/116188',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': os.environ.get("COOKIE"),
    }

    response = requests.get(currentcourseurl, headers=headers)


    tree = html.fromstring(response.content)
    nexticon = tree.xpath('//ql-icon-button[@icon="arrow_forward"]/@href')
    if len(nexticon):
        print(nexticon[0])
        nextcourseurl = nexticon[0]
        currentcourseurl = baseurl + nextcourseurl

    completebutton = tree.xpath('//ql-button[@method="post"]/@href')
    if len(completebutton):
        print(completebutton[0])

        currentcomplete = baseurl + completebutton[0]

        headers = {
            'authority': 'partner.cloudskillsboost.google',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'upgrade-insecure-requests': '1',
            'origin': 'https://partner.cloudskillsboost.google',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://partner.cloudskillsboost.google/course_sessions/747946/video/116188',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': os.environ.get("COOKIE"),
        }

        data = {
        '_method': 'post',
        'authenticity_token': os.environ.get("TOKEN")
        }

        response = requests.post(currentcomplete, headers=headers, data=data)
