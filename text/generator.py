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
        result.append("\n\nUnicode 測試：")
        result.append("你好世界")
        result.append("👋🌍")
        
        return "\n".join(result)

    def get_random_fact(self) -> str:
        """Get a random fact from Faker."""
        return self.faker.sentence()

    def generate_50_char_text(self) -> str:
        """Generate a 50-character text with special characters."""
        text = ""
        for _ in range(50):
            if random.random() < 0.3:  # 30% chance of special character
                text += random.choice(self.special_chars)
            else:
                text += random.choice(string.ascii_letters + string.digits)
        return text

    def generate_5000_char_article(self) -> str:
        """Generate a 5000-character article with special characters."""
        article = []
        while len("".join(article)) < 5000:
            if random.random() < 0.1:  # 10% chance of special character
                article.append(random.choice(self.special_chars))
            else:
                if random.random() < 0.7:  # 70% chance of common word
                    article.append(random.choice(self.common_words))
                else:
                    article.append(self.get_random_fact())
            article.append(" ")
        return "".join(article)

def main():
    generator = TextGenerator()
    
    # Generate and save special characters test
    special_chars = generator.generate_special_chars()
    generator.save_to_file(special_chars, "special_chars_test.txt")
    
    # Generate and save 50-character text
    text_50 = generator.generate_50_char_text()
    generator.save_to_file(text_50, "text_50_chars.txt")
    
    # Generate and save 5000-character article
    article_5000 = generator.generate_5000_char_article()
    generator.save_to_file(article_5000, "article_5000_chars.txt")

if __name__ == "__main__":
    main() 