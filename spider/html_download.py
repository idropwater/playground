import urllib2


class HtmlDownload(object):

    def download(self, url):
        if url is None:
            return

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return

        return response.read()
