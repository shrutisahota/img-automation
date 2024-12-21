import os
from PIL import Image


input_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder1'  
output_folder = r'C:\\Users\\DELL\\OneDrive\\Documents\\image automation\\outputfolder2'    


for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path).convert("L")  
        
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)
        print(f"Converted {filename} to greyscale and saved to {output_folder}")
