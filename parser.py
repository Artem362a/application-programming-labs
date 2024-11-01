import argparse

def create_parser():
    """
     Parsing arguments from cmd
     """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="keyword to search images")
    parser.add_argument("number", type=int, help="number of images")
    parser.add_argument("img_dir", type=str, help="path to the folder,where images will be downloaded")
    parser.add_argument("annotation_file", type=str, help="path to the annotation file")

    args = parser.parse_args()
    return args.keyword, args.number, args.img_dir, args.annotation_file