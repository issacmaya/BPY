import bpy


search_Mtrl_name = "B" # 引號內輸入找尋的材質
chang_Mtrl_name = "D" # 引號內輸入替換的材質
slt_Objs = bpy.context.selected_objects




for slt_Obj in slt_Objs : 
    slt_Obj_Mtrl_Slts = slt_Obj.material_slots[:]
    for slt_Obj_Mtrl_Slt in slt_Obj_Mtrl_Slts : 
        sh_name =slt_Obj_Mtrl_Slt.name
        if sh_name == search_Mtrl_name :
            slt_Obj_Mtrl_Slt.material = bpy.data.materials[chang_Mtrl_name]


