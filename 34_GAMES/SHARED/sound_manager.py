import pygame
import array
import math

class SoundManager:
    def __init__(self):
        self.enabled = False
        try:
            # Try to initialize mixer, but don't crash if no audio device
            pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
            self.enabled = True
            self.sounds = {}
            self._generate_sounds()
            print("Audio initialized successfully.")
        except Exception as e:
            print(f"Audio initialization failed: {e}")
            self.sounds = {}

    def _generate_sounds(self):
        try:
            self.sounds['move'] = self._make_tone(400, 0.1, 0.3)
            self.sounds['capture'] = self._make_tone(600, 0.15, 0.4)
            self.sounds['win'] = self._make_tone(800, 0.5, 0.4)
            self.sounds['select'] = self._make_tone(700, 0.05, 0.2)
            self.sounds['error'] = self._make_tone(150, 0.2, 0.4)
        except:
            self.enabled = False

    def _make_tone(self, frequency, duration, volume=0.5):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = array.array('h', [0] * n_samples)
        amplitude = 2 ** 15 - 1
        for i in range(n_samples):
            t = float(i) / sample_rate
            val = int(amplitude * volume * math.sin(2 * math.pi * frequency * t))
            decay = (n_samples - i) / n_samples
            buf[i] = int(val * decay)
        return pygame.mixer.Sound(buffer=buf)

    def play(self, name):
        if self.enabled and name in self.sounds:
            try:
                self.sounds[name].play()
            except:
                pass

    def toggle(self):
        if self.enabled:
            self.enabled = False
        else:
            # Re-init attempt? For now just toggle flag
            self.enabled = True