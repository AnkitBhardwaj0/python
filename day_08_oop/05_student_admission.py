"""
university wants to automate their admission process.
"""

class student:
     def __init__(self):
          self.__student_id=None
          self.__age=None
          self.__marks=None

     def get_id(self):
        return self.__student_id
     def set_id(self):
        self.__student_id=input("enter id")

     def get_age(self):
        return self.__age
     def set_age(self):
        self.__age=input("enter age")

     def get_marks(self):
        return self.__marks
     def set_marks(self):
        self.__marks=input("enter marks")

     def validate_age(self):
          self.set_age()
          age=self.get_age()
          try:
             age=int(age)
          except Exception as e:
             return False
          else:
              if 0<age>20:
                  self.__age=age
                  return True
              else:
                  return False
              
     def validate_marks(self):
         self.set_marks()
         marks=self.get_marks()
         try:
             marks=int(marks)
         except Exception as e:
             return False
         else:
             if 0 <= marks <=100:
                 self.__marks=marks
                 return True
             else:
                 return False
     
     def check_qualification(self):
         self.set_id()
         id=self.get_id()
         marks_result=self.validate_marks()
         age_result=self.validate_age()
         marks=self.get_marks()
         age=self.get_age()
         if marks_result==True and age_result==True:
             if marks >= 65 :
                 return True
             else:
                 return False
         else:
             return False

     def result(self):
         result=self.check_qualification()
         id=self.get_id()
         if result:
             print(f'id : {id } \npass for admitation')
         else:
             print(f'id : {id} \nfail')
             
s1=student()
s1.result()           

             

          
             
          
         
 

