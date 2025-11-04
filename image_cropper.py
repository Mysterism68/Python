from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--x1', type=int, help='The x position of the first corner.')
parser.add_argument('--y1', type=int, help='The y position of the first corner.')
parser.add_argument('--x2', type=int, help='The x position of the second corner.')
parser.add_argument('--y2', type=int, help='The y position of the second corner.')
parser.add_argument('--image_path', type=str, help='The path of the image to be cropped.')
parser.add_argument('--image_dest', type=str, help='The path of the cropped image.')
args = parser.parse_args()
image=Image.open(args.image_path)

imageBox = [args.x1, args.y1, args.x2, args.y2]
cropped = image.crop(imageBox)
cropped.save(args.image_dest)