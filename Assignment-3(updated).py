class CollegeStudent:
    #init
    def __init__(self,sname,regn,sdept,syear):
            self.sname=sname
            self.regn=regn
            self.sdept=sdept
            self.syear=syear
    
    def basic_details(self):
        return self.sname,self.regn,self.sdept,self.syear
        
    #direct argument
    def batch_details(self,batch,bname):
        print("BATCH DETAILS")
        print("Name:",self.sname)
        print("Register number:",self.regn)
        print("Batch:",batch)
        print("Year:",bname)

    #**kwargs   
    def languages_studied(self,**kwargs):
        print("\n"+self.sdept+" DEPARTMENT LANGUAGES SEMESTER WISE")
        study= []
        for key,value in kwargs.items():
            study.append("{} in {}".format(value,key))
        print (study)
        
    #*args
    def percentage(self,*args):
        print("\n"+self.sname+"("+self.regn+")'s CGPA")
        total = 0
        for x in args:
            total += x
        print ("CGPA is:",total/4)   

    #try-except   
    def fee(self,sum):
        print("\nFEES FOR THE YEAR ",self.syear)
        placement_fee =10000
        while True:
                try:
                    annual_fee=placement_fee+sum
                    print("The annual fee for this year is:",annual_fee)
                    break 
                except Exception as e:
                    print("ERROR OCCURRED!!!!",e,"Please enter the valid amount")
                    break
    
    #match case
    def match_section(self):
        print("\nSECTIONS FOR THE DEPARTMENT ",self.sdept+"\t")
        choice=self.sdept
        match choice:
          case "CSE":
              print("A1-A4")
          case "IT":
              print("B1-B4")
          case "ECE":
              print("C1-C4")
          case "EEE":
              print("D1-D4")
          case "MECH":
              print("E1-E4")
          case _:
              print("Wrong choice") 


student=CollegeStudent("Bunny","513521104099","CSE",3)
student.basic_details()
student.batch_details("2021-2025","Spartans")
student.languages_studied(sem1="Python", sem2="C", sem3="Java", sem4="Ruby") 
student.percentage(9.52,9.48,9.48,9.91)
student.fee(25000)
student.match_section()