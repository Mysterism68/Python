#TODO: Create a tile atlas having the snake (head, straight body, corner body), button, apple, and rat (2 frames) tiles. 
import pygame as pyg
from global_funcs import functions as funcs
import objs
pyg.init()
display_res = pyg.display.get_desktop_sizes()[0]
trans_color = (80, 80, 80)
screen = pyg.display.set_mode(display_res, pyg.RESIZABLE | pyg.NOFRAME)
hwnd = pyg.display.get_wm_info()["window"]
scene = [objs.snake(pyg.Rect(display_res[0] / 2 - 32, display_res[1] / 2 - 32, 64, 64), pyg.Color(75, 200, 75), screen)]
funcs.trans_win(pyg.display.get_wm_info()["window"], trans_color)
funcs.move_window(hwnd, top = True)
def draw():
  screen.fill(trans_color)
  for obj in scene:
    obj.draw()
  pyg.display.flip()
while True:
  pyg.time.Clock().tick(60)
  objs.keys = pyg.key.get_pressed()
  if pyg.event.get(pyg.QUIT) or objs.keys[pyg.K_ESCAPE]: break
  for obj in scene:
    obj.main()
  draw()
pyg.quit()