from PIL import Image, ImageDraw
import os
import random

class BaseImageGenerator:
    def __init__(self, output_dir="generated_images"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_random_color(self):
        """Generate a random RGB color."""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def create_solid_color_image(self, width=800, height=600):
        """Create a solid color image."""
        image = Image.new('RGB', (width, height), self.generate_random_color())
        return image
    
    def create_gradient_image(self, width=800, height=600):
        """Create a gradient image."""
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # Generate two random colors for the gradient
        color1 = self.generate_random_color()
        color2 = self.generate_random_color()
        
        # Create gradient
        for y in range(height):
            for x in range(width):
                # Calculate the interpolation factor
                factor = y / height
                # Interpolate between the two colors
                r = int(color1[0] * (1 - factor) + color2[0] * factor)
                g = int(color1[1] * (1 - factor) + color2[1] * factor)
                b = int(color1[2] * (1 - factor) + color2[2] * factor)
                draw.point((x, y), fill=(r, g, b))
        
        return image
    
    def create_checkerboard_image(self, width=800, height=600, tile_size=50):
        """Create a checkerboard pattern image."""
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # Generate two random colors for the checkerboard
        color1 = self.generate_random_color()
        color2 = self.generate_random_color()
        
        # Create checkerboard pattern
        for y in range(0, height, tile_size):
            for x in range(0, width, tile_size):
                color = color1 if (x // tile_size + y // tile_size) % 2 == 0 else color2
                draw.rectangle([x, y, x + tile_size, y + tile_size], fill=color)
        
        return image
    
    def save_image(self, image, filename):
        """Save the image to the output directory."""
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath)
        return filepath 