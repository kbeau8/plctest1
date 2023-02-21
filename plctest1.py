import re

def maybeemail(emails):
    identifyplease = r"([a-zA-Z0-9#%$’&+*-/=?^_`{|}~])+\.*([a-zA-Z0-9#%$’&+*-/=?^_`{|}~])*"
    return re.match(identifyplease, emails) is not None

emails = "kdarabi1@student.gsu.edu"
if maybeemail(emails):
    print(f"{emails} is good")
else:
    print(f"{emails} is not valid")