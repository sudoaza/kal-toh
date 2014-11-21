from visual import *
import numpy

class Piece:
  """
  A Kal-toh Piece

  """

  def __init__(self, position, axis):
    self.box = box(pos=position, axis=axis, length=1.50, height=0.1, width=0.1)

  def distance(self, compare):
    return diff_angle(self.box.axis, compare.box.axis) + scipy.spatial.distance.euclidean(self.box.pos, compare.box.pos)

  def rotate(self, axis, angle, origin=vector(0,0,0)):
    self.box.rotate(angle=angle, axis=axis, origin=origin)
    return self

  def clone(self):
    b = self.box
    a = self.box.axis
    return Piece(vector(b.x,b.y,b.z), vector(a.x,a.y,a.z))

  def delete(self):
    self.box.visible = False
    del self.box
    del self
