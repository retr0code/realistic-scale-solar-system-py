import pygame
from planets import Planets


# Initialize Pygame
pygame.init()

YELLOW = (255, 191, 0)
# Set the dimensions of the game window
window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
WIDTH, HEIGHT = window.get_size()
CENTER = WIDTH // 2, HEIGHT // 2

font = pygame.font.SysFont('Verdana', 14)
pygame.display.set_caption("SolarSystem Model")

p = Planets()
sun_size_difference = p.sun_diameter - min(p.planets_diameters)
print("sun ratio: ", sun_size_difference)
scale = 2

def get_relative_size_to_window(max_size):
    return max_size / WIDTH

class Object:
    def __init__(self, id: str, pos: tuple, radius: float) -> None:
        self.id = id
        self.x, self.y = pos
        self.radius = radius
    
    def draw(self, border=1, color=(255,255,255)):
        pygame.draw.circle(window, color, (self.x, self.y), self.radius, border)


def label(text: str, pos: tuple):
    l = font.render(text, True, (54, 69, 7))
    window.blit(l, pos)

planets_relative_size = get_relative_size_to_window(min(p.planets_diameters))
sun_relative_size = get_relative_size_to_window(p.sun_diameter)
relative_difference = sun_relative_size / planets_relative_size
print("relative to window", planets_relative_size, sun_relative_size)

sun = round(sun_relative_size / scale)
earth = round(planets_relative_size / scale)
print(sun, earth)
p1 = Object("Sun", CENTER, sun)
p2 = Object("Earth", CENTER, earth)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0,0,0))
    p1.draw(border=0, color=YELLOW)
    p2.draw(border=0, color=(0,0,0))

    starty = 20
    index = 0
    for value in p.planets_list[2]:
        label(f"{p.names[2][index]}: {value}", (20, starty))
        starty += 16
        index += 1

    # Update the game display
    pygame.display.update()

# Quit the game
pygame.quit()