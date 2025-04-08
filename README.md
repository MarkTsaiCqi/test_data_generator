# 测试数据生成器

这是一个用于生成测试数据的 Python 工具集，可以生成各种格式的测试文件，包括图片、音频和文本。

## 功能特点

- 图片生成
  - 随机颜色图片
  - 渐变图片
  - 支持多种格式（PNG, JPEG, BMP 等）

- 音频生成
  - 正弦波音频
  - 白噪声
  - 支持 WAV 格式

- 文本生成
  - 随机文章
  - 姓名列表
  - 地址列表
  - 支持多种语言

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 生成所有测试数据：
```bash
python main.py
```

2. 单独生成某种类型的测试数据：
```bash
# 生成图片
python image/generator.py

# 生成音频
python audio/generator.py

# 生成文本
python text/generator.py
```

## 输出目录

生成的测试文件将保存在以下目录中：
- 图片：`generated_images/`
- 音频：`generated_audio/`
- 文本：`generated_text/`

## 注意事项

- 生成的测试数据仅供测试使用
- 音频生成需要安装额外的系统依赖（如 ffmpeg）
- 文本生成支持多种语言，可以通过修改 Faker 的 locale 参数来切换 