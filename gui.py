from tkinter import *
from tkinter import ttk

root = Tk()
keys = []

def fetch(entries):
    ssn=""
    for entry in entries:
        if 'ssn' in entry[0]:
            if entry[0] == 'ssn3':
                ssn += entry[1].get()
                print (ssn)
            else:
                ssn += entry[1].get()+"-"
        else:
            field = entry[0]
            text  = entry[1].get()
            print('%s: %s' % (field, text))

content = ttk.Frame(root)
content.grid_columnconfigure(index=1,minsize=250)

ssn_label = ttk.Label(content, text="Employee\'s SSN")
ssn1 = ttk.Entry(content,width=10)
keys.append(('ssn1',ssn1))
ssn2 = ttk.Entry(content,width=8)
keys.append(('ssn2',ssn2))
ssn3 = ttk.Entry(content,width=10)
keys.append(('ssn3',ssn3))
federal_ein_lbl = ttk.Label(content, text="Employer identification number (EIN)")
federal_ein = ttk.Entry(content)
keys.append(("federal_ein",federal_ein))
wages_tips_compensation_label = ttk.Label(content, text="Wages, tips, other compensation")
wages_tips_compensation = ttk.Entry(content)
keys.append(("wages_tips_compensation",wages_tips_compensation))
fit_withheld_label = ttk.Label(content, text="Federal income tax withheld")
fit_withheld = ttk.Entry(content)
keys.append(("fit_withheld",fit_withheld))
ss_tips_label = ttk.Label(content, text="Social Security tips")
ss_tips = ttk.Entry(content)
keys.append(("ss_tips",ss_tips))
ss_wages_label = ttk.Label(content, text="Social Security wages")
ss_wages = ttk.Entry(content)
keys.append(("ss_wages",ss_wages))
ss_withheld_label = ttk.Label(content, text="Social Security tax withheld")
ss_withheld = ttk.Entry(content)
keys.append(("ss_withheld",ss_withheld))
employer_name_label = ttk.Label(content, text="Employer\'s name")
employer_name = ttk.Entry(content)
keys.append(("employer_name",employer_name))
employer_address_label = ttk.Label(content, text="Employer\'s address")
employer_address1 = ttk.Entry(content)
keys.append(("employer_address1",employer_address1))
employer_address2 = ttk.Entry(content)
keys.append(("employer_address2",employer_address2))
emp_name_label = ttk.Label(content, text="Employee\'s name")
emp_name = ttk.Entry(content)
keys.append(("emp_name",emp_name))
employee_address_label = ttk.Label(content, text="Employee\'s address")
employee_address1 = ttk.Entry(content)
keys.append(("employee_address1",employee_address1))
employee_address2 = ttk.Entry(content)
keys.append(("employee_address2",employee_address2))
allocated_tips_label = ttk.Label(content, text="Allocated tips")
allocated_tips = ttk.Entry(content)
keys.append(("allocated_tips",allocated_tips))
med_wages_label = ttk.Label(content, text="Medicare wages and tips")
med_wages = ttk.Entry(content)
keys.append(("med_wages",med_wages))
med_withheld_label = ttk.Label(content, text="Medicare tax withheld")
med_withheld = ttk.Entry(content)
keys.append(("med_withheld",med_withheld))
dependent_care_label = ttk.Label(content, text="Dependent care benefits")
dependent_care = ttk.Entry(content)
keys.append(("dependent_care",dependent_care))
non_qual_plan_label = ttk.Label(content, text="Nonqualified plans")
non_qual_plan = ttk.Entry(content)
keys.append(("non_qual_plan",non_qual_plan))
box12_codea_label = ttk.Label(content, text="12a- See instructtions for box 12")
box12_codea = ttk.Entry(content,width=8)
keys.append(("box12_codea",box12_codea))
box12_meaninga = ttk.Entry(content,width=24)
keys.append(("box12_meaninga",box12_meaninga))
box12_codeb_label = ttk.Label(content, text="12b")
box12_codeb = ttk.Entry(content,width=8)
keys.append(("box12_codeb",box12_codeb))
box12_meaningb = ttk.Entry(content,width=20)
keys.append(("box12_meaningb",box12_meaningb))
box12_codec_label = ttk.Label(content, text="12c")
box12_codec = ttk.Entry(content,width=6)
keys.append(("box12_codec",box12_codec))
box12_meaningc = ttk.Entry(content,width=18)
keys.append(("box12_meaningc",box12_meaningc))
box12_coded_label = ttk.Label(content, text="12d")
box12_coded = ttk.Entry(content,width=8)
keys.append(("box12_coded",box12_coded))
box12_meaningd = ttk.Entry(content,width=24)
keys.append(("box12_meaningd",box12_meaningd))
stat_employee_label = ttk.Label(content, text="Statutory emp")
stat_employee = ttk.Entry(content)
keys.append(("stat_employee",stat_employee))
retirement_plan_label = ttk.Label(content, text="Retirement plan")
retirement_plan = ttk.Entry(content)
keys.append(("retirement_plan",retirement_plan))
sick_pay_label = ttk.Label(content, text="Third-party sick day")
sick_pay = ttk.Entry(content)
keys.append(("sick_pay",sick_pay))



content.grid(column=0, row=0)
wages_tips_compensation_label.grid(column=3,row=1,sticky=W+E+N+S, padx=5)
wages_tips_compensation.grid(column=3,row=2,sticky=W+E+N+S, padx=5)
fit_withheld_label.grid(column=4,row=1,sticky=W+E+N+S, padx=5)
fit_withheld.grid(column=4,row=2,sticky=W+E+N+S, padx=5)
ss_tips_label.grid(column=2,row=3,sticky=W+E+N+S, padx=5)
ss_tips.grid(column=2,row=4,sticky=W+E+N+S, padx=5)
ss_wages_label.grid(column=3,row=3,sticky=W+E+N+S, padx=5)
ss_wages.grid(column=3,row=4,sticky=W+E+N+S, padx=5)
ss_withheld_label.grid(column=4,row=3,sticky=W+E+N+S, padx=5)
ss_withheld.grid(column=4,row=4,sticky=W+E+N+S, padx=5)
employer_name_label.grid(column=1,row=3,sticky=W+E+N+S, padx=5)
employer_name.grid(column=1,row=4,sticky=W+E+N+S, padx=5)
employer_address_label.grid(column=1,row=5,sticky=W+E+N+S, padx=5)
employer_address1.grid(column=1,row=6,sticky=W+E+N+S, padx=5)
employer_address2.grid(column=1,row=7,sticky=W+E+N+S, padx=5)
allocated_tips_label.grid(column=2,row=5,sticky=W+E+N+S, padx=5)
allocated_tips.grid(column=2,row=6,sticky=W+E+N+S, padx=5)
med_wages_label.grid(column=3,row=5,sticky=W+E+N+S, padx=5)
med_wages.grid(column=3,row=6,sticky=W+E+N+S, padx=5)
med_withheld_label.grid(column=4,row=5,sticky=W+E+N+S, padx=5)
med_withheld.grid(column=4,row=6,sticky=W+E+N+S, padx=5)
dependent_care_label.grid(column=3,row=7,sticky=W+E+N+S, padx=5)
dependent_care.grid(column=3,row=8,sticky=W+E+N+S, padx=5)
non_qual_plan_label.grid(column=4,row=7,sticky=W+E+N+S, padx=5)
non_qual_plan.grid(column=4,row=8,sticky=W+E+N+S, padx=5)
box12_codea_label.grid(column=2,row=9,sticky=W+E+N+S, padx=5)
box12_codea.grid(column=2,row=10,sticky=W)
box12_meaninga.grid(column=2,row=10,sticky=E, padx=5)
box12_codeb_label.grid(column=3,row=9,sticky=W+E+N+S, padx=5)
box12_codeb.grid(column=3,row=10,sticky=W)
box12_meaningb.grid(column=3,row=10,sticky=E, padx=5)
box12_codec_label.grid(column=4,row=9,sticky=W+E+N+S, padx=5)
box12_codec.grid(column=4,row=10,sticky=W)
box12_meaningc.grid(column=4,row=10,sticky=E, padx=5)
box12_coded_label.grid(column=2,row=11,sticky=W+E+N+S, padx=5)
box12_coded.grid(column=2,row=12,sticky=W)
box12_meaningd.grid(column=2,row=12,sticky=E, padx=5)
emp_name_label.grid(column=1,row=9,sticky=W+E+N+S, padx=5)
emp_name.grid(column=1,row=10,sticky=W+E+N+S, padx=5)
employee_address_label.grid(column=1,row=11,sticky=W+E+N+S, padx=5)
employee_address1.grid(column=1,row=12,sticky=W+E+N+S, padx=5)
employee_address2.grid(column=1,row=13,sticky=W+E+N+S, padx=5)
federal_ein_lbl.grid(column=2,row=13,sticky=W+E+N+S, padx=5)
federal_ein.grid(column=2,row=14,sticky=W+E+N+S, padx=5)
ssn_label.grid(column=3,row=13,sticky=W+E+N+S, padx=5)
ssn1.grid(column=3,row=14,sticky=W)
ssn2.grid(column=3,row=14)
ssn3.grid(column=3,row=14,sticky=E)

# ssn = ss1+'-'+ss2+'-'+ss3
# keys.append(('ssn',ssn))
generate = ttk.Button(content, text="Generate",command=(lambda e=keys: fetch(e)))
cancel = ttk.Button(content, text="Cancel",command=root.quit)
generate.grid(column=4, row=15,sticky=W)
cancel.grid(column=4, row=15,sticky=E)

# ssn_label.grid(column=1, row=2)
# ssn.grid(column=2, row=2)
# federal_ein_lbl.grid(column=4,row=2)
# federal_ein.grid(column=5,row=2)
# generate.grid(column=4, row=3)
# cancel.grid(column=5, row=3)

root.mainloop()


# from tkinter import *
# # id_field = 'a','b','c','e','1','2','3','4','5','6','7','8','9','10','11','12a','12b','12c','12d','13','14','15','16','17','18','19','20'
# fields = 'Employee\'s social security number', 'Employer identification number (EIN)','Employer\' name','Employees\' ', 'Country'
#
# def fetch(entries):
#    for entry in entries:
#       field = entry[0]
#       text  = entry[1].get()
#       print('%s: "%s"' % (field, text))
#
# def makeform(root, fields):
#    entries = []
#    for field in fields:
#       row = Frame(root)
#       lab = Label(row, width=30, text=field, anchor='w')
#       ent = Entry(row)
#       row.pack(side=TOP, fill=X, padx=5, pady=5)
#       lab.pack(side=LEFT)
#       ent.pack(side=RIGHT, expand=NO, fill=X)
#       entries.append((field, ent))
#    return entries
#
# def makeform1(root):
#    entries = []
#    ssn = Frame(root)
#    ssn_label = Label(ssn,text="Employee\'s social security number",borderwidth=1)
#    ssn_ent = Entry(ssn)
#    ssn_label.grid(row=0, column=0)
#    ssn_ent.grid(row=0, column=0)
#
#
#
# if __name__ == '__main__':
#    root = Tk()
#    content = Frame(root, padding=(3, 3, 12, 12))
#    frame = Frame(content, borderwidth=5, relief="sunken", width=200, height=100)
#    # ents = makeform(root, fields)
#    ents = makeform1(frame)
#    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
#    b1 = Button(root, text='Show',command=(lambda e=ents: fetch(e)))
#    b1.pack(side=LEFT, padx=5, pady=5)
#    b2 = Button(root, text='Quit', command=root.quit)
#    b2.pack(side=LEFT, padx=5, pady=5)
#    root.mainloop()