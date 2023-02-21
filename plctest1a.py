import re

def hopefullycorrect(flp):
    identifyplease = r"[+-]?(0|([1-9][0-9]*))(\.[0-9]+)?([eE][+-]?[0-9]+)?[fF]?"
    return re.match(identifyplease, flp) is not None

flp = "15.75L"
if hopefullycorrect(flp):
    print(f"{flp} is good")
else:
    print(f"{flp} is not valid")