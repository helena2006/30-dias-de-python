thirty = "Thirty"       #1
days = "days"
of = "of"
python = "Python"
space = "  "
full_string = thirty + space + days + space + of + space + python
print(full_string)

coding = "Coding"       #2
f0r = "for"
all = "all"
full_string_2 = coding + space + f0r + space + all
print(full_string_2)

company = full_string_2     #3
print(company)      #4
print(len(company))        #5
print(company.upper())      #6
print(company.lower())      #7

print(company.capitalize())     #8
print(company.title())
print(company.swapcase())

first_slice = company[0:3]      #9
print(first_slice)

company.index(coding)       #10
company.replace("coding" , "Python")        #11
company.replace("Python" , "Everyone")      #12
company.replace("all" , "Python")
print(company.split( ))     #13
string_1 = "Facebook , Google , Microsoft , Apple , IBM , Oracle , Amazon"      #14
print(string_1.split(", "))

first_letter = company[0]       #15
print(first_letter)
last_letter = company[-1]       #16
print(last_letter)
index_10 = company[10]      #17
print(index_10)

PFE = "Python for everyone"     #18
CFA = "Coding for all"      #19
print(CFA.index("C"))       #20
print(CFA.index("f"))       #21
print(CFA.rfind("l"))       #22
sentence = "You cannot end a sentence with because because because is a conjunction"        #23
print(sentence.index("because"))
print(sentence.rindex("because"))       #24
sentence.replace("because because because")     #25
print(sentence.find("because"))     #26
#27 same question in point 25