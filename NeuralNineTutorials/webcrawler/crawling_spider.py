# this would be in the "spiders/" dir
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# may want to use proxy servers to keep your ip from being blocked
class CrawlingSpider(CrawlSpider):
    """later will run in the project:
    *scrapy crawl mycrawler*
    to start prog and specify crawler"""

    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    PROXY_SERVER = "127.0.0.1"
    """ then in settings.py, got to the commented DOWNLOADER_MIDDLEWARES section and uncomment it
    then add
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
    then in middlewares.py go to the class
    somthingDownloaderMiddleware:

    * add to this class under process_request *
    request.meta['proxy'] = "127.0.0.1"
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),  # this should only give categories not spec books
        # /\ this is the basic running
        # \/ Adding more Rules
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        """ getting title, price, and availability"""
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("\n", "").replace(" ", ""),
        }