# -*- coding: utf-8 -*-
import random
import string
import os
import requests
from faker import Faker
from typing import List

class TextGenerator:
    def __init__(self, output_dir="generated_data"):
        # Define all special characters and patterns
        self.special_chars = [
            # SQL Injection - Single quote tests
            u"'",
            u"''",
            u'" OR 1=1 --',
            u"' OR '1'='1",
            u'" OR "1"="1"',
            u"' OR 1=1; --",
            u"' OR 'a'='a",
            u"') OR ('a'='a",
            u"') OR '1'='1' --",
            
            # SQL Injection - Destructive queries
            u"' OR 1=1; DROP TABLE users; --",
            u'" OR 1=1; UPDATE users SET password=\'hacked\' WHERE username=\'admin\'; --',
            u"'; DELETE FROM users WHERE 1=1; --",
            
            # SQL Injection - UNION-based
            u"' UNION SELECT 1,2,3,4,5 --",
            u'" UNION SELECT username, password FROM users --',
            u"' UNION SELECT null, null, version(), user() --",
            
            # Command Injection tests
            u"; ls -la",
            u"; rm -rf /",
            u"; cat /etc/passwd",
            u"`whoami`",
            u"$(id)",
            u"| echo HACKED",
            
            # Basic special characters
            u"!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`",
            
            # Special Unicode characters
            u"你好世界",
            u"👋🌍",
            
            # Control characters
            u"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F",
        ]
        
        # Common English words for generating meaningful text
        self.common_words = [
            "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
            "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
            "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
            "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
            "so", "up", "out", "if", "about", "who", "get", "which", "go", "me"
        ]

        # Initialize Faker
        self.faker = Faker()
        
        # Create output directory if it doesn't exist
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 定義文本文件路徑
        self.text_files = [
            "text/orwell_why_i_write.txt",
            "text/wallace_this_is_water.txt"
        ]

    def save_to_file(self, content: str, filename: str) -> str:
        """Save content to a file and return the file path."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8', errors='ignore') as f:
            if isinstance(content, bytes):
                content = content.decode('utf-8', errors='ignore')
            f.write(content)
        return filepath

    def read_text_file(self, filepath: str) -> List[str]:
        """讀取文本文件並返回段落列表"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # 按空行分割段落
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                return paragraphs
        except Exception as e:
            print(f"讀取文件 {filepath} 失敗: {e}")
            return []

    def generate_special_chars(self) -> str:
        """Generate a string containing all special characters and alphanumeric characters."""
        # Combine all special characters and injection patterns
        result = []
        
        # Add basic special characters
        result.append(u"John_Doe!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        # Add SQL Injection patterns
        result.append(u"\n\nSQL Injection 測試：")
        result.append(u"' OR '1'='1")
        result.append(u"' OR 1=1; --")
        result.append(u"'; DROP TABLE users; --")
        result.append(u"' UNION SELECT * FROM users; --")
        result.append(u"' OR 1=1; UPDATE users SET password='hacked' WHERE username='admin'; --")
        result.append(u"' OR 'a'='a")
        result.append(u"') OR ('a'='a")
        result.append(u"') OR '1'='1' --")
        
        # Add Command Injection patterns
        result.append(u"\n\nCommand Injection 測試：")
        result.append(u"; ls -la")
        result.append(u"; rm -rf /")
        result.append(u"; cat /etc/passwd")
        result.append(u"`whoami`")
        result.append(u"$(id)")
        result.append(u"| echo HACKED")
        
        # Add Unicode characters
        result.append(u"\n\nUnicode 測試：")
        result.append(u"你好世界")
        result.append(u"👋🌍")
        
        return u"\n".join(result)

    def get_random_fact(self) -> str:
        """Get a random fact from API."""
        try:
            response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
            if response.status_code == 200:
                return response.json()['text']
        except Exception as e:
            print(f"獲取隨機事實失敗: {e}")
        # 如果 API 失敗，使用 Faker 作為備用
        return self.faker.sentence()

    def generate_50_char_text(self) -> str:
        """Generate text using random facts API."""
        fact = self.get_random_fact()
        # 如果事實太短，添加一些特殊字符
        if len(fact) < 50:
            fact += " " + random.choice(self.special_chars)
        return fact

    def generate_5000_char_article(self) -> str:
        """Generate a 5000-character article using random text files."""
        # 隨機選擇一個文本文件
        filepath = random.choice(self.text_files)
        paragraphs = self.read_text_file(filepath)
        
        if not paragraphs:
            return "無法生成文章：文本文件讀取失敗"
            
        # 隨機選擇起始段落
        start_idx = random.randint(0, len(paragraphs) - 1)
        
        article = []
        current_length = 0
        
        # 從起始段落開始，逐段添加直到達到5000字符
        for i in range(start_idx, len(paragraphs)):
            paragraph = paragraphs[i]
            if current_length + len(paragraph) > 5000:
                break
            article.append(paragraph)
            current_length += len(paragraph)
            
        # 如果還沒達到5000字符，從頭開始繼續添加
        if current_length < 5000:
            for i in range(0, start_idx):
                paragraph = paragraphs[i]
                if current_length + len(paragraph) > 5000:
                    break
                article.append(paragraph)
                current_length += len(paragraph)
        
        return "\n\n".join(article)

def main():
    generator = TextGenerator()
    
    # 生成所有文本內容
    content_parts = []
    
    # 添加特殊字符測試部分
    content_parts.append(u"=== 特殊字符測試 ===")
    content_parts.append(generator.generate_special_chars())
    content_parts.append(u"\n")
    
    # 添加50字符文本部分
    content_parts.append(u"=== 50字符文本 ===")
    content_parts.append(generator.generate_50_char_text())
    content_parts.append(u"\n")
    
    # 添加5000字符文章部分
    content_parts.append(u"=== 5000字符文章 ===")
    content_parts.append(generator.generate_5000_char_article())
    
    # 合併所有內容並保存到一個文件
    all_content = u"\n".join(content_parts)
    generator.save_to_file(all_content, "test_text_all.txt")

if __name__ == "__main__":
    main() 