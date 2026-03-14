import sys
import os
import trimesh
import numpy as np

def crear_cubo():
    mesh = trimesh.creation.box(extents=(1,1,1))
    return mesh

def crear_esfera():
    mesh = trimesh.creation.icosphere(radius=0.5)
    return mesh

def crear_cilindro():
    mesh = trimesh.creation.cylinder(radius=0.5, height=1.0)
    return mesh

def main():
    if len(sys.argv) < 2:
        print("Uso: python generate_basic_shape.py [cubo|esfera|cilindro]")
        return
    shape = sys.argv[1].lower()

    output_dir = os.path.join(os.path.dirname(__file__), '../examples')
    os.makedirs(output_dir, exist_ok=True)

    if shape == "cubo":
        mesh = crear_cubo()
    elif shape == "esfera":
        mesh = crear_esfera()
    elif shape == "cilindro":
        mesh = crear_cilindro()
    else:
        print("Forma no reconocida. Usa: cubo, esfera o cilindro.")
        return
    
    export_path = os.path.join(output_dir, f"{shape}.obj")
    mesh.export(export_path)
    print(f"Modelo '{shape}' exportado exitosamente a {export_path}")

if __name__ == "__main__":
    main()