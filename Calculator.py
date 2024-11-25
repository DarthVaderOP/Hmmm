lol=input("Enter 1st no:")
yo=input("Enter mathematical operators(+,-,*,/,^2.)")
if yo == "+":
    hm=input("Enter 2nd no:")
    ans=float(lol)
    ans+=float(hm)
    ans=float(ans)
    print(f"The answer is:{ans}")
if yo=="-":
    hm=input("Enter 2nd no:")
    ans=float(lol)
    ans-=float(hm)
    ans=float(ans)
    print(f"The answer is:{ans}")
if yo=="*":
    hm=input("Enter 2nd no:")
    ans=float(lol)*float(hm)
    ans=float(ans)
    print(f"The answer is:{ans}")
if yo=="/":
    hm=input("Enter 2nd no:")
    ans=float(lol)/float(hm)
    ans=float(ans)
    print(f"The answer is:{ans}")
if yo=="^2":
    ans=float(lol)*float(lol)
    ans=float(ans)
    print(f"The answer is:{ans}")
else:
    print("Sorry, not availaible. See the options.")