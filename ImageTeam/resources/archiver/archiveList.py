import sys
import archiver as Archiver
import re
import time

def main(args):
        print(args)

	try:
		assert len(args) == 4
		inFile = args[1]
		duration = int(args[2])
		interval = float(args[3])
	except:
		print("Call Syntax: python archiveList.py <Input File> <Duration> <Interval>")
		return

	try:
		f = open(inFile, "r")
		id_list = list(f)
	except:
		print("Input File couldn't be opened")
		return

		

	start_timestamp = time.time()
	while (time.time() - start_timestamp) < duration:
		frame_timestamp = time.time()
		for cam in id_list:
			cam = re.search(r'(?P<ID>[\d]*) (?P<Type>[\S]*)', cam)
			argsIN = [None, cam.group("ID"), cam.group("Type"), 1, 1]
			try:
				Archiver.archiver(argsIN)
				
			except Exception, e:
				print e



		# Sleep until the interval between frames ends.
		time_to_sleep = interval - (time.time() - frame_timestamp)
		if time_to_sleep > 0:
			time.sleep(time_to_sleep)


if __name__ == '__main__':
	main(sys.argv)
