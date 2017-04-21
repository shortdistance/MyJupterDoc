# 这里肯定要做深拷贝，要不然python的就是对象的引用
from copy import deepcopy

class Prototype:
    def __init__(self):
        self._objs = {}

    def registerObject(self, name, obj):
        """注册对象"""
        self._objs[name] = obj

    def unregisterObject(self, name):
        """取消注册"""
        del self._objs[name]

    def clone(self, name, **attr):
        """克隆对象"""
        obj = deepcopy(self._objs[name])
        # 但是会根据attr增加或覆盖原对象的属性
        obj.__dict__.update(attr)
        return obj

if __name__ == '__main__':
    class A:
        pass

    a=A()
    prototype=Prototype()
    prototype.registerObject("a",a)
    prototype.registerObject("name", 32)
    b=prototype.clone("a",a=1,b=2,c=3)

    # 这里会返回对象a
    print prototype._objs
    print prototype.__dict__
    
    print b
    print b.__dict__
    # 这里的对象其实已经被修改成(1, 2, 3)
    print(b.a, b.b, b.c)