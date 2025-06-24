import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class WatermarkApp:
    # A simple GUI application to add watermarks to images
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")
        self.root.geometry("800x600")

        self.image_path = None
        self.image = None

        self.preview_image = None

        # UI Elements
        self.canvas = tk.Canvas(self.root, width=500, height=400, bg='gray')
        self.canvas.pack(pady=10)

        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack()

        self.watermark_entry = tk.Entry(root, width=40)
        self.watermark_entry.insert(0, "Enter watermark text")
        self.watermark_entry.pack(pady=5)

        self.add_btn = tk.Button(root, text="Add Watermark", command=self.add_watermark)
        self.add_btn.pack()

        self.save_btn = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_btn.pack(pady=5)

    # Function to upload an image file and display it on the canvas
    def upload_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])

        if file_path:
            self.image_path = file_path
            self.image = Image.open(self.image_path).convert("RGBA")
            self.display_image(self.image)

    def display_image(self, img):
        max_size = (500, 400)
        img_copy = img.copy()
        img_copy.thumbnail(max_size)

        self.preview_image = ImageTk.PhotoImage(img_copy)
        self.canvas.create_image(250, 200, image=self.preview_image)

    # Function to add a watermark to the uploaded image
    def add_watermark(self):
        if not self.image:
            messagebox.showerror("Error", "Please upload an image first.")

            return

        watermark_text = self.watermark_entry.get()

        if not watermark_text:
            messagebox.showerror("Error", "Please enter watermark text.")

            return

        base = self.image.convert("RGBA")
        txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # Font size based on image size
        font_size = int(min(base.size) * 0.1)

        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        drawable = ImageDraw.Draw(txt_layer)

        bbox = drawable.textbbox((0, 0), watermark_text, font=font)

        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Center the text
        x = (base.width - text_width) // 2
        y = (base.height - text_height) // 2

        drawable.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 100))

        # Rotate watermark
        rotated_txt = txt_layer.rotate(45, expand=1)

        # Composite rotated watermark with base image
        new_background = Image.new("RGBA", rotated_txt.size)

        offset_x = (rotated_txt.width - base.width) // 2
        offset_y = (rotated_txt.height - base.height) // 2

        new_background.paste(base, (offset_x, offset_y), base)

        combined = Image.alpha_composite(new_background, rotated_txt)

        # Crop back to original image size
        final_cropped = combined.crop((offset_x, offset_y, offset_x + base.width, offset_y + base.height))

        self.image = final_cropped
        self.display_image(self.image)
        self.save_btn.config(state=tk.NORMAL)

    # Function to save the watermarked image
    def save_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image to save.")

            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])

        if file_path:
            self.image.convert("RGB").save(file_path)

            messagebox.showinfo("Saved", f"Image saved to {file_path}")

# Function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)

    root.mainloop()
    