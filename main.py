#---------------
# Date: 13/06/2026
# Author: valentechie
#---------------

import pygame
import sys

# Canvas dimensions
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

# Center of the canvas
CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2

# Sizes of planets
PLANET_WIDTH = 408
PLANET_HEIGHT = 272

# Sizes of mass buttons
BUTTON_WIDTH = 92
BUTTON_HEIGHT = 43


def load_image(name, width, height):
    # Load and scale an image to the given size
    image = pygame.image.load(name)
    return pygame.transform.scale(image, (width, height))


def draw_image(screen, image, x, y):
    # Draw an image at position (x, y) and return its rect for click detection
    screen.blit(image, (x, y))
    return pygame.Rect(x, y, image.get_width(), image.get_height())


def wait_for_click(screen):
    # Wait until the user clicks and return (x, y) of the click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return event.pos


def main():
    pygame.init()
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Gravity Lab")

    # Show the menu and wait until the user clicks the start button
    start_rect = draw_menu(screen)
    pygame.display.flip()

    while True:
        x, y = wait_for_click(screen)
        if start_rect.collidepoint(x, y):
            break

    # Main loop: planet selection -> weight calculator -> back
    while True:
        earth_rect, mars_rect, moon_rect = draw_planet_selection(screen)
        pygame.display.flip()

        x, y = wait_for_click(screen)

        # Load the corresponding planet screen and set its gravity
        if earth_rect.collidepoint(x, y):
            gravity = 1
            planet_screen = "assets/earth_screen.png"

        elif mars_rect.collidepoint(x, y):
            gravity = 0.38
            planet_screen = "assets/mars_screen.png"

        elif moon_rect.collidepoint(x, y):
            gravity = 0.16
            planet_screen = "assets/moon_screen.png"

        else:
            continue

        back_rect, btn_10_rect, btn_12_rect, btn_23_rect, result_pos = draw_planet_screen(screen, planet_screen)
        pygame.display.flip()

        # Weight calculator loop for the selected planet
        while True:
            x, y = wait_for_click(screen)

            if back_rect.collidepoint(x, y):
                break

            elif btn_10_rect.collidepoint(x, y):
                mass = 10
                weight = mass * gravity
                result_label = f"{weight:.1f} kg"

            elif btn_12_rect.collidepoint(x, y):
                mass = 12
                weight = mass * gravity
                result_label = f"{weight:.1f} kg"

            elif btn_23_rect.collidepoint(x, y):
                mass = 23
                weight = mass * gravity
                result_label = f"{weight:.1f} kg"

            else:
                continue

            # Redraw planet screen to update the result text
            back_rect, btn_10_rect, btn_12_rect, btn_23_rect, result_pos = draw_planet_screen(screen, planet_screen)
            draw_result_text(screen, result_label, result_pos)
            pygame.display.flip()


# Planet screens
def draw_planet_screen(screen, image_name):
    # Draws the weight calculator screen for a given planet
    bg = load_image(image_name, CANVAS_WIDTH, CANVAS_HEIGHT)
    screen.blit(bg, (0, 0))

    back_rect = draw_back_button(screen)
    btn_10_rect = draw_button_10kg(screen)
    btn_12_rect = draw_button_12kg(screen)
    btn_23_rect = draw_button_23kg(screen)

    # Draw the default result text
    result_pos = (650, 410)

    return back_rect, btn_10_rect, btn_12_rect, btn_23_rect, result_pos


def draw_result_text(screen, text, pos):
    # Draw the weight result text at the given position
    font = pygame.font.SysFont(None, 32)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, pos)


# Back button (top left corner)
def draw_back_button(screen):
    img = load_image("assets/button_back.png", 128, 42)
    return draw_image(screen, img, 20, 20)


# Mass buttons
def draw_button_10kg(screen):
    img = load_image("assets/button_10kg.png", BUTTON_WIDTH, BUTTON_HEIGHT)
    return draw_image(screen, img, 450, 220)

def draw_button_12kg(screen):
    img = load_image("assets/button_12kg.png", BUTTON_WIDTH, BUTTON_HEIGHT)
    return draw_image(screen, img, 550, 220)

def draw_button_23kg(screen):
    img = load_image("assets/button_23kg.png", BUTTON_WIDTH, BUTTON_HEIGHT)
    return draw_image(screen, img, 650, 220)


# Planet selection screen
def draw_planet_selection(screen):
    # Draws the planet selection screen and returns the three planet rects
    bg = load_image("assets/background_planet.png", CANVAS_WIDTH, CANVAS_HEIGHT)
    screen.blit(bg, (0, 0))

    earth_img = load_image("assets/earth.png", PLANET_WIDTH, PLANET_HEIGHT)
    mars_img = load_image("assets/mars.png", PLANET_WIDTH, PLANET_HEIGHT)
    moon_img = load_image("assets/moon.png", PLANET_WIDTH, PLANET_HEIGHT)

    earth_rect = draw_image(screen, earth_img, -40, CENTER_Y - PLANET_HEIGHT / 2)
    mars_rect = draw_image(screen, mars_img, 195, CENTER_Y - PLANET_HEIGHT / 2)
    moon_rect = draw_image(screen, moon_img, 430, CENTER_Y - PLANET_HEIGHT / 2)

    return earth_rect, mars_rect, moon_rect


# Menu screen
def draw_menu(screen):
    # Draws the main menu and returns the start button rect
    bg = load_image("assets/background_menu.png", CANVAS_WIDTH, CANVAS_HEIGHT)
    screen.blit(bg, (0, 0))

    return draw_button_start(screen)


def draw_button_start(screen):
    # Creates and returns the start button rect centered on screen
    width_size = 320
    height_size = 164

    start_x = CENTER_X - width_size / 2
    start_y = CENTER_Y - height_size / 4

    img = load_image("assets/button_start.png", width_size, height_size)
    return draw_image(screen, img, start_x, start_y)


if __name__ == '__main__':
    main()