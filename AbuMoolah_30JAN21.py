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
#Contacts list ID properly
########### LIBRARIES ##################################
from tkinter import *
from tkinter.font import Font
from tkinter import scrolledtext
import os.path, pathlib, random, time, os, sys
from datetime import datetime

########### GLOBALS ##################################
global the_version
the_version = "AbuMoola (version 0) by AHTAR"
today = datetime.today()
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
        contact_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt", "r")
        contacts_to_show = "ID - FirstName - LastName - Addresss - #1 - #2 - Email - Insta - Extra\n" + contact_detail_read.read().replace("|", " - ")
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

def fin_add_type(type_add, update_this):
    if (type_add == "+ Type"):
        update_this.set("Can't add default")
    elif (len(type_add) < 1):
        update_this.set("Need something")
    else:
        type_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "r")
        all_types = type_detail_read.read().split("|")[:-1]
        type_detail_append = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "a")
        type_detail_append.write(type_add + "|")
        type_detail_append.close()
        update_this.set("Added " + type_add)

def fin_rem_type(type_rem, update_this):
    new_types = ""
    check_remove = False
    if (type_rem == "- Type"):
        update_this.set("Can't add default")
    elif (len(type_rem) < 1):
        update_this.set("Need something")
    else:
        try:
            type_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "r")
        except:
            update_this.set("Nothing to remove " + type_rem)
            END
        all_types = type_detail_read.read().split("|")[:-1]
        for entry in all_types:
            if entry == type_rem:
                update_this.set("Removed " + type_rem)
                check_remove = True
            else:
                new_types += entry + "|"
                type_detail_read.close()
                type_detail_write = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "w")
                type_detail_write.write(new_types)
                update_this.set("Removed " + type_rem)
        if check_remove == False:
            update_this.set(type_rem + " isn't a Type")

def currency_pref(cur_pref, update_this):
    update_cur_details = ""
    user_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/user_data/user_details.txt", "r")
    user_detil_contents = user_detail_read.read()
    if cur_pref in currency_list:
        if "HATHAHEA-FLOOS" not in user_detil_contents:
            user_detail_read.close()
            user_detail_append = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/user_data/user_details.txt", "a")
            user_detail_append.write("\nHATHAHEA-FLOOS " + cur_pref)
            user_detail_append.close()
        else:
            for line in user_detil_contents.splitlines():
                if "HATHAHEA-FLOOS" in line:
                    print(line)
                    update_cur_details += "\nHATHAHEA-FLOOS " + cur_pref
                else:
                    update_cur_details += line
            user_detail_read.close()
            user_detail_write = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/user_data/user_details.txt", "w")
            user_detail_write.write(update_cur_details)
        update_this.set(cur_pref + " is now your primary currency")
    else:
        update_this.set(cur_pref + " is not a valid currency")


def finances_page(page_open):
    page_open.destroy()
    finances = Tk()
    finances.wm_title("AbuMoola - Finances")
    finances.configure(bg = 'black')

    try:
        test_open = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "r")
        test_open.close()
    except:
        type_file = os.path.join(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt")
        type_file_open = open(type_file, "w")
        type_file_open.write("Food|")
        type_file_open.close()

    Label(finances, font = ("Times", 120), foreground = 'white', bg = 'black', text = user_alias + " Finances").grid(row = 0, column = 0, columnspan = 6)

    finances.grid_rowconfigure(1, minsize = 30)

    fin_updates = StringVar()
    fin_updates_panel = Label(finances, font = ("Times", 50), foreground = 'white', bg = 'black', textvariable = fin_updates).grid(row = 1, column = 1, columnspan = 6)

    finances.grid_rowconfigure(3, minsize = 30)

    Button(finances, font = ("Times", 50), height = 1, width = 9, text = "Add Type", command = lambda : fin_add_type(type_text.get(), fin_updates)).grid(row = 2, column = 0)

    type_text = StringVar()
    type_ent = Entry(finances, textvariable = type_text, font = ('Verdana',60), width = 9).grid(row = 2, column = 1, columnspan = 1)
    type_text.set("+ Type")

    Button(finances, font = ("Times", 50), height = 1, width = 11, text = "Remove Type", command = lambda : fin_rem_type(rem_type_text.get(), fin_updates)).grid(row = 2, column = 2)

    rem_type_text = StringVar()
    rem_type_ent = Entry(finances, textvariable = rem_type_text, font = ('Verdana',60), width = 9).grid(row = 2, column = 3, columnspan = 1)
    rem_type_text.set("- Type")

    Button(finances, font = ("Times", 50), height = 1, width = 14, text = "Pref. Currency", command = lambda : currency_pref(cur_pref_text.get(), fin_updates)).grid(row = 3, column = 0)

    cur_pref_text = StringVar()
    cur_pref_ent = Entry(finances, textvariable = cur_pref_text, font = ('Verdana',60), width = 9).grid(row = 3, column = 1, columnspan = 1)
    cur_pref_text.set("Currency")

    Button(finances, font = ("Times", 50), height = 1, width = 14, text = "Currency List", command = lambda : currency_stuff()).grid(row = 3, column = 2, columnspan = 2)

    Button(finances, font = ("Times", 50), height = 1, width = 8, text = "Add Item", command = lambda : item_add(item_text.get(), amount_text.get(), location_text.get(), type_opt_text.get(), time_text.get(), fin_updates)).grid(row = 4, column = 0, columnspan = 2)

    item_text = StringVar()
    item_ent = Entry(finances, textvariable = item_text, font = ('Verdana',60), width = 9).grid(row = 4, column = 1, columnspan = 1)
    item_text.set("Item")

    amount_text = StringVar()
    amount_ent = Entry(finances, textvariable = amount_text, font = ('Verdana',60), width = 9).grid(row = 4, column = 2, columnspan = 1)
    amount_text.set("Amount")

    location_text = StringVar()
    location_ent = Entry(finances, textvariable = location_text, font = ('Verdana',60), width = 9).grid(row = 4, column = 3, columnspan = 1)
    location_text.set("Location")

    with open(str(working_directory) + "/" + your_alias.replace(" ","") + "/types_included.txt", "r") as these_types:
        all_types_here = these_types.read().split("|")[:-1]

    type_opt_text = StringVar()
    type_opts = OptionMenu(finances, type_opt_text, *all_types_here).grid(row = 4, column = 4, columnspan = 1)
    type_opt_text.set(str(all_types_here[0]))

    time_text = StringVar()
    time_ent = Entry(finances, textvariable = time_text, font = ('Verdana',60), width = 9).grid(row = 4, column = 5, columnspan = 1)
    time_text.set("HH:MM:SS")

    try:
        item_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/item_list.txt", "r")
        item_to_show = "ID - Item - Amount - Location - Type - Time - Date\n" + item_detail_read.read().replace("|"," - ")
        item_output = scrolledtext.ScrolledText(finances, height=10)
        item_output.grid(column=0, row=5, columnspan = 6)
        item_output.configure(background="white", foreground = "black", font = ("Times", 50), wrap= 'word')
        item_output.insert(END, item_to_show)
    except:
        fin_updates.set("No list of contacts to show")

    Label(finances, text = the_version, foreground='white', bg='black', font=("system", 40), height = 1).grid(row=6, column=0, columnspan = 2)
    Button(finances, font = ("Times", 50), height = 1, width = 10, text = "Refresh", command = lambda : finances_page(finances)).grid(row = 6, column = 2, columnspan = 1)
    Button(finances, font = ("Times", 50), height = 1, width = 10, text = "Contacts", command = lambda : contact_page(finances)).grid(row = 6, column = 4, columnspan = 1)
    #last x entries
    #specific month
    #Remove ID
    #Button(finances, font = ("Times", 50), height = 1, width = 10, text = "Analytics", command = lambda : finances_page(contacts)).grid(row = 6, column = 6, columnspan = 2)

def item_add(the_item, the_amount, the_location, the_type, time_text, update_this):
    if (the_item == "Item"):
        update_this.set("Can't use default")
    elif (len(the_item) < 1):
        update_this.set("Need first name")
    else:
        try:
            item_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/item_list.txt", "r")
            last_line = item_detail_read.read().splitlines()[-1]
            last_id = int(last_line.split("|")[0])
            item_detail_read.close()
            item_detail_append = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/item_list.txt", "a")
            item_detail_append.write(str(last_id + 1) + "|" + the_item + "|" + the_amount + "|" + the_location + "|" + the_type + "|" + time_text + "|" +  today.strftime("%d/%m/%Y") + "\n")
            item_detail_append.close()
            update_this.set("Added " + the_item)
        except:
            item_file = os.path.join(str(working_directory) + "/" + your_alias.replace(" ","") + "/item_list.txt")
            item_file_open = open(item_file, "w")
            item_file_open.write("1|" + the_item + "|" + the_amount + "|" + the_location + "|" + the_type + "|" + time_text + "|" +  today.strftime("%d/%m/%Y") + "\n")
            item_file_open.close()
            update_this.set(the_item + " is your first item !")

def currency_stuff():
    all_currency_list = Tk()
    all_currency_list.wm_title("AbuMoola - Currency List")
    all_currency_list.configure(bg = 'black')

    currency_list = ("MYR: Malaysian Ringgit, ISK: Icelandic Krona,\nEEK: Estonian kroon, HKD: Hong Kong Dollar,\nIDR: Indonesian Rupiah, CAD: Canadian Dollar,\nHUF: Hungarian forint, PLN: Poland zloty,\nBRL: Brazilian real, MXN: Mexican Peso,\nNOK: Norwegian Krone, BGN: Bulgarian Lev,\nTHB: Malaysian Ringgit, HRK: Icelandic Krona,\nCZK: Estonian kroon, DKK: Hong Kong Dollar,\nCYP: Indonesian Rupiah, RUB: Canadian Dollar,\nPHP: Hungarian forint, ILS: Poland zloty,\nEUR: Brazilian real, TRL: Mexican Peso,\nSEK: Norwegian Krone, TRY: Bulgarian Lev,\nLTL: Lithuanian litas, MTL: Maltese Lira,\nAUD: Australian Dollar, SGD: Singapore Dollar,\nNZD: New Zealand Dollar, KRW: South Korean won,\nGBP: Great British Pound, LVL: Latvian lats,\nCHF: Swiss Franks, ZAR: South African Rand,\nUSD: United States Dollar, SKK: Slovak koruna,\nCNY: Chinese Yuan, JPY: Japanese Yen,\nINR: Indian Rupee, RON: Romanian Leu,\nSIT: Slovenian tolar, ROL: Romanian Leu")
    Label(all_currency_list, font = ("Times", 40), foreground = 'white', bg = 'black', text = currency_list).pack()

def contact_add(first_name, last_name, address, num_1, num_2, email, insta, extra, update_this):
    if (first_name == "First Name"):
        update_this.set("Can't use default")
    elif (len(first_name) < 1):
        update_this.set("Need first name")
    else:
        try:
            contact_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt", "r")
            last_line = contact_detail_read.read().splitlines()[-1]
            last_id = int(last_line.split("|")[0])
            contact_detail_read.close()
            contact_detail_append = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt", "a")
            contact_detail_append.write(str(last_id + 1) + "|" + first_name + "|" + last_name + "|" + address + "|" + num_1 + "|" + num_2 + "|" + email + "|" + insta + "|" + extra + "\n")
            contact_detail_append.close()
            update_this.set("Added " + first_name)
        except:
            contact_file = os.path.join(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt")
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
            contact_detail_read = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt", "r")
            for line in contact_detail_read:
                checkline = line.split('|')
                if checkline[0] == remove_this:
                    this_guy = checkline[1] + " " + checkline[2]
                    pass
                else:
                    new_contacts += line
            contact_detail_read.close()
            contact_detail_write = open(str(working_directory) + "/" + your_alias.replace(" ","") + "/contacts_details.txt", "w")
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
currency_list = ["MYR", "ISK", "EEK", "HKD", "IDR", "CAD", "HUF", "PLN", "BRL", "MXN", "NOK", "BGN", "THB", "HRK", "CZK", "DKK", "CYP", "RUB", "PHP", "ILS", "EUR", "TRL", "SEK", "TRY", "LTL", "MTL", "AUD", "SGD", "KRW", "LVL", "SKK", "ZAR", "JPY", "RON", "ROL", "NZD", "GBP", "CHF", "USD", "CNY", "INR", "SIT"]

working_directory = pathlib.Path(__file__).parent.absolute()

user_status = input("Enter '1' if exiting user or '2' if new: ")

if user_status == "1":
    your_alias = input("What is your exisiting alis?: ")
    user_detail_path = str(working_directory) + "/" + your_alias.replace(" ","") + "/user_data/"
    user_detail = open(str(working_directory) + "/" + your_alias + "/user_data/user_details.txt", "r")
elif user_status == "2":
    your_alias = input("How would you like Abu Moolah to address you? (< 20 characters please): ")
    os.system("mkdir " + your_alias.replace(" ",""))
    os.system("mkdir " + your_alias.replace(" ","") + "/user_data")
    os.system("mkdir " + your_alias.replace(" ","") + "/random_deco")
    while len(your_alias) > 20:
        your_alias = input("How would you like Abu Moolah to address you? (< 20 characters please): ")
    detail_file_open = open(str(working_directory) + "/" + your_alias + "/user_data/user_details.txt", "w")
    detail_file_open.write("HATHAHEA-ALIAS " + your_alias)
    detail_file_open.close()
    user_detail = open(str(working_directory) + "/" + your_alias + "/user_data/user_details.txt", "r")
else:
    print("1 or 2 please.")
    exit()

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

finance_but = Button(master, text="Finances", font=("system", 50), width = 20, height = 4, command = lambda : finances_page(master)).grid(row=5, column=0, columnspan = 5)

contact_but = Button(master, text="Contacts", font=("system", 50), width = 20, height = 4, command = lambda : contact_page(master)).grid(row=5, column=4, columnspan = 5)


master.grid_rowconfigure(6, minsize=100)

github_but = Button(master, text="Github", font=("system", 50), width = 51, height = 3).grid(row=8, column=2, columnspan = 5)

master.grid_rowconfigure(9, minsize=120)

Label(master, text = the_version, foreground = 'white', bg = 'black', font = ("system", 40), height = 1).grid(row = 10, column=0, columnspan = 5)

main_clock()
master.mainloop()
