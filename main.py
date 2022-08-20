import datetime
import pandas as pd
import work
import pickle
from os.path import exists

#Setup environment
def setup():
	if os.path.exists('savedata.txt') == False:
		with open('savedata.txt', 'x') as fp:
			fp.close()
	else:
		pass

#pickle and unpickle things as tuples and work with them that way, too easy

def load():
	with open('savedata.txt','rb') as f:
		return pickle.load(f)

def save():
	with open('savedata.txt','wb') as f:
		pickle.dump(dataframe, f)

def display():
	display(dataframe)

def new_work():
	datemsg = "Are you creating an object for today's date or a previous date?\n1) Today\n2) Previous Date"
	errormsg = "Invalid input"
	timeworkedmsg = "How long did you work on this date?"
	choice = ""

	print(datemsg)

	while choice != 1 and choice != 2:
		print(errormsg,datemsg)
		choice = input("")

	if choice == 1:
		dtg = datetime.datetime.now()
	elif choice == 2:
		pass

	print(timeworkedmsg)
	workchoice = ""

	while type(workchoice) != int:
		print(errormsg,timeworkedmsg) 
		workchoice = input("")


	dataframe.loc[len(dataframe.index)] = [dtg,workchoice]

def menu():
	display()

	optionsMessage = ''

	print(optionsMessage)
	choice = input('')
#need a menu loop
	#setup
	#load
	#display
	#take user input
	#save and exit

#make it do statistics - how many more days of this average to get to 10,000 hours