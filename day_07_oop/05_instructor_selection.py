class instructorSelection:
    def __init__(self,name,skills,experience,feedback):
        self.__name=name
        self.__skills=skills
        self.__experience=experience
        self.__feedback=feedback
    
    def set_name(self,name):
        self.__name=name
    
    def set_skills(self,skills):
        self.__skills=skills

    def set_experience(self,experience):
        self.__experience=experience

    def set_feedback(self,feedback):
        self.__feedback=feedback
    
    def check_eligibility(self):
        if self.__experience > 3 and self.__feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__feedback >= 4:
            return True
        return False
    
    def allocate_course(self,technology):
        if self.check_eligibility()==True and technology in self.__skills:
            return True 
        return False
        

    def show(self, technology):
        if self.allocate_course(technology):
            print(f"{self.__name} is eligible for {technology} course")
        else:
            print(f"{self.__name} is not eligible for {technology} course")

ins1=instructorSelection("amit",["java","python","c","c++"],3,4)
ins1.show("python")
ins2=instructorSelection("anshu",["java","python","c++"],4,4)
ins2.show("python")
ins3=instructorSelection("shan",["java","python","c++"],4,4)
ins3.show("c")
        
    

        