import random
import string
import os
import requests
from faker import Faker
from typing import List

class TextGenerator:
    def __init__(self, output_dir="generated_text"):
        # Define all special characters and patterns
        self.special_chars = [
            # SQL Injection - Single quote tests
            "'",
            "''",
            '" OR 1=1 --',
            "' OR '1'='1",
            '" OR "1"="1"',
            "' OR 1=1; --",
            "' OR 'a'='a",
            "') OR ('a'='a",
            "') OR '1'='1' --",
            
            # SQL Injection - Destructive queries
            "' OR 1=1; DROP TABLE users; --",
            '" OR 1=1; UPDATE users SET password=\'hacked\' WHERE username=\'admin\'; --',
            "'; DELETE FROM users WHERE 1=1; --",
            
            # SQL Injection - UNION-based
            "' UNION SELECT 1,2,3,4,5 --",
            '" UNION SELECT username, password FROM users --',
            "' UNION SELECT null, null, version(), user() --",
            
            # XSS tests
            "<script>alert('XSS!')</script>",
            '"><script>alert(\'XSS\')</script>',
            '<img src="x" onerror="alert(\'XSS\')">',
            '<a href="javascript:alert(\'XSS\')">Click Me</a>',
            '<svg onload=alert(\'XSS\')>',
            
            # Command Injection tests
            "; ls -la",
            "; rm -rf /",
            "; cat /etc/passwd",
            "`whoami`",
            "$(id)",
            "| echo HACKED",
            
            # Basic special characters
            "!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`",
            
            # Special Unicode characters
            "你好世界",
            "👋🌍",
            
            # Control characters
            "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F",
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

    def save_to_file(self, content: str, filename: str) -> str:
        """Save content to a file and return the file path."""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath

    def generate_special_chars(self) -> str:
        """Generate a string containing all special characters and alphanumeric characters."""
        # Combine all special characters and injection patterns
        result = []
        
        # Add basic special characters
        result.append("John_Doe!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        # Add SQL Injection patterns
        result.append("\n\nSQL Injection 測試：")
        result.append("' OR '1'='1")
        result.append("' OR 1=1; --")
        result.append("'; DROP TABLE users; --")
        result.append("' UNION SELECT * FROM users; --")
        result.append("' OR 1=1; UPDATE users SET password='hacked' WHERE username='admin'; --")
        result.append("' OR 'a'='a")
        result.append("') OR ('a'='a")
        result.append("') OR '1'='1' --")
        result.append("' UNION SELECT 1,2,3,4,5 --")
        result.append("' UNION SELECT username, password FROM users --")
        result.append("' UNION SELECT null, null, version(), user() --")
        
        # Add XSS patterns
        result.append("\n\nXSS 測試：")
        result.append("<script>alert('XSS!')</script>")
        result.append('"><script>alert(\'XSS\')</script>')
        result.append('<img src="x" onerror="alert(\'XSS\')">')
        result.append('<a href="javascript:alert(\'XSS\')">Click Me</a>')
        result.append('<svg onload=alert(\'XSS\')>')
        
        # Add Command Injection patterns
        result.append("\n\nCommand Injection 測試：")
        result.append("; ls -la")
        result.append("; rm -rf /")
        result.append("; cat /etc/passwd")
        result.append("`whoami`")
        result.append("$(id)")
        result.append("| echo HACKED")
        
        # Add Unicode characters
        result.append("\n\nUnicode 字元：")
        result.append("你好世界")
        result.append("👋🌍")
        
        return "\n".join(result)

    def get_random_fact(self) -> str:
        """Get a random fact from the useless facts API."""
        try:
            response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random', timeout=5)
            response.raise_for_status()
            data = response.json()
            return data.get('text', '')
        except Exception as e:
            print(f"Error fetching random fact: {str(e)}")
            return self.faker.text(max_nb_chars=100)  # Fallback to faker if API fails

    def generate_50_char_text(self) -> str:
        """Generate a meaningful English text using random facts API."""
        return self.get_random_fact()

    def generate_5000_char_article(self) -> str:
        """Generate a meaningful 5000-character English article using faker."""
        # Generate multiple paragraphs until we reach 5000 characters
        paragraphs = []
        total_length = 0
        
        while total_length < 5000:
            # Generate a paragraph with a random number of sentences
            paragraph = self.faker.paragraph(nb_sentences=random.randint(3, 8))
            paragraphs.append(paragraph)
            total_length += len(paragraph) + 2  # +2 for newlines
        
        # Join paragraphs with double newlines
        text = "\n\n".join(paragraphs)
        
        # Trim to exactly 5000 characters
        return text[:5000]

def main():
    generator = TextGenerator()
    
    # Generate all content
    print("Generating test content...")
    
    # Create content with descriptions
    content = """# 測試資料產生器輸出

## 1. 特殊字元測試字串
用途：用於測試 SQL Injection、XSS、跳脫字元等安全性問題
內容：
{}

## 2. 50字元英文文字
用途：用於測試短文字輸入欄位
內容：
{}

## 3. 5000字元英文文章
用途：用於測試長文字輸入欄位
內容：
{}
""".format(
        generator.generate_special_chars(),
        generator.generate_50_char_text(),
        generator.generate_5000_char_article()
    )
    
    # Save to file
    filepath = generator.save_to_file(content, "test_data.txt")
    print(f"所有測試資料已儲存至: {filepath}")

if __name__ == "__main__":
    main() 