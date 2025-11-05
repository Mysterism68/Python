import sys
import sdl2
import sdl2.ext
import sdl2.sdlgfx as sdlgfx
import math
import random as rand
import ctypes
from particle import *
from systems import *
mouse_x = 0
mouse_y = 0
mouse_down = False
FPS = 60
FRAME_DELAY = int(1000 / FPS)  # milliseconds per frame
def run():
  global game_speed, mouse_x, mouse_y, mouse_down, zoom
  sdl2.ext.init()
  window = sdl2.ext.Window("Particle Simulator", size=win_dim)
  window.show()
  running = Trueworld = sdl2.ext.World()
  world = sdl2.ext.World()
  movement = MovementSystem(0, 0, win_dim[0], win_dim[1])
  gravity = GravitySystem(0, 0, win_dim[1], win_dim[1])
  spriterenderer = SoftwareRenderer(window, 1)
  world.add_system(movement)
  world.add_system(gravity)
  world.add_system(spriterenderer)
  moon_mass = 64
  particles = [Particle(world, 192, 0, 0, 0, 255, 0, 0), Particle(world, 192, 0, 0, 0, 255, 0, 0),
    Particle(world, 512, moon_mass*162.54*50, int(400 / zoom), int(300 / zoom), 255, 255, 0)]
  moons = 3
  dist = 128
  for i in range(moons):
    rot = i*(360/moons)
    particles.append(Particle(world, 192, moon_mass, int((400+math.sin(rot * (math.pi / 180))*dist) / zoom),
      int((300+math.cos(rot * (math.pi / 180))*dist) / zoom), 225, 225, 255, vel_dir=rot+90, magn=100))
  mouse_particle = Particle(world, 0, 0, 418, 300)
  gravity.particles = particles
  ticks_pressed = 0
  running = True
  while running:
    spriterenderer.scale = zoom
    frame_start = sdl2.SDL_GetTicks()
    mouse_x = ctypes.c_int()
    mouse_y = ctypes.c_int()
    sdl2.SDL_GetMouseState(ctypes.byref(mouse_x), ctypes.byref(mouse_y))
    mouse_x = int(mouse_x.value / zoom)
    mouse_y = int(mouse_y.value / zoom)
    mouse_particle.sprite.x = mouse_x
    mouse_particle.sprite.y = mouse_y
    mouse_particle.gravity.vx = 0
    mouse_particle.gravity.vy = 0
    events = sdl2.ext.get_events()
    for part in particles:
      swidth, sheight = part.sprite.size
      if part.gravity.mass == 0:
        continue
      if swidth==512:
        particles[0].sprite.x = part.sprite.x
        particles[0].sprite.y = part.sprite.y
        particles[1].sprite.x = part.sprite.x + swidth
        particles[1].sprite.y = part.sprite.y + sheight
      if ((mouse_x >= part.sprite.x and mouse_x <= part.sprite.x + swidth) and
        (mouse_y >= part.sprite.y and mouse_y <= part.sprite.y + sheight)):
        print(mouse_down, end="\r")
        if mouse_down:
          part.gravity.vx = mouse_x - (part.sprite.x)
          part.gravity.vy = mouse_y - (part.sprite.y)
      else:
        if part.gravity.anchored:
          part.gravity.vx = 0
          part.gravity.vy = 0


    for event in events:
      if event.type == sdl2.SDL_QUIT:
        running = False
        break
      if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
        mouse_down = True
      elif event.type == sdl2.SDL_MOUSEBUTTONUP:
        mouse_down = False
      if event.type == sdl2.SDL_KEYDOWN:
        sdl2.SDL_SetWindowDisplayMode(window.window, sdl2.SDL_DisplayMode(w=int(win_dim[0] * zoom), h=int(win_dim[1] * zoom)))
        if event.key.keysym.sym == sdl2.SDLK_z:
          particles[0].gravity.mass = moon_mass * (27.04)
        if event.key.keysym.sym == sdl2.SDLK_c:
          particles[0].gravity.mass = -moon_mass * (27.04)
        if event.key.keysym.sym == sdl2.SDLK_w:
          cam_pos_dir[1] = -0.4
        if event.key.keysym.sym == sdl2.SDLK_s:
          cam_pos_dir[1] = 0.4
        if event.key.keysym.sym == sdl2.SDLK_a:
          cam_pos_dir[0] = -0.4
        if event.key.keysym.sym == sdl2.SDLK_d:
          cam_pos_dir[0] = 0.4
        if event.key.keysym.sym == sdl2.SDLK_SPACE:
          game_speed = 0
        if event.key.keysym.sym == sdl2.SDLK_EQUALS:
          zoom /= 2
        if event.key.keysym.sym == sdl2.SDLK_MINUS:
          zoom *= 2
      elif event.type == sdl2.SDL_KEYUP:
        if event.key.keysym.sym == sdl2.SDLK_c:
          particles[0].gravity.mass = 0
        if event.key.keysym.sym == sdl2.SDLK_z:
          particles[0].gravity.mass = 0
        if event.key.keysym.sym == sdl2.SDLK_w:
          cam_pos_dir[1] = 0
        if event.key.keysym.sym == sdl2.SDLK_s:
          cam_pos_dir[1] = 0
        if event.key.keysym.sym == sdl2.SDLK_a:
          cam_pos_dir[0] = 0
        if event.key.keysym.sym == sdl2.SDLK_d:
          cam_pos_dir[0] = 0
    cam_pos[0] += cam_pos_dir[0]
    cam_pos[1] += cam_pos_dir[1]
    world.process()
    frame_time = sdl2.SDL_GetTicks() - frame_start
    if frame_time < FRAME_DELAY:
      sdl2.SDL_Delay((FRAME_DELAY - frame_time))
    try:
      print(f"We have an FPS of :{1000 / (FRAME_DELAY - frame_time)}", end="\r")
    except:
      pass
  return 0

if __name__ == "__main__":
  sys.exit(run())