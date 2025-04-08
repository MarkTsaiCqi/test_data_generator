import numpy as np
from scipy.io import wavfile
import os

class AudioGenerator:
    def __init__(self, output_dir="generated_audio"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_sine_wave(self, frequency, duration, sample_rate=44100):
        """生成正弦波音频"""
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        signal = np.sin(2 * np.pi * frequency * t)
        return signal
    
    def generate_noise(self, duration, sample_rate=44100):
        """生成白噪声"""
        return np.random.uniform(-1, 1, int(sample_rate * duration))
    
    def save_audio(self, signal, filename, sample_rate=44100):
        """保存音频文件"""
        # 确保信号在 [-1, 1] 范围内
        signal = np.clip(signal, -1, 1)
        # 转换为 16 位整数
        signal = (signal * 32767).astype(np.int16)
        
        filepath = os.path.join(self.output_dir, filename)
        wavfile.write(filepath, sample_rate, signal)
        return filepath

if __name__ == "__main__":
    generator = AudioGenerator()
    
    # 生成测试音频
    # 1. 生成 440Hz 的正弦波（A4 音）
    sine_wave = generator.generate_sine_wave(440, 2.0)
    generator.save_audio(sine_wave, "sine_440hz.wav")
    
    # 2. 生成白噪声
    noise = generator.generate_noise(2.0)
    generator.save_audio(noise, "white_noise.wav") 