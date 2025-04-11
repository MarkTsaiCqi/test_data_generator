import random
import json
from datetime import datetime, timedelta

class PersonalDataGenerator:
    def __init__(self, output_dir="generated_data"):
        self.output_dir = output_dir

    def generate_phone_number(self, region="tw"):
        """生成隨機電話號碼"""
        if region == "tw":
            # 台灣手機號碼格式：09XX-XXX-XXX
            prefix = "09"
            middle = str(random.randint(1000, 9999))[1:]
            end = str(random.randint(1000, 9999))
            return f"{prefix}{middle}-{end[:3]}-{end[3:]}"
        elif region == "cn":
            # 中國手機號碼格式：1XX-XXXX-XXXX
            prefix = "1" + str(random.randint(30, 99))
            middle = str(random.randint(1000, 9999))
            end = str(random.randint(1000, 9999))
            return f"{prefix}-{middle}-{end}"
        elif region == "uk":
            # 英國手機號碼格式：+44 7XXX XXX XXX
            prefix = "7" + str(random.randint(100, 999))
            middle = str(random.randint(100, 999))
            end = str(random.randint(100, 999))
            return f"+44 {prefix} {middle} {end}"
        elif region == "us":
            # 美國手機號碼格式：(XXX) XXX-XXXX
            area = str(random.randint(200, 999))
            prefix = str(random.randint(200, 999))
            line = str(random.randint(1000, 9999))
            return f"({area}) {prefix}-{line}"
        elif region == "jp":
            # 日本手機號碼格式：090-XXXX-XXXX
            prefix = "090"
            middle = str(random.randint(1000, 9999))
            end = str(random.randint(1000, 9999))
            return f"{prefix}-{middle}-{end}"

    def generate_address(self, region="tw"):
        """生成隨機地址"""
        if region == "tw":
            cities = ["台北市", "新北市", "台中市", "高雄市", "台南市", "桃園市"]
            districts = {
                "台北市": ["中正區", "大安區", "信義區", "中山區", "松山區"],
                "新北市": ["板橋區", "中和區", "永和區", "新莊區", "三重區"],
                "台中市": ["西屯區", "北屯區", "南屯區", "中區", "東區"],
                "高雄市": ["前金區", "苓雅區", "新興區", "鹽埕區", "鼓山區"],
                "台南市": ["中西區", "東區", "南區", "北區", "安平區"],
                "桃園市": ["桃園區", "中壢區", "平鎮區", "八德區", "蘆竹區"]
            }
            
            city = random.choice(cities)
            district = random.choice(districts[city])
            street = random.choice(["路", "街", "大道", "巷"])
            number = random.randint(1, 999)
            floor = random.randint(1, 20)
            room = random.randint(1, 10)
            
            return f"{city}{district}{number}{street}{floor}樓{room}號"
        
        elif region == "cn":
            districts = ["東城區", "西城區", "朝陽區", "海淀區", "豐台區"]
            streets = ["東長安街", "西長安街", "建國路", "復興路", "朝陽路"]
            
            district = random.choice(districts)
            street = random.choice(streets)
            number = random.randint(1, 999)
            building = random.randint(1, 20)
            room = random.randint(1, 10)
            
            return f"北京市{district}{street}{number}號{building}棟{room}室"
        
        elif region == "uk":
            streets = ["Oxford Street", "Regent Street", "Bond Street", "Piccadilly", "Baker Street"]
            types = ["St", "Rd", "Ave", "Lane", "Square"]
            
            street = random.choice(streets)
            number = random.randint(1, 999)
            postcode = f"W{random.randint(1,9)}{random.randint(1,9)} {random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}"
            
            return f"{number} {street}, London, {postcode}, UK"
        
        elif region == "us":
            streets = ["5th Avenue", "Broadway", "Wall Street", "Madison Avenue", "Park Avenue"]
            types = ["St", "Ave", "Blvd", "Dr", "Ln"]
            
            street = random.choice(streets)
            number = random.randint(1, 999)
            zipcode = f"{random.randint(10001, 10292)}"
            
            return f"{number} {street}, New York, NY {zipcode}, USA"
        
        elif region == "jp":
            wards = ["中京區", "下京區", "東山區", "北區", "左京區"]
            streets = ["四條通", "五條通", "河原町通", "烏丸通", "堀川通"]
            
            ward = random.choice(wards)
            street = random.choice(streets)
            number = random.randint(1, 999)
            building = random.randint(1, 20)
            room = random.randint(1, 10)
            
            return f"京都府京都市{ward}{street}{number}番地{building}號{room}室"

    def generate_credit_card(self):
        """生成隨機信用卡號（僅用於測試）"""
        # 生成 16 位信用卡號
        card_number = "4"  # Visa 卡開頭
        for _ in range(15):
            card_number += str(random.randint(0, 9))
        
        # 生成到期日（未來 1-5 年）
        expiry_date = datetime.now() + timedelta(days=random.randint(365, 1825))
        expiry = expiry_date.strftime("%m/%y")
        
        # 生成 CVV
        cvv = str(random.randint(100, 999))
        
        return {
            "number": card_number,
            "expiry": expiry,
            "cvv": cvv
        }

    def generate_personal_data(self, region="tw"):
        """生成完整的個人資料"""
        return {
            "region": region,
            "phone": self.generate_phone_number(region),
            "address": self.generate_address(region),
            "credit_card": self.generate_credit_card()
        }

    def generate_all(self):
        """生成所有地區的個人資料並保存"""
        regions = [
            ("tw", "台灣"),
            ("cn", "中國北京"),
            ("uk", "英國倫敦"),
            ("us", "美國紐約"),
            ("jp", "日本京都")
        ]
        
        all_data = {}
        txt_content = ""
        
        for region_code, region_name in regions:
            data = self.generate_personal_data(region_code)
            all_data[region_code] = data
            
            txt_content += f"\n=== {region_name} ===\n"
            txt_content += f"電話號碼：{data['phone']}\n"
            txt_content += f"地址：{data['address']}\n"
            txt_content += f"信用卡號：{data['credit_card']['number']}\n"
            txt_content += f"到期日：{data['credit_card']['expiry']}\n"
            txt_content += f"CVV：{data['credit_card']['cvv']}\n"
        
        # 保存為 JSON
        with open(f"{self.output_dir}/personal_data.json", "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        # 保存為 TXT
        with open(f"{self.output_dir}/personal_data.txt", "w", encoding="utf-8") as f:
            f.write(txt_content.strip())

if __name__ == "__main__":
    generator = PersonalDataGenerator()
    generator.generate_all() 