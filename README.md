# Image Resizer

The script allows to scale, change width or/and height of the image.

## Usage

    pip install -r requirements.txt
    python3 image_resize.py -ht -wd -s -o filepath

Where:

filepath - Path to original image file

-ht (--height) - Height of new image in pixels.<br>
-wd (--width) - Width of new image in pixels.<br>
Options -ht or -wd can be used together or separately. If one of the option is not specified image will be resized proportionally.

-s (--scale) - Scale ratio of new image.<br>
Cannot be used with -ht or -wd parameter.

-o (--output) - Path to new image file.<br>
If the output file is not specified the new file will be placed in the same folder as the original file with new filesize information in filename (ex. filename_100x200.jpg).

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)