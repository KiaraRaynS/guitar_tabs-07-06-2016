from django.shortcuts import render
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def index_view(request):
    # guitar site of choice: http://www.guitartabs.cc/
    song_name = request.GET.get('song')
    search_url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song_name)
    results = requests.get(search_url).text
    search_soup = BeautifulSoup(results, 'html.parser')
    song_links = [urlparse(link.attrs['href']).path for link in search_soup.find_all('a', class_='ryzh22')]
    context = {
            'songlinks': song_links,
            }
    return render(request, 'index.html', context)


def tabs_view(request, url):
    tabs_url = 'http://www.guitartabs.cc/' + url
    results = requests.get(tabs_url).text
    tab_soup = BeautifulSoup(results, 'html.parser')
    tabs = str(tab_soup.find(class_='tabcont'))
    context = {
            'tabs': tabs,
            }
    return render(request, 'tabs.html', context)
