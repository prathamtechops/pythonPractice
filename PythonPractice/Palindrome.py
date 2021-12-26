while True:
    num = input("Enter a number: ")
    re = num[::-1]
    if re == num:
        print(f'{num} is palindrome number') 
        # The number is same when reversed
    else:
        print(f'{num} is not palindrome number')
    
