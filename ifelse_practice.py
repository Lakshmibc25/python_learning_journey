year = int(input("enter a  year:"))
if year % 400 ==0:
  print("year, is a leap year ")
else:
  print("year is not a leap year")

  
grade = input("enter your grade (A,B,C,D,E,F):").upper()
if grade == "A":
    print(" A excellent performance")
elif grade == "B":
    print(" B good pperformance")
elif grade =="C":
    print("first class")
elif grade == "D":
    print("need improvement")
else:
    print("you are fail better luck next time")
