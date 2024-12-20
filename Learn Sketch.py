#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        rootComp = design.rootComponent
        sketches = rootComp.sketches

        sketch = sketches.add(rootComp.xYConstructionPlane)
        
        sketchLines = sketch.sketchCurves.sketchLines
        startPoint = adsk.core.Point3D.create(0,0,0)
        endPoint = adsk.core.Point3D.create(5,5,0)

        sketchLines.addCenterPointRectangle(startPoint,endPoint)
        sketchLines.addByTwoPoints(startPoint,endPoint)



        ui.messageBox('Sketch Created')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
