import pygame
import array
import math
import os

class SoundManager:
    def __init__(self):
        self.enabled = False
        self.bg_music_enabled = False
        try:
            # Lower buffer for better responsiveness
            pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
            self.enabled = True
            self.sounds = {}
            self._generate_sounds()
            print("Audio (Mixer) initialized.")
        except Exception as e:
            print(f"Audio init failed: {e}")
            self.sounds = {}

    def _generate_sounds(self):
        try:
            self.sounds['move'] = self._make_tone(440, 0.1, 0.2) # A4
            self.sounds['select'] = self._make_tone(880, 0.05, 0.1) # A5
            self.sounds['error'] = self._make_tone(150, 0.2, 0.3)
            self.sounds['win'] = self._make_tone(554, 0.3, 0.2) # C#5
            self.sounds['punish'] = self._make_tone(200, 0.4, 0.3)
        except:
            self.enabled = False

    def _make_tone(self, frequency, duration, volume=0.5):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = array.array('h', [0] * n_samples * 2) # Stereo
        amplitude = 2 ** 15 - 1
        for i in range(n_samples):
            t = float(i) / sample_rate
            val = int(amplitude * volume * math.sin(2 * math.pi * frequency * t))
            decay = (n_samples - i) / n_samples
            buf[i*2] = int(val * decay)     # Left
            buf[i*2+1] = int(val * decay)   # Right
        return pygame.mixer.Sound(buffer=buf)

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def start_jazz(self, file_path=None):
        if not self.enabled: return
        try:
            if file_path and os.path.exists(file_path):
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1) # Loop
                self.bg_music_enabled = True
            else:
                # If no file, we could generate a procedural 'jazz' loop?
                # For now, let's just use a placeholder note if no file.
                print("No jazz.mp3 found. Background music disabled.")
        except:
            print("Music playback failed.")

    def stop_jazz(self):
        if self.enabled:
            pygame.mixer.music.stop()
            self.bg_music_enabled = False

    def toggle(self):
        self.enabled = not self.enabled
        if not self.enabled:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
