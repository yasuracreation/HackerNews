import requests
from bs4 import BeautifulSoup
import pprint

hn = []


def scrip_pages(page_no):

    url = 'https://news.ycombinator.com/news?p=' + str(page_no)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select('.storylink')
    subtitle = soup.select('.subtext')
    createCustom_hn(links, subtitle)
    # news.sort(key=lambda x: x['votes'], reverse=True)


def sort_by_key(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def createCustom_hn(links, subtitle):
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtitle[idx].select('.score')

        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title': title, 'link': href, 'votes': point})
    return


def main():
    for p in range(20):
        scrip_pages(p)
    pprint.pprint(sort_by_key(hn))


main()
