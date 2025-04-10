import numpy as np
import soundfile as sf
from pydub import AudioSegment
import os
import mido
from mido import Message, MidiFile, MidiTrack

class AudioGenerator:
    def __init__(self, output_dir="generated_data"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def generate_midi(self, filename="test_midi"):
        """生成一個簡單的 MIDI 文件"""
        # 創建 MIDI 文件
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        
        # 設置樂器（0 是鋼琴）
        track.append(Message('program_change', program=0, time=0))
        
        # 音符列表（C大調音階）
        notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C4 到 C5
        
        # 添加音符
        for note in notes:
            # 按下音符
            track.append(Message('note_on', note=note, velocity=64, time=0))
            # 保持音符 0.5 秒
            track.append(Message('note_off', note=note, velocity=64, time=480))
        
        # 保存 MIDI 文件
        midi_path = os.path.join(self.output_dir, f"{filename}.mid")
        mid.save(midi_path)
        return midi_path
    
    def generate_sine_wave(self, frequency, duration=1.0, sample_rate=44100):
        """生成正弦波音频"""
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        signal = np.sin(2 * np.pi * frequency * t)
        return signal
    
    def generate_white_noise(self, duration=1.0, sample_rate=44100):
        """生成白噪声"""
        return np.random.uniform(-1, 1, int(sample_rate * duration))
    
    def generate_lightsaber_sound(self, duration=1.0, sample_rate=44100):
        # 每段聲音的持續時間
        segment_duration = duration / 3
        
        def create_segment(start_time):
            # 基礎嗡嗡聲（低頻）
            base_freq = 150  # 降低基礎頻率使聲音更低沉
            base_sound = self.generate_sine_wave(base_freq, segment_duration, sample_rate)
            
            # 嘶嘶聲（高頻噪音）- 降低音量
            noise = self.generate_white_noise(segment_duration, sample_rate) * 0.1
            
            # 聲音強度的包絡線（使聲音有起伏）
            t = np.linspace(0, segment_duration, int(sample_rate * segment_duration))
            envelope = 0.5 + 0.5 * np.sin(2 * np.pi * 1.5 * t)  # 1.5Hz的調製
            
            # 混合並應用包絡線
            segment = (base_sound + noise) * envelope
            
            # 添加淡入淡出效果
            fade_samples = int(0.05 * sample_rate)  # 50ms 淡入淡出
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            segment[:fade_samples] *= fade_in
            segment[-fade_samples:] *= fade_out
            
            return segment
        
        # 生成三段聲音
        segment1 = create_segment(0)
        segment2 = create_segment(segment_duration)
        segment3 = create_segment(2 * segment_duration)
        
        # 在段落之間添加短暫的停頓
        pause_samples = int(0.1 * sample_rate)  # 100ms 的停頓
        pause = np.zeros(pause_samples)
        
        # 組合所有段落
        combined = np.concatenate([
            segment1, pause,
            segment2, pause,
            segment3
        ])
        
        return combined
    
    def generate_8bit_sound(self, duration=1.0, sample_rate=44100):
        """生成 8-bit 風格的音效，模擬老式遊戲機的聲音"""
        # 基本音階頻率（C大調）
        frequencies = [262, 330, 392, 440]  # C4, E4, G4, A4
        
        # 生成方波（模擬 NES 的聲音特點）
        def square_wave(freq, t):
            return np.sign(np.sin(2 * np.pi * freq * t))
        
        # 創建時間序列
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        # 生成音樂序列
        melody = np.zeros_like(t)
        note_duration = duration / 8
        for i in range(8):
            freq = frequencies[i % len(frequencies)]
            start = int(i * note_duration * sample_rate)
            end = int((i + 1) * note_duration * sample_rate)
            melody[start:end] = square_wave(freq, t[start:end]) * 0.5
        
        # 添加簡單的包絡（使聲音更有游戲感）
        envelope = np.ones_like(t)
        attack = int(0.01 * sample_rate)
        decay = int(0.05 * sample_rate)
        envelope[:attack] = np.linspace(0, 1, attack)
        
        # 應用包絡
        melody = melody * envelope
        
        return melody
    
    def save_audio(self, signal, filename, sample_rate=44100):
        """保存音频文件"""
        # 确保信号在 [-1, 1] 范围内
        signal = np.clip(signal, -1, 1)
        
        # 保存為 WAV 文件
        wav_path = os.path.join(self.output_dir, f"{filename}.wav")
        sf.write(wav_path, signal, sample_rate)
        
        # 轉換為 MP3
        mp3_path = os.path.join(self.output_dir, f"{filename}.mp3")
        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        
        # 轉換為 FLAC
        flac_path = os.path.join(self.output_dir, f"{filename}.flac")
        audio.export(flac_path, format="flac")
        
        return wav_path, mp3_path, flac_path

def main():
    generator = AudioGenerator()
    
    # 生成 MIDI 文件（測試用）
    generator.generate_midi("test_midi")
    
    # 生成基本測試音頻（只輸出 MP3）
    frequencies = [220, 440, 880]
    for freq in frequencies:
        signal = generator.generate_sine_wave(freq)
        wav_path, mp3_path, flac_path = generator.save_audio(signal, f"sine_{freq}hz")
        os.remove(wav_path)  # 刪除 WAV 文件
        os.remove(flac_path)  # 刪除 FLAC 文件
    
    # 生成白噪聲（只輸出 MP3）
    noise = generator.generate_white_noise()
    wav_path, mp3_path, flac_path = generator.save_audio(noise, "white_noise")
    os.remove(wav_path)  # 刪除 WAV 文件
    os.remove(flac_path)  # 刪除 FLAC 文件
    
    # 生成光劍聲音（輸出所有格式）
    lightsaber = generator.generate_lightsaber_sound(duration=2.0)
    generator.save_audio(lightsaber, "lightsaber")

if __name__ == "__main__":
    main() 