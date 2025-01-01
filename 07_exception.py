try:
    a=int(input("enter your number: "))
    print(a)
except Exception as e:
    print(e,type(e))
print("thank you")

'''
output:
enter your number: harry
invalid literal for int() with base 10: 'harry' <class 'ValueError'>
thank you
'''
