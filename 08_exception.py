try:
    a=int(input("enter your number: "))
    print(a)

except ValueError as v:
    print("it is a value-error",type(v))
except Exception as e:
    print(e,type(e))
print("thank you")

'''
output:
enter your number: harry
it is a value-error <class 'ValueError'>
thank you
'''