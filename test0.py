import pygame as pyg
import math
pyg.init()
class Vector2():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    pass

class Vector3():
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    pass
camera_pos = Vector3(16, 16, 0)
camera_rot = Vector3(0, 0, 0)
keys = []
def Vec3to2(x: float, y: float, z: float, fov_factor = 1):
  """
  x = x - camera_pos.x
  y = y - camera_pos.y
  z = z - camera_pos.z
  if z <= 0:
    return float('inf'), float('inf')
  # x_projected = (x / z) * fov_factor
  # y_projected = (y / z) * fov_factor
  projected_x = x * fov_factor/z
  projected_y = y * fov_factor/z
  screen_x = projected_x + (800 / 2)
  screen_y = projected_y + (600 / 2)
  return screen_x, screen_y
  """
  plane_distance = 1
  point_A = (x, y, z)
  point_C = (camera_pos.x, camera_pos.y, camera_pos.z)
  translated_x = point_A[0] - point_C[0]
  translated_y = point_A[1] - point_C[1]
  translated_z = point_A[2] - point_C[2]
    # 2. Apply camera rotations (inverse of camera's orientation)
    # We rotate the point around the origin (which is now the camera)
    # The order of rotations (Z-Y-X or roll-pitch-yaw) is important.
    # The Wikipedia article uses Tait-Bryan angles, which typically means
    # yaw (around Y), pitch (around X), then roll (around Z).
    # Since we are rotating the point relative to the camera's fixed orientation,
    # we apply the *inverse* rotations in the *opposite* order.

    # Rotate around Z (roll)
  theta_x = camera_rot.x
  theta_y = camera_rot.y
  theta_z = camera_rot.z
  temp_x = translated_x * math.cos(-theta_z) - translated_y * math.sin(-theta_z)
  temp_y = translated_x * math.sin(-theta_z) + translated_y * math.cos(-theta_z)
  translated_x, translated_y = temp_x, temp_y
    # Rotate around Y (pitch)
  temp_x = translated_x * math.cos(-theta_y) + translated_z * math.sin(-theta_y)
  temp_z = -translated_x * math.sin(-theta_y) + translated_z * math.cos(-theta_y)
  translated_x, translated_z = temp_x, temp_z

  # Rotate around X (yaw)
  temp_y = translated_y * math.cos(-theta_x) - translated_z * math.sin(-theta_x)
  temp_z = translated_y * math.sin(-theta_x) + translated_z * math.cos(-theta_x)
  translated_y, translated_z = temp_y, temp_z

    # 3. Perspective Projection
    # Now that the point is relative to the camera's orientation and position,
    # we project it onto the 2D plane.
    # The plane is `plane_distance` away from the camera along the camera's Z-axis.

    # If the point is behind the camera (translated_z <= 0), it cannot be projected
    # (or it would result in division by zero or a flipped image).
  if translated_z <= 0:
    return float('inf'), float('inf') # Or handle as an off-screen point
    # The projection formula is:
    # x_projected = (plane_distance / translated_z) * translated_x
    # y_projected = (plane_distance / translated_z) * translated_y
  Bx = (plane_distance / translated_z) * translated_x + 400
  By = (plane_distance / translated_z) * translated_y + 300
  return Bx, By
screen = pyg.display.set_mode((800, 600), pyg.RESIZABLE)
def draw_line(aX: float, aY: float, aZ: float, bX: float, bY: float, bZ: float, color, width = 8):
  pointA = Vec3to2(aX, aY, aZ)
  pointB = Vec3to2(bX, bY, bZ)
  dirToB = m.atan2(pointA[1] - pointB[1], pointA[0] - pointB[0]) / (m.pi / 180) + 180
  line_lenth = m.sqrt(abs(pointA[0] - pointB[0]) ** 2 + abs(pointA[1] - pointB[1]) ** 2)
  rect = pyg.Surface((width, float(line_lenth)))
  rect.fill(color)
  rotatedRect = pyg.transform.rotate(rect, dirToB)
  """
  pyg.draw.circle(screen, color, (pointA[0], pointA[1]), width)
  pyg.draw.circle(screen, color, (pointB[0], pointB[0]), width)
  """
  screen.blit(rotatedRect, (pointA[0], pointA[1]))
tick = 0
def draw():
  global tick
  tick += 1
  posA = Vec3to2(32, 32, 1)
  posB = Vec3to2(0, 32, 1)
  posC = Vec3to2(0, 0, 1)
  posD = Vec3to2(32, 0, 1)
  posE = Vec3to2(32, 32, 33)
  posF = Vec3to2(0, 32, 33)
  posG = Vec3to2(0, 0, 33)
  posH = Vec3to2(32, 0, 33)
  pyg.draw.line(screen, [200, 100, 255], posA, posB, 8)
  pyg.draw.line(screen, [200, 100, 255], posB, posC, 8)
  pyg.draw.line(screen, [200, 100, 255], posC, posD, 8)
  pyg.draw.line(screen, [200, 100, 255], posD, posA, 8)
  pyg.draw.line(screen, [200, 100, 255], posE, posF, 8)
  pyg.draw.line(screen, [200, 100, 255], posF, posG, 8)
  pyg.draw.line(screen, [200, 100, 255], posG, posH, 8)
  pyg.draw.line(screen, [200, 100, 255], posH, posE, 8)
  pyg.draw.line(screen, [200, 100, 255], posA, posE, 8)
  pyg.draw.line(screen, [200, 100, 255], posB, posF, 8)
  pyg.draw.line(screen, [200, 100, 255], posC, posG, 8)
  pyg.draw.line(screen, [200, 100, 255], posD, posH, 8)
  """
  draw_line(32, 32, 1.25, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))
  draw_line(32, 32, 1, 0, 32, 1, (200, 100, 255))"""

  if keys[pyg.K_d]:
    camera_pos.x += 0.125
  if keys[pyg.K_a]:
    camera_pos.x -= 0.125
  if keys[pyg.K_e]:
    camera_pos.y += 0.125
  if keys[pyg.K_q]:
    camera_pos.y -= 0.125
  if keys[pyg.K_w]:
    camera_pos.z -= 0.025
  if keys[pyg.K_s]:
    camera_pos.z += 0.025
  if keys[pyg.K_RIGHT]:
    camera_rot.x += 3 * (math.pi / 180)
  if keys[pyg.K_LEFT]:
    camera_rot.x -= 3 * (math.pi / 180)
while True:
  keys = pyg.key.get_pressed()
  if pyg.event.get(pyg.QUIT): break
  screen.fill([10, 0, 20])
  draw()
  pyg.display.flip()
pyg.quit()