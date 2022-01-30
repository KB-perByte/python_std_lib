# day - 3
# nested functions as it is dynamicly loaded the is almost 20 to 30 % slower than global var func

from typing import List

list_of_students: List[str] = ["Yu", "Ali", "Mark"]

def pick_students(students: List[str]):

    if not all(isinstance(item, str) for item in students): #validation before sub/ nested function call
        raise TypeError("Students must be a list of string.")

    def find_priority_student(student: str): # relatively costly opeartion here
        return 1/len(student) # prioritize students with shortest names

    priorities: List[float] = list(map(lambda student: find_priority_student(student), students))
    highest_priority_index = priorities.index(max(priorities))

    return students[highest_priority_index]

print(pick_students(list_of_students))