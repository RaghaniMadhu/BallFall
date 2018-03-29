from Colours import *
from Ball import *
from Surface import *
from Slot import *
from Button import *


if __name__ == "__main__":
    '''----------CODE FOR BALL FALL-------------'''
    pygame.init()
    s1 = Surface((0, 0), "Ball Fall", black)
    b1 = Ball(0, 50, 40, blue, fall=False)
    s1.draw_surface()
    b1.draw_ball(s1.game_display)
    run_game = True
    while run_game:
        for event in pygame.event.get():  # Iterating over list of events
            if event.type == pygame.QUIT:  # Clicked The Close Button at the top right
                run_game = False
            elif event.type == pygame.KEYDOWN:  # Any Keyboard Key Is Pressed
                if event.key == pygame.K_SPACE:  # Key value Is Matched With Space bar Key Value
                    b1.fall = True
        s1.draw_surface()
        b1.move_along_x_axis(7, 0, 1370)
        b1.draw_ball(s1.game_display)
        if b1.fall:
            b1.move_along_y_axis(3, 700)
        b1.refresh_ball()
        s1.refresh_background()
    pygame.quit()
    quit()
