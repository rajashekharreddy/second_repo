class A(object):
	pass

class B(A):
	pass

class C(A):
	pass

class D(B,C):
	pass

#obj_D = D()
#print(obj_D)

#import inspect
#print(inspect.getmro(D))

print(D.mro())