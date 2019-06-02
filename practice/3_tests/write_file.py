import random, time, io
with io.open("log2.txt", "a+") as file_obj:

	while True:

		rad = random.randint(1,255)
		ip = "192.168.1.{}".format(rad)
		print("writing {}".format(ip))
		file_obj.write(ip)
		file_obj.write("\n")
		time.sleep(3)
		file_obj.flush()