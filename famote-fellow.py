# os is for executing commands
import os

# setting up the version
ver = "v0.0"
# variables
index = None
NP = None
P = None
print("Running... Famote Fellow" + ver)


# the code that should sync OS standards
def makeFILE():
    # windows
    if os.name == "nt":
        os.system("nul > index.py")
    # other than windows
    else:
        os.system("touch index.py")


# Fetching Path, if you don't want tho just type "SKIP"
def PATH_FETCH():
    # makes the variable global for using
    global P
    # looping before an answer expcet a break
    while P != "" or P != "0":
        P = input(
            "Choose a (vaild) path for the project (type 'SKIP' if you don't need too): "
        )
        # skips
        if P == "SKIP":
            break
        # warns input is blank.
        elif P == "":
            print("the Blank should be filled.")
        # idc if it's not valid.
        else:
            os.chdir(P)
            break


# Naming Project
def NAME_PROJECT():
    global NP
    NP = input("Name for This Project: ")
    os.system("mkdir " + NP)
    os.chdir(NP)


# Templates: Usually it's ready to use commands
def TEMPLATE():
    print("Available Templates: ")
    print("")
    print("Basic: Prints Hello World.")
    print("Manual: Lets you change the options")
    global T
    T = input("(1 - Basic. 2 - Manual): ")


# Main Project Creator
def projectMAKE():
    PATH_FETCH()
    NAME_PROJECT()
    TEMPLATE()
    print("Making the 'index.py' file...")
    makeFILE()
    # if Template 1 then insert a command that outputs "Hello World".
    if T == "1":
        with open("index.py", "a") as Fi:
            Fi.write("""print("Hello World")\n""")
    # if Template 2 then modify the options.
    elif T == "2":
        print("Importing Modules / Libraries...")
        global index
        print("Modules should be typed SEVERALLY to be applied")
        # inserting the module(s)
        while index != "DONE":
            index = input(
                "Which module you want to put (type 'DONE' for finish the Section) "
            )
            if index == "DONE":
                break
            with open("index.py", "a") as Fi:
                Fi.write("import " + index + "\n")
    print("The Project should be created now... Good Luck")


# to executing function
projectMAKE()
