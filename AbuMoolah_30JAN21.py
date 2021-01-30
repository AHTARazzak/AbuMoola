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
from tkinter import scrolledtext
import os.path, pathlib, random, time, os, sys
from datetime import datetime

########### GLOBALS ##################################
global the_version
the_version = "AbuMoola (version 0) by AHTAR"

########### FUNCTIONS ##################################
def contact_page(page_open):
    page_open.destroy()
    contacts = Tk()
    contacts.wm_title("AbuMoola - Contacts")
    contacts.configure(bg = 'black')

    Label(contacts, font = ("Times", 120), foreground = 'white', bg = 'black', text = user_alias + " Contacts").grid(row = 0, column = 1, columnspan = 8)

    contacts.grid_rowconfigure(1, minsize = 30)

    con_updates = StringVar()
    con_update_panel = Label(contacts, font = ("Times", 50), foreground = 'white', bg = 'black', textvariable = con_updates).grid(row = 1, column = 1, columnspan = 8)

    contacts.grid_rowconfigure(3, minsize = 30)

    Button(contacts, font = ("Times", 50), height = 2, width = 5, text = "Add", command = lambda : contact_add(first_text.get(), last_text.get(), address_text.get(), num_1_text.get(), num_2_text.get(), email_text.get(), insta_text.get(), extra_text.get(), con_updates)).grid(row = 2, column = 0, rowspan = 2)

    first_text = StringVar()
    first_name_ent = Entry(contacts, textvariable = first_text, font = ('Verdana',60), width = 10).grid(row = 2, column = 1, columnspan = 1)
    first_text.set("First Name")

    last_text = StringVar()
    last_name_ent = Entry(contacts, textvariable = last_text, font = ('Verdana',60), width = 10).grid(row = 3, column = 1, columnspan = 1)
    last_text.set("Last Name")

    address_text = StringVar()
    addr_ent = Entry(contacts, textvariable = address_text, font = ('Verdana',60), width = 28).grid(row = 2, column = 2, columnspan = 2)
    address_text.set("Address")

    num_1_text = StringVar()
    n1_ent = Entry(contacts, textvariable = num_1_text, font = ('Verdana',60), width = 14).grid(row = 3, column = 2, columnspan = 1)
    num_1_text.set("Number #1")

    num_2_text = StringVar()
    n2_ent = Entry(contacts, textvariable = num_2_text, font = ('Verdana',60), width = 14).grid(row = 3, column = 3, columnspan = 1)
    num_2_text.set("Number #2")

    email_text = StringVar()
    email_ent = Entry(contacts, textvariable = email_text, font = ('Verdana',60), width = 15).grid(row = 2, column = 4, columnspan = 1)
    email_text.set("Email")

    insta_text = StringVar()
    insta_ent = Entry(contacts, textvariable = insta_text, font = ('Verdana',60), width = 15).grid(row = 3, column = 4, columnspan = 1)
    insta_text.set("Instagram")

    extra_text = StringVar()
    extra_ent = Entry(contacts, textvariable = extra_text, font = ('Verdana',60), width = 15).grid(row = 2, column = 5, columnspan = 2)
    extra_text.set("Extra")

    Button(contacts, font = ("Times", 50), height = 1, width = 5, text = "Remove", command = lambda : contact_remove(rem_text.get(), con_updates)).grid(row = 3, column = 5, rowspan = 1)
    rem_text = StringVar()
    rem_ent = Entry(contacts, textvariable = rem_text, font = ('Verdana',60), width = 6).grid(row = 3, column = 6, columnspan = 1)
    rem_text.set("ID")

    try:
        contact_detail_read = open(user_detail_path + "/contacts_details.txt", "r")
        contacts_to_show = "ID|FirstName|LastName|Addresss|#1|#2|Email|Insta|Extra\n" + contact_detail_read.read()
        con_output = scrolledtext.ScrolledText(contacts, height=10)
        con_output.grid(column=1, row=4, columnspan = 6)
        con_output.configure(background="white", foreground = "black", font = ("Times", 50), wrap= 'word')
        con_output.insert(END, contacts_to_show)
    except:
        con_updates.set("No list of contacts to show")

    contacts.grid_rowconfigure(5, minsize = 20)

    Label(contacts, text = the_version, foreground='white', bg='black', font=("system", 40), height = 1).grid(row=6, column=1, columnspan = 2)
    Button(contacts, font = ("Times", 50), height = 1, width = 10, text = "Refresh", command = lambda : contact_page(contacts)).grid(row = 6, column = 3, columnspan = 2)
    Button(contacts, font = ("Times", 50), height = 1, width = 10, text = "Finances", command = lambda : finances_page(contacts)).grid(row = 6, column = 5, columnspan = 2)

    contacts.mainloop()

def finances_page(page_open):
    page_open.destroy()
    finances = Tk()
    finances.wm_title("AbuMoola - Finances")
    finances.configure(bg = 'black')

    Label(finances, font = ("Times", 120), foreground = 'white', bg = 'black', text = user_alias + " Finances").grid(row = 0, column = 1, columnspan = 8)

    finances.grid_rowconfigure(1, minsize = 30)

    fin_updates = StringVar()
    fin_updates_panel = Label(contacts, font = ("Times", 50), foreground = 'white', bg = 'black', textvariable = fin_updates).grid(row = 1, column = 1, columnspan = 8)

    finances.grid_rowconfigure(3, minsize = 30)


def contact_add(first_name, last_name, address, num_1, num_2, email, insta, extra, update_this):
    if (first_name =="First Name"):
        update_this.set("Can't use default")
    elif (len(first_name) < 1):
        update_this.set("Need first name")
    else:
        try:
            contact_detail_read = open(user_detail_path + "/contacts_details.txt", "r")
            last_line = contact_detail_read.read().splitlines()[-1]
            last_id = int(last_line.split("|")[0])
            contact_detail_read.close()
            contact_detail_append = open(user_detail_path + "/contacts_details.txt", "a")
            contact_detail_append.write(str(last_id + 1) + "|" + first_name + "|" + last_name + "|" + address + "|" + num_1 + "|" + num_2 + "|" + email + "|" + insta + "|" + extra + "\n")
            contact_detail_append.close()
            update_this.set("Added " + first_name)
        except:
            contact_file = os.path.join(user_detail_path + "/contacts_details.txt")
            contact_file_open = open(contact_file, "w")
            contact_file_open.write("1|" + first_name + "|" + last_name + "|" + address + "|" + num_1 + "|" + num_2 + "|" + email + "|" + insta + "|" + extra + "\n")
            contact_file_open.close()
            update_this.set(first_name + " is your first contact !")

def contact_remove(remove_this, update_this):
    new_contacts = ""
    if (remove_this == "ID"):
        update_this.set("Can't remove default")
    else:
        try:
            contact_detail_read = open(user_detail_path + "/contacts_details.txt", "r")
            for line in contact_detail_read:
                checkline = line.split('|')
                if checkline[0] == remove_this:
                    this_guy = checkline[1] + " " + checkline[2]
                    pass
                else:
                    new_contacts += line
            contact_detail_read.close()
            contact_detail_write = open(user_detail_path + "/contacts_details.txt", "w")
            contact_detail_write.write(new_contacts)
            update_this.set(this_guy + "was removed.")
        except:
            update_this.set("Something went wrong")

def main_clock():
    global time1
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1:
        time1=time2
        the_time.config(text=time2, width = 10)
    the_time.after(200, main_clock)


########### PREPARTAION ##################################

working_directory = pathlib.Path(__file__).parent.absolute()
user_detail_path = str(working_directory) + "/user_data/"

try:
    user_detail = open(user_detail_path + "/user_details.txt", "r")
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

master.grid_rowconfigure(4, minsize=100)

finance_but = Button(master, text="Finances", font=("system", 50), width = 20, height = 4).grid(row=5, column=0, columnspan = 5)

contact_but = Button(master, text="Contacts", font=("system", 50), width = 20, height = 4, command = lambda : contact_page(master))
contact_but.grid(row=5, column=4, columnspan = 5)


master.grid_rowconfigure(6, minsize=100)

github_but = Button(master, text="Github", font=("system", 50), width = 51, height = 3).grid(row=8, column=2, columnspan = 5)

master.grid_rowconfigure(9, minsize=120)

Label(master, text = the_version, foreground = 'white', bg = 'black', font = ("system", 40), height = 1).grid(row = 10, column=0, columnspan = 5)

main_clock()
master.mainloop()
