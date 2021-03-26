import subprocess
import easygui
import glob
import os
import os.path
from os import path
import re
import sys



adminpass = "123456"
passfolder = '$psswrd$'
dir_ = os.getcwd() + "\\"+ passfolder
    
def savepassword(website, password, name):

    if not path.exists(passfolder):
        os.mkdir(passfolder)
        subprocess.check_call(["attrib","+H",dir_])
    savedfile = open(passfolder+ "/" + name+".txt", "w")
    savedfile.write(name + "|, ")
    savedfile.write(website + "|, ")
    savedfile.write(password + "|,")
    savedfile.close()

def main():
    dir_ = os.getcwd() + "\\" + passfolder
    what2to = easygui.enterbox("'store' OR 'get' OR 'remove' OR 'list'  (cancel to exit)")

    while what2to == "":
        what2to = easygui.enterbox("'store' OR 'get' OR 'remove' OR 'list'  (cancel to exit)")

    if what2to == "store":

        password = easygui.enterbox("Enter admin password")

        while password == "":
            password = easygui.enterbox("Enter admin password")

        if password == adminpass:

            website = easygui.enterbox("Enter name of website")
            name = easygui.enterbox("Enter custom name")
            password = easygui.enterbox("Enter password")

            easygui.msgbox("Press 'ok' to create")

            savepassword(website, password, name)

            easygui.msgbox("Stored password successfully. ")

        else:
            easygui.msgbox("Incorrect password.")
            main()


    elif what2to == "get":

        password = easygui.enterbox("Enter admin password")
        if password == adminpass:
            passwordname = easygui.enterbox("Enter name to extract password from")

            while passwordname == "":
                passwordname = easygui.enterbox("Enter name to extract password from")

            dir_ = os.getcwd() + "\\" + passfolder

            for file in glob.glob(dir_ + "\\*"):

                if file == dir_ + "\\" + passwordname + ".txt":
                    file = open(file, "r")
                    filecontent = file.read()
                    file.close()

                    res = re.sub("|,' ]", "", filecontent).split()

                    name_ = res[0]
                    website_ = res[1]
                    password_ = res[2]

                    name_ = name_[:-2]
                    website_ = website_[:-2]
                    password_ = password_[:-2]

                    easygui.msgbox(
                        "name: '" + name_ + "' \n" + "website: '" + website_ + "' \n" + "password: '" + password_ + "'")
                    sys.exit()
            else:
                easygui.msgbox("There was no password stored with the name '" + passwordname + "'")


        else:
            easygui.msgbox("Incorrect password.")
            main()

    elif what2to == "remove":
        password = easygui.enterbox("Enter admin password")

        if password == adminpass:

            remove = easygui.enterbox("Enter name to delete")

            while remove == "":
                remove = easygui.enterbox("Enter name to delete")
            if path.exists(dir_ + "\\" +remove + ".txt"):
                os.remove(dir_ + "\\" +remove  + ".txt")

                easygui.msgbox("Press 'ok' to create")

                easygui.msgbox("Removed file '"+remove+"' successfully. ")
                sys.exit()
            else:
                easygui.msgbox("There was no file called '"+remove+"'")
                main()


        else:
            easygui.msgbox("Incorrect password.")
            main()

    elif what2to == "list":
        password = easygui.enterbox("Enter admin password")

        if password == adminpass:
            filearray = []
            for file in glob.glob(dir_ + "\\*"):
                newfile = file.replace(dir_, "")
                newfile = newfile.replace("\\", "")

                filearray.append(newfile.replace("{", ""))

            easygui.msgbox(filearray)

    elif what2to == "cancel":
        sys.exit()

    else:
        main()


if __name__ == "__main__":
    main()
