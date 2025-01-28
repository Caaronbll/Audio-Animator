import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Glowing Sphere")

# Colors
BLACK = (0, 0, 0)

def draw_glowing_sphere(surface, x, y, radius1, radius2, color, max_intensity=255):
    """Draw a glowing sphere with a radial gradient effect."""

    glow_surface = pygame.Surface((radius2 * 2, radius2 * 2), pygame.SRCALPHA)
    pygame.draw.circle(glow_surface, (50, 100, 250, 255), (radius1, radius1), radius1)


    for i in range(0, radius2, 1):
        # Calculate transparency and color intensity
        alpha = int(max_intensity * (1 - (i / radius2)))
        #print(alpha)
        r = max(0, color[0] * (i / radius2))  # Red
        g = max(0, color[1] * (i / radius2))  # Green
        b = max(0, color[2] * (i / radius2))  # Blue
        
        # Create a surface with per-pixel alpha
        #glow_surface = pygame.Surface((radius2 * 2, radius2 * 2), pygame.SRCALPHA)
        #pygame.draw.circle(glow_surface, (r, g, b, alpha), (radius2, radius2), i)
        
        # Blit the surface onto the main screen
        surface.blit(glow_surface, (x - radius2, y - radius2))

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
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    # Draw the glowing sphere
    draw_glowing_sphere(screen, center_x, center_y, 150, 300, (255, 100, 50), 255)
    
    # Refresh screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()