from rich.console import Console
from itertools import permutations
import random, math, time, pyautogui, mouse
import argparse
BLOCK_CHAR = "██"
def char(text: str, color: tuple[int, int, int]) -> str:
  return f"[rgb({color[0]},{color[1]},{color[2]})]{text}"
parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, help='Width of the scan area.')
parser.add_argument('--height', type=int, help='Height of the scan area.')
args = parser.parse_args()
main_console = Console()
if args.width:
  MAP_WIDTH = args.width
else:
  MAP_WIDTH = 13
if args.height:
  MAP_HEIGHT = args.height
else:
  MAP_HEIGHT = 13
color_array = []
text = ""
tick = 0
def magnify():
  global text
  screen = pyautogui.screenshot()
  mX, mY = mouse.get_position()
  text_array = []
  for y in range(MAP_HEIGHT):
    line = ""
    for x in range(MAP_WIDTH):
      pixelX = math.floor(mX + (x - MAP_WIDTH / 2))
      pixelY = math.floor(mY + (y - MAP_HEIGHT / 2))
      if pyautogui.onScreen(pixelX, pixelY):
        line += (char(BLOCK_CHAR, screen.getpixel([pixelX, pixelY])))
      else:
        line += (char(BLOCK_CHAR, (10, 0, 20)))
    text_array.append(line)
  text = "\n".join(text_array)
with main_console.status("") as status:
  while True:
    magnify()
    status.update(f"\n{text}")
    time.sleep(0.016)
    tick += 1
