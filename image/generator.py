from PIL import Image, ImageDraw
import random
import os
from typing import Tuple, Optional
import time

class ImageGenerator:
    def __init__(self, output_dir="generated_data"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def _show_progress(self, current: int, total: int, prefix: str = "", suffix: str = ""):
        """顯示進度條"""
        bar_length = 50
        filled_length = int(round(bar_length * current / float(total)))
        percents = round(100.0 * current / float(total), 1)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r{prefix} [{bar}] {percents}% {suffix}', end='')
        if current == total:
            print()
    
    def generate_random_color(self) -> Tuple[int, int, int]:
        """生成隨機 RGB 顏色"""
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def generate_random_image(self, width: int, height: int, format: str = "PNG") -> str:
        """生成隨機顏色的圖片"""
        print(f"\n正在生成隨機顏色圖片 ({width}x{height})...")
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        total_pixels = width * height
        processed = 0
        
        # 填充隨機顏色
        for x in range(width):
            for y in range(height):
                draw.point((x, y), fill=self.generate_random_color())
                processed += 1
                if processed % 1000 == 0:  # 每1000個像素更新一次進度
                    self._show_progress(processed, total_pixels, "進度：")
        
        filename = f"random_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        print(f"圖片已保存：{filename}")
        return filepath
    
    def generate_gradient_image(self, width: int, height: int, format: str = "PNG") -> str:
        """生成漸變圖片"""
        print(f"\n正在生成漸變圖片 ({width}x{height})...")
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        total_pixels = width * height
        processed = 0
        
        # 創建漸變
        for x in range(width):
            for y in range(height):
                r = int((x / width) * 255)
                g = int((y / height) * 255)
                b = int(((x + y) / (width + height)) * 255)
                draw.point((x, y), fill=(r, g, b))
                processed += 1
                if processed % 1000 == 0:
                    self._show_progress(processed, total_pixels, "進度：")
        
        filename = f"gradient_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        print(f"圖片已保存：{filename}")
        return filepath
    
    def generate_solid_color_image(self, width: int = 800, height: int = 600, format: str = "PNG") -> str:
        """生成純色圖片"""
        print(f"\n正在生成純色圖片 ({width}x{height})...")
        image = Image.new('RGB', (width, height), self.generate_random_color())
        filename = f"solid_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        print(f"圖片已保存：{filename}")
        return filepath
    
    def generate_checkerboard_image(self, width: int = 800, height: int = 600, 
                                  tile_size: int = 50, format: str = "PNG") -> str:
        """生成棋盤格圖片"""
        print(f"\n正在生成棋盤格圖片 ({width}x{height})...")
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        
        # 生成兩種隨機顏色用於棋盤格
        color1 = self.generate_random_color()
        color2 = self.generate_random_color()
        
        total_tiles = (width // tile_size) * (height // tile_size)
        processed = 0
        
        # 創建棋盤格圖案
        for y in range(0, height, tile_size):
            for x in range(0, width, tile_size):
                color = color1 if (x // tile_size + y // tile_size) % 2 == 0 else color2
                draw.rectangle([x, y, x + tile_size, y + tile_size], fill=color)
                processed += 1
                if processed % 10 == 0:  # 每10個格子更新一次進度
                    self._show_progress(processed, total_tiles, "進度：")
        
        filename = f"checkerboard_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        image.save(filepath, format)
        print(f"圖片已保存：{filename}")
        return filepath
    
    def generate_big_image(self, width: int = 4000, height: int = 3000, format: str = "PNG") -> str:
        """生成大尺寸圖片"""
        print(f"\n正在生成大尺寸圖片 ({width}x{height})...")
        return self.generate_random_image(width, height, format)
    
    def generate_resolution_image(self, width: int, height: int, format: str = "PNG") -> str:
        """生成指定分辨率的圖片"""
        print(f"\n正在生成指定分辨率圖片 ({width}x{height})...")
        return self.generate_random_image(width, height, format)
    
    def generate_gif(self, width: int = 800, height: int = 600, frames: int = 10, 
                    duration: int = 100, format: str = "GIF") -> str:
        """生成 GIF 動畫"""
        print(f"\n正在生成 GIF 動畫 ({width}x{height}, {frames}幀)...")
        images = []
        for frame in range(frames):
            print(f"\r正在生成第 {frame + 1}/{frames} 幀...", end='')
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            for x in range(width):
                for y in range(height):
                    draw.point((x, y), fill=self.generate_random_color())
            images.append(image)
        print()
        
        filename = f"animation_{width}x{height}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        images[0].save(filepath, save_all=True, append_images=images[1:], 
                      duration=duration, loop=0)
        print(f"GIF 動畫已保存：{filename}")
        return filepath

def main():
    generator = ImageGenerator()
    
    # 生成各種測試圖片
    generator.generate_random_image(800, 600)
    generator.generate_gradient_image(800, 600)
    generator.generate_solid_color_image()
    generator.generate_checkerboard_image()
    generator.generate_big_image()
    generator.generate_resolution_image(1920, 1080)
    generator.generate_gif()

if __name__ == "__main__":
    main() 