# exif_extracter

## Overview

The Image EXIF Data Extractor is a Python-based tool that allows you to extract Exchangeable Image File Format (EXIF) data from image files. EXIF data often contains valuable information about the image, such as camera settings, location, and more.

This tool utilizes the Pillow library to open and analyze images and extract their EXIF metadata.

## Features

- Extracts EXIF metadata from image files.
- Supports various image file formats (JPEG, PNG, etc.).
- Simple command-line interface (CLI) for quick extraction.
- Easily customizable and extensible for your specific needs.

## Installation

1. Clone this repository to your local machine or download the source code.

2. Install the required Python libraries using pip:

   ```shell
   pip install Pillow
   ```

## Usage

1. Open your terminal or command prompt.

2. Navigate to the directory where the tool is located.

3. Run the tool by providing the path to the image you want to analyze. For example:

   ```shell
   python extract_exif.py /exif-samples-master/jpg/gps/DSCN0021.jpg
   ```

4. The tool will display the extracted EXIF data, or it will indicate if no EXIF data is found.

## Sample Output

Here's an example of the output you can expect when running the tool:

```
EXIF Data:
GPSInfo: {1: 'N', 2: (43.0, 28.0, 1.49399999), 3: 'E', 4: (11.0, 53.0, 4.33799999), 5: b'\x00', 7: (14.0, 36.0, 47.23), 8: '06', 16: '\x00', 18: 'WGS-84   ', 29: '2008:10:23'}
ResolutionUnit: 2
ExifOffset: 268
ImageDescription:                                
Make: NIKON
Model: COOLPIX P6000
Software: Nikon Transfer 1.1 W
Orientation: 1
DateTime: 2008:11:01 21:15:08
YCbCrPositioning: 1
XResolution: 300.0
YResolution: 300.0
ExifVersion: 0220
```

## Contributing

Contributions to this project are welcome. If you have ideas for improvements or would like to add new features, feel free to submit a pull request.

## License

This tool is open-source and released under the MIT License.

## Author

- Akshit

If you have any questions or need assistance, please feel free to contact the author.

---

Enjoy extracting EXIF data from your images!

Replace `"/exif-samples-master/jpg/gps/DSCN0021.jpg"` with the actual path to your tool's Python script for extracting EXIF data.
