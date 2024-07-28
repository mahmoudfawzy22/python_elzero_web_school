students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

# for student in students:
#     print('-' * 30)
#     print(f"-- student Name ==> {student}")
#     print('-' * 30)
#     total_point = 0  

#     for degree in students[student]:

#         if students[student][degree] == 'A':
#             total_point += 100
#             print(f"- {degree} ==> 100 points")

#         elif students[student][degree] == 'B':
#             total_point += 80
#             print(f"- {degree} ==> 80 points")

#         elif students[student][degree] == 'C':
#             total_point += 40
#             print(f"- {degree} ==> 40 points")
#         elif students[student][degree] == 'D':
#             total_point += 10
#             print(f"- {degree} ==> 10 points")
#     else:
#         print("Total point Is {} Is points".format(total_point))        

for student in students:
    print('-' * 30)
    print(f"-- student Name ==> {student}")
    print('-' * 30)

    total_point = 0  

    for studentCourse, studentDegree in students[student].items():
        if  studentDegree == 'A':
            total_point += 100
            print(f"- {studentCourse} ==> 100 points")

        elif studentDegree == 'B':
            total_point += 80
            print(f"- {studentCourse} ==> 80 points")

        elif studentDegree == 'C':
            total_point += 40
            print(f"- {studentCourse} ==> 40 points")

        elif studentDegree == 'D':
            total_point += 20
            print(f"- {studentCourse} ==> 20 points")

    else:
        print("Total point Is {} Is points".format(total_point))  
