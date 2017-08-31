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
                  geompy.MakeVertex(100, -100, 0), vertexes[len(vertexes) - 1] ]


Line_1 = geompy.MakeLineTwoPnt(outer_vertexes[0], outer_vertexes[1])
Line_2 = geompy.MakeLineTwoPnt(outer_vertexes[1], outer_vertexes[2])
Line_3 = geompy.MakeLineTwoPnt(outer_vertexes[2], outer_vertexes[3])
Line_4 = geompy.MakeLineTwoPnt(outer_vertexes[4], outer_vertexes[5])

elems = list()
elems.extend([Vertex_1, Vertex_2, Vertex_3, Vertex_4, Vertex_5])
elems.extend(arcs)

Face_1 = geompy.MakeFaceWires(elems, 1)
Disk_1 = geompy.MakeDiskR(15, 1)
Cut_1 = geompy.MakeCutList(Face_1, [Disk_1], True)

geompy.addToStudy(O, 'O')
geompy.addToStudy(OX, 'OX')
geompy.addToStudy(OY, 'OY')
geompy.addToStudy(OZ, 'OZ')


geompy.addToStudy(Vertex_1, 'Vertex_1')
geompy.addToStudy(Vertex_2, 'Vertex_2')
geompy.addToStudy(Vertex_3, 'Vertex_3')
geompy.addToStudy(Vertex_4, 'Vertex_4')
geompy.addToStudy(Line_1, 'Line_1')
geompy.addToStudy(Line_2, 'Line_2')
geompy.addToStudy(Line_3, 'Line_3')
geompy.addToStudyInFather(Line_3, Line_3_vertex_3, 'Line_3:vertex_3')
geompy.addToStudyInFather(Line_1, Line_1_vertex_2, 'Line_1:vertex_2')
geompy.addToStudy(Line_4, 'Line_4')
geompy.addToStudy(Face_1, 'Face_1')
geompy.addToStudy(Disk_1, 'Disk_1')
geompy.addToStudy(Cut_1, 'Cut_1')

for i in range(len(vertexes)):
  geompy.addToStudy(vertexes[i], 'Ve')
  geompy.addToStudy(vertex)
geompy.addToStudy(Face_1_1, 'Face_1')
geompy.addToStudy(Disk_1_1, 'Disk_1')
geompy.addToStudy(Cut_1_1, 'Cut_1')
#
# geompy.addToStudy(Vertex_5, 'Vertex_5')
# geompy.addToStudy(Vertex_6, 'Vertex_6')
# geompy.addToStudy(Vertex_7, 'Vertex_7')
# geompy.addToStudy(Vertex_8, 'Vertex_8')
# geompy.addToStudy(Vertex_9, 'Vertex_9')
# geompy.addToStudy(Arc_1, 'Arc_1')
# geompy.addToStudyInFather(Arc_1, Arc_1_vertex_3, 'Arc_1:vertex_3')
# geompy.addToStudy(Arc_2, 'Arc_2')

if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser(True)
