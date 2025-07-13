#IMPORTS
from tracker import Tracker

def app():
    #INSTANCE
    TRACKER = Tracker()

    commands = {
        '1': TRACKER.add_mount
    }

    while True:
        #Here instruccions
        try:
            console_line = input("$User: ")
            if console_line == 'exit':
                print('BYE!')
                break
            commands[console_line]()
        except:
            print("Command not exist");      
app()