# Watermark Maker

A simple and user-friendly GUI application for adding watermarks to images using Python and Tkinter.

## Features

- **Easy Image Upload**: Upload images in various formats (JPG, JPEG, PNG, BMP, GIF)
- **Text Watermarks**: Add custom text watermarks to your images
- **Automatic Positioning**: Watermarks are automatically centered and rotated at 45 degrees
- **Real-time Preview**: See your watermarked image before saving
- **Multiple Save Formats**: Save your watermarked images as PNG or JPEG files
- **Responsive UI**: Clean and intuitive graphical user interface

## Screenshots

The application provides a simple interface with:

- Canvas area for image preview
- Upload button to select images
- Text entry field for watermark text
- Add Watermark button to apply the watermark
- Save button to export the final image

## Requirements

- Python 3.6+
- Pillow (PIL)
- Tkinter (usually comes with Python)

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install Pillow
```

Note: Tkinter is typically included with Python installations.

## Usage

1. Run the application:

```bash
python main.py
```

2. Click "Upload Image" to select an image file from your computer

3. Enter your desired watermark text in the text field

4. Click "Add Watermark" to apply the watermark to your image

5. Preview the result in the canvas area

6. Click "Save Image" to save the watermarked image to your desired location

## How It Works

- The watermark text is positioned at the center of the image
- Text size is automatically calculated based on image dimensions (10% of the smallest dimension)
- The watermark is applied with 45-degree rotation and semi-transparent white text
- The application preserves image quality and supports transparency

## Technical Details

- Built with Python's Tkinter for the GUI
- Uses PIL (Pillow) for image processing
- Supports RGBA color mode for transparency handling
- Automatic font sizing based on image dimensions
- Cross-platform compatibility

## Future Enhancements

Potential improvements that could be added:

- Font selection options
- Watermark color customization
- Position adjustment controls
- Opacity/transparency controls
- Batch processing for multiple images
- Different watermark styles (not just rotated text)

## License

This project is created for educational purpose.
