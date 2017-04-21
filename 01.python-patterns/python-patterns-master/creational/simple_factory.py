#coding:utf-8
#通过一个工厂来决定创建哪种具体的产品实例。
#Description:
    # 1. 存在一个基类Base
    # 2. 各种“产品”类基于Base
    # 3. “产品”都具有相同的功能， 但是“产品”相同功能的作用有一定差异。
    # 4. 创建“产品”的工厂方法： 根据用户输入的参数，返回该参数对应“产品”类的实例化对象。
    # 5. 调用该“产品”类的实例化对象的方法， 执行对应的操作。
# Elements:
    # 1. 工厂函数 create_XXXX(string)
    # 2. 产品的抽象接口或抽象类
    # 3. 具体产品类

    
def create_operator(op):
    if op == '+':
        return AddOperation()
    elif op == '-':
        return SubOperation()
    elif op ==  '*':
        return MulOperation()
    elif op == '/':
        return DivOperation()
    
class Operation:
    def Calc(self):
        pass


class AddOperation(Operation):
    def Calc(self, x, y):
        return x + y
    
class SubOperation(Operation):
    def Calc(self, x, y):
        return x - y
    
class MulOperation(Operation):
    def Calc(self, x, y):
        return x * y
    
class DivOperation(Operation):
    def Calc(self, x, y):
        return x / y

op = create_operator('/')
op.Calc(1, 2)