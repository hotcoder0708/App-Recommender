BOT_NAME = 'appstore'

SPIDER_MODULES = ['appstore.spiders']
NEWSPIDER_MODULE = 'appstore.spiders'
ITEM_PIPLINES = {
	'appstore.pipelines.AppstorePipeline': 300,
}
DOWNLOAD_DELAY = 5

