while True:
  username = input("Please Enter Username: ")

  if username.lower() != 'kendo':
    print("invalid username")
    continue

  password = input("Please Enter Your Password: ")

  if password.lower() == 'swordfish':
    break
print("Access granted ")
