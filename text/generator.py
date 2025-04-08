from faker import Faker
import os

class TextGenerator:
    def __init__(self, output_dir="generated_text"):
        self.output_dir = output_dir
        self.faker = Faker()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_random_text(self, num_paragraphs=3):
        """生成随机文本"""
        return self.faker.text(max_nb_chars=2000) * num_paragraphs
    
    def generate_name_list(self, count=10):
        """生成随机姓名列表"""
        return [self.faker.name() for _ in range(count)]
    
    def generate_address_list(self, count=10):
        """生成随机地址列表"""
        return [self.faker.address() for _ in range(count)]
    
    def save_text(self, content, filename):
        """保存文本到文件"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return filepath

if __name__ == "__main__":
    generator = TextGenerator()
    
    # 生成测试文本
    # 1. 生成随机文章
    text = generator.generate_random_text(5)
    generator.save_text(text, "random_article.txt")
    
    # 2. 生成姓名列表
    names = "\n".join(generator.generate_name_list(20))
    generator.save_text(names, "name_list.txt")
    
    # 3. 生成地址列表
    addresses = "\n".join(generator.generate_address_list(20))
    generator.save_text(addresses, "address_list.txt") 