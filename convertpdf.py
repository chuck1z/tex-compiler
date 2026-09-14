from pdf2image import convert_from_path
import argparse
parser = argparse.ArgumentParser(description='PDF file source')
parser.add_argument('filename', help='PDF file to convert')
parser.add_argument('--verbose', action='store_true',
                    help='print verbose output')

args = parser.parse_args()

print(args.filename)
images = convert_from_path(args.filename)

for i, image in enumerate(images):
    image.save(f'page_{i+1}.png', 'PNG')
