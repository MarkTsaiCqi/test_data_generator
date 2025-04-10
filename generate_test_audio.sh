#!/bin/bash

# 創建 generated_data 目錄（如果不存在）
mkdir -p generated_data

# 運行音頻生成器
echo "生成測試音頻..."
python3 audio/generator.py

# 將生成的音頻文件移動到 generated_data 目錄
echo "移動音頻文件到 generated_data 目錄..."
mv *.wav *.mp3 generated_data/ 2>/dev/null || true

echo "音頻生成完成！生成的音頻文件在 generated_data 目錄中。" 