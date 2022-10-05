from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
music=None
while True:
    xx=input('选择背景音乐:1、无，2、海阔天空，3、鸡你太美，4、Walk Thru Fire，5、Outside，6、ZombiesOnYourLawn')
    if xx==str(1):
        music=1
        break
    if xx==str(2):
        music=2
        break
    if xx==str(3):
        music=3
        break
    if xx==str(4):
        music=4
        break
    if xx==str(5):
        music=5
        break
    if xx==str(6):
        music=6
        break
bullet = None
window.title='亡牌飞行员'
class tk(Entity):
    def __init__(self,life=10):
        super().__init__(model='files/3d/tk.obj',parent=op,collider='box',rotation_y=90,position=(random.randint(-45,45),5,random.randint(-45,45)),sp=random.randint(33,80))
        self.life=life
    def update(self):
        self.z -= (player.sp - self.sp) / 100
        if self.z>230:
            self.z=-230
        if self.z<-230:
            self.z=230
        hit_info=self.intersects()
        if hit_info.hit:
            self.life-=0.3
        if abs(self.x-pdpd.x)<15 and abs(self.z-pdpd.z)<15 and pdpd.y!=-500:
            self.life-=0.2
        if not(self.life>0):
            tk()
            player.jf+=1
            destroy(self)
class jt(Entity):
    def __init__(self,life=100,time=random.randint(3,7)):
        super().__init__(model='files/3d/jt.obj',collider='box',parent=op,rotation_y=0,sp=random.randint(110,130))
        self.y=5
        if random.randint(1,2)==1:
            self.x=random.randint(-150,-45)
        else:
            self.x=random.randint(45,150)
        if random.randint(1,2)==1:
            self.z=random.randint(-150,-45)
        else:
            self.z=random.randint(45,150)
        self.life=life
        self.time=time
    def update(self):
        self.z -= (player.sp - self.sp) / 100
        if self.z>230:
            self.z=-230
        if self.z<-230:
            self.z=230
        if self.time>0:
            self.time-=0.01
        if self.time<0:
            self.time=0
        if self.time==0:
            invoke(Audio, 'files/music/fkp.wav')
            self.y+=6
            self.look_at(air)
            self.y-=6
            FKP(model="files/3d/fkp.obj",
                scale=0.1,
                color=color.lime,
                position=self.world_position+(0,6,0),
                rotation=self.rotation)
            self.rotation=(0,0,0)
            self.time=random.randint(3,7)
        hit_info=self.intersects()
        if hit_info.hit:
            self.life-=0.3
        if abs(self.x - pdpd.x) < 15 and abs(self.z - pdpd.z) < 15 and pdpd.y!=-500:
            self.life -= 1
        if not(self.life>0):
            jt()
            player.jf+=5
            destroy(self)
class fj(Entity):
    def __init__(self,life=40,time=random.randint(6,9)):
        super().__init__(model='files/3d/fj2.obj',parent=op,collider='box',rotation_y=0,sp=random.randint(150,250))
        self.y=random.randint(50,110)
        if random.randint(1,2)==1:
            self.x=random.randint(-150,-20)
        else:
            self.x=random.randint(20,150)
        if random.randint(1,2)==1:
            self.z=random.randint(-150,-20)
        else:
            self.z=random.randint(20,150)
        self.life=life
        self.time=time
    def update(self):
        self.z -= (player.sp - self.sp) / 100
        if self.z>230:
            self.z=-230
        if self.z<-230:
            self.z=230
        if self.time>0:
            self.time-=0.01
        if self.time<0:
            self.time=0
        if self.time==0 and self.world_x<player.x:
            for m in range(10):
                invoke(Audio, 'files/music/jq.wav')
                self.y += 6
                self.look_at(air)
                self.y -= 6
                FJQ(model="files/3d/zd.obj",
                    scale=0.05,
                    color=color.orange,
                    position=self.world_position + (0, 6, 0),
                    rotation=self.rotation)
                self.rotation = (0, 0, 0)
                self.time = random.randint(6, 8)
        hit_info=self.intersects()
        if hit_info.hit:
            self.life-=0.3
        if abs(self.x - pdpd.x) < 15 and abs(self.z - pdpd.z) < 15 and pdpd.y!=-500:
            self.life -= 2
        if not(self.life>0):
            fj()
            player.jf+=3
            destroy(self)
class PD(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        ray=raycast(self.world_position,self.forward,distance=self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            self.world_position += self.forward * self.speed * time.dt
            a = self.world_position
            destroy(self)
            invoke(Audio, 'files/music/boom.ogg')
            boom = Entity(model = 'cube',texture = 'files/image/boom.png',position = a,scale=3)
            pdpd.position=boom.position
            help.x=1
            destroy(boom,delay = 5)
class jyj(Entity):
    def __init__(self):
        super().__init__(model='files/3d/jyj.obj',parent=op,collider='box',rotation_y=0,sp=random.randint(200,320))
        self.y=random.randint(120,145)
        if random.randint(1,2)==1:
            self.x=random.randint(15,45)
        else:
            self.x=random.randint(-45,-15)
        self.z=-200
    def update(self):
        self.z -= (player.sp - self.sp) / 100
        if self.z>230:
            self.z=-230
        if self.z<-230:
            self.z=230
        if abs(self.world_x - player.x) < 15 and abs(self.world_z - player.z) < 15 and abs(self.world_y-player.y)<15:
            if pdsljs.x<5:
                pdsljs.x+=5
            else:
                pdsljs.x=10
            if zdsljs.x<700:
                zdsljs.x+=300
            else:
                zdsljs.x=1000
            if player.life<10:
                player.life+=1
            else:
                player.life=10
            jyj()
            destroy(self)
class FKP(Entity):
    def __init__(self,speed=450,lifetime=20,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        if time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            self.world_position += self.forward * self.speed * time.dt
            destroy(self,delay=0.25)
        if abs(myplane.x-self.world_position[0])<2.5 and abs(myplane.y-self.world_position[1])<2.5 and abs(myplane.z-self.world_position[2])<2.5:
            player.life-=1
            self.world_position += self.forward * self.speed * time.dt
            a = self.world_position
            destroy(self)
            invoke(Audio, 'files/music/boom.ogg')
            boom = Entity(model='cube', texture='files/image/boom.png', position=a, scale=3)
            destroy(boom, delay=5)
class FJQ(Entity):
    def __init__(self,speed=500,lifetime=5,**kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
    def update(self):
        if time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            self.world_position += self.forward * self.speed * time.dt
            destroy(self,delay=0.25)
        if abs(myplane.x-self.world_position[0])<5 and abs(myplane.y-self.world_position[1])<5 and abs(myplane.z-self.world_position[2])<5:
            player.life-=0.05
            self.world_position += self.forward * self.speed * time.dt
            destroy(self)
def input(key):
    if key == "escape":
        quit()
    if key == "z":
        sy.x=1
    if key == "x":
        sy.x=2
        invoke(Audio, 'files/music/p.ogg')
    if key == "f"and pdsljs.x>0:
        pdsljs.x-=1
        invoke(Audio, 'files/music/fs.wav')
        PD(model="files/3d/hjd.obj",
           scale=0.5,
           position=player.camera_pivot.world_position,
           rotation=player.camera_pivot.world_rotation)
def update():
    if held_keys['w'] and water.y>-150:
        water.y -= 0.3
        if water.rotation_x<20:
            water.rotation_x+=0.5
    if held_keys['s'] and water.y<-30:
        water.y += 0.3
        if water.rotation_x > -30:
            water.rotation_x -= 0.5
    if water.rotation_x!=0 and not (held_keys['w']or held_keys['s']):
        if water.rotation_x<0:
            water.rotation_x+=0.2
        if water.rotation_x>0:
            water.rotation_x-=0.2
    if held_keys['q'] and player.sp<340.1:
        player.sp+=0.5
    if held_keys['e'] and player.sp>33:
        player.sp-=0.5
    if held_keys['a'] and water.rotation_z<30:
        water.rotation_z+=0.5
    if held_keys['d'] and water.rotation_z>-30:
        water.rotation_z-=0.5
    if water.rotation_z!=0 and not (held_keys['a']or held_keys['d']):
        if water.rotation_z<0:
            water.rotation_z+=0.2
        if water.rotation_z>0:
            water.rotation_z-=0.2
    player.high = (player.y-water.y)*20
    playerhigh.text =('high:' + str(round(player.high, 3)) + 'M')
    playerspkm.text = ('speed:' + str(round(player.sp*3.6, 1)) + 'KM/h')
    playerspm.text = ('speed:' + str(round(player.sp, 1)) + 'M/s')
    temperature.text = ('Temperature:' + str(round(31-((player.high-300)/270), 1)) + '°C')
    zdsl.text = ('zidan:' + str(int(zdsljs.x)) + '/1000')
    pjfs.text = ('jifen:'+str(int(player.jf)))
    pdsl.text = ('paodan:' + str(int(pdsljs.x)) + '/10')
    plife.text = ('life:' + str(int(player.life)))
    op.position=water.position+(0,1,0)
    op.rotation=(water.rotation_x,op.rotation_y,water.rotation_z)
    if sy.x==1:
        myplane.position=player.position+(0,-8,0)
    if sy.x==2:
        myplane.position=player.position+(0,-3,0)
    if held_keys['left mouse']and zdsljs.x>0:
        global bullet
        bullet = Entity(parent=player, model='files/3d/zd.obj', scale=.1, collider='box',color=color.orange,world_rotation=player.camera_pivot.world_rotation)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position + (bullet.forward*2500), curve=curve.linear, duration=1)
        invoke(Audio, 'files/music/jq.wav')
        zdsljs.x-=1
        destroy(bullet, delay=5)
    player.y=air.y
    if pdpd.y != -500:
        if pdpd.rotation_z < 0:
            pdpd.rotation_z = 0
        if pdpd.rotation_z != 0:
            pdpd.rotation_z -= 0.01
        if pdpd.rotation_z == 0:
            pdpd.y = -500
            pdpd.rotation_z = 0.2
    if int(player.life)==0 and player.jf<100 and lfpd.x==0:
        invoke(Audio, 'files/music/no.ogg')
        lfpd.x=1
    if player.jf>99 and int(player.life)>0 and lfpd.y==0:
        invoke(Audio, 'files/music/winmusic.ogg')
        lfpd.y = 1
app=Ursina()
player = FirstPersonController(speed=0,y=0.5,high=1000,sp=70,jf=0,life=10)
Sky()
myplane=Entity(model='files/3d/fj1.obj',rotation=(0,-90,0),texture="wb.png")
sy=Entity(model='cube',texture='air.png')
water = Entity(model = 'cube',scale = (250,1,250),color = color.white,texture = "water.png",texture_scale = (250,250),position=(0,-50,0),collider="box")
air = Entity(model = 'cube',scale = (0.1,1,0.1),texture = "air.png",texture_scale = (1,1),collider="box")
op = Entity(model = 'cube',texture = "air.png")
playerhigh = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.46))
playerspkm = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.4))
playerspm = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.34))
temperature = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.28))
zdsl = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.22))
zdsljs=Entity(model='cube',texture='air.png',position=(1000,0,0))
pjfs = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.1))
pdpd=Entity(model = 'cube',texture = "air.png",position=(0,-500,0),rotation_z=0.2)
help = Entity(model = 'cube',texture = "air.png")
pdsl = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.16))
pdsljs=Entity(model='cube',texture='air.png',position=(10,0,0))
plife = Button(scale=(0.3,0.05),text_scale=3,text_color=color.white,text='text',position=(0.5,-0.04))
lfpd=Entity(model='cube',texture='air.png')
invoke(Audio, 'files/music/fj.wav',loop=True)
if music==2:
    invoke(Audio, 'files/music/hktk.mp3', loop=True)
if music==3:
    invoke(Audio, 'files/music/jntm.mp3', loop=True)
if music==4:
    invoke(Audio, 'files/music/Walk Thru Fire.mp3', loop=True)
if music==5:
    invoke(Audio, 'files/music/outside.mp3', loop=True)
if music==6:
    invoke(Audio, 'files/music/ZombiesOnYourLawn.ogg', loop=True)
tk()
tk()
tk()
tk()
tk()
jt()
jt()
fj()
fj()
fj()
fj()
fj()
fj()
fj()
jyj()
sy.x=1
app.run()