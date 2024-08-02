# Anayze please 
print("Gimme two numbers and i will divide them .")
print("Enter the 'q' to quit ")
while True:
    first_number = input("\n First Number :")
    if first_number ==0:
        break
    second_number = input("Enter the number :")
    try:
        answer = int(first_number)/int(second_number)
    except:
        print(answer)