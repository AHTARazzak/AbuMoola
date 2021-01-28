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
from tkinter import *
from tkinter.font import Font
import os.path, pathlib, random, time, os, sys
from datetime import datetime

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

with open(str(working_directory) + "/random_deco/greetings.txt", "r") as the_greetings:
	greetings_contents = the_greetings.read().split("\n")
	the_greeting = random.choice(greetings_contents[:-1])

master = Tk()
master.wm_title("AbuMoola")
master.geometry('1000x800'.format(1000, 800))
master.configure(bg = 'black')
#master.grid_columnconfigure(0, weight=5)
now = datetime.now()

title = Label(master, font = ("Times", 80), foreground='white', bg='black', text = str(the_greeting), height = 1, width = 40)
title.grid(row = 0, column = 0, columnspan = 10)

user_name = Label(master, font = ("Times", 150), foreground='white', bg='black', text = str(user_alias), height = 1, width = 20)
user_name.grid(row = 1, column = 0, columnspan = 10)

the_date = Label(master, font = ("Times", 50), foreground='white', bg='black', height = 1, text = time.strftime("%d/%m/%Y"), width = 10)
the_date.grid(row = 3, column = 0, columnspan = 6)

the_time = Label(master, font = ("Times", 50), foreground='white', bg='black', height = 1)
the_time.grid(row = 3, column = 3, columnspan = 6)
time1=""
def main_clock():
    global time1
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1:
        time1=time2
        the_time.config(text=time2, width = 10)
    the_time.after(200, main_clock)

master.grid_rowconfigure(4, minsize=100)

finance_but = Button(master, text="Finances", font=("system", 50), width = 20, height = 4)#, command=calander)
finance_but.grid(row=5, column=0, columnspan = 5)

contact_but = Button(master, text="Contacts", font=("system", 50), width = 20, height = 4)#, command=calander)
contact_but.grid(row=5, column=4, columnspan = 5)

master.grid_rowconfigure(6, minsize=100)

github_but = Button(master, text="Github", font=("system", 50), width = 51, height = 3)#, command=calander)
github_but.grid(row=8, column=2, columnspan = 5)

master.grid_rowconfigure(9, minsize=120)

github_but = Label(master, text="AbuMoola (version 0) by AHTAR", foreground='white', bg='black', font=("system", 40), height = 1)#, command=calander)
github_but.grid(row=10, column=0, columnspan = 5)

main_clock()
master.mainloop()
