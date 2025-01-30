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

### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

([Face], status) = smesh.CreateMeshesFromMED( r'C:/00_MODELOS/02_ESTUDO_CODE_ASTER/Code_Aster_Module1_Basic_training/Fichiers_TP/TP02.mmed' )
[ LAB, LDA, NOEUDA, NOEUDB, NOEUDC, NOEUDD ] = Face.GetGroups()
([smeshObj_1], status) = smesh.CreateMeshesFromMED( r'C:\00_MODELOS\02_ESTUDO_CODE_ASTER\Code_Aster_Module1_Basic_training\Fichiers_TP\TP02.mmed' )
[ smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7 ] = smeshObj_1.GetGroups()
[ LAB, LDA, NOEUDA, NOEUDB, NOEUDC, NOEUDD ] = Face.GetGroups()
smesh.SetName(Face, 'Face')
try:
  Face.ExportMED(r'C:/00_MODELOS/02_ESTUDO_CODE_ASTER/Code_Aster_Module1_Basic_training/Fichiers_TP/Estudo_TP2_2D_completo_Files\RunCase_1\Result-Stage_1\_ExportedFromSalomeObject_0_1_3_3.med',auto_groups=0,version=33,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')
smesh.SetName(Face, 'Face')
try:
  Face.ExportMED(r'C:/00_MODELOS/02_ESTUDO_CODE_ASTER/Code_Aster_Module1_Basic_training/Fichiers_TP/Estudo_TP2_2D_completo_Files\RunCase_2\Result-Stage_1\_ExportedFromSalomeObject_0_1_3_3.med',auto_groups=0,version=33,overwrite=1,meshPart=None,autoDimension=1)
  pass
except:
  print('ExportMED() failed. Invalid file name?')

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_7))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1.GetMesh()))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(NOEUDC, 'NOEUDC')
smesh.SetName(NOEUDB, 'NOEUDB')
smesh.SetName(NOEUDA, 'NOEUDA')
smesh.SetName(NOEUDD, 'NOEUDD')
smesh.SetName(Face.GetMesh(), 'Face')
smesh.SetName(LAB, 'LAB')
smesh.SetName(LDA, 'LDA')

###
### PARAVIS component
###

###
### ASTERSTUDY component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
