import numpy as np

# Standard color mapping (modify based on your cube)
COLOR_MAP={
    'white':'U',
    'yellow':'D',
    'green':'F',
    'blue':'B',
    'red':'R',
    'orange':'L'
}

def create_color_library(processed_faces):
    """Create reference color library from center pieces"""
    color_lib={}
    color_names=['white','yellow','orange','red','green','blue']
    
    for face, color_name in zip(processed_faces,color_names):
        center_color=tuple(face[1, 1])  # Convert to hashable tuple
        color_lib[center_color]=color_name
        
    return color_lib

def map_to_standard(processed_faces):
    """Map detected colors to standard notation"""
    color_lib=create_color_library(processed_faces)
    cube_string=[]
    
    face_order=[0,1,2,3,4,5]  # U, D, L, R, F, B
    
    for face_idx in face_order:
        face=processed_faces[face_idx]
        for i in range(3):
            for j in range(3):
                color=tuple(face[i,j])  # Convert to hashable tuple
                closest=min(color_lib.keys(), 
                            key=lambda x: sum((a-b)**2 for a,b in zip(x,color)))
                cube_string.append(COLOR_MAP[color_lib[closest]])
    
    return ''.join(cube_string)
