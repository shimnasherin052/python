def armstrong_check(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp % 10
        sum+=didgits ** 3
        temp//=10
        if num==sum:
            print(num,"is an a")
