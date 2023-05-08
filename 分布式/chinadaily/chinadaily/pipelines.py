import csv

class ChinadailyPipeline:
    def __init__(self):
        self.f = open('data.csv', 'w', encoding='utf-8', newline='')
        self.write = csv.DictWriter(self.f,  fieldnames=['标题', '简介', 'url地址'])
        self.write.writeheader()

    def process_item(self, item, spider):
        print(item)
        self.write.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close()
