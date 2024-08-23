import os
import io
import base64
from typing import List

from PIL import Image


def load_images_from_folder(folder: str):
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif')):
            img_path = os.path.join(folder, filename)
            images.append(img_path)

    return images


def image_to_base64(image_path: str):
    try:
        if not os.path.exists(image_path):
            return "Error: File does not exist."

        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    except Exception as e:
        return f"Error: {str(e)}"


def batch_image_to_base64(image_paths: List[str]):
    encoded_images = []
    for image_path in image_paths:
        encoded_image = image_to_base64(image_path)
        encoded_images.append(encoded_image)
    return encoded_images


if __name__ == "__main__":
    image = "../model/image_dataset/avatar.jpg"
    encoded_string = image_to_base64(image)
    print(encoded_string)
