def main():
    expression = input("Expression: ").lower().strip()
    result = interpreter(expression)
    print(result)

def interpreter(expression):

    x,y,z = expression.split(" ")
    x = float(x)
    z = float(z)

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
main()
