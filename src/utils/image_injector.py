from PIL import Image

def image_injection(image_file_name):
    return Image.open(f"./src/images/{image_file_name}")