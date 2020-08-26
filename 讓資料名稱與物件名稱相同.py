import bpy

Ornl_objNm = bpy.context.selected_objects

for objNm in Ornl_objNm :
    objNm.data.name = objNm.name