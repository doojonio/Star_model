from graphics import color_rgb

# WINDOW SETTINGS
WINDOW_NAME = "Window"  # Name of the window
WINDOW_LENGTH = 600  # Lenght of the window
WINDOW_WIDTH = 600  # Width of the window

# COLOR SETTINGS
COLORS = {
    'Black': color_rgb(0, 0, 0),
    'Dark_red': color_rgb(139, 0, 0),
    'Red': color_rgb(100, 0, 0),
    'Yellow': color_rgb(255, 255, 0),
    'White': color_rgb(255, 255, 255),
    'Bluish_white': color_rgb(166, 202, 240),
    'Blue': color_rgb(0, 0, 255),
}
# MOVEMENT SETTINGS
TIME_SLEEP = 0.05  # Sleep time for animation creating
MOVE_STEP = 1  # Move speed per TIME SLEEP

# TIME SETTINGS
TIME_STEP = 0.5 # Million years
THOUSAND_YEARS = 0.1

# STAR MATURITY SETTINGS
STAR_RADIUS_DECREASE = 0.9
STAR_RADIUS_INDCREASE = 1.1
STAR_TEMP_DECREASE = 0.9
STAR_TEMP_INCREASE = 1.1
STAR_LUM_DECREASE = 0.9
STAR_LUM_INCREASE = 1.1
INIT_STAGE_STAND_DUR = 1.    # Initial stage duration for stars like a sun (million years)
INIT_STAGE_DUR_COEF = 100
BIG_MASS = 1.4

#NAMES
INIT_STAGE_NAME = 'Init'



