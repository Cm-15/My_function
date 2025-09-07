import sys

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <number1> <number2>")
        return
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print(f"ผลรวมคือ: {result}")
    except ValueError:
        print("ValueError")
if __name__ == "__main__":
    main()
