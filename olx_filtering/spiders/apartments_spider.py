import scrapy


class ApartmentsSpider(scrapy.Spider):
    name = "apartments"

    def start_requests(self):
        urls = [
            'https://www.olx.pl/nieruchomosci/mieszkania/warszawa/?search%5Bdistrict_id%5D=381&page=1',
        ]
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'}
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{self.name}-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
