#!/bin/bash

# 定义输出目录
OUTPUT_DIR="generated_data"
TEXT_DIR="$OUTPUT_DIR/text"
IMAGE_DIR="$OUTPUT_DIR/image"

# 创建输出目录
mkdir -p "$TEXT_DIR"
mkdir -p "$IMAGE_DIR"

# 定义文本大小 (KB)
TEXT_SIZES=(1 10 100 1024) # 1KB, 10KB, 100KB, 1MB

# 定义图片大小 (MB)
IMAGE_SIZES=(1 10 20) # 1MB, 10MB, 20MB

# 函数：生成指定大小的文本文件
generate_text() {
    local size_kb=$1
    local filename="$TEXT_DIR/text_${size_kb}kb.txt"
    local target_bytes=$((size_kb * 1024))

    echo "正在生成 $filename..."
    # 使用 head 和 /dev/urandom 生成随机数据，稍微多一点以确保足够
    head -c $((target_bytes + 1024)) /dev/urandom | base64 | head -c $target_bytes > "$filename"
    echo "已生成 $filename ($(du -h "$filename" | cut -f1))"
}

# 函数：生成指定大小的图片文件 (调用 Python 脚本)
generate_image() {
    local size_mb=$1
    local filename_base="image_${size_mb}mb"
    local target_bytes=$((size_mb * 1024 * 1024))
    local script_path="image/big_imageGenerator.py" # 假设脚本在 image 目录下

    echo "正在生成 ${filename_base}.png... (目标大小: ${size_mb}MB)"
    # 调用 Python 脚本生成图片，传递目标大小和基础文件名
    if python3 "$script_path" --target_size $target_bytes --filename "$IMAGE_DIR/$filename_base"; then
        # Python 脚本应该自己处理命名和报告大小
        echo "调用 Python 脚本完成 (可能需要检查脚本输出以确认大小)"
    else
        echo "错误：调用 Python 脚本失败 $script_path"
    fi
}


# --- 主程序 --- #

echo "开始生成测试数据..."

# 生成文本文件
echo "--- 生成文本文件 ---"
for size in "${TEXT_SIZES[@]}"; do
    generate_text $size
done

# 生成图片文件
echo "--- 生成图片文件 ---"
if [ -f "image/big_imageGenerator.py" ]; then
    # 准备 Python 脚本所需的参数 (示例)
    # 注意：big_imageGenerator.py 现在可能需要不同的参数格式
    # 这里假设它接受 --target_size (bytes) 和 --filename (包含路径和基础名)
    # 并且它会自己添加 .png 和处理嵌入文本
    # 我们需要修改 big_imageGenerator.py 以适应这种调用方式或修改此处的调用

    # 示例调用，假设脚本已修改或适配
    # 实际调用需要根据 big_imageGenerator.py 的最终接口调整
    # generate_image 1  # 生成 1MB 图片
    # generate_image 10 # 生成 10MB 图片
    # generate_image 20 # 生成 20MB 图片

    # --- 替代方案：直接运行 Python 脚本一次性生成所有图片 --- #
    echo "调用 image/big_imageGenerator.py 生成所有预设图片..."
    if python3 image/big_imageGenerator.py; then
         echo "Python 脚本执行完毕。"
    else
         echo "错误：执行 image/big_imageGenerator.py 失败。"
    fi

else
    echo "警告：未找到 image/big_imageGenerator.py，跳过图片生成。"
fi

echo "--- 测试数据生成完毕 ---" 