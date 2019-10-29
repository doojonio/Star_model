from graphics import color_rgb, Point

# WINDOW SETTINGS
WINDOW_NAME = "Window"  # Name of the window
WINDOW_LENGTH = 600  # Lenght of the window
WINDOW_WIDTH = 600  # Width of the window
WINDOW_CENTRE = Point(WINDOW_LENGTH/2, WINDOW_WIDTH/2)
SUN_RAD_IN_PIX = 100 # Solar radius in pixels
STAR_LAB_INDENT = 100
STAR_LABEL_WIDTH = 40
LAB_RAD_POS = Point(WINDOW_LENGTH - STAR_LAB_INDENT, WINDOW_WIDTH - 4 * STAR_LABEL_WIDTH)
LAB_LUM_POS = Point(WINDOW_LENGTH - STAR_LAB_INDENT, WINDOW_WIDTH - 3 * STAR_LABEL_WIDTH)
LAB_TEMP_POS = Point(WINDOW_LENGTH - STAR_LAB_INDENT, WINDOW_WIDTH - 2 * STAR_LABEL_WIDTH)
LAB_MASS_POS = Point(WINDOW_LENGTH - STAR_LAB_INDENT, WINDOW_WIDTH - STAR_LABEL_WIDTH)
N_DEC = 3 # Number of decimal places

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
TIME_SLEEP = 0.5  # Sleep time for animation creating
MOVE_STEP = 1  # Move speed per TIME SLEEP

# TIME SETTINGS
TIME_STEP = 0.0001 # Million years

# STAR MATURITY SETTINGS
STAR_RADIUS_DECREASE = 0.9
STAR_RADIUS_INDCREASE = 1.2
STAR_TEMP_DECREASE = 0.9
STAR_TEMP_INCREASE = 1.3
STAR_LUM_DECREASE = 0.9
STAR_LUM_INCREASE = 1.2
INIT_STAGE_STAND_DUR = 1.    # Initial stage duration for stars like a sun (million years)
INIT_STAGE_DUR_COEF = 100
BIG_MASS = 1.4

#NAMES
INIT_STAGE_NAME = 'Init'



