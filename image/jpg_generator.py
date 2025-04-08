from base_generator import BaseImageGenerator

class JPGGenerator(BaseImageGenerator):
    def generate_test_images(self):
        """Generate various test JPG images."""
        print("Generating JPG test images...")
        
        # Generate solid color image
        solid_image = self.create_solid_color_image()
        solid_path = self.save_image(solid_image, "solid_color.jpg")
        print(f"Solid color image saved to: {solid_path}")
        
        # Generate gradient image
        gradient_image = self.create_gradient_image()
        gradient_path = self.save_image(gradient_image, "gradient.jpg")
        print(f"Gradient image saved to: {gradient_path}")
        
        # Generate checkerboard image
        checkerboard_image = self.create_checkerboard_image()
        checkerboard_path = self.save_image(checkerboard_image, "checkerboard.jpg")
        print(f"Checkerboard image saved to: {checkerboard_path}")

def main():
    generator = JPGGenerator()
    generator.generate_test_images()

if __name__ == "__main__":
    main() 