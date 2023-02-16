dog = {}        #1
dog["name"] = "Helena"        #2
dog["color"] = "Blue"
dog["breed"] = "Spanish"
dog["legs"] = "2"
dog["age"] = "16"
studen_dictionary = {"first_name" : "Helena" , "last_name" : "Troncoso" , "gender" : "female" , "age" : "16" , "marital_status" : "single" , "skills" : ["creativity", "imagine"] , "country" : "Spain" , "City" : "Jerez" , "address" : "street"}       #3
print(len(dog))     #4
values_skills = studen_dictionary["skills"].values()      #5
type(studen_dictionary["skills"])