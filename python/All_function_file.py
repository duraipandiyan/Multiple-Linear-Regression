class Allfunction:
    def Subfields(self,fields):
        print("Sub-fields in AI are")
        print('')
        count=0
        for i in fields:
            count+=1
            print(count,".",i)
#    odd_even         
    def OddEven(self,num):
        if num%2!=0:
            return num," is odd number"
        else:
            return num," is even number"
        
#         finding marrage eligiblity
        
    def eligibility(self,male_age,female_age):
        if male_age<21 and female_age<18:
            return "Both are not eligible for marry"
        elif male_age>=21 and female_age<18:
            return "Male eligible for marry but female not eligible for marry"
        elif male_age<21 and female_age>=18:
            return "Male is not eligible for marry but female eligible for marry"
        else:
            return "Both are eligible for marry"
        
#         Finding percentage
        
    def percentage(self,English,Tamil,Maths,science, social):
        Total=English+Tamil+Maths+science+social
        return Total/500*100
    
# finding Area
    def triangle(self,Height,Breadth):
        Area_formula=(Height*Breadth)/2
        return Area_formula   
    
# finding perimeter

    def perimeter(self,Height1, Height2,Breadth):
        Perimeter_formula=Height1+Height2+Breadth
        return  Perimeter_formula
    
    
   