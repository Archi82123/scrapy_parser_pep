import scrapy
from typing import Generator

from pep_parse.items import PepParseItem
from pep_parse.settings import PEPS_PYTHON_ORG_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEPS_PYTHON_ORG_DOMAIN]
    start_urls = [f'https://{PEPS_PYTHON_ORG_DOMAIN}/']

    def parse(self, response: scrapy.http.Response) -> Generator[PepParseItem, None, None]:
        main_table = response.xpath('//section[@id="numerical-index"]')
        pep_table = main_table.xpath('.//tbody')
        rows = pep_table.xpath('.//tr')
        pep_links = rows.xpath('.//td[2]/a/@href').getall()

        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response: scrapy.http.Response) -> Generator[PepParseItem, None, None]:
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
