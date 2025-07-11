#IMPORTS
import tracker

#INSTANCE
TRACKER = tracker.tracker

def app():
    commands = {
        "1": TRACKER.add_mount
    }
    while True:
        #Here instruccions
        try:
            console_line = input("$User: ")
            commands[console_line]()
        except:
            print("Command not exist");      
app()