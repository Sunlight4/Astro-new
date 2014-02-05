import pygame, resources, random
class GObject(pygame.sprite.Sprite):
    def __init__(self, img_name, img_domain="images", pos=[0,0], hp=1):
        img=resources.get_resource_path(img_name, img_domain)
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()
        self.rect.left, self.rect.top = pos
        self.hp=hp
        super(GObject, self).__init__()
    def update_callback(self, kw):pass
    def update(self, kw):
        if self.hp<=0:self.kill()
        else:
            groups=self.groups()
            for i in groups:i.remove(self)
            self.update_callback(kw)
            for i in groups:i.add(self)
class Projectile(GObject):
    def __init__(self, img_name, img_domain, pos, battle, hp, distance, speed, direction, target):
        self.rm_rate=hp/float(distance)
        self.battle=battle
        self.speed=speed
        self.target=target
        self.direction=direction
        super(Projectile, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        t_group=kw[self.target]
        x=pygame.sprite.spritecollide(self, t_group, False)
        if x:
            for sprite in x:
                sprite.hp-=self.battle
                self.hp-=self.battle
        xspeed, yspeed = self.direction
        self.rect.left += xspeed * self.speed
        self.rect.top += yspeed * self.speed
        self.hp-=self.rm_rate
class PoliceEnemy(GObject):
    def __init__(self, pos):
        self.battle=2
        img_name="PoliceEnemy.png"
        img_domain="images"
        hp=25
        super(PoliceEnemy, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        if random.random() < 0.025:
            shots=random.randrange(0, self.battle)
            for i in range(shots):
                proj=Projectile("BulletL.png", "images", self.rect.topleft, 2, 10, 128, 4, [-1, 0], "heroes")
                kw["others"].add(proj)
                kw["rendered"].add(proj)
        x=pygame.sprite.spritecollide(self, kw["solid"], False)
        if not x:
            self.rect.top+=3
class PoliceGood(GObject):
    def __init__(self, pos):
        self.battle=2
        img_name="PoliceGood.png"
        img_domain="images"
        hp=25
        super(PoliceGood, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        if random.random() < 0.025:
            shots=random.randrange(0, self.battle)
            for i in range(shots):
                proj=Projectile("BulletR.png", "images", self.rect.topleft, 2, 10, 128, 4, [1, 0], "villains")
                kw["others"].add(proj)
                kw["rendered"].add(proj)
        x=pygame.sprite.spritecollide(self, kw["solid"], False)
        if not x:
            self.rect.top+=3
class Astro(GObject):
    def __init__(self, pos):
        self.battle=5
        self.attack=1
        img_name="Astro.png"
        img_domain="images"
        hp=100
        self.jump=16
        super(Astro, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        events=kw["events"]
        print len(events)
        attacking=False
        for i in events:
            print i
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LEFT:
                    self.rect.left-=3
                elif i.key==pygame.K_RIGHT:
                    self.rect.left+=3
                elif i.key==pygame.K_UP:
                    if self.jump > 0:
                        self.rect.top -= 12
                        self.jump-=1
                elif i.key==pygame.K_z:
                    if self.attack >= 1:
                        self.attack=0
                        attacking=True
        if attacking:
            shots=random.randrange(0, self.battle)
            for i in range(shots):
                proj=Projectile("BulletR.png", "images", self.rect.topleft, 1, 2, 128, 8, [1, 0], "villains")
                kw["others"].add(proj)
                kw["rendered"].add(proj)
        else:
            if self.attack < 1:
                self.attack+=0.1
            
        x=pygame.sprite.spritecollide(self, kw["solid"], False)
        if not x:
            self.rect.top+=3
        else:
            self.jump=16
class SolidTile(GObject):pass
class CityTile(GObject):
    def __init__(self, pos):
        img_name="CityTile.png"
        super(CityTile, self).__init__(img_name, "images", pos)
        
