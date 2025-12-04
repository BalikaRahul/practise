n=456
remaning=0
while(n>0):
    lastNum=n%10
    remaning=remaning*10+lastNum
    n=n//10
if(n==remaning):
    print("parlindrome")
else:
    print("not a parlindrom")

