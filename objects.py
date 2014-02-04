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
        t_group=kw[target]
        x=pygame.sprite.spritecollide(self, t_group, False)
        if x:
            for sprite in x:
                sprite.hp-=self.battle
                self.hp-=self.battle
        xspeed, yspeed = direction
        self.rect.left += xspeed * self.speed
        self.rect.top += yspeed * self.speed
        self.hp-=self.rm_rate
class PoliceEnemy(GObject):
    def __init__(self, pos):
        self.battle=5
        img_name="PoliceEnemy.png"
        img_domain="images"
        hp=20
        super(PoliceEnemy, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        if random.random() < 0.075:
            shots=random.randrange(0, self.battle)
            for i in range(shots):
                proj=Projectile("BulletL.png", "images", self.rect.topleft, 5, 10, 128, 4, [-1, 0], "heroes")
                kw["others"].add(proj)
                kw["rendered"].add(proj)
        x=pygame.sprite.spritecollide(self, kw["solid"], False)
        if not x:
            self.rect.top+=3
class PoliceGood(GObject):
    def __init__(self, pos):
        self.battle=5
        img_name="PoliceGood.png"
        img_domain="images"
        hp=20
        super(PoliceEnemy, self).__init__(img_name, img_domain, pos, hp)
    def update_callback(self, kw):
        if random.random() < 0.075:
            shots=random.randrange(0, self.battle)
            for i in range(shots):
                proj=Projectile("BulletR.png", "images", self.rect.topleft, 5, 10, 128, 4, [1, 0], "villains")
                kw["others"].add(proj)
                kw["rendered"].add(proj)
        x=pygame.sprite.spritecollide(self, kw["solid"], False)
        if not x:
            self.rect.top+=3
class SolidTile(GObject):pass
class CityTile(GObject):
    def __init__(self, pos):
        img_name="CityTile.png"
        super(CityTile, self).__init__(img_name, "images", pos)
        
