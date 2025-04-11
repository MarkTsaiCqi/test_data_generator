# Shell 腳本使用說明

本文檔詳細說明了項目中所有 shell 腳本的使用方法和功能。

## 目錄
- [圖片生成腳本](#圖片生成腳本)
- [音頻生成腳本](#音頻生成腳本)
- [文本生成腳本](#文本生成腳本)
- [文件生成腳本](#文件生成腳本)
- [大文件生成腳本](#大文件生成腳本)
- [無效文件生成腳本](#無效文件生成腳本)
- [Base64 轉換腳本](#base64-轉換腳本)
- [個人資料生成腳本](#個人資料生成腳本)

## 圖片生成腳本

### generate_test_images.sh
生成各種類型的圖片文件。

**使用方法：**
```bash
./generate_test_images.sh
```

**生成文件：**
- 隨機圖片：`random_800x600.png`
- 漸變圖片：`gradient_800x600.png`
- 純色圖片：`solid_800x600.png`
- 棋盤格圖片：`checkerboard_800x600.png`
- 動畫：`animation_800x600.gif`

### generate_test_bigImages.sh
生成大尺寸的測試圖片。

**使用方法：**
```bash
./generate_test_bigImages.sh
```

**生成文件：**
- 1920x1080 隨機圖片：`random_1920x1080.png`
- 4000x3000 隨機圖片：`random_4000x3000.png`

### generate_test_smallImages.sh
生成小尺寸的測試圖片。

**使用方法：**
```bash
./generate_test_smallImages.sh
```

**生成文件：**
- 100KB 圖片：`100kb.jpg`
- 200KB 圖片：`200kb.jpg`
- 500KB 圖片：`500kb.jpg`
- 1MB 圖片：`1mb.jpg`

## 音頻生成腳本

### generate_test_audio.sh
生成各種類型的音頻文件。

**使用方法：**
```bash
./generate_test_audio.sh
```

**生成文件：**
- 光劍音效：`lightsaber.wav`、`lightsaber.mp3`、`lightsaber.flac`
- 白噪音：`white_noise.mp3`
- 正弦波：`sine_220hz.mp3`、`sine_440hz.mp3`、`sine_880hz.mp3`
- MIDI：`test_midi.mid`

### generate_test_bigAudio.sh
生成大尺寸的音頻文件。

**使用方法：**
```bash
./generate_test_bigAudio.sh
```

**生成文件：**
- 24MB 音頻：`24mb.mp3`
- 25MB 音頻：`25mb.mp3`
- 26MB 音頻：`26mb.mp3`

## 文本生成腳本

### generate_test_text.sh
生成各種類型的文本文件。

**使用方法：**
```bash
./generate_test_text.sh
```

**生成文件：**
- 純文本：`test_text_all.txt`
- 測試數據：`test_data.txt`、`test_data.json`、`test_data.md`、`test_data.csv`、`test_data.xml`

## 文件生成腳本

### generate_test_files.sh
生成各種類型的文件。

**使用方法：**
```bash
./generate_test_files.sh
```

**生成文件：**
- 文檔：`test_data.xlsx`、`test_data.docx`、`test_data.pdf`

## 大文件生成腳本

### generate_test_bigFiles.sh
生成大尺寸的測試文件。

**使用方法：**
```bash
./generate_test_bigFiles.sh
```

**生成文件：**
- 24MB 文件：`24mb.bin`
- 25MB 文件：`25mb.bin`
- 26MB 文件：`26mb.bin`

## 無效文件生成腳本

### generate_test_notSupport.sh
生成無效的測試文件。

**使用方法：**
```bash
./generate_test_notSupport.sh
```

**生成文件：**
- 執行檔：`test_file.exe`、`test_file.bat`、`test_file.apk`、`test_file.dll`
- 影片檔：`test_file.mp4`、`test_file.mov`、`test_file.avi`、`test_file.mkv`

## Base64 轉換腳本

### scripts/base64_to_file.sh
將 Base64 編碼的字符串轉換為文件。支持所有類型的文件。

**使用方法：**
```bash
./scripts/base64_to_file.sh <base64_string> <output_file>
```

**參數說明：**
- `base64_string`：Base64 編碼的字符串
- `output_file`：輸出文件名（可以指定任何擴展名）

**示例：**
```bash
# 轉換為文本文件
./scripts/base64_to_file.sh "SGVsbG8gV29ybGQ=" hello.txt

# 轉換為圖片
./scripts/base64_to_file.sh "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==" image.png

# 轉換為音頻
./scripts/base64_to_file.sh "SUQzBAAAAAAAI1RTU0UAAAALAAAT..." audio.mp3
```

### scripts/file_to_base64.sh
將任何類型的文件轉換為 Base64 編碼的字符串。

**使用方法：**
```bash
./scripts/file_to_base64.sh <input_file>
```

**參數說明：**
- `input_file`：輸入文件名（支持任何類型的文件）

**示例：**
```bash
# 轉換文本文件
./scripts/file_to_base64.sh hello.txt

# 轉換圖片
./scripts/file_to_base64.sh image.png

# 轉換音頻
./scripts/file_to_base64.sh audio.mp3
```

## 個人資料生成腳本

### generate_test_personal_data.sh
生成測試用的個人資料。

**使用方法：**
```bash
./generate_test_personal_data.sh
```

**生成文件：**
- JSON 格式：`personal_data.json`
- 文本格式：`personal_data.txt`

**生成內容：**
- 電話號碼（台灣格式）
- 地址（包含城市、區、街道、門牌號碼）
- 信用卡資訊（卡號、到期日、CVV）

## 注意事項

1. 所有腳本都需要在虛擬環境中運行
2. 運行腳本前請確保已安裝所有依賴
3. 生成的文件將保存在 `generated_data` 目錄下
4. 部分腳本需要較長時間執行，請耐心等待
5. Base64 轉換腳本位於 `scripts` 目錄下，使用時請注意路徑 