from Affirmations import affirm
from datetime import datetime

@affirm() # prints an affirmation to stdout 20% of the time this function is run
def seshTrack(recordname): #take any type for recordname
    '''
    Prints the current time in dd/mm/YY H:M:S format
    '''
    now = datetime.now() # datetime object w/ current date and time
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S") #store date string in explicit format
    print(f"{recordname}", dt_string) #recordname as string to tag the date

if __name__ == "__main__":
    pass
else:
    seshTrack("Initializing new session:")