#The coordinates are going to be scaled by scalepx
from global_funcs import functions, Vector2
import pygame as pyg
import random as r
import math as m
pyg.init()
display_size = [800, 600]
screen = pyg.display.set_mode(display_size, pyg.RESIZABLE)
TPS = 0
keys = {}
lines = []
points = []
mouse: Vector2 = Vector2(0, 0)
cam_offset = Vector2(0, 0)
class line():
  def __init__(self, pointA: Vector2, pointB: Vector2):
    self.start = pointA
    self.end = pointB
    random_num = str(r.randint(0, 999999))
    self.__id = " " * (6 - len(random_num)) + random_num
    pass
  def main(self):
    for obj in lines:
      if self.__id != obj._line__id:
        points.append(functions.get_line_intersect(self.start, self.end, obj.start, obj.end))
def vec_oper(vector_A: Vector2, vector_B: Vector2, oper: int):
  oper = min(max(oper, 0), 3)
  if oper == 0:
    return Vector2(vector_A.x * vector_B.x, vector_A.y * vector_B.y)
  elif oper == 1:
    return Vector2(vector_A.x / vector_B.x, vector_A.y / vector_B.y)
  elif oper == 2:
    return Vector2(vector_A.x + vector_B.x, vector_A.y + vector_B.y)
  elif oper == 3:
    return Vector2(vector_A.x - vector_B.x, vector_Ay - vector_B.y)
scale = 40
def draw_grid():
  screen.fill([255, 255, 255])
  for x in range(m.ceil(display_size[0] / scale)):
    screen_w = m.ceil(display_size[0] / (scale * 2))
    draw_x = display_size[0] / 2 - (screen_w - x) * scale - cam_offset.x % scale
    pyg.draw.line(screen, [175, 175, 175], [draw_x, 0], [draw_x, display_size[1]], 3)
    if x == m.ceil(display_size[0] / scale):
      for i in range(3):
        draw_x = display_size[0] / 2 - (m.ceil(display_size[0] / scale) + 1 + i) * scale - cam_offset.x % scale
        pyg.draw.line(screen, [175, 175, 175], [draw_x, 0], [draw_x, display_size[1]], 3)

  for y in range(m.ceil(display_size[1] / scale)):
    screen_h = m.ceil(display_size[1] / (scale * 2))
    draw_y = display_size[1] / 2 - (screen_h - y) * scale - cam_offset.y % scale
    pyg.draw.line(screen, [175, 175, 175], [0, draw_y], [display_size[0], draw_y], 3)
    if y == m.ceil(display_size[1] / scale):
      for i in range(3):
        draw_y = display_size[1] / 2 - (m.ceil(display_size[1] / scale) + 1 + i) * scale - cam_offset.y % scale
        pyg.draw.line(screen, [175, 175, 175], [0, draw_y], [display_size[0], draw_y], (3/40) * scale)
  pyg.draw.line(screen, [100, 100, 100], [display_size[0] / 2 - cam_offset.x,
    0], [display_size[0] / 2 - cam_offset.x, display_size[1]], 8)
  pyg.draw.line(screen, [100, 100, 100], [0, display_size[1] / 2 - cam_offset.y],
    [display_size[0], display_size[1] / 2 - cam_offset.y], 8)
speed = 4.8
while True:
  keys = pyg.key.get_pressed()
  TPS = pyg.time.Clock().tick(60)
  if pyg.event.get(pyg.QUIT) or keys[pyg.K_ESCAPE]: break
  if keys[pyg.K_DOWN] or keys[pyg.K_s]:
    cam_offset.y += speed
  if keys[pyg.K_UP] or keys[pyg.K_w]:
    cam_offset.y -= speed
  if keys[pyg.K_RIGHT] or keys[pyg.K_d]:
    cam_offset.x += speed
  if keys[pyg.K_LEFT] or keys[pyg.K_a]:
    cam_offset.x -= speed
  if keys[pyg.K_e]:
    scale += 1.2
  if keys[pyg.K_q]:
    scale -= 1.2
  scale = max(scale, 12)
  if keys[pyg.K_SPACE]:
    cam_offset = Vector2(0, 0)
  display_size = pyg.display.get_window_size()
  mouse.x, mouse.y = pyg.mouse.get_pos()
  print(f"{mouse.x}, {mouse.y}{"  " if mouse.x <= 99 or mouse.y <= 99 else ""}", end="\r")
  draw_grid()
  pyg.display.flip()
pyg.quit()