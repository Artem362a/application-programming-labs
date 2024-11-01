import os
from icrawler.builtin import BingImageCrawler

def download_images(keyword: str, num_images:int, img_dir:str):
    """
       Download images with keyword using BingImageCrawler
       :param keyword: Keyword to search images
       :param img_dir: Directory to save images
       :param num_images: Number of images
       :return: None
       """
    if not (os.path.exists(img_dir)):
        os.mkdir(img_dir)
    for filename in os.listdir(img_dir):
        os.remove(os.path.join(img_dir, filename))
    bing_crawler = BingImageCrawler(feeder_threads=1,
                                    parser_threads=2,
                                    downloader_threads=4,
                                    storage={'root_dir': img_dir})
    bing_crawler.crawl(keyword=keyword, max_num=num_images)