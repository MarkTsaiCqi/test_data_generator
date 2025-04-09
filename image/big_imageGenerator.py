import os
import argparse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 解析命令列參數
parser = argparse.ArgumentParser(description='生成指定大小的圖片')
parser.add_argument('--output-dir', default='generated_data', help='輸出目錄')
args = parser.parse_args()

# 更新大小測試圖像的檔名
target_sizes = [
    (1.9 * 1024 * 1024, "size_1.9MB.png"),
    (2.0 * 1024 * 1024, "size_2.0MB.png"),
    (2.1 * 1024 * 1024, "size_2.1MB.png")
]

# 確保輸出目錄存在
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# 生成特定大小的 PNG 圖像
def generate_image(target_size, filename, text):
    # 初始圖像大小
    width, height = 1000, 1000
    
    # 創建隨機圖像數據
    data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # 創建圖像
    img = Image.fromarray(data, 'RGB')
    draw = ImageDraw.Draw(img)
    
    # 添加文字
    font = ImageFont.truetype("arial", 50)  # 使用更大的字體
    textwidth, textheight = draw.textbbox((0, 0), text, font=font)[2:4]
    text_x = (width - textwidth) / 2
    text_y = (height - textheight) / 2
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))  # 使用白色文字
    
    # 調整圖像大小直到達到目標大小
    for _ in range(100):  # 限制最大迭代次數
        output_path = os.path.join(args.output_dir, filename)
        img.save(output_path, format='PNG', optimize=True)
        current_size = os.path.getsize(output_path)
        if abs(current_size - target_size) < 1024:  # 允許 1KB 的誤差
            break
        scale_factor = (target_size / current_size) ** 0.5
        width = int(width * scale_factor)
        height = int(height * scale_factor)
        img = img.resize((width, height))
    else:
        print(f"無法生成指定大小的 {filename}。最終大小: {current_size / (1024 * 1024):.2f} MB")

# 生成圖像
for size, filename in target_sizes:
    text = filename.split('_')[1].replace('.png', '')
    generate_image(size, filename, text)
    print(f"已生成 {filename}，大小: {os.path.getsize(os.path.join(args.output_dir, filename)) / (1024 * 1024):.2f} MB") 