class Candidate:
    def __init__(self, name, pythonExperience, curiosity, skills):
        super().__init__()
        self.name = name
        self.pythonExperience = pythonExperience
        self.curiosity = curiosity
        self.skills = skills


pwdList = ["Ib#", "Blo", "F09", "Hkf", "Ev!", "K%2", "Awe", "Cve", "Lee", "J61", "Gvc", "Dde"]

skillList = ["Git", "Django", "Flask", "Ansible", "CI"]

cdt = Candidate("YOU !", 0, 0, skillList)

for skill in cdt.skills:
    if skill in skillList:
        cdt.pythonExperience += 1
    else:
        cdt.curiosity += 1

if cdt.pythonExperience + cdt.curiosity > 4:
    pwdList.sort()
    thePassword = ""
    test = 'lol un castor"'
    for i in range(0, 5):
        thePassword += pwdList[i][1:]

    print("Give this password to Nathalie our HR manager: " + thePassword)