# Python has __init__() function just like the constructor in C++
# self is a paramter we can pass in a function in a class. Whatever we write after self. will make a var in that class of that particular object
# Examples for this can be shown below

class Marks:
    def __init__(self,name,maths,bio,science):
        self.name = name
        self.maths = maths
        self.bio = bio
        self.science = science

    def Get_Result(self):
        self.result = self.maths + self.bio + self.science
        self.result /= 300
        self.result *=100
        return self.result

Student1 = Marks("Tim",89,59,79)
Student2 = Marks("Billy",95,85,78)

# You cannot concatenate float and string 

print("Result of " + Student1.name + " is: ")
print(Student1.Get_Result())
print("Result of " + Student2.name + " is: ")
print(Student2.Get_Result())

# Unless you convert it into string

print("Result of " + Student1.name + " is: " + str(Student1.Get_Result()))
print("Result of " + Student2.name + " is: " + str(Student2.Get_Result()))