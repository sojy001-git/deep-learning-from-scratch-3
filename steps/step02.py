import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, in_data):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        return x ** 2


x = Variable(np.array(10)) #x.data=10
f = Square() #객체 생성
y = f(x) #Square()(x)==f.__call__(x) 호출  ... call은 f(x)로 되는데 forward는 f.forwrd(~~)
         #self=f, input=x, x'=x.data, y=f.forward(x.data)==f.forward(10)==100, output=Variable(100) 
         #y = Variable(100)
print(type(y))
print(y.data) #y.data = 100 
