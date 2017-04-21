#abstract factory
class BulletClip:
    def __init__(self, size=1):
        self.stack = []
        self.size = size;
        self.top = -1

    def setSize(self, size):
        self.size = size;
        
    def getCurrLen(self):
        return len(self.stack)

    def push(self, element):
        if self.isFull():
            raise "StackOverflow"
        else:
            self.stack.append(element)
            self.top = self.top + 1

    def pop(self):
        if self.isEmpty():
            raise "StackUnderflow"
        else:
            element = self.stack[-1]
            self.top = self.top - 1;
            del self.stack[-1]
            return element

    def Top(self):
        return self.top

    def empty(self):
        self.stack = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False
    

class Gun(object):
    def __init__(self, bulletClipSize, name='Gun'):
        self.BulletClip = BulletClip(bulletClipSize)
        self.name = name
    
    def loadBullet(self, bullet):
        print '%s loads bullet %s' % ( self.name, bullet)
        self.BulletClip.push(bullet)
        
    def shootBullet(self):
        bullet = self.BulletClip.pop()
        print '%s shoots bullet: %s' % (self.name, bullet)
        
    def showBulletCount(self):
        print '%s have %d bullets left' % (self.name, self.BulletClip.getCurrLen())
        

class Bullet(object):
    def __init__(self, name, size, quality):
        self.name = name
        self.size = size 
        self.quality = quality

        
class AK47(Gun):
    def __init__(self, bulletClipSize=20, name='AK47'):
        super(AK47, self).__init__(bulletClipSize, name)
        
        
class DesertEagle(Gun):
    def __init__(self, bulletClipSize=5, name='DesertEagle'):
        super(DesertEagle, self).__init__(bulletClipSize, name)
        
        
class AK47Bullet(Bullet):
    def __init__(self, name='AK47Bullet', size='Mid', quality='Silver'):
        super(AK47Bullet, self).__init__(name, size, quality)
        
        
class DesertEagleBullet(Bullet):
    def __init__(self, name='DesertEagleBullet', size='Large', quality='Godden'):
        super(DesertEagleBullet, self).__init__(name, size, quality)
        

        
class WeaponFactory(object):
    def createGun(self):
        pass
    
    def createBullet(self):
        pass
    
class AK47Factory(WeaponFactory):
    def createGun(self):
        return AK47()
    
    def createBullet(self):
        return AK47Bullet()

    
class DesertEagleFactory(WeaponFactory):
    def createGun(self):
        return DesertEagle()
    
    def createBullet(self):
        return DesertEagleBullet()
    
if __name__ == "__main__":
    ak47 = AK47Factory().createGun()
    ak47_bullet_1 = AK47Factory().createBullet()
    ak47_bullet_2 = AK47Factory().createBullet()
    ak47_bullet_3 = AK47Factory().createBullet()
    
    ak47.loadBullet(ak47_bullet_1)
    ak47.loadBullet(ak47_bullet_2)
    ak47.loadBullet(ak47_bullet_3)
    
    ak47.showBulletCount()
    ak47.shootBullet()
    ak47.showBulletCount()
    
    desert_eagle = DesertEagleFactory().createGun()
    desert_eagle_bullet = DesertEagleFactory().createBullet()
    
    desert_eagle.loadBullet(desert_eagle_bullet)
    desert_eagle.showBulletCount()
    desert_eagle.shootBullet()
    desert_eagle.showBulletCount()
    
    
