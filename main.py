import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse


def pars() -> tuple[str, str]:
    """
    Parse command line arguments to get input and output filenames.

    Returns:
        tuple[str, str]: A tuple containing the input filename and output filename.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filename', type=str, help='path to input file')
    parser.add_argument('output_filename', type=str, help='path to save output file')
    args = parser.parse_args()
    return args.input_filename, args.output_filename


def load_image(image_path: str) -> np.ndarray:
    """
    Load an image from the specified path using OpenCV.

    Args:
        image_path: str: The path to the image file.

    Returns:
        np.ndarray: The loaded image.

    Raises:
        ValueError: If the image cannot be loaded (e.g., file not found).
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Picture is not available")
    return image


def resize_image(image: np.ndarray, new_size:tuple) -> np.ndarray:
    """
    Resize the input image to the specified new size.

    Args:
        image: np.ndarray: The input image.
        new_size: tuple[int, int]: The new size (width, height).

    Returns:
        np.ndarray: The resized image.
    """
    return cv2.resize(image, new_size)


def show_pic(image: np.ndarray) -> None:
    """
    Display the given image in a window using OpenCV.

    Args:
        image: np.ndarray: The image to display.
    """
    cv2.imshow('Image', image)
    cv2.waitKey(0)


def display_histogram(image: np.ndarray) -> None:
    """
    Calculate and display the histogram of the input image.

    Args:
        image: np.ndarray: The input image.
    """
    color = ('b', 'g', 'r')
    plt.figure(figsize=(10, 5))
    for i, col in enumerate(color):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.title('Histogram of changed image')
    plt.xlabel('Pixel intensity')
    plt.ylabel('Frequency')
    plt.legend(['Blue', 'Green', 'Red'])
    plt.grid()
    plt.show()


def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Save the modified image to the specified output path.

    Args:
        image: np.ndarray: The modified image.
        output_path: str: The path to save the image.
    """
    cv2.imwrite(output_path, image)
    print(f"Changed image saved as: {output_path}")


def print_size(image: np.ndarray) -> None:
    """
    Print the dimensions (width and height) of the input image.

    Args:
        image: np.ndarray: The input image.
    """
    print(f"Original size: {image.shape[1]}x{image.shape[0]} pixels")


def display_original_and_resized(original_image: np.ndarray, resized_image: np.ndarray) -> None:
    """
    Display the original image and the resized image side by side.

    Args:
        original_image: np.ndarray: The original image.
        resized_image: np.ndarray: The resized image.
    """
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.title('Resized Image')
    plt.axis('off')

    plt.show()

def main() -> None:
    """
    The main function of the script.
    """
    filename1, filename2 = pars()
    try:
        image = load_image(filename1)
    except ValueError as e:
        print(e)
        return

    print_size(image)
    show_pic(image)
    new_size = (900, 600)
    resized_image = resize_image(image, new_size)
    print_size(resized_image)
    display_histogram(resized_image)
    save_image(resized_image, filename2)

    display_original_and_resized(image, resized_image)


if __name__ == "__main__":
    main()
