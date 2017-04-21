#!/usr/bin/env python
# -*- coding: utf-8 -*-

#所谓单例，是指一个类从始至终只能创建一次；
#方法1：实现__new__方法  
#如果想使得某个类从始至终最多只有一个实例，使用__new__方法会很简单。Python中类是通过__new__来创建实例的：  
#并在将一个类的实例绑定到类变量_instance上,  
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
#如果cls._instance不为None,直接返回cls._instance

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_inst'):
            cls._inst=super(Singleton,cls).__new__(cls,*args,**kwargs)
            return cls._inst

class A(Singleton):
    def __init__(self,s):
        self.s=s 
            

print '1st method: __new__'
a=A('apple')  
b=A('banana')
print id(a),a.s
print id(b),b.s



#方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)  
#同一个类的所有实例天然拥有相同的行为(方法),  
#只需要保证同一个类的所有实例具有相同的状态(属性)即可  
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)  
#可参看:http://code.activestate.com/recipes/66531/ 

class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'
        self.age = 1

    def __str__(self):
        return self.state, self.age
    

class YourBorg(Borg):
    pass


print '2nd method:'
rm1 = Borg()
rm2 = Borg()

rm1.state = 'Idle'
rm1.age = 20
rm2.state = 'Running'
rm2.age = 30

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))

rm2.state = 'Zombie'

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))

print('rm1 id: {0}'.format(id(rm1)))
print('rm2 id: {0}'.format(id(rm2)))

rm3 = YourBorg()

print('rm1: {0}'.format(rm1))
print('rm2: {0}'.format(rm2))
print('rm3: {0}'.format(rm3))

### OUTPUT ###
# rm1: Running
# rm2: Running
# rm1: Zombie
# rm2: Zombie
# rm1 id: 140732837899224
# rm2 id: 140732837899296
# rm1: Init
# rm2: Init
# rm3: Init