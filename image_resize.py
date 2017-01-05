import argparse
import os
import sys

from PIL import Image

def get_args():
    parser = argparse.ArgumentParser(description="Image resize script. Change height, width or scale")
    parser.add_argument("-ht", "--height", help="Height of new image in pixels", type=int)
    parser.add_argument("-wd", "--width", help="Width of new image in pixels", type=int)
    parser.add_argument("-s", "--scale", help="Scale ratio of processed image. Cannot be used with -ht or -wd parameter", type=float)
    parser.add_argument("-o", "--output",
                        help="Path to new image file. If not specified new file will be placed in the same folder as the original file")
    parser.add_argument("filepath", help="Path to original image file")
    args = parser.parse_args()

    if args.scale and (args.height or args.width):
        sys.exit('Cannot use --scale(-sc) option with --height(-ht) or/and --width(-wd)')

    if not args.scale and not (args.height or args.width):
        sys.exit('Reqired optional aguments: --scale(-sc) or --height(-ht) or/and --width(-wd)')

    return args


def is_proportions_equal(img_width, img_height, new_width, new_height):
    proportion = img_width / new_width - img_height / new_height
    return proportion == 0

def open_image(path_to_file):
    try:
        image = Image.open(path_to_file)
    except IOError:
        sys.exit('No such file or file provided is not an image file. Please specify correct path or filename.')
    return image


def save_image(input_image_path, output_image, output_image_path):
    img_width, img_height = output_image.size
    if output_image_path:
        try:
            full_path = os.path.join(os.getcwd(), output_image_path)
        except IOError:
            sys.exit('Wrong path for output file.')
        except KeyError:
            sys.exit('Wrong extension of output file. Please use image file format extension.')
    else:
        filename, extension = os.path.os.path.splitext(input_image_path)
        full_path = os.path.join(os.getcwd(), '{filename}__{width}x{height}{extension}'.format(
            filename=filename,
            width=img_width,
            height=img_height,
            extension=extension
        ))
    output_image.save(full_path)
    print('File saved as {}'.format(full_path))


def validate_new_image_size_or_exit(new_width, new_height):
    error_text = 'Result image is {width}x{height}, which is too {{size}}. Please use {{number}} numbers in parameters'.format(
        width=new_width, height=new_height)
    if new_width < 30 or new_height < 30:
        sys.exit(error_text.format(size="small", number='bigger'))
    elif new_width > 5000 or new_height > 5000:
        sys.exit(error_text.format(size="big", number='smaller'))


def resize_image(input_image, scale, height, width):
    img_width, img_height = input_image.size

    if scale:
        new_height = int(scale * img_height)
        new_width = int(scale * img_width)
    elif height and not width:
        new_height = height
        new_width = img_width * new_height / img_height
    elif width and not height:
        new_width = width
        new_height = img_height * new_width / img_width
    elif height and width:
        new_height = height
        new_width = width
        if not is_proportions_equal(img_width, img_height, new_width, new_height):
                print("Proportion of the output image are not equal to proportion original image.")

    validate_new_image_size_or_exit(new_width, new_height)
    new_image = input_image.resize((new_width, new_height), Image.ANTIALIAS)

    return new_image

if __name__ == '__main__':
    arguments = get_args()
    input_image = open_image(arguments.filepath)
    output_image = resize_image(input_image, arguments.scale, arguments.height, arguments.width)
    save_image(arguments.filepath, output_image, arguments.output)
