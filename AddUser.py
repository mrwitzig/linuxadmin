# AddUser Script

# Matthew Witzig
# 12/6/2020

# Need to import this so we can have python and the OS talk to each other. Kind of important!
import os

# Open text files and make their contents readable
imported1 = open("UserNamesLvl1.txt","r")
imported2 = open("UserNamesLvl2.txt","r")

# beginning the class war right here and now. Or at least making a class of their data
class employees:
    def __init__(self, first, last, group):
        self.firstname = first
        self.lastname = last
        self.group = group
        self.user_id = self.firstname[0]+"."+self.lastname[0:4]

    def __str__(self):
        return '{}-{}'.format(self.user_id,self.group)

count = 0 # Counter variable
nameslist = [] # defining the other variables
admins = []
developers = []
staff = []
temp = []
userobjects = []

# Adding to the master list of names. YOU'RE ON THE LIST, BUDDY
for lines in imported1:
    nameslist.append(lines.upper())
for lines in imported2:
    nameslist.append(lines.upper())

# Define a function to create new users based on which group they belong to

def createuser(firstname,lastname,group):

    name = employees(firstname,lastname,group)
    userobjects.append(name)

    # Create an admin user, add them to the admin and sudo group, set password, do not create group for user, set username to the user ID created
    if name.group == 'admins':
        print("Added", name.user_id, "to", name.group)
        os.system("useradd -m -G admins -p changeme -N "+ name.user_id)
    # Create developer user, add to developers group, change default shell to C shell,set password, do not create group for user, set username to user ID created
    if name.group == 'developer':
        print("Added", name.user_id, "to", name.group)
        os.system("useradd -m -G developer -s /bin/csh -p changeme -N "+ name.user_id)
    # Create staff user, add to staff group, set password, do not create group for user, set username to user ID created
    if name.group == 'staff':
        print("Added", name.user_id, "to", name.group)
        os.system("useradd -m -G staff -p changeme -N "+ name.user_id)
    # Create temp user, add to temp group, set password, set username to user ID created
    if name.group == 'temp':
        print("Added", name.user_id, "to", name.group)
        os.system("useradd -m -G temps -p changeme -N "+ name.user_id)

# A function to delete all users. This was helpful when testing and troubleshooting my script.
##def delete_all_users():
#    for user in list_of_user_obj:
#        os.system("deluser --remove-home "+ user.user_id)


# Arbitrarily splitting the list of names into four categories
for names in nameslist :

    if count <= 20:
        admins.append(names)
    if count > 20 and count <= 40:
        developers.append(names)
    if count > 40 and count <= 100:
        staff.append(names)
    if count > 100:
        temp.append(names)
    count += 1

# Creating list of admins
for admin in admins:
    splitad = admin.split()
    firstname = splitad[0]
    lastname = splitad[-1]
    group = 'admins'
    createuser(firstname,lastname, group)

# creating devs.
for developer in developers:
    splitdev = developer.split()
    firstname = splitdev[0]
    lastname = splitdev[-1]
    group = 'developer'
    createuser(firstname,lastname, group)

# Same as above but for staff
for staff in staff:
    splitstaff = staff.split()
    firstname = splitstaff[0]
    lastname = splitstaff[-1]
    group = 'staff'
    createuser(firstname,lastname, group)

# yadayada, stops at the end of temp
for temp in temp:
    if temp != '':
        splittemp = temp.split()
        firstname = splittemp[0]
        lastname = splittemp[-1]
        group = 'temp'
        createuser(firstname,lastname, group)



#delete_all_users()
