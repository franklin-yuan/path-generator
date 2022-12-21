
WIDTH, HEIGHT = 876, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spline Tool")

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

FPS = 60
FIELD_WIDTH, FIELD_HEIGHT = 876, 594
ROBOT_WIDTH, ROBOT_HEIGHT = 60, 60

FIELD_IMAGE = pg.image.load(os.path.join('assets','vex_field.png'))
FIELD_IMAGE = pg.transform.scale(FIELD_IMAGE, (FIELD_WIDTH, FIELD_HEIGHT))
ROBOT_IMAGE = pg.image.load(os.path.join('assets','robot_square.png'))
ROBOT_IMAGE = pg.transform.scale(ROBOT_IMAGE, (ROBOT_WIDTH, ROBOT_HEIGHT))

def drawWindow(robot):
    WIN.fill(WHITE)
    WIN.blit(FIELD_IMAGE, (0,0))
    WIN.blit(ROBOT_IMAGE, (robot.x, robot.y))
    pg.display.update()

