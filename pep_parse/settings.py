from pathlib import Path

CSV_FORMAT = 'csv'
PEPS_PYTHON_ORG_DOMAIN = 'peps.python.org'

BASE_DIR = Path(__file__).resolve().parent.parent

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'results/pep_%(time)s.{CSV_FORMAT}': {
        'format': CSV_FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}
