# Pdf_To_Image
This reopository convert the pdf file into image
# PDF to Image Converter Application

This Python application converts PDF files to images using the `pdf2image` module and requires the `poppler` library. Follow the instructions below to set up and use the application.

## Installation

1. **Install pdf2image**: Run the following command in your terminal to install the `pdf2image` module:

    ```
    pip install pdf2image==1.14.0
    ```

2. **Install poppler**:
    - **Windows**: Windows users need to download and install poppler for Windows. [Download poppler](https://github.com/oschwartz10612/poppler-windows/releases/) and extract it.
    - **Linux**: Poppler should be available in your distribution's package manager.
    - **MacOS**: Poppler can be installed using Homebrew: `brew install poppler`.

    Make sure to add the `bin/` folder of the poppler installation to your PATH environment variable. Alternatively, you can specify the poppler path in the code.

## Usage

1. Clone or download the repository to your local machine.

2. Ensure that your PDF files are located in a directory. Modify the `pdf_directory` variable in the Python script to point to this directory.

3. Specify the output folder where you want to save the JPG files by modifying the `output_folder` variable in the Python script.

4. Run the Python script `main.py`. This script converts PDF files to JPG images and saves them in the specified output folder.

    ```
    python main.py
    ```

5. After running the script, you will find the converted images in the output folder.

## Notes

- If you encounter any issues with poppler installation or path configuration, refer to the poppler documentation or seek assistance online.
- Ensure that the `pdf2image` module and its dependencies are correctly installed in your Python environment.
- This application currently supports converting PDF files to images without rotation. If you wish to implement rotation functionality, uncomment the relevant code in the Python script and modify it as needed.

