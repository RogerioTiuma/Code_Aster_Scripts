#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Lenovo/00_MODELOS/00_TREINO_SOFTWARE/00_CURSO_WIKKI/00_CURSO_CODE_ASTER/CODE_ASTER_SCRIPS')

### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Group_1 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [33])
[Group_1] = geompy.GetExistingSubObjects(Box_1, False)
Group_1.SetColor(SALOMEDS.Color(1,1,0))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudyInFather( Box_1, Group_1, 'Group_1' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

smeshObj_1 = smesh.Mesh(Box_1)
Projection_3D = smesh.CreateHypothesis('Projection_3D')
status = smeshObj_1.AddHypothesis(Projection_3D)
isDone = smeshObj_1.Compute()
NETGEN_3D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters', 'NETGENEngine', 34.641, 0 )
Mesh_2 = smesh.Mesh(Box_1,'Mesh_2')
Regular_1D = Mesh_2.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(15)
Quadrangle_2D = Mesh_2.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_2.Hexahedron(algo=smeshBuilder.Hexa)
Group_1_1 = Mesh_2.GroupOnGeom(Group_1,'Group_1',SMESH.FACE)
isDone = Mesh_2.Compute()
[ Group_1_1 ] = Mesh_2.GetGroups()

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1.GetMesh()))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(Projection_3D, 'Projection_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
smesh.SetName(Group_1_1, 'Group_1')

###
### ASTERSTUDY component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
