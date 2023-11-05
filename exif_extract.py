pip install Pillow
from PIL import Image
from PIL.ExifTags import TAGS

def extract_exif_data(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                exif_info = {}
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    if isinstance(value, bytes):
                        # If the value is in bytes, decode it to a human-readable string
                        value = value.decode('utf-8', errors='replace')
                    exif_info[tag_name] = value
                return exif_info
            else:
                return "No EXIF data found in the image."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    image_path = "/exif-samples-master/jpg/gps/DSCN0021.jpg"  # Replace with the path to your image
    exif_data = extract_exif_data(image_path)
    if isinstance(exif_data, str):
        print(exif_data)
    else:
        print("EXIF Data:")
        for tag, value in exif_data.items():
            print(f"{tag}: {value}")

