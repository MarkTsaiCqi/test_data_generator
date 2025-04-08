from base_generator import BaseImageGenerator

class WEBPGenerator(BaseImageGenerator):
    def generate_test_images(self):
        """Generate various test WEBP images."""
        print("Generating WEBP test images...")
        
        # Generate solid color image
        solid_image = self.create_solid_color_image()
        solid_path = self.save_image(solid_image, "solid_color.webp")
        print(f"Solid color image saved to: {solid_path}")
        
        # Generate gradient image
        gradient_image = self.create_gradient_image()
        gradient_path = self.save_image(gradient_image, "gradient.webp")
        print(f"Gradient image saved to: {gradient_path}")
        
        # Generate checkerboard image
        checkerboard_image = self.create_checkerboard_image()
        checkerboard_path = self.save_image(checkerboard_image, "checkerboard.webp")
        print(f"Checkerboard image saved to: {checkerboard_path}")

def main():
    generator = WEBPGenerator()
    generator.generate_test_images()

if __name__ == "__main__":
    main() 