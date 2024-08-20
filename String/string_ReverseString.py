n = str(input("Enter a string: "))
if n == "":
    print("Empty string")
elif n == n[::-1]:
    print("Palindrome" + "\n" + "Reverse of the string: " + n[::-1])
else:
    print("Not a palindrome" + "\n" + "Reverse of the string: " + n[::-1])

