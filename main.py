from image.generator import ImageGenerator
from audio.generator import AudioGenerator
from text.generator import TextGenerator
from formats.generator import FileGenerator

def generate_test_data():
    # 生成图片
    print("生成测试图片...")
    img_generator = ImageGenerator()
    img_generator.generate_random_image(800, 600)
    img_generator.generate_gradient_image(800, 600)
    
    # 生成音频
    print("生成测试音频...")
    audio_generator = AudioGenerator()
    sine_wave = audio_generator.generate_sine_wave(440, 2.0)
    audio_generator.save_audio(sine_wave, "sine_440hz.wav")
    noise = audio_generator.generate_noise(2.0)
    audio_generator.save_audio(noise, "white_noise.wav")
    
    # 生成文本
    print("生成测试文本...")
    text_generator = TextGenerator()
    text = text_generator.generate_random_text(5)
    text_generator.save_text(text, "random_article.txt")
    names = "\n".join(text_generator.generate_name_list(20))
    text_generator.save_text(names, "name_list.txt")
    addresses = "\n".join(text_generator.generate_address_list(20))
    text_generator.save_text(addresses, "address_list.txt")
    
    # 生成文件
    print("生成测试文件...")
    file_generator = FileGenerator()
    file_generator.generate_json()
    file_generator.generate_txt()
    file_generator.generate_md()
    file_generator.generate_csv()
    file_generator.generate_xml()
    file_generator.generate_excel()
    file_generator.generate_doc()
    file_generator.generate_pdf()
    
    print("测试数据生成完成！")

if __name__ == "__main__":
    generate_test_data() 