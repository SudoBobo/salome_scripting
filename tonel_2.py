# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.2.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook

notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert(0, r'/home/bobo/PycharmProjects/salome_scripting')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


class dot():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    x = property()
    y = property()

    @x.getter
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @y.getter
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


def make_arcs_and_vertexes(arcs, vertexes, x_0, y_0, x_fin, y_fin, x_step, y_step):
    x = x_0
    y = y_0

    init_vertex = geompy.MakeVertex(x_0, y_0, 0)

    vertexes.append(init_vertex)
    vertex_3 = init_vertex

    while x < x_fin and y > y_fin:
        vertex_1 = vertex_3

        x = x + x_step
        y = y

        vertex_2 = geompy.MakeVertex(x, y, 0)
        vertexes.append(vertex_2)

        x = x
        y = y + y_step

        vertex_3 = geompy.MakeVertex(x, y, 0)
        vertexes.append(vertex_3)

        arc = geompy.MakeArc(vertex_1, vertex_2, vertex_3)
        arcs.append(arc)


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

arcs = list()
vertexes = list()

x_0 = 0
y_0 = 100

x_step = 5
y_step = -5

x_fin = 100
y_fin = 0

make_arcs_and_vertexes(arcs, vertexes, x_0, y_0, x_fin, y_fin, x_step, y_step)

outer_vertexes = [vertexes[0], geompy.MakeVertex(-100, 100, 0), geompy.MakeVertex(-100, -100, 0),
                  geompy.MakeVertex(100, -100, 0), vertexes[len(vertexes) - 1]]

lines = []
for i in range(4):
    lines.append(geompy.MakeLineTwoPnt(outer_vertexes[i], outer_vertexes[i + 1]))

elems = list()
elems.extend(lines)
elems.extend(arcs)

Face_1 = geompy.MakeFaceWires(elems, 1)
Disk_1 = geompy.MakeDiskR(15, 1)
Cut_1 = geompy.MakeCutList(Face_1, [Disk_1], True)

geompy.addToStudy(O, 'O')
geompy.addToStudy(OX, 'OX')
geompy.addToStudy(OY, 'OY')
geompy.addToStudy(OZ, 'OZ')

for v in range(len(vertexes)):
    geompy.addToStudy(vertexes[v], 'Vertex_{}'.format(v))

for outer_v in range(1, len(outer_vertexes) - 1, 1):
    geompy.addToStudy(outer_vertexes[outer_v], 'Outer_Vertex{}'.format(outer_v))

for l in range(len(lines)):
    geompy.addToStudy(lines[l], 'Line_{}'.format(l))

for a in range(len(arcs)):
    geompy.addToStudy(arcs[a], 'Arc_{}'.format(a))

geompy.addToStudy(Face_1, 'Face_1')
geompy.addToStudy(Disk_1, 'Disk_1')
geompy.addToStudy(Cut_1, 'Cut_1')


if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser(True)
