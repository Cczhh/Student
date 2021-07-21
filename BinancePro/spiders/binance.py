import scrapy


class BinanceSpider(scrapy.Spider):
    name = 'binance'
    # allowed_domains = ['www.binance.com/zh-CN/support/announcement/aec178a59f824162ab77a17a5d0838a5']
    start_urls = ['http://www.binance.com/zh-CN/support/announcement/aec178a59f824162ab77a17a5d0838a5/']

    def parse(self, response):
        resp = response.xpath('//article[@class="css-1ii68zy"]')              # 获得存放公告的路径
        greet = resp.xpath('//div[@class="css-3fpgoh"]/strong/text()').get()  # 提取开头称呼
        print(greet)

        # 正文提取和输出
        content = resp.xpath('//div[@class="css-mm1dbi"]/text()').getall()
        incontent = resp.xpath('//div[@class="css-mm1dbi"]/a/text()').get()
        print(content[0] + incontent + content[1])
        print(content[2])

        # 结束语和落款的提取与输出
        endwords = resp.xpath('//div[@class="css-3fpgoh"]/text()').getall()
        for x in range(0, 3):
            print(endwords[x])
