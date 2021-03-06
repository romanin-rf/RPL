import os, sys, pickle, time, configparser

config_data = configparser.ConfigParser()
config_data.read('config.ini')

if sys.platform == "win32":
	os.system("title {0}".format(config_data.get("names", "name")))

data = {"varing": {}, "libs": {}}
work = True

while work:
	try:
		command_user = str(input())
	except:
		break
	while True:
		if command_user.startswith('text '):
			if not(len(command_user) <= 5):
				if command_user[5] == "'":
					if command_user[len(command_user) - 1] == ";":
						wag_command_text = 6
						start_wag_text_command = wag_command_text
						while wag_command_text != len(command_user):
							if command_user[wag_command_text] == "'":
								end_wag_text_command = wag_command_text
								break
							wag_command_text += 1
						text_output_command = command_user[start_wag_text_command:end_wag_text_command]
						print(text_output_command, end = "")
						break
		if command_user.startswith('textln '):
			if not(len(command_user) <= 7):
				if command_user[7] == "'":
					if command_user[len(command_user) - 1] == ";":
						wag_command_text = 8
						start_wag_text_command = wag_command_text
						while wag_command_text != len(command_user):
							if command_user[wag_command_text] == "'":
								end_wag_text_command = wag_command_text
								break
							wag_command_text += 1
						text_output_command = command_user[start_wag_text_command:end_wag_text_command]
						print(text_output_command)
						break
		if command_user.startswith('vartext '):
			if not(len(command_user) <= 8):
				if command_user[len(command_user) - 1] == ";":
					wag_command_textvar = 8
					start_wag_textvar_command = wag_command_textvar
					end_wag_textvar_command = len(command_user) - 1
					vartext_out_comannd = data["varing"]["{0}".format(command_user[start_wag_textvar_command:end_wag_textvar_command])]
					print(vartext_out_comannd, end = "")
					break
		if command_user.startswith('vartextln '):
			if not(len(command_user) <= 10):
				if command_user[len(command_user) - 1] == ";":
					wag_command_textvar = 10
					start_wag_textvar_command = wag_command_textvar
					end_wag_textvar_command = len(command_user) - 1
					vartext_out_comannd = data["varing"]["{0}".format(command_user[start_wag_textvar_command:end_wag_textvar_command])]
					print(vartext_out_comannd)
					break
		if command_user.startswith('varstr '):
			if not(len(command_user) <= 7):
				if command_user[len(command_user) - 1] == ";":
					wag_command_varstr = 7
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == "=":
							wag_command_varstr += 1
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					name_new_varstr = '{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command])
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == ";":
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					var_naw_varstr = str('{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command]))
					data["varing"]["{0}".format(name_new_varstr[0:(len(name_new_varstr) - 1)])] = var_naw_varstr
					break
		if command_user.startswith('varint '):
			if not(len(command_user) <= 7):
				if command_user[len(command_user) - 1] == ";":
					wag_command_varstr = 7
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == "=":
							wag_command_varstr += 1
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					name_new_varstr = '{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command])
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == ";":
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					var_naw_varstr = int('{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command]))
					data["varing"]["{0}".format(name_new_varstr[0:(len(name_new_varstr) - 1)])] = var_naw_varstr
					break
		if command_user.startswith('varfloat '):
			if not(len(command_user) <= 9):
				if command_user[len(command_user) - 1] == ";":
					wag_command_varstr = 9
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == "=":
							wag_command_varstr += 1
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					name_new_varstr = '{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command])
					start_wag_varstr_command = wag_command_varstr
					while wag_command_varstr != len(command_user):
						if command_user[wag_command_varstr] == ";":
							end_wag_varstr_command = wag_command_varstr
							break
						wag_command_varstr += 1
					var_naw_varstr = float('{0}'.format(command_user[start_wag_varstr_command:end_wag_varstr_command]))
					data["varing"]["{0}".format(name_new_varstr[0:(len(name_new_varstr) - 1)])] = var_naw_varstr
					break
		if command_user.startswith('del '):
			if not(len(command_user) <= 3):
				if command_user[len(command_user) - 1] == ";":
					if str(command_user[4:(len(command_user) - 1)]) in data["varing"]:
						del data["varing"]["{0}".format(str(command_user[4:(len(command_user) - 1)]))]
		if command_user.startswith('sleep '):
			if not(len(command_user) <= 6):
				if command_user[len(command_user) - 1] == ";":
					wag_command_sleep = 6
					start_wag_sleep_command = wag_command_sleep
					end_wag_sleep_command = len(command_user) - 1
					work_sleep_command = False
					try:
						varing_time_sleep_command = int(command_user[start_wag_sleep_command:end_wag_sleep_command])
						work_sleep_command = True
					except ValueError:
						try:
							varing_time_sleep_command = float(command_user[start_wag_sleep_command:end_wag_sleep_command])
							work_sleep_command = True
						except ValueError:
							if str(command_user[start_wag_sleep_command:end_wag_sleep_command]) in data["varing"]:
								if type(data["varing"][str(command_user[start_wag_sleep_command:end_wag_sleep_command])]) == int:
									varing_time_sleep_command = int(data["varing"][str(command_user[start_wag_sleep_command:end_wag_sleep_command])])
									work_sleep_command = True
								else:
									if type(data["varing"][str(command_user[start_wag_sleep_command:end_wag_sleep_command])]) == float:
										varing_time_sleep_command = float(data["varing"][str(command_user[start_wag_sleep_command:end_wag_sleep_command])])
										work_sleep_command = True
					if work_sleep_command:
						time.sleep(varing_time_sleep_command)
		if command_user.startswith('save '):
			if not(len(command_user) <= 4):
				wag_command_namefile = '{0}.rpld'.format(command_user[5:(len(command_user))])
				open_file_data = open(wag_command_namefile, 'wb')
				pickle.dump(data, open_file_data)
				open_file_data.close()
			break
		if command_user.startswith('load '):
			if not(len(command_user) <= 4):
				wag_command_namefile = '{0}.rpld'.format(command_user[5:(len(command_user))])
				open_file_data = open(wag_command_namefile, 'rb')
				data = pickle.load(open_file_data)
				open_file_data.close()
			break
		if command_user == 'dirdata':
			print(data)
			break
		if command_user == 'cwin':
			if str(sys.platform) == "win32":
				os.system("cls")
			else:
				if str(sys.platform) == "linux":
					os.system("clear")
			break
		if command_user == 'cdata':
			data = {"varing": {}, "libs": {}}
			break
		if command_user == 'exit':
			work = False
		if command_user == 'info':
			print("-------------------------------------------")
			print("> Name: {0}".format(config_data.get("names", "name")))
			print(">> Name Author: {0}".format(config_data.get("names", "name-author")))
			print(">>> Version: {0}".format(config_data.get("settings", "version")))
			print("-------------------------------------------")
			break
		else:
			break