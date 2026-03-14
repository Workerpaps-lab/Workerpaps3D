import bpy
import sys
import os

# Cambia este path al que desees importar
obj_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../examples/cubo.obj'))

# Elimina todos los objetos de la escena actual
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Importa el archivo OBJ
bpy.ops.import_scene.obj(filepath=obj_path)
print(f"Modelo importado desde: {obj_path}")