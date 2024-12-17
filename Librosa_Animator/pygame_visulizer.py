import pygame
import math

# Initialize Pygame
pygame.init()

# Screen Size
SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Visual")

# Colors
BLACK = (0, 0, 0)

def draw_glowing_sphere(surface, x, y, radius, color, max_intensity=255):
    """Draw a glowing sphere with a radial gradient effect."""
    for i in range(0, radius):
        # Calculate transparency and color intensity
        alpha = int((radius - i) / 50)
        r = max(0, color[0] * (i / radius))  # Red
        g = max(0, color[1] * (i / radius))  # Green
        b = max(0, color[2] * (i / radius))  # Blue

        # Create a surface with per-pixel alpha
        glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (r, g, b, alpha), (radius, radius), i)
        
        # Blit the surface onto the main screen
        surface.blit(glow_surface, (x - radius, y - radius))

# Main loop
running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(BLACK)

    # Sphere position (oscillating slightly for animation)
    center_x = SCREEN_WIDTH // 2
    center_y = SCREEN_HEIGHT // 2

    # Draw the glowing sphere
    draw_glowing_sphere(screen, center_x, center_y, 250, (255, 100, 50))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
