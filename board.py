from visual import *
from piece import Piece
from time import sleep
import math

class Board:
  """
  Collection of Pieces

  """

  def __init__(self):
    self.pieces = []

  def delete(self):
    for p in self.pieces:
      p.delete()
    del self.pieces
    del self

  # construye la forma final
  def final(self):
    side = 2.1*sin(pi/5.0)

    # The first piece
    first = Piece(vector(-1,-1.6*side,0),vector(0,0,1))

    # We form the first pentagon
    self.pieces = [first,
        first.clone().rotate(vector(0,1,0), 2.0/5.0*pi),
        first.clone().rotate(vector(0,1,0), 4.0/5.0*pi),
        first.clone().rotate(vector(0,1,0), 6.0/5.0*pi),
        first.clone().rotate(vector(0,1,0), 8.0/5.0*pi)]

    # Rotate the pentagon an create the bown
    defased = self.clone().rotate(vector(0,1,0),0.2*pi)

    faces = []
    for rot in defased.pieces:
      o = vector(rot.box.x * side, rot.box.y, rot.box.z* side)
      faces.append(self.clone().rotate(rot.box.axis, -16.7/5.0*pi, o))

    for face in faces:
      self.merge(face)
      face.delete

    defased.delete()

    roted = self.clone().rotate(vector(1,0,0),pi).rotate(vector(0,1,0),pi/5.0)
    self.merge(roted)
    roted.delete()
#vector(-sqrt(3),-10,-0.5)


  def similarity(self, compare):
    best = self.get_closest(compare)
    i = 0
    similarity = 0

    for other in compare:
      similarity = similarity + other.distance(best[i])
      i = i + 1

    return similarity

  def get_closest(self, compare):
    best = []

    for other in compare.pieces:
      closest = false
      closest_dist = 999999

      for one in self.pieces:
        tmp_dist = one.distance(other)
        if tmp_dist < closest_dist:
          closest = one
          closest_dist = tmp_dist

      best.append(closest)

    return best

  def rotations(self):
    rots = []
    rot_axises = [vector(1,0,0), vector(0,1,0), vector(0,0,1)]
    for axis in rot_axises:
      for angle in [0.025*pi, 0.05*pi, 0.075*pi, 0.1*pi, 0.125*pi, 0.15*pi, 0.175*pi, 0.2*pi]:
        rots.append([axis, angle])
    #rot_axises_2 = [vector(0,1,1),vector(1,1,0), vector(1,1,1),vector(1,0,1)]
    rot_axises_2 = []
    for axis in rot_axises_2:
      for angle in [0.05*pi, 0.1*pi, 0.15*pi, 0.175*pi]:
        rots.append([axis, angle])
    return rots

  def rotate(self, axis, angle, origin=vector(0,0,0)):
    sleep(0.2)
    for piece in self.pieces:
      piece.rotate(axis, angle, origin)
    return self

  def clone(self):
    c = Board()
    for pie in self.pieces:
      p = pie.clone()
      c.pieces.append(p)
    return c

  def merge(self, other):
    for p in other.pieces:
      self.pieces.append(p.clone())
