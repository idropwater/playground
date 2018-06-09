class HtmlParser(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write('<html>')

        for data in self.datas:
            fout.write(data['title'])

        fout.write('</html>')
