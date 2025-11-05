import sys
import sdl2
import sdl2.ext
from particle import *
class MovementSystem(sdl2.ext.Applicator):
  def __init__(self, minx, miny, maxx, maxy):
    super(MovementSystem, self).__init__()
    self.componenttypes = Gravity, sdl2.ext.Sprite
    self.minx = minx
    self.miny = miny
    self.maxx = maxx
    self.maxy = maxy
  def process(self, world, componentsets):
    for velocity, sprite in componentsets:
      swidth, sheight = sprite.size
      sprite.x += int(velocity.vx)
      sprite.y += int(velocity.vy)
    if swidth & sheight < 1:
      return
    """
    if sprite.x + swidth > self.maxx:
      sprite.x = self.maxx + swidth
    if sprite.x < 0:
      sprite.x = 0
    if sprite.y + sheight > self.maxy:
      sprite.y = self.maxy + sheight
    if sprite.y < 0:
      sprite.y = 0
    """

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
  def __init__(self, window, scale: float):
    super(SoftwareRenderer, self).__init__(window)
    self.scale = scale
  def render(self, components):
    sdl2.ext.fill(self.surface, sdl2.ext.Color(10, 0, 20))
    for sprite in components:
      if sprite is None:
        continue
      x, y = sprite.position
      w, h = sprite.size
      scaled_rect = sdl2.SDL_Rect(
        int(x * self.scale)-int(cam_pos[0]/zoom),
        int(y * self.scale)-int(cam_pos[1]/zoom),
        int(max(w * self.scale, 4)),
        int(max(h * self.scale, 4))
      )
      center = (sprite.position[0] + w, sprite.position[1] + h)
      sdl2.SDL_BlitScaled(sprite.surface, None, self.surface, scaled_rect)
    sdl2.SDL_UpdateWindowSurface(self.window)


class GravitySystem(sdl2.ext.Applicator):
  def __init__(self, minx, miny, maxx, maxy):
    super(GravitySystem, self).__init__()
    self.componenttypes = Gravity, sdl2.ext.Sprite
    self.particles = None
    self.minx = minx
    self.miny = miny
    self.maxx = maxx
    self.maxy = maxy
  def process(self, world, componentsets):
    items = [comp for comp in componentsets]
    for part in self.particles:
      part.main(self.particles)