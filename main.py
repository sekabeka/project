import schedule

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings


from result import MySpider



tmp = {
    'LOG_FILE' : 'log.log',
    'LOG_FILE_APPEND' : False,
    'REQUEST_FINGERPRINTER_IMPLEMENTATION' : "2.7",
    "FEEDS" : {
        "auchan.jsonl" : {
            "format" : "jsonlines",
            "encoding" : "utf-8",
            "overwrite" : True
        }
    }
}
settings = Settings()
settings.setdict(tmp)

# settings.set(
#     "LOG_FILE", 'log.log'
# )
# settings.set(
#     'REQUEST_FINGERPRINTER_IMPLEMENTATION', "2.7"
# )
process = CrawlerProcess(settings)
process.crawl(MySpider)
process.start()