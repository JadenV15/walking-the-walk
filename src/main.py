#!/usr/bin/python
import math
import pygame

from engine.framebuffer import Framebuffer
from engine.renderer import Renderer
from engine.mesh import create_cube

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH , HEIGHT))

clock = pygame.time.Clock()

framebuffer = Framebuffer(WIDTH, HEIGHT)

renderer = Renderer(WIDTH, HEIGHT)

cube = create_cube()

angle = 0.0

running = True

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += dt

    framebuffer.clear((20, 20, 30))

    renderer.render_mesh(
        framebuffer,
        cube,
        angle
    )

    framebuffer.present(screen)

    pygame.display.flip()

pygame.quit()

