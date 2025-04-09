# 測試資料生成工具

這是一個用於生成各種測試資料的工具，包括文字、圖片和音頻檔案。

## 功能特點

- 生成不同長度的英文文字（50字元、5000字元）
- 生成包含特殊字元的文字
- 生成不同大小（1.9MB、2.0MB、2.1MB）的圖片
- 生成不同解析度（1920x1080、3840x2160、800x600）的圖片
- 支援圖片與 Base64 編碼的相互轉換
- 生成不同長度的音頻檔案（5秒、10秒、15秒）

## 安裝說明

1. 克隆此倉庫：
```bash
git clone [repository_url]
cd test_data_generator
```

2. 創建並啟動虛擬環境：
```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
source venv/bin/activate
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 使用說明

1. 確保虛擬環境已啟動（終端機提示符前應顯示 (venv)）

2. 執行主腳本：
```bash
./generate_test_data.sh
```

3. 根據選單選擇要執行的操作：
   - 1: 生成所有測試文檔和圖檔
   - 2: 生成Base64編碼的圖片
   - 3: 從Base64檔案還原圖片
   - 4: 退出

## 注意事項

- 每次打開新的終端機使用此工具時，都需要先執行 `source venv/bin/activate` 來啟動虛擬環境
- 使用完畢後，可以執行 `deactivate` 來退出虛擬環境
- 生成的檔案會保存在 `generated_data` 目錄下

## 依賴套件

- Pillow==10.2.0：用於生成圖片
- numpy==1.26.4：用於生成音頻
- pydub==0.25.1：用於音頻處理
- faker==37.1.0：用於生成文本
- python-dotenv==1.0.1
- requests==2.31.0：用於網絡請求
- beautifulsoup4==4.12.3：用於解析HTML 