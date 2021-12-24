class HaxxError:
    pass


try:
    import os
except ModuleNotFoundError:
    print("Error: do pip(3) install os to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
try:
    import readline
except ModuleNotFoundError:
    print("Error: do pip(3) install readline to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
try:
    import time
except ModuleNotFoundError:
    print("Error: do pip(3) install time to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
try:
    import pickle
except ModuleNotFoundError:
    print("Error: do pip(3) install pickle to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
try:
    import requests
except ModuleNotFoundError:
    print("Error: do pip(3) install requests to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
try:
    import sys
except ModuleNotFoundError:
    print("Error: do pip(3) install sys to use Binbows™")
    print("If you do not have pip, see https://pip.pypa.io/en/stable/installation/")
    exit()
cmdlst = [
    "neofetch",
    "sleep",
    "wipe",
    "customwipe",
    "makecall",
    "removecall",
    "editcall",
    "cat",
    "lstcalls",
    "echo",
    "warn",
    "exportlib",
    "importlib",
    "execute",
    "update",
    "haxx",
]
warnlst = ["wipe", "customwipe"]
calldict = {}

# credit to the guys at https://stackoverflow.com/questions/8505163/ for the function below
def input_with_prefill(prompt: str, text: str) -> str:
    """
    Prompt a user with a string, prefilled with editable text.
    """

    def hook() -> None:
        """Child of input_with_prefill; inserts text."""
        readline.insert_text(text)
        readline.redisplay()

    readline.set_pre_input_hook(hook)
    result = input(prompt)
    readline.set_pre_input_hook()
    return result


def terminal() -> None:
    """Opens the Binbows terminal."""
    print("\x1B[2J")
    while True:
        try:
            cmd = input("binbowsonly@polarbear:~$ ")
            if cmd:
                if cmd[0] == "q":
                    break
                parsestring(cmd)
        except EOFError:
            pass
        except KeyboardInterrupt:
            pass


def neofetch(v: str) -> None:
    """
    Fetches them neos
    """
    print(
        f"""------------
            You are using Binbows {v}
            -> good: yes
     🅱      -> resolution: yes
            -> memory: yes
            -> distro: Plebian
------------"""
    )


def sleep(seconds: str) -> None:
    time.sleep(float(seconds))


def wipe(wiping: str) -> None:
    """
    Opens a file and replaces all its contents with 'Wiped by Binbows'.
    """
    try:
        if os.path.exists(wiping):
            if (
                wiping.split(".")[1] == "py"
                or wiping.split(".")[1] == "pyc"
                or wiping.split(".")[1] == "html"
                or wiping.split(".")[1] == "bxe"
                or wiping.split(".")[1] == "binbowslib"
            ):
                print("Permission Denied.")
            else:
                with open(wiping, "w") as wipedfile:
                    wipedfile.write("Wiped by Binbows")
        else:
            print(f"Error: the file '{wiping}' does not exist.")
    except IndexError:
        print("You need to have a dot (.) in a file you want to wipe.")


def customwipe(wipingargs: str) -> None:
    """
    Opens a file and replaces its content with a user-provided string.
    """
    wipestr = wipingargs.split(", ")[0]
    wiping = wipingargs.split(", ")[1]
    try:
        if os.path.exists(wiping):
            if (
                wiping.split(".")[1] == "py"
                or wiping.split(".")[1] == "pyc"
                or wiping.split(".")[1] == "html"
                or wiping.split(".")[1] == "bxe"
                or wiping.split(".")[1] == "binbowslib"
            ):
                print("Permission Denied.")
            else:
                with open(wiping, "w") as wipedfile:
                    wipedfile.write(wipestr)
        else:
            print(f"Error: the file '{wiping}' does not exist.")
    except IndexError:
        print("You need to have a dot (.) in a file you want to wipe.")


def makecall(callname: str) -> None:
    """Creates an empty call."""
    if callname not in calldict:
        calldict[callname] = ""
    else:
        print(f"Error: the call '{callname}' already exists.")


def removecall(callname: str) -> None:
    """Removes a calls from the dictionary."""
    if warn(f"remove the call '{callname}'") and calldict.pop(callname, None) is None:
        print(f"Error: the call '{callname}' does not exist")


def eterminal(callname: str) -> None:
    """A terminal for editing existing code within calls."""
    while True:
        line = ""
        insertbefore = insertafter = delline = False
        for i, cmd in enumerate(calldict[callname].splitlines()):
            if i:
                print(str(i) + " ~ " + cmd)
        while not line:
            line = input("Which line to edit? [Press q to quit] >>> ")
        if line == "q":
            return
        if line[0] == "<" and len(line) > 1:
            insertbefore = True
            line = line[1:]
        elif line[0] == ">" and len(line) > 1:
            insertafter = True
            line = int(line[1:]) + 1
        elif line[0] == "-" and len(line) > 1:
            if warn("delete that line"):
                delline = True
                line = line[1:]
        try:
            line = int(line)
            if not insertbefore and not insertafter and not delline:
                newcode = input_with_prefill(
                    f"[{line}] ", calldict[callname].splitlines()[line]
                )
                newcodelst = calldict[callname].splitlines()
                newcodelst[line] = newcode
                calldict[callname] = "\n".join(newcodelst)
            elif insertbefore or insertafter:
                newcode = input(f"[{line}] ")
                newcodelst = calldict[callname].splitlines()
                newcodelst.insert(line, newcode)
                calldict[callname] = "\n".join(newcodelst)
            elif delline:
                newcodelst = calldict[callname].splitlines()
                newcodelst.pop(line)
                calldict[callname] = "\n".join(newcodelst)
        except ValueError:
            print("Error: enter a number.")
        except IndexError:
            print("Error: that line does not exist.")


def asterminal(callname: str) -> None:
    """A terminal for strating anew and appending to a call."""
    arrows = True
    print("Enter q at any time to quit.")
    while True:
        if arrows:
            cmd = input(">>> ")
            arrows = False
        else:
            cmd = input("... ")
        if cmd:
            if cmd == "q":
                break
            calldict[callname] += "\n" + f"{cmd}"


def editcall(callname: str) -> None:
    """Edits the contents of a call."""
    if callname in calldict:
        print("How do you want to edit the call?")
        edittype = input(
            "'e' = edit existing code; 'a' = append; 's' = start anew >>> "
        )
        if edittype == "s":
            if calldict[callname]:
                if warn("start anew"):
                    calldict[callname] = ""
                else:
                    editcall(callname)
                    return
        elif edittype == "a":
            print("\nCode so far:")
            print(calldict[callname] + "\n\n(END)\n")
        elif edittype == "e":
            eterminal(callname)
            return
        else:
            print("Error: you did not enter any of the above.")
            return
        asterminal(callname)
    else:
        print(f"Error: the call '{callname}' does not exist.")


def cat(callname: str) -> None:
    """Displays the contents of a call."""
    try:
        print(calldict[callname] + "\n")
    except KeyError:
        print(f"Error: the call {callname} does not exist.")


def lstcalls(specific: str) -> None:
    """Lists all calls."""
    if not specific:
        for callname in calldict:
            print(callname)
    else:
        if specific in calldict:
            print(f"lstcalls => The call '{specific}' does exist.")
        else:
            print(f"lstcalls => The call '{specific}' does not exist.")


def call(callname: str) -> None:
    """Runs code within a call."""
    cmds = calldict[callname]
    for seperatedcmd in cmds.splitlines()[1:]:
        parsestring(seperatedcmd)


def echo(msg: str) -> None:
    """Print a message."""
    print(msg)


def warn(keywrd: str) -> bool:
    """Warn a user about something."""
    do_cmd = input(f"Are you sure you want to {keywrd}? [Y/n] >>> ")
    if do_cmd == "y" or do_cmd == "Y":
        return True
    else:
        return False


def exportlib(libname: str) -> None:
    """Export all calls to a library."""
    option = ""
    while option != "a" and option != "n" and option != "o" and option != "q":
        option = input(
            "'a': append, 'n': new, 'o': overwrite current libs (if they exist), 'q': quit this prompt >>> "
        )
        if option == "q":
            return
    libname = libname + ".binbowslib"
    if option == "o":
        with open(libname, "wb") as lib:
            pickle.dump(calldict, lib)
    elif option == "n":
        try:
            with open(libname, "xb") as lib:
                pickle.dump(calldict, lib)
        except FileExistsError:
            print("Error: that file already exists.")
    elif option == "a":
        try:
            with open(libname, "rb") as lib:
                unappended = pickle.load(lib)
            with open(libname, "wb") as lib:
                for callname in calldict:
                    unappended[callname] = calldict[callname]
                appended = unappended
                pickle.dump(appended, lib)
        except FileNotFoundError:
            print("Error: library does not exist.")
        except EOFError:
            print("Error: empty library.")


def importlib(libname: str) -> None:
    """Import a library."""
    global calldict
    libname = libname + ".binbowslib"
    try:
        with open(libname, "rb") as lib:
            imported = pickle.load(lib)
        for callname in imported:
            calldict[callname] = imported[callname]
    except FileNotFoundError:
        print("Error: library does not exist.")
    except EOFError:
        print("Error: empty library.")


def execute(filename: str) -> None:
    with open(filename, "r") as bxe:
        executable = bxe.read()[:-1]
    for cmd in executable.splitlines():
        parsestring(cmd)


def update(cmds: str) -> None:
    """
    Update to latest and greatest binbows version!
    """
    if cmds:
        with open(cmds, "w") as update:
            update.write(
                requests.get("https://phil-gates.github.io/srcs/binbows.py").text
            )
    else:
        with open(__file__, "w") as update:
            update.write(
                requests.get("https://phil-gates.github.io/srcs/binbows.py").text
            )


def haxx(whatever):
    print("Enabling haxx...")
    sleep(5)
    print("Uh Oh. You got caught for enabling haxx...")
    sleep(3)
    raise HaxxError("Kicked for haxx")


def parsestring(cmd: str) -> None:
    """Parses the user's command."""
    arglst = cmd.split(" ")
    keywrd = arglst[0]
    if keywrd[0] != "%" and cmd[0] != "#":
        if keywrd[-1] == "!":
            keywrd = keywrd[:-1]
            if keywrd in cmdlst:
                exec(keywrd + f"""("{" ".join(arglst[1:])}")""")
            else:
                print(f"Error: the keyword '{keywrd}' does not exist.")
        elif keywrd in warnlst:
            run = warn(keywrd)
            if run:
                arglst[0] += "!"
                unwarned = " ".join(arglst)
                parsestring(unwarned)
        elif keywrd in cmdlst:
            exec(keywrd + f'("{" ".join(arglst[1:])}")')
        else:
            print(f"Error: the keyword '{keywrd}' does not exist.")
    elif cmd[0] == "#":
        pass
    else:
        if keywrd[1:] in calldict:
            call(keywrd[1:])
        else:
            print(f"Error: the call '{keywrd[1:]}' does not exist.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        terminal()
    elif sys.argv[1] == "-m" and len(sys.argv) >= 3:
        cmds = " ".join(sys.argv[2:])
        for cmd in cmds.split(" // "):
            parsestring(cmd)
