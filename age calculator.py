from datetime import datetime 
current_year = datetime.now().year
birth_year=int(input("Enter your are birth year : "))
age=current_year - birth_year
print("you are",age,"year old")
if(age>=18):
    print("you are adult")
else:
    print("you are minor")