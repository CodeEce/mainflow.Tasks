# DATA ANALYSIS WITH PYTHON
# TASK 1 : Write a python program to create a list,a dictionary,and
# a set,Perform basic operations like adding,removing,and modifying elements.
# creating list
gadgets = ["vivo", "oppo", "samsung","motorola"]
gadgets.append("iphone")
gadgets[3] = "redmi"
gadgets.remove("oppo")
print("The New gadgets list :",gadgets)

# Creating dictionary
patient_data = {"patientId":"IDP01","Name":"Vinothini","age":25}
patient_data["BloodGroup"] = "A+ve"
patient_data["age"] = 28
del patient_data["patientId"]
print("The updated data of Patient:",patient_data)

# Creating set
deparment = {"physics","chemistry","maths"}
deparment.add("computer")
deparment.update(["AI","DSA"])
deparment.discard("physics")
print("The updated set :",deparment)

