# Day21-PongGame - Written in 14 lines and courtesy of Reddit: https://www.reddit.com/r/Python/comments/ty15no/pong_game_in_just_14_lines/
# Controls:
#   P1 = UP and DOWN Arrows
#   P2 = W and S Keys

import pygame
pygame.init()
win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
rects = [pygame.Rect(0, 0, 20, 60), pygame.Rect(780, 0, 20, 60), pygame.Rect(390, 290, 20, 20)]
ball_vel = [5, 5]
while clock.tick(60) and not pygame.QUIT in [event.type for event in pygame.event.get()]:
    keys = pygame.key.get_pressed()
    rects = rects[0].move(0, (keys[pygame.K_s] - keys[pygame.K_w]) * 5).clamp(win.get_rect()), rects[1].move(0, (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5).clamp(win.get_rect()), rects[2].move(*ball_vel)
    rects[2].topleft = (390, 290) if rects[2].x < 0 or rects[2].right > 800 else rects[2].topleft
    ball_vel[1], ball_vel[0] = -ball_vel[1] if rects[2].y < 0 or rects[2].bottom > 600 else ball_vel[1], -ball_vel[0] if rects[2].collidelist(rects[:-1]) != -1 else ball_vel[0]
    win.fill((0, 0, 0))
    [[pygame.draw.rect, pygame.draw.ellipse][1 if rect == rects[2] else 0](win, (255, 255, 255), rect) for rect in rects]
    pygame.display.update()