print("="*25)
name=input("Enter Name : ")
id=int(input("Enter ID : "))
gender=input("Enter Gender : ")
kh=int(input("Enter Score Khmer : "))
math=int(input("Enter Score Math : "))
english=int(input("Enter Score English : "))
total=kh+math+english
avg=total/3
if 0>=avg<50:
    grade = "F"
elif 50>=avg<=65:
    grade = "E"
elif 66>=avg<=75:
    grade = "D"
elif 76>=avg<=85:
    grade ="C"
elif 86>=avg<=95:
    grade = "B"
elif 96>=avg<=100:
    grade = "A"
else:
    print("Invalia score")
print("="*25)
print("="*25)
print(f"Name : {name}")
print(f"ID : {id}")
print(f"Gender : {gender}")
print(f"Score Khmer : {kh}")
print(f"Score Math : {math}")
print(f"Score English : {english}")
print(f"Total Score : {total}")
print(f'Average : {avg}')
print(f"Grade : {grade}")
print("="*25)