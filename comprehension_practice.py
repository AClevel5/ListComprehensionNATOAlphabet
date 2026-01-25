#adding 1 to each num
# list_1 = (1, 2, 3)
# list_2 = [n + 1 for n in list_1]
# print(list_2)

#splitting each letter of a work into a list
# name = "Alex"
# letters_list = [letter for letter in name]
# print(letters_list)

#multiplying each number in a range
# num_range = range(1,5)
# num_multiplied = [n * 2 for n in num_range]
# print(num_multiplied)

#using a condition to determine if an item belongs in a new list.
# names = ("Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie")
# short_names = [name for name in names if len(name) == 4]
# cap_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)
# print(cap_names)

#Comprehension with dictionaries
# import random
# names = ("Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie")
# students = {name:random.randint(1,100) for name in names}
# passed_students = {name:score for name, score in students.items() if score > 60}
# print(passed_students)

#Convert dict of days and temps to f
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:temp * 9/5 + 32 for day, temp in weather_c.items()}
# print(weather_f)

#comprehension with pandas
# import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
# student_data_frame = pandas.DataFrame(student_dict)
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)