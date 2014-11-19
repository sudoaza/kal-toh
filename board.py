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

  def final(self):
    first = Piece(vector(-1,0,0),vector(0,0,1))
    self.pieces = [first, first.clone().rotate(vector(0,1,0), 2.0/5.0*pi), first.clone().rotate(vector(0,1,0), 4.0/5.0*pi), first.clone().rotate(vector(0,1,0), 6.0/5.0*pi), first.clone().rotate(vector(0,1,0), 8.0/5.0*pi)]

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
    rot_axises = [vector(0,0,1), vector(1,1,0), vector(1,1,1)]
    for axis in rot_axises:
      for angle in [0.025*pi, 0.05*pi, 0.075*pi, 0.1*pi, 0.125*pi, 0.15*pi, 0.175*pi]:
        rots.append(self.clone().rotate(axis, angle))
    return rots

  def rotate(self, axis, angle):
    for piece in self.pieces:
      piece.rotate(axis, angle)
    return self

  def clone(self):
    c = Board()
    for pie in self.pieces:
      p = pie.clone()
      c.pieces.append(p)
    return c
