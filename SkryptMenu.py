import bpy

#wywołanie np. bpy.ops.object.resize_selected_selected(size_x = 3,size_y=4,size_z=3)
class ZmienRozmiar(bpy.types.Operator): # nowy operator
    """ Mój właśny operator("""
    bl_idname = "object.resize_selected" # nazwa operatora
    bl_label = "Zmień wielkość zaznaczonego obiektu"
    bl_options={'REGISTER','UNDO'}      #jezeli chcemy zeby byl wyswietalny w podpowiedziach to register
    
    
    
    # stworzenie sliderów
    size_x: bpy.props.FloatProperty( # stworzenie sliderów
        name="Rozmiar w osi X",
    )
    size_y: bpy.props.FloatProperty(
      
        name="Rozmiar w osi Y",
    )
    size_z: bpy.props.FloatProperty(
        name="Rozmiar w osi Z",
    )
        
    def execute(self,context): 
        bpy.context.object.scale[0] = self.size_x
        bpy.context.object.scale[1] = self.size_y
        bpy.context.object.scale[2] = self.size_z  
        return {'FINISHED'}
      
class MojeMenu(bpy.types.Panel):
    
    bl_label = 'Panel z kształtami' # nagłówek menu
    bl_space_type = 'VIEW_3D' # widok w jakim pracuje menu, widok 3d w którym tworzymy obiekty
    bl_region_type = 'UI' # miejce gdzie otwiera sie nasz panel, po prawej stronie pod options, koło zakładalem item, top i view
    bl_category = 'Menu' # zmiana nazwy kategorii na menu
    
    def draw(self,context):
    
        
    
        box = self.layout.box()
        
        box.label(text="Menu dodawania kształtów")
        
        box.operator("mesh.primitive_circle_add",text="Dodaj koło",icon = "MESH_CIRCLE")
        box.operator("mesh.primitive_uv_sphere_add",text="Dodaj kulę" ,icon = "MESH_UVSPHERE")
        box.operator("mesh.primitive_cube_add",text="Dodaj sześcian" ,icon = "CUBE")
        box.operator("mesh.primitive_cylinder_add",text="Dodaj cylinder" ,icon = "MESH_CYLINDER")
        box.operator("mesh.primitive_cone_add",text="Dodaj stożek" ,icon = "CONE")
        
        
        box.label(text="Menu edytowania - ( tylko object mode ) ")
        box.operator("object.select_all", text="zaznacz/odznacz wszystkie elementy").action = 'TOGGLE'
        
        box.operator("object.delete", text="usuń zaznaczony element").use_global=False
        box.operator('object.resize_selected',text="Zmień wielkość obiektu") # DODANIE NASZEGO OPERATORA !!!
        box.operator('object.default_resize',text="Zresetuj wielkość obiektu")
        box.operator('object.double_size',text="rozmiar x2")       
        box.operator('object.halve_size',text="rozmiar /2")       
        
        
bpy.utils.register_class(MESH_OT_ZmienRozmiar2)
bpy.utils.register_class(ZresetujRozmiar)
bpy.utils.register_class(PodwojRozmiar)
bpy.utils.register_class(PomniejszRozmiar)
bpy.utils.register_class(MojeMenu)


#Kolejny krok to dodanie nowego operatora do menu.Ponieważ nowy stworzony operator jest rozszerzeniem klasy bpy.types.Operator i możemy go używać tak jak w przykładzie powyżej jesteśmy w stanie dodać go używająć tego samego polecenia co wcześniej, czyli nazwa
#naszego wiersza lub w tym przypadku box, który odpowiada miejscue gdzie są przyciski .operator. 
# SCR Dodania i test nowego operatora
# 
#
#




#



