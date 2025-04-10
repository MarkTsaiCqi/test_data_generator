from PIL import Image, ImageDraw
import random
import os
from typing import Tuple
import numpy as np
import argparse

class ImageSizeGenerator:
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
    
    def generate_image_with_target_size(self, target_size: float, is_kb: bool = False, format: str = "JPEG") -> str:
        """生成指定大小的圖片
        
        Args:
            target_size: 目標大小
            is_kb: 是否使用 KB 作為單位（否則使用 MB）
            format: 圖片格式
        """
        unit = "KB" if is_kb else "MB"
        print(f"\n正在生成大小約為 {target_size}{unit} 的圖片...")
        
        # 計算目標字節數
        if is_kb:
            target_bytes = target_size * 1024
        else:
            target_bytes = target_size * 1024 * 1024
        
        # 計算目標像素數（考慮 JPEG 壓縮，每個像素約佔 1 字節）
        target_pixels = int(target_bytes)
        
        # 計算圖片尺寸（保持 1:1 比例，因為是頭像）
        size = int(np.sqrt(target_pixels))
        
        # 增加初始尺寸（考慮 JPEG 壓縮和額外像素）
        size = int(size * 2.0)  # 增加到 2 倍
        
        # 創建圖片
        image = Image.new('RGB', (size, size))
        draw = ImageDraw.Draw(image)
        
        # 填充隨機顏色
        total_pixels = size * size
        processed = 0
        
        for x in range(size):
            for y in range(size):
                draw.point((x, y), fill=(random.randint(0, 255), 
                                       random.randint(0, 255), 
                                       random.randint(0, 255)))
                processed += 1
                if processed % 1000 == 0:
                    self._show_progress(processed, total_pixels, "進度：")
        
        # 保存圖片
        filename = f"size_{target_size}{unit.lower()}.{format.lower()}"
        filepath = os.path.join(self.output_dir, filename)
        
        # 調整質量以達到目標大小
        quality = 95
        min_quality = 1
        max_quality = 100
        tolerance = 0.1  # 允許 0.1 單位的誤差
        
        while True:
            image.save(filepath, format, quality=quality)
            actual_size = os.path.getsize(filepath) / (1024 if is_kb else 1024 * 1024)
            
            if abs(actual_size - target_size) <= tolerance:
                break
            
            # 根據實際大小調整質量
            if actual_size > target_size:
                max_quality = quality
                quality = (quality + min_quality) // 2
            else:
                min_quality = quality
                quality = (quality + max_quality) // 2
            
            if max_quality - min_quality <= 1:
                break
        
        print(f"\n圖片已保存：{filename}")
        print(f"實際大小：{actual_size:.2f}{unit}")
        print(f"圖片尺寸：{size}x{size}")
        return filepath

def main():
    parser = argparse.ArgumentParser(description='生成指定大小的測試圖片')
    parser.add_argument('--small', action='store_true', help='生成 KB 級別的圖片（用於頭像）')
    args = parser.parse_args()
    
    generator = ImageSizeGenerator()
    
    if args.small:
        # 生成 KB 級別的圖片（用於頭像）
        generator.generate_image_with_target_size(1900, is_kb=True)  # 1900KB
        generator.generate_image_with_target_size(2048, is_kb=True)  # 2048KB
        generator.generate_image_with_target_size(2100, is_kb=True)  # 2100KB
    else:
        # 生成 MB 級別的圖片
        generator.generate_image_with_target_size(19)  # 19MB
        generator.generate_image_with_target_size(20)  # 20MB
        generator.generate_image_with_target_size(21)  # 21MB

if __name__ == "__main__":
    main() 