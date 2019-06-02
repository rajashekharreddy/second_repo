class Foo(object):
    def __new__(cls, *args, **kwargs):
        print "Creating Instance"
        instance = super(Foo, cls).__new__(cls, *args, **kwargs)
        return instance
 
    def __init__(self, a, b):
    	print("Initializing")
        self.a = a
        self.b = b
 
    def bar(self):
        pass

i = Foo(2,3)

i.bar()



class AbstractClass(object):
 
    def __new__(cls, a, b):
        instance = super(AbstractClass, cls).__new__(cls)
        instance.__init__(a, b)
        return 3
 
    def __init__(self, a, b):
        print "Initializing Instance", a, b


a = AbstractClass(2, 3)

print(a)