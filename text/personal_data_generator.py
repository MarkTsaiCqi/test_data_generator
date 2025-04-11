import random
import json
from datetime import datetime, timedelta

class PersonalDataGenerator:
    def __init__(self, output_dir="generated_data"):
        self.output_dir = output_dir
        self.interests = {
            "tw": ["登山", "單車", "攝影", "咖啡", "手作", "閱讀", "電影", "音樂", "旅行", "美食"],
            "cn": ["書法", "太極", "圍棋", "茶道", "國畫", "京劇", "太極拳", "象棋", "剪紙", "園藝"],
            "uk": ["足球", "板球", "網球", "高爾夫", "閱讀", "園藝", "攝影", "騎馬", "划船", "品酒"],
            "us": ["棒球", "籃球", "美式足球", "衝浪", "露營", "攝影", "音樂", "電影", "健身", "烹飪"],
            "jp": ["茶道", "花道", "書道", "劍道", "弓道", "和服", "動漫", "遊戲", "攝影", "旅行"]
        }
        self.companies = {
            "tw": ["科技公司", "金融機構", "製造業", "服務業", "教育機構", "醫療機構", "媒體公司", "零售業", "餐飲業", "建築業"],
            "cn": ["科技公司", "國有企業", "金融機構", "製造業", "教育機構", "醫療機構", "媒體公司", "零售業", "餐飲業", "建築業"],
            "uk": ["Technology Company", "Financial Institution", "Manufacturing", "Service Industry", "Education", "Healthcare", "Media Company", "Retail", "Hospitality", "Construction"],
            "us": ["Tech Company", "Financial Institution", "Manufacturing", "Service Industry", "Education", "Healthcare", "Media Company", "Retail", "Hospitality", "Construction"],
            "jp": ["テクノロジー企業", "金融機関", "製造業", "サービス業", "教育機関", "医療機関", "メディア企業", "小売業", "飲食業", "建設業"]
        }
        self.positions = {
            "tw": ["工程師", "經理", "專員", "顧問", "主任", "助理", "主管", "總監", "副總", "總經理"],
            "cn": ["工程师", "经理", "专员", "顾问", "主任", "助理", "主管", "总监", "副总", "总经理"],
            "uk": ["Engineer", "Manager", "Specialist", "Consultant", "Director", "Assistant", "Supervisor", "Head", "VP", "CEO"],
            "us": ["Engineer", "Manager", "Specialist", "Consultant", "Director", "Assistant", "Supervisor", "Head", "VP", "CEO"],
            "jp": ["エンジニア", "マネージャー", "スペシャリスト", "コンサルタント", "ディレクター", "アシスタント", "スーパーバイザー", "ヘッド", "VP", "CEO"]
        }
        self.email_domains = {
            "tw": ["gmail.com", "yahoo.com.tw", "hotmail.com", "msn.com", "pchome.com.tw"],
            "cn": ["163.com", "qq.com", "126.com", "sina.com", "sohu.com"],
            "uk": ["gmail.com", "yahoo.co.uk", "hotmail.co.uk", "outlook.com", "btinternet.com"],
            "us": ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"],
            "jp": ["gmail.com", "yahoo.co.jp", "hotmail.co.jp", "outlook.jp", "docomo.ne.jp"]
        }

    def generate_email(self, region="tw"):
        """生成隨機電子郵件地址"""
        first_names = {
            "tw": ["陳", "林", "黃", "張", "李", "王", "吳", "劉", "蔡", "楊"],
            "cn": ["王", "李", "張", "劉", "陳", "楊", "趙", "黃", "周", "吳"],
            "uk": ["John", "David", "Michael", "James", "Robert", "William", "Thomas", "Christopher", "Daniel", "Paul"],
            "us": ["John", "Michael", "David", "James", "Robert", "William", "Thomas", "Christopher", "Daniel", "Paul"],
            "jp": ["佐藤", "鈴木", "高橋", "田中", "伊藤", "渡邊", "山本", "中村", "小林", "加藤"]
        }
        last_names = {
            "tw": ["小明", "大華", "志明", "美玲", "雅婷", "家豪", "怡君", "建國", "淑芬", "俊傑"],
            "cn": ["小明", "大華", "志明", "美玲", "雅婷", "家豪", "怡君", "建國", "淑芬", "俊傑"],
            "uk": ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Robinson", "Wright"],
            "us": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"],
            "jp": ["一郎", "二郎", "三郎", "花子", "太郎", "次郎", "美咲", "翔太", "優子", "健太"]
        }
        
        first_name = random.choice(first_names[region])
        last_name = random.choice(last_names[region])
        number = random.randint(100, 999)
        domain = random.choice(self.email_domains[region])
        
        return f"{first_name}{last_name}{number}@{domain}"

    def generate_birthday(self, region="tw"):
        """生成隨機生日"""
        # 生成 18-65 歲之間的生日
        age = random.randint(18, 65)
        today = datetime.now()
        birth_year = today.year - age
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)  # 簡單起見，統一使用 28 天
        
        if region in ["tw", "cn"]:
            return f"{birth_year}/{birth_month:02d}/{birth_day:02d}"
        elif region in ["uk", "us"]:
            return f"{birth_month:02d}/{birth_day:02d}/{birth_year}"
        elif region == "jp":
            return f"{birth_year}年{birth_month}月{birth_day}日"

    def generate_id_number(self, region="tw"):
        """生成隨機身份證字號（僅用於測試）"""
        if region == "tw":
            # 台灣身份證字號格式：A123456789
            first_char = random.choice("ABCDEFGHJKLMNPQRSTUVXYWZIO")
            numbers = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            return f"{first_char}{numbers}"
        elif region == "cn":
            # 中國身份證字號格式：18位數字
            return ''.join([str(random.randint(0, 9)) for _ in range(18)])
        elif region == "jp":
            # 日本住民票番號格式：12位數字
            return ''.join([str(random.randint(0, 9)) for _ in range(12)])
        else:
            return None

    def generate_company_info(self, region="tw"):
        """生成公司資訊"""
        company = random.choice(self.companies[region])
        position = random.choice(self.positions[region])
        return {
            "company": company,
            "position": position
        }

    def generate_interests(self, region="tw"):
        """生成興趣愛好"""
        num_interests = random.randint(2, 5)
        return random.sample(self.interests[region], num_interests)

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
        company_info = self.generate_company_info(region)
        return {
            "region": region,
            "email": self.generate_email(region),
            "birthday": self.generate_birthday(region),
            "id_number": self.generate_id_number(region),
            "phone": self.generate_phone_number(region),
            "address": self.generate_address(region),
            "company": company_info["company"],
            "position": company_info["position"],
            "interests": self.generate_interests(region),
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
            txt_content += f"電子郵件：{data['email']}\n"
            txt_content += f"生日：{data['birthday']}\n"
            if data['id_number']:
                txt_content += f"身份證字號：{data['id_number']}\n"
            txt_content += f"電話號碼：{data['phone']}\n"
            txt_content += f"地址：{data['address']}\n"
            txt_content += f"公司：{data['company']}\n"
            txt_content += f"職位：{data['position']}\n"
            txt_content += f"興趣：{', '.join(data['interests'])}\n"
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