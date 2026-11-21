import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")

background_image = pygame.transform.scale(
    pygame.image.load('White HD Backgrounds-WallpaperTag.jpg').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT)
)
girl_image = pygame.transform.scale(
    pygame.image.load('downlaod.jpg').convert_alpha(300, 300)
)
girl_rect = girl_image.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()

