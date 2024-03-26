import scrapy
from Crawl_Scrapy.items import CrawlScrapyItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://itcast.cn"]

    
    
    def parse(self, response):
        # filename = "teacher.html"
        # open(filename,'w').write(response.body)
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            item = CrawlScrapyItem()

            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            item['name'] = name[0]
            item['title'] = name[0]
            item['info'] = name[0]

            
            items.append(item)
        print(items)
        return items