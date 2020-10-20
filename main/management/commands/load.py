import requests
from bs4 import BeautifulSoup
from main.models import Numbering
from django.core.management.base import BaseCommand


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('tr')

    for tr in trs:
        try:
            tds = tr.find_all('td')
            print(tds)

            abs_def = tds[0].text.replace('\t', '')
            fr = tds[1].text.replace('\t', '')
            to = tds[2].text.replace('\t', '')
            capacity = tds[3].text.replace('\t', '')
            operator = tds[4].text.replace('\t', '')
            region = tds[5].text.replace('\t', '')

            n = Numbering(kod=abs_def, fr=fr, to=to, capacity=capacity, operator=operator, region=region)
            n.save()
        except:
            pass

    print(len(trs))


def get_html(url):
    r = requests.get(url, verify=False)
    r.encoding = 'utf-8'
    if r.ok:  # 200  # 403  # 404
        return r.text
    print(r.status_code)


class Command(BaseCommand):
    help = 'Loading numberings from rossvyaz'

    def handle(self, *args, **options):
        Numbering.objects.all().delete()

        url = 'https://rossvyaz.gov.ru/data/DEF-9xx.html'
        get_page_data(get_html(url))
