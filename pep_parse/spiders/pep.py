import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        main_table = response.xpath('//section[@id="numerical-index"]')
        pep_table = main_table.xpath('.//tbody')
        rows = pep_table.xpath('.//tr')
        pep_links = rows.xpath('.//td[2]/a/@href').getall()

        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        main_pep_section = response.xpath('//section[@id="pep-content"]')
        title = main_pep_section.xpath('.//h1//text()').get().split('–')
        status_tag = (main_pep_section
                      .xpath('.//dt[contains(text(), "Status")]'))

        data = {
            'number': title[0].split('PEP ')[1].strip(),
            'name': title[1].strip(),
            'status':
                status_tag.xpath('following-sibling::*[1]//text()').get(),
        }
        yield PepParseItem(data)
