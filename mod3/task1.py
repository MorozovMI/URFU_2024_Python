user_input = input ("Enter: ")
a, b, c = sorted(map(int, user_input.split())) if -1000 >= int(user_input.split()[0]) and int(user_input.split()[2]) <= 1000 else  print("Invalid input")
print(a, b, c)