from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def index_view(request):
    # guitar site of choice: http://www.guitartabs.cc/
    song_name = request.GET.get('song')
    search_url = "http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(song_name)
    results = requests.get(search_url).text
    search_soup = BeautifulSoup(results, 'html.parser')
    song_links = [link.attrs['href'] for link in search_soup.find_all('a', class_='ryzh22')]
    print(song_links)
    return render(request, 'index.html', {})
