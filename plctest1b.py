import re

def hopefullycorrect(ic):
    identifyplease = r"(0[xX][0-9a-fA-F]+)|([0-7]+)|([1-9][0-9]*)([uUil]?)|0"
    return re.match(identifyplease, ic) is not None

ic = "024"
if hopefullycorrect(ic):
    print(f"{ic} is good")
else:
    print(f"{ic} is not valid")