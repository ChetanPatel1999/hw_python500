#wap to print word to given number.
number={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30:"thirty",
    40:"fourty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninty",
    100:"one hundred",
    200:"two hundred ",
    300:"three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred",
}
num=int(input("enter a num : "))#511
p=len(str(num))
if p==2:
    l=num%10
    m=num-l
    print(number[num]) if num in number else print(f"{number[m]} {number[l]}")
else :
    c=(num//100)*100
    m = ((num//10)%10)*10 if (num%100) not in number else (num%100)
    l=num%10
    print(number[num]) if num in number else print(f"{number[c]} ", number[m] if m in number and ('0' not in str(m)) else f"{number[m]} {number[l]}" )  