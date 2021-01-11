import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Creature(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('creature.png', -1)
        self.visible = False
        self.x, self.y = 0, 0

    def change_pos(self, events, speed=10):
        for event in events:
            if event.key == pygame.K_LEFT:
                self.x -= speed
            if event.key == pygame.K_RIGHT:
                self.x += speed
            if event.key == pygame.K_UP:
                self.y -= speed
            if event.key == pygame.K_DOWN:
                self.y += speed

    def ret_pos(self):
        return self.x, self.y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(size)
    running = True
    monster = Creature()
    move = False
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if move:
                    memory.append(event)
                move = True
                memory = [event]
            if event.type == pygame.KEYUP:
                move = False
        if move:
            monster.change_pos(memory)
        clock.tick(fps)
        screen.blit(monster.image, monster.ret_pos())
        pygame.display.flip()
