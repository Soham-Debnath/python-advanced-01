a=int(input("enter a= "))
b=int(input("enter b= "))
# print(f"a/b is {a/b}")
# b=0 dunga to "ZeroDivisionError: division by zero" dikhayega

if(b==0):
    raise ZeroDivisionError("oye zero se divide mat kar")
else:
    print(f"a/b is {a/b}")
# b=o dunga to ab "ZeroDivisionError: oye zero se divide mat kar" dikhayega