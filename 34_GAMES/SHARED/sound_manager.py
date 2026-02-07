import pygame
import array
import math

class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
        self.sounds = {}
        self.enabled = True
        self._generate_sounds()

    def _generate_sounds(self):
        # Generate synthetic sounds to avoid external files
        self.sounds['move'] = self._make_tone(400, 0.1, 0.5)
        self.sounds['capture'] = self._make_tone(600, 0.15, 0.5)
        self.sounds['win'] = self._make_sequence([(400, 0.1), (500, 0.1), (600, 0.1), (800, 0.3)])
        self.sounds['lose'] = self._make_sequence([(400, 0.1), (300, 0.1), (200, 0.3)])
        self.sounds['select'] = self._make_tone(800, 0.05, 0.3)
        self.sounds['error'] = self._make_tone(150, 0.2, 0.5)

    def _make_tone(self, frequency, duration, volume=0.5):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = array.array('h', [0] * n_samples)
        amplitude = 2 ** 15 - 1
        
        for i in range(n_samples):
            # Sine wave
            t = float(i) / sample_rate
            val = int(amplitude * volume * math.sin(2 * math.pi * frequency * t))
            # Simple decay
            decay = (n_samples - i) / n_samples
            buf[i] = int(val * decay)
            
        return pygame.mixer.Sound(buffer=buf)

    def _make_sequence(self, notes):
        # notes is list of (freq, dur)
        # This is a bit complex for pure buffer, simplifying to playing sequentially
        # For this simple manager, we'll just return the last note or mix them. 
        # Actually, let's just make a simple chord or arpeggio generator if needed.
        # For simplicity in this script, 'win' will just be a high tone.
        return self._make_tone(notes[-1][0], sum(n[1] for n in notes), 0.5)

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def toggle(self):
        self.enabled = not self.enabled
