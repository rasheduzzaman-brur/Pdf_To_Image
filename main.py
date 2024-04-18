from pdf2image import convert_from_path
import os
import random

def pdf_to_jpg(pdf_files, output_folder):
    for pdf_file in pdf_files:
        # Get the base filename without extension
        base_filename = os.path.splitext(os.path.basename(pdf_file))[0]
        # Convert PDF to images
        images = convert_from_path(pdf_file, poppler_path='C:/Program Files/poppler-24.02.0/Library/bin')
        for i, image in enumerate(images):
            # Save each page as JPG
            image.save(f"{output_folder}/{base_filename}_page_0{i+1}.jpg", "JPEG")

# Provide the directory containing PDF files and the output folder where you want to save the JPG files
pdf_directory = "orientation_dataset/"
output_folder = "orientation_data_image/"

# Get a list of PDF files in the directory
pdf_files = [os.path.join(pdf_directory, file) for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# Convert PDF files to JPG images
pdf_to_jpg(pdf_files, output_folder)
