def stack_test(n):
    if n < 0:
        return
    print("first part: ", n)
    stack_test(n-1)
    print("last part: ", n)


if __name__ == "__main__":
    stack_test(5)