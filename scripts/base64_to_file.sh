#!/bin/bash

# 检查是否提供了文件路径
if [ -z "$1" ]; then
  echo "请提供要转换的 Base64 文件路径。"
  echo "用法: $0 <base64文件路径> [输出文件名]"
  exit 1
fi

# 获取文件路径
BASE64_FILE="$1"

# 检查文件是否存在
if [ ! -f "$BASE64_FILE" ]; then
  echo "文件不存在: $BASE64_FILE"
  exit 1
fi

# 获取输出文件名
if [ -z "$2" ]; then
  # 如果没有提供输出文件名，则使用原始文件名（去掉.base64后缀）
  OUTPUT_FILE="${BASE64_FILE%.base64}"
else
  OUTPUT_FILE="$2"
fi

# 将 Base64 转换回原始文件
base64 -d "$BASE64_FILE" > "$OUTPUT_FILE"

echo "Base64 文件已转换回原始文件并保存到: $OUTPUT_FILE" 