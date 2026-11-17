import os
import pygame




music_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "Background2.mp3"
)

print("Mixer:", pygame.mixer.get_init())
print("Music file exists:", os.path.exists(music_file))

pygame.mixer.music.load(music_file)
pygame.mixer.music.set_volume(1.0)



pygame.mixer.init()
sound = pygame.mixer.Sound("chew2.wav")