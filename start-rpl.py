import os, sys

list_file_dir = os.listdir(path = ".")
wag = 0

while len(list_file_dir) != wag:
	if list_file_dir[wag] == "RPL.py":
		if str(sys.platform) == "win32":
			start_command = 'python RPL.py < '
			break
		if str(sys.platform) == "linux":
			start_command = 'python3 RPL.py < '
			break
	if list_file_dir[wag] == "RPL.exe":
		if str(sys.platform) == "win32":
			start_command = "RPL.exe < "
			break
	wag += 1

while True:
	filename_rpl_for_start = str(input())
	if filename_rpl_for_start.find('.rpl'):
		os.system(f"{start_command}{filename_rpl_for_start}")