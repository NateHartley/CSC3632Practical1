folderpath1 = "/home/student/Documents/git_projects/known-cyber-attacks/1996-1999 Moonlight Maze attacks/README.md"
folderpath2 = "/home/student/Documents/git_projects/known-cyber-attacks/2009-2010 GhostNet and Shadow Net/README.md"
folderpath3 = "/home/student/Documents/git_projects/known-cyber-attacks/2009-2010 Stuxnet attacks on Iranian nuclear facilities/README.md"
folderpath4 = "/home/student/Documents/git_projects/known-cyber-attacks/2010 Operation Aurora Attack/README.md"
folderpath5 = "/home/student/Documents/git_projects/known-cyber-attacks/2011 PlayStation Network Outage/README.md"
folderpath6 = "/home/student/Documents/git_projects/known-cyber-attacks/2012-2016 Yahoo Data Breaches/README"
folderpath7 = "/home/student/Documents/git_projects/known-cyber-attacks/2013 Adobe Data Breach/README.md"
folderpath8 = "/home/student/Documents/git_projects/known-cyber-attacks/2014 Sony Pictures Hack/README.md"
folderpath9 = "/home/student/Documents/git_projects/known-cyber-attacks/2015 Ukraine Power Grid Hack/README.md"
folderpath10 = "/home/student/Documents/git_projects/known-cyber-attacks/2015-16 Democratic National Committee cyber attacks/README.md"
folderpath11 = "/home/student/Documents/git_projects/known-cyber-attacks/2017 NotPetya malware attack/README.md"
folderpath12 = "/home/student/Documents/git_projects/known-cyber-attacks/2017 WannaCry Cyber Attack/README.md"
folderpath13 = "/home/student/Documents/git_projects/known-cyber-attacks/2019 CapitalOne-CyberAttack/README.md"
folderpath14 = "/home/student/Documents/git_projects/known-cyber-attacks/2020 SolarWinds cyberattack/README.md"
folderpath15 = "/home/student/Documents/git_projects/known-cyber-attacks/2021 Florida Water Supply Attack/README.md"

folderpathList = [folderpath1, folderpath2, folderpath3, folderpath4, folderpath5, folderpath6, folderpath7, folderpath8, folderpath9, folderpath10, folderpath11, folderpath12, folderpath13, folderpath14, folderpath15]
i = 0
str = ""

for i in folderpathList:
    print(i)
    file = open(i, 'r') # opens currect README.md
    lines = file.readlines() # adds lines to list
    str = str.join(lines) # converts list into long string

with open('Compile.md', 'w') as compileFile: # opens my file
    compileFile.write(str) # writes long string to it

## Current Problem! ##
# something is wrong with str, it gets stuck on the 2019 README.md and just prints the same line over and over again
# all content before that works fine, but 2019 seems to mess everything up