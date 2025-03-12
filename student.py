# Description: This file is used to test the Student class in the student.py file


class Student():
    
    def __init__(self, avggrade:str, name:str , age:int) -> None:
        self.avggrade = avggrade
        self.name = name
        self.age = age
        self.benchmark:bool = True
        self.s_grade:int = 0
        
    def conversion(self,avggrade:str) -> int:
        convert = {'F':55 , 'F+':60 , 'D':65 , 'D+':70 , 'C':75 , 'C+':80, 'B':85,'B+':90,'A':95,'A+': 100}
        self.s_grade = convert[avggrade]
        return self.s_grade
        
    def elegibility(self,avggrade:str=None) -> bool:
        if avggrade == None:
            avggrade = self.avggrade
        self.conversion(avggrade)
        
        if self.s_grade >=90:
            self.benchmark = True
        else:
            self.benchmark = False
        return self.benchmark
            
    
        
        
student1 = Student(name="Etho", age=15, avggrade='C')
student2 = Student(name="mia", age=16, avggrade='B+')

print(student2.elegibility())
