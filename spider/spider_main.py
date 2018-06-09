import html_download
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlParser()

    def crawl(self, root_url):
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                self.outputer.output_html()
            except:
                print('failed')


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    spider = SpiderMain()
    spider.crawl(root_url)