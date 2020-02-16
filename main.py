import pyglet
from pyglet import gl
import math
from pyglet.window import key
import numpy
import sounddevice as sd

level = [
    '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',
    '-                                                                 ---                                         ---                                 ---       -',
    '-               ---             ---                                                         -                                       ---                     -',
    '-                                                     ---                                                        ---                                        -',
    '-       ---              ---                ---                      ---                      ---                                                           -',
    '-                                                                                                                          ---                   ---        -',
    '-                                                                                                                                                           -',
    '-               -                 -                      -                          -                          -                              -             -',
    '-                                                                                            ---                                                            -',
    '-                     ---                       ---               -                                      ---               ---        ---                   -',
    '-                                     ---                                    ---                                                                    ---     -',
    '-         ---                                                  -                          ---                                                               -',
    '-                              -                                                                                   -                                        -',
    '-                                                        -                ---                       ---                            -                        -',
    '-                                        ---                                           -                                ---                         -       -',
    '-               -             -                                    ---                                          ---                                         -',
    '-                                                                                                   ---                                   -                 -                              -                 -                        -     -     -           -',
    '-        ---                               ---                -                         -                                          -                    ---                             -                    ---                     -       -                    ---                             -                    ----',
    '-                                                                                                                ---            --                                                   -                                          --                ---                                                                     -',
    '-                         -                                          --                ---                                                                                           -             -                -           --  -             ---                                                                     -',
    '--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
]
level.reverse()

W, H = 780, 630
BG_COLOR = (.75, .75, .75, 1.)

RADIUS = 20
SIZE = 30
COLOR = (0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0)
SPEED_CIRCLE = 300
penalty = [0]
SPEED_BG = 300

window = pyglet.window.Window(width=W, height=H, caption='GAME')
window.set_location(5, 30)
window.set_mouse_visible(visible=False)
counter = pyglet.window.FPSDisplay(window=window)

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

keys = key.KeyStateHandler()
window.push_handlers(keys)

penalty_label = pyglet.text.Label(
    text=f'Штраф: {penalty[0]}', font_name='Times difference Roman', color=(255, 0, 0, 255),
    x=W // 2, y=H - SIZE, anchor_x='center', anchor_y='top', font_size=16,
    batch=batch, group=foreground)

# start QUARD
polygon_list = []
x = y = 0
for raw in level:
    for col in raw:
        if col == '-':
            polygon = batch.add(
                4, pyglet.gl.GL_QUADS, background,
                ('v2f', [x, y, x, y + SIZE, x + SIZE, y + SIZE, x + SIZE, y]),
                ('c3f', COLOR)
            )
            polygon_list.append(polygon)
        x += SIZE
    y += SIZE
    x = 0
# stop QUARD


# start smail
def face(a, b, c, x1, y1, radius):
    point_list = []
    for angle in range(a, b, c):
        rads = math.radians(angle)
        s = radius * math.sin(rads)
        c = radius * math.cos(rads)
        point_list.append(x1 + c)
        point_list.append(y1 + s)
    NP = len(point_list) // 2
    circle_list = batch.add(
        NP, pyglet.gl.GL_POINTS, foreground,
        ('v2f', point_list),
        ('c4f', (1, 0, 0, .5) * NP)
    )
    face_list.append(circle_list)
    return circle_list
# stop smail


def update(dt):
    if keys[key.LEFT]:
        for ver in face_list:
            ver.vertices = [element - SPEED_CIRCLE * dt if index % 2 == 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.RIGHT]:
        for ver in face_list:
            ver.vertices = [element + SPEED_CIRCLE * dt if index % 2 == 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.UP]:
        for ver in face_list:
            ver.vertices = [element + SPEED_CIRCLE * dt if index % 2 != 0 else element for index, element in enumerate(ver.vertices)]
    if keys[key.DOWN]:
        for ver in face_list:
            ver.vertices = [element - SPEED_CIRCLE * dt if index % 2 != 0 else element for index, element in enumerate(ver.vertices)]

    for ver in polygon_list:
        ver.vertices = [elem - SPEED_BG * dt if e % 2 == 0 else elem for e, elem in enumerate(ver.vertices)]

    # collision
    if circle_list.vertices[0] < W - RADIUS * 2:
        for ver in polygon_list:
            nx = max(ver.vertices[0], min(circle_list.vertices[0] - RADIUS, ver.vertices[0] + SIZE))
            ny = max(ver.vertices[1], min(circle_list.vertices[1], ver.vertices[1] + SIZE))
            dtc = (nx - (circle_list.vertices[0] - RADIUS)) ** 2 + (ny - circle_list.vertices[1]) ** 2
            if dtc <= RADIUS ** 2:
                penalty[0] += 0.1
                penalty_label.text = f'Штраф: {round(penalty[0], 1)}'


@window.event
def on_draw():
    window.clear()
    batch.draw()
    counter.draw()


def audio_callback(indata, frames, time, status):
    list_y.append(numpy.linalg.norm(indata) * 20)


gl.glPointSize(3)
gl.glEnable(gl.GL_POINT_SMOOTH)
gl.glClearColor(*BG_COLOR)
gl.glEnable(gl.GL_BLEND)
gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

face_list = []
circle_list = face(0, 360, 6, W // 2, H // 2, RADIUS)
face(0, 360, 36, W // 2 - RADIUS * 0.42, H // 2 + RADIUS * 0.2, RADIUS // 6)
face(0, 360, 36, W // 2 + RADIUS * 0.42, H // 2 + RADIUS * 0.2, RADIUS // 6)
face(210, 340, 10, W // 2, H // 2, RADIUS * 0.6)

list_y = []
stream = sd.InputStream(callback=audio_callback)
with stream:
    pyglet.clock.schedule_interval(update, 1 / 60.0)
    pyglet.app.run()

'''
pyglet.graphics.draw(
        4, pyglet.gl.GL_QUADS,
        ('v2f', [x, y, x, y + SIZE, x + SIZE, y + SIZE, x + SIZE, y]),
        ('c3f', COLOR))
'''
