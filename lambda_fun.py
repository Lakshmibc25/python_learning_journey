students = [
    {"name":"lakshmi", "marks":10},
    {"name":"harshitha","marks":96},
    {"name":"priya","marks":78}
]
students.sort(key= lambda x:x["marks"],reverse= True)
print(students)