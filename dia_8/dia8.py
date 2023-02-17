dog = {}        #1
dog["name"] = "Helena"        #2
dog["color"] = "Blue"
dog["breed"] = "Spanish"
dog["legs"] = "2"
dog["age"] = "16"

studen_dictionary = {"first_name" : "Helena" , "last_name" : "Troncoso" , "gender" : "female" , "age" : 16 , "marital_status" : "single" , "skills" : ["creativity", "adaptability"] , "country" : "Spain" , "City" : "Jerez" , "address" : {"city" : "Jerez" , "CP" : "11405"}}       #3
print(len(dog))     #4
values_skills = studen_dictionary["skills"].values()      #5
type(studen_dictionary["skills"])

studen_dictionary["skills"].append("teamwork" , "communication")
keys = dog.keys()       #7
print(keys)
values = dog.values()       #8
print(values)
print(dog.items())      #9

dog.pop("first_name")       #10
del dog     #11