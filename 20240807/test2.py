# -*- coding: utf-8 -*-
# Auther : jianlong

import pygame
import sys

pygame.init()

# 创建一个pygame窗口
screen = pygame.display.set_mode((600, 300))

# 加载音乐文件
pygame.mixer.music.load('/Users/dongzhiqiao/Music/网易云音乐/童话镇-陈一发儿.mp3')

# 播放音乐
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 结束pygame
pygame.quit()
sys.exit()