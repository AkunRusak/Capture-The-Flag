from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    image = Image.open(image_path)
    exifdata = image.getexif()

    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        print(f"{tag:25}: {data}")

# Contoh penggunaan
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python metadata-finder.py <image-file>")
    else:
        extract_metadata(sys.argv[1])