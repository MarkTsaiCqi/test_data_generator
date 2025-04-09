#!/bin/bash

# 检查是否提供了文件路径
if [ -z "$1" ]; then
  echo "请提供要转换的文件路径。"
  echo "用法: $0 <文件路径>"
  exit 1
fi

# 获取文件路径
FILE_PATH="$1"

# 检查文件是否存在
if [ ! -f "$FILE_PATH" ]; then
  echo "文件不存在: $FILE_PATH"
  exit 1
fi

# 生成输出文件名
OUTPUT_FILE="${FILE_PATH}.base64"

# 将文件转换为 Base64 并输出到新文件
base64 "$FILE_PATH" > "$OUTPUT_FILE"

echo "文件已转换为 Base64 并保存到: $OUTPUT_FILE"
