from visual import *
from piece import Piece
from board import Board

def main():
  scene.width=800
  scene.height=600
  scene.center=vector(0,0,0)
  scene.forward=vector(1,-1,-1)
  scene.userzoom=true
  scene.userspin=true
  scene.autoscale=false
  scene.range=5

  x = box(pos=vector(0,0,0), axis=vector(1,0,0), length=20, height=0.02, width=0.02, color=(1,0,0))
  y = box(pos=vector(0,0,0), axis=vector(0,1,0), length=20, height=0.02, width=0.02, color=(0,1,0))
  z = box(pos=vector(0,0,0), axis=vector(0,0,1), length=20, height=0.02, width=0.02, color=(0,0,1))

  b = Board()
  b.final()
  rots = b.rotations()
#  for ro in rots:
#    b.clone().rotate(ro[0],ro[1])

  i=0
  while True:
    rate(10)
    r = i % len(rots)
#    scene.forward = scene.forward.rotate(angle=0.02,axis=scene.up)
    b.rotate(rots[r][0], rots[r][1])
    i = i+1


if __name__ == "__main__":
  main()
