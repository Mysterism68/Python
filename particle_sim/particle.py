import sdl2
import sdl2.ext
import random as ran
import math
win_dim = (800, 600)
zoom = 0.03125
GRAV = 1#6.674 * 10**-11 #Normal Gravity
speed = 1
cam_pos = [win_dim[0] // int(2 / zoom) , win_dim[1] // int(2 / zoom)]
cam_pos_dir = [0, 0]
def color(r, g, b):
  return sdl2.ext.Color(r, g, b)
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
class Gravity(object):
  def __init__(self, mass: float, anchorage: bool):
    super(Gravity, self).__init__()
    #The gravitational properties of an object
    self.vx = 0
    self.vy = 0
    self.mass = mass
    self.anchored = anchorage
class Particle(sdl2.ext.Entity):
  def __init__(self, world, diam: int, mass: float, posx=0,posy=0,
    red=ran.randint(100, 255), green=ran.randint(100, 255), blue=ran.randint(100, 255), anc = False, vel_dir=0, magn = 0):
    self.sprite = factory.from_color(color(red, green, blue), size=(diam, diam))
    self.sprite.position = posx - diam//2, posy - diam//2
    self.gravity = Gravity(mass, anc)
    self.gravity.mass = mass
    actual_dir = vel_dir * (math.pi / 180)
    self.gravity.vx = math.sin(actual_dir) * magn
    self.gravity.vy = math.cos(actual_dir) * magn
  def apply_gravity(self, dist: float, speed: float, rot: float, sprite2):
    swidth, sheight = sprite2.size
    average_rad = (swidth + sheight) / 4
    if dist >= speed:
      self.gravity.vx += math.sin(rot) * speed * speed
      self.gravity.vy += math.cos(rot) * speed * speed
    else:
      self.gravity.vx = math.sin(rot) * (dist-average_rad)
      self.gravity.vy = math.cos(rot) * (dist-average_rad)
  def main(self, particles):
    if particles and not self.gravity.anchored:
      for part in particles:
        sprite_grav = part.gravity #Gravity class
        sprite = part.sprite #Sprite class
        swidth, sheight = sprite.size
        our_width, our_height = self.sprite.size
        if sprite is self.sprite:
          continue
        #print(f"Current Particle's Gravity: {sprite_grav.vx}, Other Particle's Gravity: {part.gravity.vx}", end="\r")
        center_sprite = (self.sprite.position[0] + our_width // 2, self.sprite.position[1] + our_height // 2)
        other_center_sprite = (sprite.position[0] + swidth // 2, sprite.position[1] + sheight // 2)
        dist = get_dist(other_center_sprite, center_sprite)
        if dist <= (swidth + sheight) / 4:
          continue
        rot = get_rel_rot(center_sprite, other_center_sprite)
        speed = calculate_force(self.gravity.mass, sprite_grav.mass, dist)
        self.apply_gravity(dist, speed, rot, sprite)
        """
        average_rad = (swidth + sheight) / 4
        if dist >= speed:
          sprite_grav.vx += math.sin(rot) * -speed
          sprite_grav.vy += math.cos(rot) * -speed
        else:
          sprite_grav.vx = math.sin(rot) * -(dist-average_rad)
          sprite_grav.vy = math.cos(rot) * -(dist-average_rad)
        """
def calculate_force(mass1: float, mass2: float, dist: float):
  return GRAV * (mass1 * mass2) / dist**2
def get_dist(pos1: (float, float), pos2: (float, float)):
  return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
def get_rel_rot(pos1: (float, float), pos2: (float, float)):
  return math.atan2((pos1[0] - pos2[0]), (pos1[1] - pos2[1])) + math.pi