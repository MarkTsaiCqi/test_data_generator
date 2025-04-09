import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 解析命令列參數
parser = argparse.ArgumentParser(description='生成指定解析度的圖片')
parser.add_argument('--width', type=int, required=True, help='圖片寬度')
parser.add_argument('--height', type=int, required=True, help='圖片高度')
parser.add_argument('--output-dir', default='generated_data', help='輸出目錄')
args = parser.parse_args()

# 確保輸出目錄存在
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# 生成隨機圖片
def generate_image(width, height):
    # 創建隨機圖像數據
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # 創建圖像
    img = Image.fromarray(data, 'RGB')
    draw = ImageDraw.Draw(img)
    
    # 添加解析度資訊
    text = f"{width}x{height}"
    font = ImageFont.truetype("arial", 50)
    textwidth, textheight = draw.textbbox((0, 0), text, font=font)[2:4]
    text_x = (width - textwidth) / 2
    text_y = (height - textheight) / 2
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))
    
    # 儲存圖片
    filename = f"resolution_{width}x{height}.png"
    output_path = os.path.join(args.output_dir, filename)
    img.save(output_path, format='PNG')
    print(f"已生成 {filename}，解析度: {width}x{height}")

if __name__ == "__main__":
    generate_image(args.width, args.height) 