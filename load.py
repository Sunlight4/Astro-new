import pygame, random, resources
def loadroom(room):
    pygame.init()
    mixer=pygame.mixer
    mixer.init()
    music=mixer.music
    heroes, villains, solid, rendered, music_name, bg=room()
    print villains.sprites()
    path=resources.get_resource_path(music_name, "music")
    music.load(path)
    music.set_volume(0.5)
    music.play(-1)
    others=pygame.sprite.Group()
    pygame.key.set_repeat(10, 10)
    screen=pygame.display.set_mode([640,480])
    fill=screen.fill
    blit=screen.blit
    flip=pygame.display.flip
    load=pygame.image.load
    clock=pygame.time.Clock()
    groups=[heroes, villains, others]
    while True:
        screen.fill(bg)
        rendered.draw(screen)
        clock.tick(30)
        events=pygame.event.get()
        for i in groups:
            i.update({"heroes":heroes, "others":others, "rendered":rendered,
                      "solid":solid, "events":pygame.event.get()})
        rendered.draw(screen)
        flip()
