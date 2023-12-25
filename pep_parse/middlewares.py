from scrapy import signals
from scrapy.http import Request, Response
from scrapy.spiders import Spider
from scrapy.crawler import Crawler
from typing import Any, Generator, List, Optional

from pep_parse.items import PepParseItem


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseSpiderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(
            self,
            response: Response,
            spider: Spider
    ) -> Optional[None]:
        return None

    def process_spider_output(
            self,
            response: Response,
            result: List[PepParseItem],
            spider: Spider
    ) -> Generator[PepParseItem, None, None]:
        for i in result:
            yield i

    def process_spider_exception(
            self,
            response: Response,
            exception: Exception,
            spider: Spider
    ) -> Optional[None]:
        pass

    def process_start_requests(
            self,
            start_requests: List[Request],
            spider: Spider
    ) -> Generator[Request, None, None]:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(
            cls,
            crawler: Crawler
    ) -> 'PepParseDownloaderMiddleware':
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(
            self,
            request: Request,
            spider: Spider
    ) -> Optional[None]:
        return None

    def process_response(
            self,
            request: Request,
            response: Response,
            spider: Spider
    ) -> Response:
        return response

    def process_exception(
            self,
            request: Request,
            exception: Exception,
            spider: Spider
    ) -> Optional[None]:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
