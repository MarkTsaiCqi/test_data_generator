# 測試資料產生器

這是一個用於產生測試資料的 Python 工具集，可以產生各種格式的測試檔案，包括圖片、音訊和文字。

## 功能特點

- 圖片產生
  - 隨機顏色圖片
  - 漸層圖片
  - 支援多種格式（PNG、JPEG、BMP 等）

- 音訊產生
  - 正弦波音訊
  - 白噪音
  - 支援 WAV 格式

- 文字產生
  - 隨機文章
  - 姓名列表
  - 地址列表
  - 支援多種語言

## 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方法

1. 產生所有測試資料：
```bash
python main.py
```

2. 單獨產生某種類型的測試資料：
```bash
# 產生圖片
python image/generator.py

# 產生音訊
python audio/generator.py

# 產生文字
python text/generator.py
```

## 輸出目錄

產生的測試檔案將保存在以下目錄中：
- 圖片：`generated_images/`
- 音訊：`generated_audio/`
- 文字：`generated_text/`

## 注意事項

- 產生的測試資料僅供測試使用
- 音訊產生需要安裝額外的系統依賴（如 ffmpeg）
- 文字產生支援多種語言，可以透過修改 Faker 的 locale 參數來切換
