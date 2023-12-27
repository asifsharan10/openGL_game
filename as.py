from OpenGL.GL import *
from OpenGL.GLUT import *


W_Width, W_Height = 500, 500


rain_x = 0.5  # Initial raindrop x-position
rain_y = 1.0  # Initial raindrop y-position
rain_speed = 0.001  # Slower raindrop speed
direction = 1  # 1 for right, -1 for left


def draw_house():
    glColor3f(1.0, 1.0, 1.0)  # White color for the house
    glBegin(GL_LINES)


    # House base
    glVertex2d(0.2, 0.2)
    glVertex2d(0.2, 0.6)
    glVertex2d(0.2, 0.6)
    glVertex2d(0.6, 0.6)
    glVertex2d(0.6, 0.6)
    glVertex2d(0.6, 0.2)
    glVertex2d(0.6, 0.2)
    glVertex2d(0.2, 0.2)


    # Roof
    glVertex2d(0.2, 0.6)
    glVertex2d(0.4, 0.8)
    glVertex2d(0.4, 0.8)
    glVertex2d(0.6, 0.6)


    glEnd()


def draw_raindrop(x, y):
    glColor3f(0.0, 0.0, 1.0)  # Blue color for raindrop
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2d(x, y)
    glEnd()


def special_keys(key, x, y):
    global direction


    if key == GLUT_KEY_LEFT:
        direction = -1  # Left arrow key
    elif key == GLUT_KEY_RIGHT:
        direction = 1  # Right arrow key


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    draw_house()
    draw_raindrop(rain_x, rain_y)


    glutSwapBuffers()


def animate():
    global rain_x, rain_y, direction


    rain_x += direction * rain_speed
    rain_y -= 0.01  # Adjust the raindrop's vertical position


    if rain_x > 1.0:
        rain_x = 0.0
    elif rain_x < 0.0:
        rain_x = 1.0


    if rain_y < 0.0:
        rain_y = 1.0


    glutPostRedisplay()


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"House with Raindrop")


glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(special_keys)


glutMainLoop()
