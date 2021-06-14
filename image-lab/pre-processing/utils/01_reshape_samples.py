from pathlib import Path
import cv2
import numpy as np



def find_smallest_sizes(all_image_paths : list) -> list:
    """
    Method that reads all images and their corresponding shapes
    to find the smallest size. Prints the sizes in console, returns list of images
    """
    shapes = []
    images = []
    for img_path in all_image_paths:
        img = cv2.imread(str(img_path), 0)
        shapes.append(img.shape)
        images.append((img_path, img))

    min_x = 10000
    min_y = 10000
    for shape in shapes:
        if shape[0] <= min_x:
            min_x = shape[0]
        if shape[1] <= min_y:
            min_y = shape[1]
    print(min_x, min_y)
    print(shapes)

    return images


def resize_images(images: list, target_shape = (410,340)):
    """
    Resizes and saves the images in the list images
    """
    for path, image in images:
        res = cv2.resize(image, dsize=target_shape, interpolation=cv2.INTER_CUBIC)
        img2 = cv2.merge((res,res,res))
        cv2.imwrite(str(path), img2)
        print(img2.shape)


if __name__ == "__main__":
    # Relative path to dataset
    path_to_dataset = Path("../../Covid19-dataset")
    # Finds all images
    all_image_paths = list(path_to_dataset.glob('*/*/*.jpeg')) + list(path_to_dataset.glob('*/*/*.jpg')) + list(path_to_dataset.glob('*/*/*.png'))
    print(len(all_image_paths))
    # Finds sizes and then reshapes and overwrites old images
    images = find_smallest_sizes(all_image_paths)
    resize_images(images)