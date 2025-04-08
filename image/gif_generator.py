from base_generator import BaseImageGenerator
from PIL import Image, ImageDraw
import os

class GIFGenerator(BaseImageGenerator):
    def create_animated_gradient(self, width=800, height=600, frames=10):
        """Create an animated gradient GIF."""
        images = []
        
        for i in range(frames):
            # Create a gradient image with phase shift
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            
            # Generate two random colors for the gradient
            color1 = self.generate_random_color()
            color2 = self.generate_random_color()
            
            # Create gradient with phase shift
            for y in range(height):
                for x in range(width):
                    # Calculate the interpolation factor with phase shift
                    factor = (y / height + i / frames) % 1.0
                    # Interpolate between the two colors
                    r = int(color1[0] * (1 - factor) + color2[0] * factor)
                    g = int(color1[1] * (1 - factor) + color2[1] * factor)
                    b = int(color1[2] * (1 - factor) + color2[2] * factor)
                    draw.point((x, y), fill=(r, g, b))
            
            images.append(image)
        
        return images
    
    def create_animated_checkerboard(self, width=800, height=600, tile_size=50, frames=10):
        """Create an animated checkerboard GIF."""
        images = []
        
        for i in range(frames):
            # Create a checkerboard image with phase shift
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            
            # Generate two random colors for the checkerboard
            color1 = self.generate_random_color()
            color2 = self.generate_random_color()
            
            # Create checkerboard pattern with phase shift
            for y in range(0, height, tile_size):
                for x in range(0, width, tile_size):
                    # Add phase shift to the pattern
                    phase = (x // tile_size + y // tile_size + i) % 2
                    color = color1 if phase == 0 else color2
                    draw.rectangle([x, y, x + tile_size, y + tile_size], fill=color)
            
            images.append(image)
        
        return images
    
    def generate_test_images(self):
        """Generate various test GIF images."""
        print("Generating GIF test images...")
        
        # Generate solid color image
        solid_image = self.create_solid_color_image()
        solid_path = self.save_image(solid_image, "solid_color.gif")
        print(f"Solid color image saved to: {solid_path}")
        
        # Generate animated gradient
        gradient_images = self.create_animated_gradient()
        gradient_path = os.path.join(self.output_dir, "animated_gradient.gif")
        gradient_images[0].save(
            gradient_path,
            save_all=True,
            append_images=gradient_images[1:],
            duration=100,  # 100ms per frame
            loop=0  # Infinite loop
        )
        print(f"Animated gradient saved to: {gradient_path}")
        
        # Generate animated checkerboard
        checkerboard_images = self.create_animated_checkerboard()
        checkerboard_path = os.path.join(self.output_dir, "animated_checkerboard.gif")
        checkerboard_images[0].save(
            checkerboard_path,
            save_all=True,
            append_images=checkerboard_images[1:],
            duration=100,  # 100ms per frame
            loop=0  # Infinite loop
        )
        print(f"Animated checkerboard saved to: {checkerboard_path}")

def main():
    generator = GIFGenerator()
    generator.generate_test_images()

if __name__ == "__main__":
    main() 