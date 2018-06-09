import re

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='urf-8')

        new_urls = self.get_new_urls(page_url, soup)

        new_data = self.get_new_data(page_url, soup)
        print(new_data)

        return  new_urls, new_data

    def get_new_urls(self, page_url, soup):
        urls = []
        links = soup.find_all('a')

        for link in links:
            urls.append(link)

        return urls

    def get_new_data(self, page_url, soup):
        res_data = {}

        try:
            title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
            res_data['title'] = title_node.get_text()

            summary_node = soup.find('div', class_="lemma-summary")
            res_data['summary'] = summary_node.get_text()

        except:
            print('parse failed')

        return res_data
