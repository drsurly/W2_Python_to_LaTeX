# Elifaleth Cantu Alanis
# Date: 2/17/2016

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

lengthPath=0
for s in file_path.split("/"):
    lengthPath += 1

f = open(file_path, 'r+')
file_path = file_path.strip(s)
file_path = file_path+"/w-2_formatTesting.tex"
latexF = open(file_path,'w')
latexF.write("\\documentclass[10pt]{report}\n\\usepackage{tikz}\n\\usepackage{geometry}")
latexF.write("\n\geometry{legalpaper, portrait, margin=0in}\n\n")
latexF.write("\\newcommand\PlaceText[3]{%\n\\begin{tikzpicture}[remember picture,overlay]\n")
latexF.write("\\node[outer sep=0pt,inner sep=0pt,anchor=south west] \n at ([xshift=#1,yshift=-#2]current page.north west) {#3};\n")
latexF.write("\end{tikzpicture}%\n}\n\\begin{document}")
info = {}
i=0
field=""
numW2=0
listOfPersons = []
for line in f: # Reads all the lines in the file
    if (not line.isspace()): # Ignore al the empty lines
        if (line == "</w2>\n") or (line == "</w2>"):
            listOfPersons.append(info)
            info = {}
            numW2 += 1
        if (line[0] == '<'):
            if(field):
                info[category]=field
                field = ""
                i=0
            category = line.strip('<>\n')
        else:
            if (i==0):
                field = line.strip('\n')
                i += 1
            else:
                field = field+"\n"+line.strip('\n')

for p in listOfPersons:
    k = 0
    for k in range(0,4):
        Y = k*62
        name = ""
        suff = ""
        lastName = ""
        address = ""
        emploAddress = ""
        for key in p.keys():
            if(key == "federal_ein"):
                latexF.write("\n\PlaceText{"+str(95)+"mm}{"+str(53+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "employer_name"):
                latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(30+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "employer_address"):
                emploAddress = p[key]
            elif(key == "ssn"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(53+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "emp_name"):
                name = p[key]
            elif(key == "last_name"):
                lastName = p[key]
            elif(key == "emp_suffix"):
                suff=p[key]
            elif(key == "employee_address"):
                address = p[key]
            elif(key == "wages_tips_compensation"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(15+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "fit_withheld"):
                latexF.write("\n\PlaceText{"+str(166)+"mm}{"+str(15+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "ss_wages"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(22+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "ss_withheld"):
                latexF.write("\n\PlaceText{"+str(166)+"mm}{"+str(22+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "med_wages"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(28+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "med_withheld"):
                latexF.write("\n\PlaceText{"+str(166)+"mm}{"+str(28+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "ss_tips"):
                latexF.write("\n\PlaceText{"+str(95)+"mm}{"+str(22+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "allocated_tips"):
                latexF.write("\n\PlaceText{"+str(95)+"mm}{"+str(28+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "eic_payment"):
                print(p[key])
            elif(key == "dependent_care"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(34+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "non_qual_plan"):
                latexF.write("\n\PlaceText{"+str(166)+"mm}{"+str(34+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "stat_employee"):
                latexF.write("\n\PlaceText{"+str(131)+"mm}{"+str(46+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "retirement_plan"):
                latexF.write("\n\PlaceText{"+str(143)+"mm}{"+str(46+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "sick_pay"):
                latexF.write("\n\PlaceText{"+str(154)+"mm}{"+str(46+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box14_codea"):
                print(p[key])
            elif(key == "boxe14_meaninga"):
                print(p[key])
            elif(key == "box14_codeb"):
                print(p[key])
            elif(key == "boxe14_meaningb"):
                print(p[key])
            elif(key == "box14_codec"):
                print(p[key])
            elif(key == "boxe14_meaningc"):
                print(p[key])
            elif(key == "box12_codea"):
                latexF.write("\n\PlaceText{"+str(95)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_meaninga"):
                latexF.write("\n\PlaceText{"+str(105)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_codeb"):
                latexF.write("\n\PlaceText{"+str(130)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_meaningb"):
                latexF.write("\n\PlaceText{"+str(140)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_codec"):
                latexF.write("\n\PlaceText{"+str(166)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_meaningc"):
                latexF.write("\n\PlaceText{"+str(176)+"mm}{"+str(40+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_coded"):
                latexF.write("\n\PlaceText{"+str(95)+"mm}{"+str(46+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "box12_meaningd"):
                latexF.write("\n\PlaceText{"+str(105)+"mm}{"+str(46+Y+k)+"mm}{"+p[key]+"}")
            elif(key == "state1_code"):
                print(p[key])
            elif(key == "state1_ein"):
                print(p[key])
            elif(key == "state1_wages"):
                print(p[key])
            elif(key == "state1_tax"):
                print(p[key])
            elif(key == "local1_wages"):
                print(p[key])
            elif(key == "local1_tax"):
                print(p[key])
            elif(key == "locality1"):
                print(p[key])
            elif(key == "state2_code"):
                print(p[key])
            elif(key == "state2_ein"):
                print(p[key])
            elif(key == "state2_wages"):
                print(p[key])
            elif(key == "state2_tax"):
                print(p[key])
            elif(key == "local2_wages"):
                print(p[key])
            elif(key == "local2_tax"):
                print(p[key])
            elif(key == "locality2"):
                print(p[key])
            #elif(key == "year"):
             #   print(info[key])
            elif(key == "amended"):
                print(p[key])
            elif(key == "amended_date"):
                print(p[key])
            #elif(key == "print_instruction"):
             #   print(info[key])

        latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(48+Y+k)+"mm}{"+name+" "+suff+" "+lastName+"}")

        i = 0
        for a in address.split('\n'):
            if(i==0):
                a1 = a
            else:
                a2 = a
            i += 1
        latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(53+Y+k)+"mm}{"+a1+"}")
        latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(56+Y+k)+"mm}{"+a2+"}")

        i = 0
        for a in emploAddress.split('\n'):
            if(i==0):
                ae1 = a
            else:
                ae2 = a
            i += 1
        latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(34+Y+k)+"mm}{"+ae1+"}")
        latexF.write("\n\PlaceText{"+str(15)+"mm}{"+str(38+Y+k)+"mm}{"+ae2+"}")

        k += 1

    latexF.write("\n\\newpage")
latexF.write("\n\\end{document}")

