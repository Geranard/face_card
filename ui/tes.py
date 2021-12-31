import json

with open("../data/class_student.json", mode="r") as file:
    temp = json.load(file)

# print(temp)

# for data in temp:
#     # print(f"{data}")
#     # student = temp[f"{data}"]["StudentNIM"]
#     session = temp[f"{data}"]["Session"]
#     for date in session:
#         print(date)
#         # print(session[f"{date}"])
#         # absence = session[f"{date}"]
#         # for nim in absence:
#         #     print(absence[nim])

data = {
    "ABC123":{
        "Subject": "AIUEO",
        "StudentNIM": [],
        "Lecturer": "Heru Geming",
        "Session": {},
    }
}

temp.update(data)

with open("../data/class_student.json", mode="w") as file:
    file.write(str(json.dumps(temp, indent=4, sort_keys=True)))