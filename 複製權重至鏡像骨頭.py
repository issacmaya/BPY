import bpy
from bpy.props import *
# Var
obj = bpy.context.object
slctGroupIDX=bpy.context.active_object.vertex_groups.active_index
slctGroupNM=bpy.context.active_object.vertex_groups[slctGroupIDX].name


# Function
def ChangRorL(Strinto):
    rStr=DeleCopy(Strinto)    
    if ".R" in rStr:
        rStr=Strinto.replace(".R",".L")
        return(rStr)
    if ".L" in rStr:
        rStr=Strinto.replace(".L",".R")
        return(rStr)
    if ".r" in rStr:
        rStr=Strinto.replace(".r",".l")
        return(rStr)
    if ".l" in rStr:
        rStr=Strinto.replace(".l",".r")
        return(rStr)

def DeleCopy(Strinto):
    rStr=Strinto
    if "_copy" in rStr:
        rStr=Strinto.replace("_copy","")
        return(rStr)
    return(rStr)


def ChangRorLandDeleCopy(Strinto):
    rStr=DeleCopy(Strinto)
    rStr2=ChangRorL(rStr)
    return(rStr2)




#dele Mirro Bones
vg = obj.vertex_groups.get(ChangRorLandDeleCopy(slctGroupNM))
obj.vertex_groups.remove(vg)

#copy and Mirro Weight
bpy.ops.object.vertex_group_copy()
bpy.ops.object.vertex_group_mirror(use_topology=False)

#reName
slctGroupIDX=bpy.context.active_object.vertex_groups.active_index
bpy.context.active_object.vertex_groups[slctGroupIDX].name = ChangRorLandDeleCopy(slctGroupNM)



