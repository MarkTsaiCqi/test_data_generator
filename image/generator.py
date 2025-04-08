from PIL import Image, ImageDraw
import random
import os

class ImageGenerator:
    def __init__(self, output_dir="generated_images"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_random_image(self, width, height, format="PNG"):
        """生成随机颜色的图片"""
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # 填充随机颜色
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                ))
        
        filename = f"random_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        return filepath
    
    def generate_gradient_image(self, width, height, format="PNG"):
        """生成渐变图片"""
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # 创建渐变
        for x in range(width):
            for y in range(height):
                r = int((x / width) * 255)
                g = int((y / height) * 255)
                b = int(((x + y) / (width + height)) * 255)
                draw.point((x, y), fill=(r, g, b))
        
        filename = f"gradient_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        return filepath

if __name__ == "__main__":
    generator = ImageGenerator()
    # 生成测试图片
    generator.generate_random_image(800, 600)
    generator.generate_gradient_image(800, 600) 