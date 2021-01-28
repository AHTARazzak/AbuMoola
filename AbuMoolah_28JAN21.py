#
#     $$$$$$\  $$\                 $$\      $$\                     $$\           $$\
#    $$  __$$\ $$ |                $$$\    $$$ |                    $$ |          $$ |
#    $$ /  $$ |$$$$$$$\  $$\   $$\ $$$$\  $$$$ | $$$$$$\   $$$$$$\  $$ | $$$$$$\  $$$$$$$\
#    $$$$$$$$ |$$  __$$\ $$ |  $$ |$$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ | \____$$\ $$  __$$\
#    $$  __$$ |$$ |  $$ |$$ |  $$ |$$ \$$$  $$ |$$ /  $$ |$$ /  $$ |$$ | $$$$$$$ |$$ |  $$ |
#    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |
#    $$ |  $$ |$$$$$$$  |\$$$$$$  |$$ | \_/ $$ |\$$$$$$  |\$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |
#    \__|  \__|\_______/  \______/ \__|     \__| \______/  \______/ \__| \_______|\__|  \__|
#    By AHTAR
#
########### TO DO ######################################
#Landing page with randomly generated greeting
#Landing page hosts time
#MrMoola version, github link button corner
#Hosts buttons for Contcts and finances
########### LIBRARIES ##################################
from PySide6 import QtCore, QtWidgets, QtGui
import os.path
import pathlib
import random

working_directory = pathlib.Path(__file__).parent.absolute()
user_detail = str(working_directory) + "/user_data/"

try:
	user_detail = open(user_detail + "/user_details.txt", "r")
except:
	print("Please provide details (will need to enter once)")
	your_alias = input("How would you like Abu Moolah to address you? (< 20 characters please): ")
	while len(your_alias) > 20:
		your_alias = input("How would you like Abu Moolah to address you? (< 20 characters please): ")
	detail_file = os.path.join(user_detail + "user_details.txt")
	detail_file_open = open(detail_file, "w")
	detail_file_open.write("HATHAHEA-ALIAS " + your_alias)
	detail_file_open.close()

for line in user_detail:
	if "HATHAHEA-ALIAS" in line:
		user_alias = line.split()[1]


master = Tk(className="HOME")
master.wm_title("AbuMoola")
master.geometry('650x800'.format(900, 900))
master.configure(bg='black')

title = Label(master, text="Abu Moola",anchor='w')
title.configure(foreground='white',bg='black',font=("Times",250),anchor='w')
title.grid(row=0,column=0,columnspan=5)