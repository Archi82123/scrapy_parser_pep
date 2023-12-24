import csv
from datetime import datetime
from collections import defaultdict

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.filepath = BASE_DIR / 'results'
        self.filepath.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.status_count['Total'] = sum(self.status_count.values())

        current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{current_datetime}.csv'

        with open(self.filepath / filename, 'w', newline='') as csvfile:
            fieldnames = ['Статус', 'Количество']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writeheader()
            for status, value in self.status_count.items():
                csv_writer.writerow({'Статус': status, 'Количество': value})
