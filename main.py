import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from typing import Tuple
import argparse

def get_image_dimensions(path: str) -> Tuple[int, int, int]:
    """
    Get the dimensions of an image from the given path.

    Args:
        path (str): Path to the image.

    Returns:
        Tuple[int, int, int]: A tuple containing the width, height, and depth of the image.
    """
    with Image.open(path) as img:
        width, height = img.size
        depth = len(img.getbands())
    return width, height, depth

def filter_images_by_size(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Filter the DataFrame based on the given width and height values.

    Args:
        df (pd.DataFrame): The original DataFrame.
        max_width (int): The maximum width.
        max_height (int): The maximum height.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    return df[(df['width'] <= max_width) & (df['height'] <= max_height)]

def plot_area_histogram(df: pd.DataFrame) -> None:
    """
    Plot a histogram of the area distribution.

    Args:
        df (pd.DataFrame): DataFrame containing size information.
    """
    plt.hist(df['area'], bins=20, edgecolor='black')
    plt.xlabel('Image Area')
    plt.ylabel('Frequency')
    plt.title('Distribution of Image Areas')
    plt.show()

def main(csv_path: str, max_width: int, max_height: int) -> None:
    """
    Main function to process the CSV file and plot the histogram.

    Args:
        csv_path (str): Path to the CSV file.
        max_width (int): The maximum width.
        max_height (int): The maximum height.
    """
    df = pd.read_csv(csv_path)
    df.columns = ['abs_path', 'rel_path']

    print("First few rows of the DataFrame:")
    print(df.head())
    print()

    df[['width', 'height', 'depth']] = df['abs_path'].apply(lambda x: pd.Series(get_image_dimensions(x)))

    print("First few rows of the DataFrame after adding image dimension columns:")
    print(df.head())
    print()

    statistics = df[['width', 'height', 'depth']].describe()
    print("Statistical information:")
    print(statistics)
    print()

    df_filtered = filter_images_by_size(df, max_width, max_height).copy()
    df_filtered['area'] = df_filtered['width'] * df_filtered['height']
    df_sorted = df_filtered.sort_values(by='area')

    print("First few rows of the sorted DataFrame:")
    print(df_sorted.head())
    print()

    plot_area_histogram(df_sorted)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=str, help="Path to the CSV file.")
    parser.add_argument("max_width", type=int, help="Maximum width.")
    parser.add_argument("max_height", type=int, help="Maximum height.")

    args = parser.parse_args()

    main(args.csv_path, args.max_width, args.max_height)
