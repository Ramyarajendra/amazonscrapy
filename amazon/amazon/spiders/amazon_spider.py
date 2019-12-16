# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem
import csv
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/b/ref=bhp_toplists?ie=UTF8&node=11913537011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=NY7MZKYKM8TRAT07YDYJ&pf_rd_r=NY7MZKYKM8TRAT07YDYJ&pf_rd_t=101&pf_rd_p=5139dc51-e8c2-42c6-a524-4ac0ec2f6566&pf_rd_p=5139dc51-e8c2-42c6-a524-4ac0ec2f6566&pf_rd_i=283155']

    def parse(self, response):
        items =AmazonItem()
        product_name = response.css('.a-link-normal .a-size-base::text').extract()
        product_author = response.css('.acs_product-metadata__contributors::text').extract()
        product_price= response.css('.acs_product-price__buying::text').extract()
        product_image=response.css('.aok-align-center::attr(src)').extract()
        items['product_name']=product_name
        items['product_author']=product_author
        items['product_price']=product_price
        items['product_image']=product_image
        yield items
        print(type(product_name))
        for i in product_name:
            print('proname',i)
        print(type(items['product_name']))
        rows=zip(product_name,product_author,product_price,product_image)
        with open('result.csv', mode='w+') as res_file:
            writer = csv.writer(res_file)
            writer.writerow(['Name','Author','Price','Image'])
            for row in rows:
                writer.writerow(row)
        pass
