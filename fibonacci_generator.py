def fibonacci_series_generator(up_to:int) -> list[int]:
    arr = [0,1]
    for i in range(up_to):
        arr.append(sum(arr[-2:]))
    return arr[:-2]

def main():
    up_to = int(input("Fibonacci series up to: "))
    print(f"Printing the first {up_to} number in the fibonacci series")
    print(fibonacci_series_generator(up_to))

if __name__ == "__main__":
    main()