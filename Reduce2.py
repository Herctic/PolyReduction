import os
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
              
cleanPath = ""
originalPath = cmds.fileDialog2(cap = "Choose folder to reduce", ds = 1, fm = 3)

if originalPath != None and originalPath != "":
    cleanPath = str(originalPath[0])

for root, dirs, files in os.walk(cleanPath):
    print root, dirs, files
    for fileName in files:
        if fileName.endswith('.fbx'):
            print (fileName)
            filePath = root + "/" + fileName
            cmds.file(filePath, open = True, force = True)
            obj = cmds.ls(geometry = True)
            for item in obj:
                try:
                    cmds.polyReduce(p = 50, n = cmds.select(item))
                except:
                    pass
            pm.mel.FBXExport(f = filePath)