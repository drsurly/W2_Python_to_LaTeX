# Elifaleth Cantu Alanis
# Date: 2/17/2016

f = open('w-2Format', 'r+')
info = {}
i=0
field=""
for line in f: # Reads all the lines in the file
    if (not line.isspace()): # Ignore al the empty lines
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

i = 1
for key in info.keys():
    if(key == 'control_number'):
        print(info[key])
    elif(key == "federal_ein"):
        print(info[key])
    elif(key == "employer_name"):
        print(info[key])
    elif(key == "employer_address"):
        print(info[key])
    elif(key == "ssn"):
        print(info[key])
    elif(key == "emp_name"):
        print(info[key])
    elif(key == "last_name"):
        print(info[key])
    elif(key == "emp_suffix"):
        print(info[key])
    elif(key == "employee_address"):
        print(info[key])
    elif(key == "wages_tips_compensation"):
        print(info[key])
    elif(key == "fit_withheld"):
        print(info[key])
    elif(key == "ss_wages"):
        print(info[key])
    elif(key == "ss_withheld"):
        print(info[key])
    elif(key == "med_wages"):
        print(info[key])
    elif(key == "med_withheld"):
        print(info[key])
    elif(key == "ss_tip"):
        print(info[key])
    elif(key == "allocated_tips"):
        print(info[key])
    elif(key == "eic_payment"):
        print(info[key])
    elif(key == "dependent_care"):
        print(info[key])
    elif(key == "non_qual_plan"):
        print(info[key])
    elif(key == "stat_employee"):
        print(info[key])
    elif(key == "retirement_plan"):
        print(info[key])
    elif(key == "sick_pay"):
        print(info[key])
    elif(key == "box14_codea"):
        print(info[key])
    elif(key == "boxe14_meaninga"):
        print(info[key])
    elif(key == "box14_codeb"):
        print(info[key])
    elif(key == "boxe14_meaningb"):
        print(info[key])
    elif(key == "box14_codec"):
        print(info[key])
    elif(key == "boxe14_meaningc"):
        print(info[key])
    elif(key == "box12_codea"):
        print(info[key])
    elif(key == "boxe12_meaninga"):
        print(info[key])
    elif(key == "box12_codeb"):
        print(info[key])
    elif(key == "boxe12_meaningb"):
        print(info[key])
    elif(key == "box12_codec"):
        print(info[key])
    elif(key == "boxe12_meaningc"):
        print(info[key])
    elif(key == "box12_coded"):
        print(info[key])
    elif(key == "boxe12_meaningd"):
        print(info[key])
    elif(key == "state1_code"):
        print(info[key])
    elif(key == "state1_ein"):
        print(info[key])
    elif(key == "state1_wages"):
        print(info[key])
    elif(key == "state1_tax"):
        print(info[key])
    elif(key == "local1_wages"):
        print(info[key])
    elif(key == "local1_tax"):
        print(info[key])
    elif(key == "locality1"):
        print(info[key])
    elif(key == "state2_code"):
        print(info[key])
    elif(key == "state2_ein"):
        print(info[key])
    elif(key == "state2_wages"):
        print(info[key])
    elif(key == "state2_tax"):
        print(info[key])
    elif(key == "local2_wages"):
        print(info[key])
    elif(key == "local2_tax"):
        print(info[key])
    elif(key == "locality2"):
        print(info[key])
    elif(key == "year"):
        print(info[key])
    elif(key == "amended"):
        print(info[key])
    elif(key == "amended_date"):
        print(info[key])
    elif(key == "print_instruction"):
        print(info[key])

    print (i)
    i += 1