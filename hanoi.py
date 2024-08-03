steps=0
def hanoi(n,s,e,d):
    global steps
    steps+=1
    if n==1:
        print("move",1,"from",s,"to",d)
        return
    hanoi(n-1,s,d,e)
    print("move",n,"from",s,"to",d)
    hanoi(n-1,e,s,d)
hanoi(3,"source","extra","destiny")

    
