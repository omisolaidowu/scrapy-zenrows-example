from scrapy import Request
import scrapy
from scrapy_zenrows import ZenRowsRequest


class BlockopenSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = [
        "www.scrapingcourse.com",
        "httpbin.io",
        "httpbin.org",
    ]
    # start_urls = ["https://www.scrapingcourse.com/cloudflare-challenge"]

    start_urls = ["https://httpbin.io/headers"]

    def start_requests(self):
        # Use ZenRowsRequest for customization
        for url in self.start_urls:
            yield ZenRowsRequest(
                url=url,
                params={
                    "js_render": "true",
                    "custom_headers": "true",
                },
                headers={
                    "Referer": "https://www.google.com/",
                    # "Zr-Cookies": "test=this",
                },
                cookies={
                    "currency": "USD",
                    "country": "UY",
                },
                # meta={"cookiejar": 1},  # Meta field for cookie handling
                callback=self.parse,
            )

    def parse(self, response):
        # Debugging to check if cookies are set correctly
        print(response.text)

        print("Request Headers:", response.request.headers)
        print("Request Cookies:", response.request.cookies)
        print("Request meta:", response.request.meta)
        print("Response Cookies:", response.headers.getlist("Set-Cookie"))

        # python setup.py sdist bdist_wheel
        # twine upload --repository testpypi dist/*
