#---------------
# Date: 13/06/2026
# Author: valentechie
#---------------

from graphics import Canvas

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


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Show the menu and wait until the user clicks the start button
    start = draw_menu(canvas)
    while True:
        x, y = canvas.wait_for_click()
        if start in canvas.find_overlapping(x, y, x, y):
            break

    # Main loop: planet selection -> weight calculator -> back
    while True:
        canvas.clear()
        earth, mars, moon = draw_planet_selection(canvas)

        x, y = canvas.wait_for_click()
        objs = canvas.find_overlapping(x, y, x, y)
        canvas.clear()

        # Load the corresponding planet screen and set its gravity
        if earth in objs:
            gravity = 1
            back, button_10, button_12, button_23, result_text = draw_planet_screen(canvas, "earth_screen.png")

        elif mars in objs:
            gravity = 0.38
            back, button_10, button_12, button_23, result_text = draw_planet_screen(canvas, "mars_screen.png")

        elif moon in objs:
            gravity = 0.16
            back, button_10, button_12, button_23, result_text = draw_planet_screen(canvas, "moon_screen.png")

        else:
            continue

        # Weight calculator loop for the selected planet
        while True:
            x, y = canvas.wait_for_click()
            objs = canvas.find_overlapping(x, y, x, y)

            if back in objs:
                break

            elif button_10 in objs:
                mass = 10
                weight = mass * gravity
                canvas.change_text(result_text, f"{weight:.1f} kg")

            elif button_12 in objs:
                mass = 12
                weight = mass * gravity
                canvas.change_text(result_text, f"{weight:.1f} kg")

            elif button_23 in objs:
                mass = 23
                weight = mass * gravity
                canvas.change_text(result_text, f"{weight:.1f} kg")


# Planet screens
def draw_planet_screen(canvas, image_name):
    # Draws the weight calculator screen for a given planet
    canvas.create_image_with_size(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        image_name
    )

    back = back_button(canvas)

    button_10 = button_10kg(canvas)
    button_12 = button_12kg(canvas)
    button_23 = button_23kg(canvas)

    result_text = canvas.create_text(
        650,
        410,
        "--",
        font_size=24,
        color="white"
    )

    return back, button_10, button_12, button_23, result_text


# Back button (top left corner)
def back_button(canvas):
    return canvas.create_image_with_size(
        20,
        20,
        128,
        42,
        "button_back.png"
    )


# Mass buttons
def button_10kg(canvas):
    return canvas.create_image_with_size(
        450,
        220,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "button_10kg.png"
    )


def button_12kg(canvas):
    return canvas.create_image_with_size(
        550,
        220,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "button_12kg.png"
    )


def button_23kg(canvas):
    return canvas.create_image_with_size(
        650,
        220,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
        "button_23kg.png"
    )


# Planet selection screen
def draw_planet_selection(canvas):
    # Draws the planet selection screen and returns the three planet objects
    canvas.create_image_with_size(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "background_planet.png"
    )

    earth = canvas.create_image_with_size(
        -40,
        CENTER_Y - PLANET_HEIGHT / 2,
        PLANET_WIDTH,
        PLANET_HEIGHT,
        "earth.png"
    )

    mars = canvas.create_image_with_size(
        195,
        CENTER_Y - PLANET_HEIGHT / 2,
        PLANET_WIDTH,
        PLANET_HEIGHT,
        "mars.png"
    )

    moon = canvas.create_image_with_size(
        430,
        CENTER_Y - PLANET_HEIGHT / 2,
        PLANET_WIDTH,
        PLANET_HEIGHT,
        "moon.png"
    )

    return earth, mars, moon


# Menu screen
def draw_menu(canvas):
    # Draws the main menu and returns the start button object
    canvas.create_image_with_size(
        0,
        0,
        CANVAS_WIDTH,
        CANVAS_HEIGHT,
        "background_menu.png"
    )

    return button_start(canvas)


def button_start(canvas):
    # Creates and returns the start button centered on screen
    width_size = 320
    height_size = 164

    start_x = CENTER_X - width_size / 2
    start_y = CENTER_Y - height_size / 4

    return canvas.create_image_with_size(
        start_x,
        start_y,
        width_size,
        height_size,
        "button_start.png"
    )


if __name__ == '__main__':
    main()