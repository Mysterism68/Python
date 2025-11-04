import pygame as pyg
import math
from global_funcs import functions as funcs
pyg.init()
keys = {}
tick = 0
def debug_print(text, surface):
  funcs.text_render(text, (400, 16), 32, (255, 255, 255), 0, surface, pyg)
def replace_color(image: pyg.Surface, old_color: pyg.Color, new_color: pyg.Color):
  new_image = image
  for y in range(image.get_height()):
    for x in range(image.get_width()):
      if image.get_at((x, y)) == old_color:
        new_image.set_at((x, y), new_color)
  return new_image
atlas_image = pyg.image.load("main_tile_atlas.png")
def get_tile(x: float, y: float):
  return atlas_image.subsurface(pyg.Rect((x * 64, y * 64), (64, 64)))
atlas = {
  "snake": {
    "head": get_tile(0, 0),
    "line_body": get_tile(1, 0),
    "corn_body": get_tile(2, 0),
    "line_body_end": get_tile(0, 1),
    "corn_body_end":  get_tile(1, 1),
  },
  "plate": {
    "top_left": get_tile(0, 2),
    "top_center": get_tile(1, 2),
    "top_right": get_tile(2, 2),
    "middle_left": get_tile(0, 3),
    "middle_center": get_tile(2, 3),
    "middle_right": get_tile(2, 3),
    "middle_left": get_tile(0, 4),
    "middle_center": get_tile(2, 4),
    "middle_right": get_tile(2, 4),
  },
  "food": {
    "apple": get_tile(1, 2),
    "egg": get_tile(0, 5),
    "fried_egg": get_tile(1, 5),
  },
  "roller": get_tile(2, 5)
}
class snake():
  def __init__(self, rect: pyg.Rect, color: pyg.Color, surf: pyg.Surface):
    self.rect = rect
    self.acc = rect.w
    self.rot = 0
    self.tick = 0
    self.color = color
    self.surf = surf
    self.tail_poses = []
    self.past_poses = []
    self.tail_length = 10
    self.keys_in_update = []
    self.life = True
    pass
  def snakify(self, surf, rot):
    return replace_color(pyg.transform.scale(pyg.transform.rotate(surf,
      rot / (math.pi / 180)), self.rect.size),pyg.Color(10, 10, 10), self.color)
  def draw(self):
    self.surf.blit(self.snakify(atlas["snake"]["head"], -self.rot), self.rect)
    for idx in range(len(self.tail_poses)):
      tail_seg = self.tail_poses[idx]
      position = (tail_seg["pos"][0] - 32, tail_seg["pos"][1] - 32)
      tail_seg["peice"] = "line_body"
      next_seg 
      if (idx == len(self.tail_poses) - 1):
        tail_seg["peice"] = "line_body_end"
      self.surf.blit(self.snakify(atlas["snake"][tail_seg["peice"]], tail_seg["rot"]), position)
  def main(self):
    self.tick += 1
    if not self.life:
      return
    if self.tick >= 10:
      next_key = None
      last_rot = self.rot
      for tail in self.tail_poses:
        if self.rect.center == tail["pos"]:
          self.life = False
          break
          return
      for idx in range(len(self.keys_in_update)):
        key = self.keys_in_update[idx]
        print(f"\r{self.keys_in_update}, w:{pyg.K_w}, s:{pyg.K_s}, a:{pyg.K_a}, d:{pyg.K_d},")
        if key == pyg.K_w | pyg.K_s and self.keys_in_update[idx - 1] == pyg.K_a | pyg.K_d:
          next_key = key
          break
        if self.keys_in_update[idx - 1] == pyg.K_w | pyg.K_s and key == pyg.K_a | pyg.K_d:
          next_key = key
          break
        if key == pyg.K_w and self.rot != math.pi:
          self.rot = 0
        if key == pyg.K_s and self.rot != 0:
          self.rot = math.pi
        if key == pyg.K_a and self.rot != math.pi / 2:
          self.rot = -math.pi / 2
        if key == pyg.K_d and self.rot != -math.pi / 2:
          self.rot = math.pi / 2
      if self.rot == last_rot + math.pi or self.rot == last_rot - math.pi:
        key = self.keys_in_update[len(self.keys_in_update) - 1]
        if key == pyg.K_w and self.rot != math.pi:
          self.rot = 0
        if key == pyg.K_s and self.rot != 0:
          self.rot = math.pi
        if key == pyg.K_a and self.rot != math.pi / 2:
          self.rot = -math.pi / 2
        if key == pyg.K_d and self.rot != -math.pi / 2:
          self.rot = math.pi / 2
      else:
        self.keys_in_update = []
      self.past_poses.append({"pos": self.rect.center, "rot": -self.rot})
      self.tail_poses.clear()
      for idx in range(self.tail_length):
        try:
          self.tail_poses.append(self.past_poses[len(self.past_poses) - idx - 1])
        except IndexError:
          pass
      self.rect.centerx += self.acc * math.sin(self.rot)
      self.rect.centery -= self.acc * math.cos(self.rot)
      self.keys_in_update = []
      if next_key:
        self.keys_in_update.append(next_key)
      self.tick = 0
    for event in pyg.event.get():
      if event.type == pyg.KEYDOWN:
        self.keys_in_update.append(event.key)