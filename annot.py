import csv
import os

def create_annotation(img_dir: str, csv_path: str):
    """
       Making annotation which contains the absolute and relative path to each image
       :param csv_path: Path to file to save annotation
       :param img_dir: Directory with images
       :return: None
       """
    with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation:
        writer = csv.writer(annotation)
        headers = ['rel_path ', ' abs_path']
        writer.writerow(headers)
        list_img = os.listdir(img_dir)

        for img in list_img:
            if img.endswith(("jpg", "jpeg", "png")):
                rel_path = os.path.relpath(os.path.join(img_dir, img), start=img_dir)
                abs_path = os.path.abspath(os.path.join(img_dir, img))
                writer.writerow([rel_path, abs_path])
            else:
                raise ValueError("This is not an image file")