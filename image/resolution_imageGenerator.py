import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 預設解析度列表
DEFAULT_RESOLUTIONS = [
    (1920, 1080),  # Full HD
    (3840, 2160),  # 4K
    (1280, 720),   # HD
    (2560, 1440),  # 2K
    (640, 480),    # VGA
]

# 解析命令列參數
parser = argparse.ArgumentParser(description='生成指定解析度的圖片')
parser.add_argument('--width', type=int, help='圖片寬度')
parser.add_argument('--height', type=int, help='圖片高度')
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
    
    try:
        # 添加解析度資訊
        text = f"{width}x{height}"
        font = ImageFont.truetype("arial", 50)
        textwidth, textheight = draw.textbbox((0, 0), text, font=font)[2:4]
        text_x = (width - textwidth) / 2
        text_y = (height - textheight) / 2
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))
    except Exception as e:
        print(f"警告：無法加載字體或繪製文字：{str(e)}")
    
    # 儲存圖片
    filename = f"resolution_{width}x{height}.png"
    output_path = os.path.join(args.output_dir, filename)
    img.save(output_path, format='PNG')
    print(f"已生成 {filename}，解析度: {width}x{height}")

if __name__ == "__main__":
    if args.width is not None and args.height is not None:
        # 如果提供了寬度和高度，只生成指定解析度的圖片
        generate_image(args.width, args.height)
    else:
        # 否則生成所有預設解析度的圖片
        for width, height in DEFAULT_RESOLUTIONS:
            generate_image(width, height) 