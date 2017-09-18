import csv
import requests
from lxml import html

page = requests.get('http://www.mah.gov.on.ca/page1591.aspx')
tree = html.fromstring(page.content)
muni_names = tree.xpath(
    '//*[@id="content"]/div/table/tbody[2]/tr/td[1]/p/a[contains(@href, "h")]/text()'
)
muni_urls = tree.xpath(
    '//*[@id="content"]/div/table/tbody[2]/tr/td[1]/p/a/@href'
)
muni_geo = None
muni_phone = None
print(len(muni_names))
print(len(muni_urls))
muni_data = list(zip(muni_names, muni_urls))
print(muni_data[-5:])
