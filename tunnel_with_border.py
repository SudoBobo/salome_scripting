# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.2.0 with dump python functionality
###
import random
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


def create_border(x_0, y_0, x_fin, y_fin, step, border_vertexes, border_lines, coef):


    # add ALL border dots (r_o and r_fin)
    k = (y_fin - y_0) / (x_fin - x_0)
    a = y_0 - k * x_0

    x = x_0
    y = y_0

    prev_vertex = geompy.MakeVertex(x_0, y_0, 0)
    border_vertexes.append(prev_vertex)

    while x < x_fin - step and y > y_fin :

        x = x + step
        y = k * x + a + random.random() * coef * step

        new_vertex = geompy.MakeVertex(x, y, 0)
        border_vertexes.append(new_vertex)

        border_lines.append(geompy.MakeLineTwoPnt(prev_vertex, new_vertex))

        prev_vertex = new_vertex

    final_vertex = geompy.MakeVertex(x_fin, y_fin, 0)
    border_vertexes.append(final_vertex)
    border_lines.append(geompy.MakeLineTwoPnt(prev_vertex, final_vertex))


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

# spatial_characteristic ('x' on the pic)
sc = 10

x_0 = 0
y_0 = 20 * sc

x_fin = 20 * sc
y_fin = -20 * sc


# trap created
trap_vertexes = [geompy.MakeVertex(x_0, y_0, 0), geompy.MakeVertex(-20*sc, 20*sc, 0), geompy.MakeVertex(-20*sc, -20*sc, 0),
            geompy.MakeVertex(x_fin, y_fin, 0)]
trap_lines = []
for i in range(len(trap_vertexes) - 1):
    trap_lines.append(geompy.MakeLineTwoPnt(trap_vertexes[i], trap_vertexes[i + 1]))
# trap_lines.append(geompy.MakeLineTwoPnt(trap_vertexes[3], trap_vertexes[0]))

#border created
border_vertexes = list()
border_lines = list()
step = 5

coef = 4
create_border(x_0, y_0, x_fin, y_fin, step, border_vertexes, border_lines, coef)

# tunnel created
tunnel_vertexes = [geompy.MakeVertex(-sc, -sc, 0), geompy.MakeVertex(0, sc, 0), geompy.MakeVertex(sc, -sc, 0)]
tunnel_line = geompy.MakeLineTwoPnt(tunnel_vertexes[0], tunnel_vertexes[2])
tunnel_arc = geompy.MakeArc(tunnel_vertexes[0], tunnel_vertexes[1], tunnel_vertexes[2])


# create triangle vertexes
triangle_vertexes = [geompy.MakeVertex(0, 20*sc, 0), geompy.MakeVertex(20*sc, 20*sc, 0), geompy.MakeVertex(20*sc, -20*sc, 0)]
# create triangle lines
triangle_lines = [geompy.MakeLineTwoPnt(triangle_vertexes[0], triangle_vertexes[1]),
                  geompy.MakeLineTwoPnt(triangle_vertexes[1], triangle_vertexes[2])]

triangle_border_vertexes = list(border_vertexes)
triangle_border_lines = list(border_lines)

# create copy of border for second (triangle) face
# create_border(x_0, y_0, x_fin, y_fin, step, triangle_border_vertexes, triangle_border_lines)


# create face_1 (don't forget to cut out tunnel), face_2, compound
tunnel_face = geompy.MakeFaceWires([tunnel_arc, tunnel_line], 1)
trap_face = geompy.MakeFaceWires(trap_lines + border_lines, 1)
#
cut_trap_face = geompy.MakeCutList(trap_face, [tunnel_face], True)
#
triangle_face = geompy.MakeFaceWires(triangle_lines + triangle_border_lines, 1)
#
Compound = geompy.MakeCompound([cut_trap_face, triangle_face])

geompy.addToStudy(O, 'O')
geompy.addToStudy(OX, 'OX')
geompy.addToStudy(OY, 'OY')
geompy.addToStudy(OZ, 'OZ')


all_vertexes = trap_vertexes + tunnel_vertexes + border_vertexes + triangle_vertexes + triangle_border_vertexes
all_lines = trap_lines + [tunnel_line] + border_lines + triangle_lines + triangle_border_lines
all_arcs = [tunnel_arc]

for v in range(len(all_vertexes)):
    geompy.addToStudy(all_vertexes[v], 'Vertex_{}'.format(v))

for l in range(len(all_lines)):
    geompy.addToStudy(all_lines[l], 'Line_{}'.format(l))

for a in range(len(all_arcs)):
    geompy.addToStudy(all_arcs[a], 'Arc_{}'.format(a))


geompy.addToStudy(tunnel_face, 'tunnel_face')
geompy.addToStudy(trap_face, 'trap_face')
geompy.addToStudy(cut_trap_face, 'cut_trap_face')
geompy.addToStudy(triangle_face, 'triangle_face')
geompy.addToStudy(Compound, 'Compound')

if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser(True)
