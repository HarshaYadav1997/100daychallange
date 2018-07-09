import random as ran

def game(count,point):
    count =count + 1
    num1=int(ran.randint(1,999))
    num2=int(ran.randint(1,999))
    problem=int(ran.randint(1,2))
    
    if(problem==1):
        sym=' + '
        result = int(num1+num2)
    elif(problem==2):
        sym=' - '
        result = int(num1-num2)
    print('\n'+'Ques.'+str(count)+'=> '+str(num1)+sym+str(num2))
    
    ans=int(input('Ans. '))
    if(ans==result):
        print("Your Answer is Correct")
        points+=1
        print("Total Correct Answer :",point)
        game(count,points)
    else:
        print("Incorrect Answer")
        print("Total Correct Answer :",point)
        game(count,point)
    return count


count=0
point=0
game(count,point)
