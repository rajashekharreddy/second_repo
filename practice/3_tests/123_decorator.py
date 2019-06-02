

def decorated(fun):

	def inner():

		print("Innser Start")
		fun()
		print("Inner Stop")

	return inner

@decorated
def wrapper():

	print("Wrapper Start")
	import time
	print(time.timezone)
	print("Wrapper done")

wrapper()
