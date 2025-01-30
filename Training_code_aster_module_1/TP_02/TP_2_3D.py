#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Lenovo/00_MODELOS/00_TREINO_SOFTWARE/CODE_ASTER_SCRIPS/Training_code_aster_module_1')

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
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

([smeshObj_1], status) = smesh.CreateMeshesFromMED( r'C:/00_MODELOS/00_TREINO_CODE_ASTER/01_ESTUDO_CODE_ASTER/Code_Aster_Module1_Basic_training/Fichiers_TP/TP2/TP02.mmed' )
[ smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7 ] = smeshObj_1.GetGroups()
([Tank], status) = smesh.CreateMeshesFromMED( r'C:/00_MODELOS/00_TREINO_CODE_ASTER/01_ESTUDO_CODE_ASTER/Code_Aster_Module1_Basic_training/Fichiers_TP/TP2/Tank.med' )
[ Interieur, Bas, G1, G2 ] = Tank.GetGroups()

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1.GetMesh()))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_7))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(G1, 'G1')
smesh.SetName(G2, 'G2')
smesh.SetName(Tank.GetMesh(), 'Tank')
smesh.SetName(Bas, 'Bas')
smesh.SetName(Interieur, 'Interieur')

###
### ASTERSTUDY component
###

###
### PARAVIS component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
