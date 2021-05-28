from celery import Celery
from celery import shared_task, task
import requests
import json
from api.models import Articles,Authors
from celery.schedules import crontab


categores = ['AI','SoftwareEngineering','Algorithm Analysis and Problem Complexity','Data Mining and Knowledge Discovery','Database Management',

'Information Storage and Retrieval','Management of Computing and Information Systems','Programming Languages, Compilers, Interpreters']

@shared_task
def get_data():
    for category in categores:
        num = 1
        while num < 102:
            print(num)
            headers = {
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
                'Cookie': 'idp_marker=a2e879ba-c050-497f-b8dd-7e2e7616ca69'
            }
            try:
                req = requests.get(
                    f'http://api.springer.com/meta/v2/json?api_key=9e4f8b01ac9095a31fd621b759df65f4&q=subject:"{category}"&s={num}&p=100', timeout=10, headers=headers)
                print(req.status_code)
            except:
                num += 100
                continue
            if req.status_code != 200:
                num += 100
            else:
                myjson = req.json()
                recieve_data(myjson,category)
                num += 100


def recieve_data(data,category):
    data = data["records"]
    for record_dict in data:
        contentType = record_dict['contentType']
        title = record_dict['title']
        publicationName = record_dict['publicationName']
        doi = record_dict['doi']
        publicationDate = record_dict['publicationDate']
        abstract = record_dict['abstract']
        url = record_dict['url']
        try:
            d = dict((i['format'], i['value']) for i in url)
            html = d.get('html', 'html')
            pdf = d.get('pdf', 'pdf')
            doi_url = d.get('', 'doi')
        except:
            pass
        
        creators = record_dict['creators']
        if Articles.objects.filter(doi=doi).exists():
            print('path')
            pass
        else:
            category = category.replace(',','')
            article = Articles.objects.create(contenttype=contentType,title=title,url_page=html,url_pdf=pdf,url_doi=doi_url,publicationname=publicationName,doi=doi,publicationdate=publicationDate,abstract=abstract,category=category)
            article.save()
            for i in creators :
                author_value = i.get('creator')
                author_value = author_value.replace(',', '').replace('.','').replace("'","")
                if Authors.objects.filter(author_name=author_value).exists():
                    get_author = Authors.objects.get(author_name=author_value)
                    article.author.add(get_author)
                    article.save()
                    print('done old')
                else:
                    author1 = Authors.objects.create(author_name=author_value)
                    author1.save()
                    get_author = Authors.objects.get(author_name=author_value)
                    article.author.add(get_author)
                    article.save()   
                    print('done')



