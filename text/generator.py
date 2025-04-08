import random
import string
import os
from typing import List

class TextGenerator:
    def __init__(self, output_dir="generated_text"):
        # Define all special characters and patterns
        self.special_chars = [
            # Basic special characters
            "!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`",
            # SQL Injection patterns
            "' OR '1'='1",
            "'; DROP TABLE users; --",
            "' UNION SELECT * FROM users; --",
            # HTML special characters
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert('xss')>",
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
        # Generate a name
        name = "John_Doe"
        
        # All special characters
        special = "!@#$%^&*()_+={}[]|\\:;\"'<>,.?/~`"
        
        # Numbers
        numbers = "1234567890"
        
        # Lowercase letters
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        
        # Uppercase letters
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # Combine all characters
        return f"{name}{special}{numbers}{lowercase}{uppercase}"

    def generate_50_char_text(self) -> str:
        """Generate a meaningful 50-character English text."""
        words = []
        current_length = 0
        
        while current_length < 50:
            word = random.choice(self.common_words)
            if current_length + len(word) + 1 <= 50:  # +1 for space
                words.append(word)
                current_length += len(word) + 1
            else:
                break
        
        return " ".join(words)

    def generate_5000_char_article(self) -> str:
        """Generate a meaningful 5000-character English article."""
        paragraphs = []
        current_length = 0
        
        while current_length < 5000:
            # Generate a paragraph
            sentences = []
            paragraph_length = 0
            
            while paragraph_length < 200:  # Average paragraph length
                sentence = []
                sentence_length = 0
                
                # Generate a sentence
                while sentence_length < 50:  # Average sentence length
                    word = random.choice(self.common_words)
                    if sentence_length + len(word) + 1 <= 50:
                        sentence.append(word)
                        sentence_length += len(word) + 1
                    else:
                        break
                
                if sentence:
                    sentence[0] = sentence[0].capitalize()
                    sentence_text = " ".join(sentence) + ". "
                    sentences.append(sentence_text)
                    paragraph_length += len(sentence_text)
            
            paragraph = "".join(sentences)
            paragraphs.append(paragraph)
            current_length += len(paragraph)
        
        return "\n\n".join(paragraphs)

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