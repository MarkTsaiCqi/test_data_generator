import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 更新大小測試圖像的檔名
target_sizes = [
    (1.9 * 1024 * 1024, "image_19mb.png"),
    (2.0 * 1024 * 1024, "image_20mb.png"),
    (2.1 * 1024 * 1024, "image_21mb.png")
]

# 圖像保存目錄
output_dir = "image/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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
        img.save(filename, format='PNG', optimize=True)
        current_size = os.path.getsize(filename)
        if abs(current_size - target_size) < 1024:  # 允許 1KB 的誤差
            break
        scale_factor = (target_size / current_size) ** 0.5
        width = int(width * scale_factor)
        height = int(height * scale_factor)
        img = img.resize((width, height))
    else:
        print(f"Failed to generate {filename} with exact size. Final size: {current_size / (1024 * 1024):.2f} MB")

# 生成圖像
for size, filename in target_sizes:
    text = filename.split('_')[1].replace('mb', ' MB')
    text = text.replace('19 MB', '1.9 MB').replace('20 MB', '2.0 MB').replace('21 MB', '2.1 MB')
    generate_image(size, os.path.join(output_dir, filename), text)
    print(f"Generated {filename} with size {os.path.getsize(os.path.join(output_dir, filename)) / (1024 * 1024):.2f} MB") 