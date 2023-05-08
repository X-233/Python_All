import scrapy


class ChinadaSpider(scrapy.Spider):
    name = "chinada"
    allowed_domains = ["chinadaily.com"]
    start_urls = ["http://language.chinadaily.com.cn/thelatest"]

    def parse(self, response):
        select = response.css('div.gy_box')
        for i in select:
            title = i.css('p.gy_box_txt2>a::text').get().strip()
            title1 = i.css('p.gy_box_txt3>a::text').get().strip()
            image_url = i.css('img::attr(src)').get()
            data = {
                '标题': title,
                '简介': title1,
                'url地址': 'http:' + image_url,
            }
            yield data
