import bpy
from bpy.props import *

bpy.ops.mesh.select_random(seed=2)
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.flip_normals()
bpy.ops.object.editmode_toggle()





