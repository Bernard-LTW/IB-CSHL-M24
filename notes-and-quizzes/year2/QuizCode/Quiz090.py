def doSomething(n):
    if n>0:
        doSomething(n-1)
        print(n)
        doSomething(n-1)

doSomething(3)