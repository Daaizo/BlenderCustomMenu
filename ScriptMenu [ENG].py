import bpy
#classes responsible for new operators 
class ChangeSize(bpy.types.Operator): 
    """Resize the selected item""" # tooltip displayed when moving the mouse over an operator or button with it
    bl_idname = "object.resize_selected" # operator name
    bl_label = "Resize the selected item"# title of the operator window
    bl_options={'REGISTER','UNDO'}      #If you want it to be displayed in the tooltips
    
    # slider creation
    size_x: bpy.props.FloatProperty(
        name="Size in X axis",
    )
    size_y: bpy.props.FloatProperty(
        name="Size in Y axis",
    )
    size_z: bpy.props.FloatProperty(
        name="Size in Z axis",
    )

    #method to check if an object exists
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    # assign the initial values of sliders so that they correspond to the size of the object in the given axis
    def invoke(self, context, event):
        self.size_x = bpy.context.object.scale[0] 
        self.size_y = bpy.context.object.scale[1]  
        self.size_z = bpy.context.object.scale[2] 
        return self.execute(context)
    # assigning a slider value to scale in each axis 
    def execute(self,context):  
        bpy.context.object.scale[0] = self.size_x
        bpy.context.object.scale[1] = self.size_y
        bpy.context.object.scale[2] = self.size_z  
        return {'FINISHED'}
    
class ResetSize(bpy.types.Operator): 
    """Reset the size of the selected object"""
    bl_idname = "object.default_resize" 
    bl_label = "Reset the size of the selected object
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    def execute(self, context):
        bpy.context.object.scale[0] = 1
        bpy.context.object.scale[1] = 1
        bpy.context.object.scale[2] = 1
        return  {'FINISHED'}      
    
class DoubleSize(bpy.types.Operator): 
    """Double the size of the object"""
    bl_idname = "object.double_size" 
    bl_label = "Double the size of the object"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    def execute(self, context):
        bpy.context.object.scale[0] *= 2
        bpy.context.object.scale[1] *= 2
        bpy.context.object.scale[2] *= 2
        return  {'FINISHED'}     

class HalveSize(bpy.types.Operator): 
    """Halve the object size"""
    bl_idname = "object.halve_size" 
    bl_label = "Halve the object size"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.scale[0] /= 2
        bpy.context.object.scale[1] /= 2
        bpy.context.object.scale[2] /= 2
        return  {'FINISHED'}     
    
class MoveObject(bpy.types.Operator): 
    """Move the selected object""" 
    bl_idname = "object.move_selected" 
    bl_label = "Move the selected object"
    bl_options={'REGISTER','UNDO'}  
    
    
    move_x: bpy.props.FloatProperty(
        name="Move in X axis",
    )
    move_y: bpy.props.FloatProperty(
        name="Move in Y axis",
    )
    move_z: bpy.props.FloatProperty(
        name="Move in Z axis",
    )
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    def invoke(self, context, event): 
        self.move_x = bpy.context.object.location[0]
        self.move_y = bpy.context.object.location[1] 
        self.move_z = bpy.context.object.location[2] 
        return self.execute(context)
    
    def execute(self,context): 
        bpy.context.object.location[0] = self.move_x
        bpy.context.object.location[1] = self.move_y
        bpy.context.object.location[2] = self.move_z  
        return {'FINISHED'} 
         
    
class ResetPosition(bpy.types.Operator):
    """Reset the position of the selected object """
    bl_idname = "object.default_position" 
    bl_label = "Reset the position of the selected object "
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.location[0] = 0 
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0 
        return  {'FINISHED'}      
class RotateObject(bpy.types.Operator): 
    """Rotate the selected object""" 
    bl_idname = "object.rotate_selected"
    bl_label = "Rotate the selected object"
    bl_options={'REGISTER','UNDO'}    
    
    rotate_x: bpy.props.FloatProperty(
        name="Rotate in X axis",
    )
    rotate_y: bpy.props.FloatProperty(
        name="Rotate in Y axis",
    )
    rotate_z: bpy.props.FloatProperty(
        name="Rotate in Z axis",
    )
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None

    def invoke(self, context, event): 
        self.rotate_x = bpy.context.object.rotation_euler[0]
        self.rotate_y = bpy.context.object.rotation_euler[1] 
        self.rotate_z = bpy.context.object.rotation_euler[2] 
        return self.execute(context)
    
    def execute(self,context): 
        bpy.context.object.rotation_euler[0] = self.rotate_x 
        bpy.context.object.rotation_euler[1] = self.rotate_y
        bpy.context.object.rotation_euler[2] = self.rotate_z 
        return {'FINISHED'} 
         
    
class ResetRotation(bpy.types.Operator): 
    """Reset rotation of the selected object"""
    bl_idname = "object.default_rotation" 
    bl_label = "Reset rotation of the selected object"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.rotation_euler[0] = 0 
        bpy.context.object.rotation_euler[1] = 0
        bpy.context.object.rotation_euler[2] = 0
        return  {'FINISHED'}      
             

#class which creates menu
class MyMenu(bpy.types.Panel):
    
    bl_label = 'Basic object operations' #menu header
    bl_space_type = 'VIEW_3D' # view in which the menu works, 3d view in which we create objects
    bl_region_type = 'UI' #  the place where our panel is opened, right side under options button
    
    bl_category = 'Basic operations' #  rename the category in which the menu opens
    
    #function responsible for drawing menus
    def draw(self,context):
        box = self.layout.box()    #everything will be in a frame
        box.label(text="Adding shapes",icon="ADD") # adding a title and an icon
        
        #assignment of predefined operators with icons
        box.operator("mesh.primitive_circle_add",text="Add circle",icon = "MESH_CIRCLE")
        box.operator("mesh.primitive_uv_sphere_add",text="Add sphere" ,icon = "MESH_UVSPHERE")
        box.operator("mesh.primitive_cube_add",text="Add cube" ,icon = "CUBE")
        box.operator("mesh.primitive_cylinder_add",text="Add cylidner" ,icon = "MESH_CYLINDER")
        box.operator("mesh.primitive_cone_add",text="Add cone" ,icon = "CONE")
            
        box.label(text="Editing objects",icon ="MODIFIER_DATA") #  title of the next section 
        box.operator("object.select_all", text="select/unselect all objects").action = 'TOGGLE'
        box.operator("object.delete", text="delete the selected item").use_global=False
        
    
        # assignment of new operators which we created with icons
        
        box.label(text="Changing the size of the object", icon="MOD_LENGTH")#  title of the next section 
        row = box.row() # placing buttons on one line
        row.operator('object.resize_selected',text="Resize the object") 
        row.operator('object.default_resize',text="Reset object size") 
        row = box.row() #new row

        row.operator('object.double_size')       
        row.operator('object.divide_size')  
         
        box.label(text="Moving objects",icon="EMPTY_ARROWS") 
        row = box.row() 
        row.operator('object.move_selected')  
        row.operator('object.default_position',text="Reset position")
        
        box.label(text="Rotating objects", icon ="ORIENTATION_GIMBAL")
        row = box.row() 
        row.operator('object.rotate_selected')  
        row.operator('object.default_rotation',text="Reset rotation")
       

        
#registration of all classes of newly created operators
bpy.utils.register_class(ChangeSize)
bpy.utils.register_class(ResetSize)
bpy.utils.register_class(DoubleSize)
bpy.utils.register_class(HalveSize)
bpy.utils.register_class(MoveObject)
bpy.utils.register_class(ResetPosition)
bpy.utils.register_class(RotateObject)
bpy.utils.register_class(ResetRotation)


#registration of menu class
bpy.utils.register_class(MyMenu)
