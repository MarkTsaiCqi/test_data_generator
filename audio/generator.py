import numpy as np
import soundfile as sf
from pydub import AudioSegment
import os
import mido
from mido import Message, MidiFile, MidiTrack
from pydub.generators import Sine, WhiteNoise
import random
import argparse
from tqdm import tqdm

class AudioGenerator:
    def __init__(self, output_dir="generated_data"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def _show_progress(self, current: int, total: int, prefix: str = "", suffix: str = ""):
        """顯示進度條"""
        bar_length = 50
        filled_length = int(round(bar_length * current / float(total)))
        percents = round(100.0 * current / float(total), 1)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r{prefix} [{bar}] {percents}% {suffix}', end='')
        if current == total:
            print()
    
    def generate_audio_with_target_size(self, target_size_mb: float, format: str = "mp3") -> str:
        """生成指定大小的音頻文件
        
        Args:
            target_size_mb: 目標大小（MB）
            format: 音頻格式
        """
        print(f"\n正在生成大小約為 {target_size_mb}MB 的音頻...")
        
        # 計算目標字節數
        target_bytes = target_size_mb * 1024 * 1024
        
        # 對於 MP3 格式，我們需要考慮壓縮率
        # 假設平均壓縮率約為 1:11（未壓縮的 WAV 到 MP3）
        # 44.1kHz, 16-bit, stereo 的 WAV 每秒約佔 176,400 字節
        # 所以 MP3 每秒約佔 16,036 字節
        target_duration_ms = int((target_bytes / 16036) * 1000)
        
        print(f"目標音頻長度：{target_duration_ms/1000:.1f}秒")
        
        # 生成白噪聲（比正弦波更容易達到目標大小）
        print("生成白噪聲...")
        audio = WhiteNoise().to_audio_segment(duration=target_duration_ms)
        
        # 保存音頻
        filename = f"size_{target_size_mb}mb.{format}"
        filepath = os.path.join(self.output_dir, filename)
        
        # 計算初始比特率
        # MP3 比特率計算公式：比特率(kbps) = (文件大小(bytes) * 8) / (音頻長度(秒) * 1000)
        initial_bitrate = int((target_bytes * 8) / (target_duration_ms / 1000) / 1000)
        initial_bitrate = min(max(initial_bitrate, 32), 320)  # 限制在 32-320kbps 範圍內
        
        # 調整比特率以達到目標大小
        bitrate = initial_bitrate
        min_bitrate = 32
        max_bitrate = 320
        tolerance = 0.2  # 增加容差範圍到 0.2MB
        max_iterations = 5  # 減少最大迭代次數
        
        print("\n正在優化音頻文件大小...")
        pbar = tqdm(range(max_iterations), desc="進度", unit="次")
        for i in pbar:
            # 計算比特率百分比 (32kbps = 0%, 320kbps = 100%)
            bitrate_percent = int((bitrate - 32) / (320 - 32) * 100)
            pbar.set_postfix({
                "品質": f"{bitrate_percent}%",
                "目標": f"{target_size_mb}MB"
            })
            audio.export(filepath, format=format, bitrate=f"{bitrate}k")
            actual_size_mb = os.path.getsize(filepath) / (1024 * 1024)
            
            if abs(actual_size_mb - target_size_mb) <= tolerance:
                print(f"\n✓ 已找到合適的品質: {bitrate_percent}%")
                break
            
            # 根據實際大小調整比特率
            if actual_size_mb > target_size_mb:
                max_bitrate = bitrate
                bitrate = (bitrate + min_bitrate) // 2
            else:
                min_bitrate = bitrate
                bitrate = (bitrate + max_bitrate) // 2
            
            if max_bitrate - min_bitrate <= 1:
                print(f"\n! 無法進一步優化，使用當前品質: {bitrate_percent}%")
                break
        
        print(f"\n✓ 音頻已保存：{filename}")
        print(f"✓ 實際大小：{actual_size_mb:.2f}MB")
        print(f"✓ 音頻長度：{target_duration_ms/1000:.1f}秒")
        return filepath
    
    def generate_test_audio(self):
        """生成各種測試音頻"""
        # 生成白噪聲
        print("\n生成白噪聲...")
        noise = WhiteNoise().to_audio_segment(duration=5000)  # 5秒
        noise.export(os.path.join(self.output_dir, "white_noise.mp3"), format="mp3")
        
        # 生成不同頻率的正弦波
        frequencies = [220, 440, 880]  # Hz
        for freq in frequencies:
            print(f"\n生成 {freq}Hz 正弦波...")
            sine = Sine(freq).to_audio_segment(duration=5000)  # 5秒
            sine.export(os.path.join(self.output_dir, f"sine_{freq}hz.mp3"), format="mp3")
        
        # 生成光劍音效
        print("\n生成光劍音效...")
        lightsaber = self._generate_lightsaber_sound()
        lightsaber.export(os.path.join(self.output_dir, "lightsaber.wav"), format="wav")
        lightsaber.export(os.path.join(self.output_dir, "lightsaber.mp3"), format="mp3")
        lightsaber.export(os.path.join(self.output_dir, "lightsaber.flac"), format="flac")
        
        # 生成 MIDI 文件
        print("\n生成 MIDI 文件...")
        self._generate_midi_file(os.path.join(self.output_dir, "test_midi.mid"))
    
    def _generate_lightsaber_sound(self) -> AudioSegment:
        """生成光劍音效"""
        # 創建基礎音頻
        base = WhiteNoise().to_audio_segment(duration=1000)  # 1秒
        
        # 添加頻率掃描效果
        sweep = Sine(100).to_audio_segment(duration=1000)
        sweep = sweep._spawn(sweep.raw_data, overrides={
            "frame_rate": int(sweep.frame_rate * 2)  # 提高採樣率
        })
        
        # 混合音頻
        result = base.overlay(sweep)
        
        # 添加淡入淡出效果
        result = result.fade_in(100).fade_out(100)
        
        return result
    
    def _generate_midi_file(self, output_path: str):
        """生成簡單的 MIDI 文件"""
        from midiutil import MIDIFile
        
        # 創建 MIDI 文件
        midi = MIDIFile(1)  # 1個音軌
        
        # 設置音軌
        track = 0
        time = 0
        midi.addTrackName(track, time, "Test Track")
        midi.addTempo(track, time, 120)
        
        # 添加音符
        for i in range(8):
            midi.addNote(track, 0, 60 + i, time + i, 1, 100)  # C4 到 C5
        
        # 保存文件
        with open(output_path, "wb") as output_file:
            midi.writeFile(output_file)
    
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
    parser = argparse.ArgumentParser(description='生成測試音頻文件')
    parser.add_argument('--big', action='store_true', help='生成大音頻文件（用於測試上傳限制）')
    args = parser.parse_args()
    
    generator = AudioGenerator()
    
    if args.big:
        # 生成大音頻文件
        generator.generate_audio_with_target_size(24)  # 24MB
        generator.generate_audio_with_target_size(25)  # 25MB
        generator.generate_audio_with_target_size(26)  # 26MB
    else:
        # 生成測試音頻
        generator.generate_test_audio()

if __name__ == "__main__":
    main() 