# author : Sarvin Nami
firstNumber = int(input("please enter an integere number between 1 - 9\n")) 
secondNumber = (int((firstNumber * 2 + 8 + firstNumber - 2) / 3) - firstNumber) * 4
print("for each number you have chosen our resault of calculation will be : ",secondNumber)