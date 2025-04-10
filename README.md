# 測試數據生成器

這是一個用於生成各種測試數據的 Python 工具，可以生成圖片、音頻、文本和多種格式的文件。

## 功能特點

### 圖片生成
- 隨機圖片
- 漸變圖片

### 音頻生成
- 正弦波
- 白噪聲

### 文本生成
- 特殊字符測試文本
- 50字符隨機文本
- 5000字符文章
- 隨機事實文本

### 多種格式文件生成
- JSON 文件
- TXT 文本文件
- Markdown 文件
- CSV 文件
- XML 文件
- Excel 文件（xlsx）
- Word 文檔（docx）
- PDF 文件

## 目錄結構

```
test_data_generator/
├── audio/          # 音頻生成相關代碼
├── formats/        # 多種格式文件生成相關代碼
├── image/          # 圖片生成相關代碼
├── text/           # 文本生成相關代碼
├── generated_data/ # 生成的測試數據存放目錄
├── main.py         # 主程序入口
└── README.md       # 項目說明文檔
```

## 使用方法

1. 安裝依賴：
```bash
pip install -r requirements.txt
```

2. 運行腳本：
```bash
./generate_test_files.sh
```

或者直接運行 Python 文件：
```bash
python main.py
```

生成的測試數據將保存在 `generated_data` 目錄中。

## 依賴項

- Pillow
- numpy
- soundfile
- faker
- pandas
- python-docx
- reportlab
