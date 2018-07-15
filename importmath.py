import math
import sys #system

#def mycalculation(x, y):
#    return math.log(x, y)
#
#if __name__=="__main__":
#    print("You are running {script}".format(script=sys.argv[0]))
##    a = (sys.argv[1])
##    b = (sys.argv[2])
##    print(mycalculation(a, b))
    
    
class MyFirstClass:
    def my_Print(a, b):
        for item in range(b, a+1):
            print(item)
    def CheckAnB(a, b):
        if a > b:
            print("a is greater than b!")
            MyFirstClass.my_Print(a, b)
        else:
            print("a is less than or equal to b!")
    def my_Divide(a, b):
        try:
            result = a/b
            print(result)
        except:
            print("b is 0")
MyFirstClass.CheckAnB(10,1)
MyFirstClass.my_Divide(1, 0)
