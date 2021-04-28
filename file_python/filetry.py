#def main():

 #   answer = 0

#def add(x, y):
 #   return x + y

def calculate():
   # answer = 0
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    if operation == '+':
        file = open("data.txt", "r")
        for line in file:
            answer = ((line))

        f=open("out.txt",'w')
        print(answer, file=f)
        file.close()

      #  print(answer, file=f)
      # num1 = int(input('Please enter the first number: '))
       # num2 = int(input('Please enter the second number: '))
       # print(num1, "+", num2, "=", add(num1, num2))
       # output = add(num1, num2) 
      #  file = open("out.txt","a") 
       # file.write(output) 
       # file.close() 
    

    file = open("data.txt", "r")

   # def add()

    #for line in file:
     #   answer += (int (line))

   # print(answer)
   # f=open("out.txt",'w')

    #print(answer, file=f)

    #file.close()

calculate()    





