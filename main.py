from parser import create_parser
from downloader import download_images
from iteratorr import Iterator
from annot import create_annotation

def main():
   keyword, number, img_dir, annotation_file = create_parser()
   try:
      download_images(keyword, number, img_dir)
      create_annotation(img_dir, annotation_file)
      iterator = Iterator(annotation_file)
      for i in iterator:
         print(i)
   except Exception as e:
      print(f"Something went wrong: {e} ")

if __name__ == '__main__':
   main()