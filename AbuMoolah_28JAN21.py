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
from flexx import flx
import os.path
import pathlib

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
		user_alias = line.split()[1])

#class abumoola_make(flx.Widget):
#	def init(self):
#		with flx.VBox():
#		flx.Label(style='background:#cfc;', wrap=1,
#		text='Here is some content at the top for which we want to '
#		'use minimal size. Thus the use of a VBox. '
#                        'Below is a splitter, with a box layout on the left '
#                        'and a fix layout on the right.')
#			flx.Button(text = "Contacts", flex = 1)
#			flx.Button(text = "Finances", flex = 1)
#
#if __name__ == '__main__':
#    m = flx.launch(abumoola_make)
#    flx.run()
#
#mm_app = flx.App(abumoola_make)
#app.export('AbuMoola.html', link=0)