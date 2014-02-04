import pygame, objects
def demo():
    bg_color=[239,169,119]
    heroes=pygame.sprite.Group()
    heroes.add(objects.PoliceGood([0,320]))
    villains=pygame.sprite.Group()
    villains.add(objects.PoliceEnemy([256,320]))
    rendered=pygame.sprite.Group()
    solid=pygame.sprite.Group()
    for i in range(0, 640, 64):
        s=objects.CityTile(pos=[i, 320+64])
        solid.add(s)
    groups=[heroes, villains, solid]
    for group in groups:
        for sprite in group.sprites():
            rendered.add(sprite)
    return [heroes, villains, solid, rendered, "AmberCity.ogg", bg_color]
