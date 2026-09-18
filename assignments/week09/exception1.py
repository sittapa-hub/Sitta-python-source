try:
    num1 = float(input("กรอกเลขตัวที่1: "))
    num2 = float(input("กรอกเลขตัวที่2: "))
    operator = input("กรอกเครื่องหมาย(+,-,*,/): ")
    result = 0          
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2
    else:
        raise ValueError("ต้องกรอกเครืองหมาย +,-,*,/ เท่านั้น")

    print(f"{num1} {operator} {num2} = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
     print("ไม่สามารถหารด้วยศูนย์ได้")

else:
    print("ทำงานได้สมบูรณ์")

finally:
    print("จบการทำงาน")
