def create_phone_number(n):
    #your code here
    number=""
    for i,val in enumerate(n):
        if i == 0:
            number +="("
            number+=str(val)
        elif i == 2:
            number+=str(val)
            number +=") "
        elif i==5:
            number+=str(val)
            number+="-"
        else:
            number+=str(val)
    print(number)
    return number

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])