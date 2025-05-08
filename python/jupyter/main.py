import math

def math_fail(x,y):
    print(f'x is {x} and y is {y}')
    try:
        return x/y
    except:
        return math.nan
def main():
    print("Hello from jupyter!")
    x = math_fail(6,0)
    if math.isnan(x):
        print(f"Divide by zero error.")
    else:
        print(f'The answer is {x}')


if __name__ == "__main__":
    main()
