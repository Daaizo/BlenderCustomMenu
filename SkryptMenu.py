import bpy
#klasy odpowiadajace za nowe operatory 
class ZmienRozmiar(bpy.types.Operator): 
    """Zmiana wielkości zaznaczego elementu""" # podpowiedz wyświetlana po najechaniu myszka na operator
    bl_idname = "object.resize_selected" # nazwa operatora
    bl_label = "Zmień wielkość zaznaczonego obiektu"# tytuł okna operatora
    bl_options={'REGISTER','UNDO'}      #jezeli chcemy zeby byl wyswietalny w podpowiedziach to register
    
    # tworzenie sliderów
    size_x: bpy.props.FloatProperty(
        name="Rozmiar w osi X",
    )
    size_y: bpy.props.FloatProperty(
        name="Rozmiar w osi Y",
    )
    size_z: bpy.props.FloatProperty(
        name="Rozmiar w osi Z",
    )
    
    @classmethod   #metoda sprawdzająca czy jakiś obiekt istnieje
    def poll(cls, context):
        return context.object is not None
    
    def invoke(self, context, event):
        self.size_x = bpy.context.object.scale[0] # przypisanie początkowych wartości sliderów
        self.size_y = bpy.context.object.scale[1] # ,tak aby odpowiadały rozmiarowi obiektu w danej osi 
        self.size_z = bpy.context.object.scale[2] 
        return self.execute(context)
    
    def execute(self,context):  # przypisanie wartosci slidera do scalowania obiektu
        bpy.context.object.scale[0] = self.size_x
        bpy.context.object.scale[1] = self.size_y
        bpy.context.object.scale[2] = self.size_z  
        return {'FINISHED'}
    
class ZresetujRozmiar(bpy.types.Operator): 
    """ Zresetuj wielkość zaznaczonego obiektu """
    bl_idname = "object.default_resize" 
    bl_label = "Zresetuj wielkość zaznaczonego obiektu"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    def execute(self, context):
        bpy.context.object.scale[0] = 1
        bpy.context.object.scale[1] = 1
        bpy.context.object.scale[2] = 1
        return  {'FINISHED'}      
    
class PodwojRozmiar(bpy.types.Operator): 
    """Podwój rozmiar obiektu"""
    bl_idname = "object.double_size" 
    bl_label = "Podwój rozmiar obiektu"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    
    def execute(self, context):
        bpy.context.object.scale[0] *= 2
        bpy.context.object.scale[1] *= 2
        bpy.context.object.scale[2] *= 2
        return  {'FINISHED'}     

class PomniejszRozmiar(bpy.types.Operator): 
    """Podziel rozmiar obiektu na pół"""
    bl_idname = "object.divide_size" 
    bl_label = "Podziel rozmiar obiektu na pół"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.scale[0] /= 2
        bpy.context.object.scale[1] /= 2
        bpy.context.object.scale[2] /= 2
        return  {'FINISHED'}     
    
class PrzesunObiekt(bpy.types.Operator): 
    """Przesuwań obiekt """ 
    bl_idname = "object.move_selected" 
    bl_label = "Przesuń obiekt w dowolnej osi"
    bl_options={'REGISTER','UNDO'}  
    
    # tworzenie sliderów
    move_x: bpy.props.FloatProperty(
        name="Przesuń w osi X",
    )
    move_y: bpy.props.FloatProperty(
        name="Przesuń w osi Y",
    )
    move_z: bpy.props.FloatProperty(
        name="Przesuń w osi Z",
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
         
    
class ZresetujPolozenie(bpy.types.Operator):
    """ Zresetuj położenie zaznaczonego obiektu """
    bl_idname = "object.default_position" 
    bl_label = "Zresetuj położenie zaznaczonego obiektu"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.location[0] = 0 
        bpy.context.object.location[1] = 0
        bpy.context.object.location[2] = 0 
        return  {'FINISHED'}      

class ObrocObiekt(bpy.types.Operator): 
    """Obróć obiekt """ 
    bl_idname = "object.rotate_selected"
    bl_label = "Obróć obiekt w dowolnej osi"
    bl_options={'REGISTER','UNDO'}    
    
    # tworzenie sliderów
    rotate_x: bpy.props.FloatProperty(
        name="Obróć w osi X",
    )
    rotate_y: bpy.props.FloatProperty(
        name="Obróć w osi Y",
    )
    rotate_z: bpy.props.FloatProperty(
        name="Obróć w osi Z",
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
         
    
class ZresetujObrot(bpy.types.Operator): 
    """ Zresetuj obrocenie zaznaczonego obiektu """
    bl_idname = "object.default_rotation" 
    bl_label = "Zresetuj obrocenie zaznaczonego obiektu"
    bl_options={'REGISTER','UNDO'} 
    
    @classmethod   
    def poll(cls, context):
        return context.object is not None
    def execute(self, context):
        bpy.context.object.rotation_euler[0] = 0 
        bpy.context.object.rotation_euler[1] = 0
        bpy.context.object.rotation_euler[2] = 0
        return  {'FINISHED'}      
             

# klasa opowiadajaca za menu
class MojeMenu(bpy.types.Panel):
    
    bl_label = 'Podstawowe operacje na obiektach' # nagłówek menu
    bl_space_type = 'VIEW_3D' # widok w jakim pracuje menu, widok 3d w którym tworzymy obiekty
    bl_region_type = 'UI' # miejce gdzie otwiera sie nasz panel, po prawej stronie pod options, koło zakładalem item, top i view
    bl_category = 'Podstawowe operacje' # zmiana nazwy kategorii w której otwierja się menu
    
    #funkcja odpowiedzialna za rysowanie menu
    def draw(self,context):
        box = self.layout.box()    #wszystko bedzie w obramowaniu
        box.label(text="Dodawanie kształtów",icon="ADD") # dodanie tytulu i ikony
        
        #przypisanie kolejnych operatorow wraz z ikonami
        box.operator("mesh.primitive_circle_add",text="Dodaj koło",icon = "MESH_CIRCLE")
        box.operator("mesh.primitive_uv_sphere_add",text="Dodaj kulę" ,icon = "MESH_UVSPHERE")
        box.operator("mesh.primitive_cube_add",text="Dodaj sześcian" ,icon = "CUBE")
        box.operator("mesh.primitive_cylinder_add",text="Dodaj cylinder" ,icon = "MESH_CYLINDER")
        box.operator("mesh.primitive_cone_add",text="Dodaj stożek" ,icon = "CONE")
            
        box.label(text="Edytowanie obiektów ",icon ="MODIFIER_DATA") # tytuł kolnej sekcji 
        box.operator("object.select_all", text="zaznacz/odznacz wszystkie elementy").action = 'TOGGLE'
        box.operator("object.delete", text="usuń zaznaczony element").use_global=False
        
    
        # Dodanie stworzonych operatorow
        
        box.label(text="Zmiana wielkości obiektu", icon="MOD_LENGTH")# tytuł kolnej sekcji 
        row = box.row() # umieszczenie przycisków w jednym wierszu
        row.operator('object.resize_selected',text="Zmień wielkość obiektu") 
        row.operator('object.default_resize',text="Zresetuj wielkość obiektu") 
        row = box.row() # nowy wiersz

        row.operator('object.double_size')       
        row.operator('object.divide_size')  
         
        box.label(text="Przemieszczanie obiektów",icon="EMPTY_ARROWS")# tytuł kolnej sekcji 
        row = box.row() 
        row.operator('object.move_selected')  
        row.operator('object.default_position',text="Zresetuj położenie")
        
        box.label(text="Obracanie obiektów", icon ="ORIENTATION_GIMBAL") # tytuł kolnej sekcji 
        row = box.row() 
        row.operator('object.rotate_selected')  
        row.operator('object.default_rotation',text="Zresetuj obrót")
       
        
#zarejestrowanie wszystkich klas  operatów  
bpy.utils.register_class(ZmienRozmiar)
bpy.utils.register_class(ZresetujRozmiar)
bpy.utils.register_class(PodwojRozmiar)
bpy.utils.register_class(PomniejszRozmiar)
bpy.utils.register_class(PrzesunObiekt)
bpy.utils.register_class(ZresetujPolozenie)
bpy.utils.register_class(ObrocObiekt)
bpy.utils.register_class(ZresetujObrot)


#zarejestrowanie klasy menu
bpy.utils.register_class(MojeMenu)
