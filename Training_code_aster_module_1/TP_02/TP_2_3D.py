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

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("C", 950)
notebook.set("C05", "C/2")
notebook.set("Dex", 219)
notebook.set("Rex", "Dex/2")
notebook.set("t", 6)
notebook.set("Rin", "Rex-t")
notebook.set("Cd", 133)
notebook.set("Cd05", "Cd/2")
notebook.set("r1", 15)
notebook.set("r2", 3)
notebook.set("d", 3.6)
notebook.set("DL", "Dex+2*tL")
notebook.set("RL", "DL/2")
notebook.set("LL", 230)
notebook.set("LL05", "LL/2")
notebook.set("tL", 4)
notebook.set("Pi", 3.14)
notebook.set("Ld", 102)
notebook.set("Ld05", "Ld/2")
notebook.set("tetha", "Ld05/Rex")
notebook.set("SL1", "Cd05+t-d")
notebook.set("e", "t-d")
notebook.set("e1", "d+tL")
notebook.set("SL2", "Cd05-r1")
notebook.set("tetha1", "(Ld05+t-d)/Rex")
notebook.set("n", 8)
notebook.set("n3", "7*n")
notebook.set("D", 219)
notebook.set("d", 3.6)
notebook.set("t", 6)
notebook.set("D_2", 109.5)
notebook.set("p", 16)
notebook.set("p05", "p/2")
####################################################
##        End of NoteBook variables section       ##
####################################################
###
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
