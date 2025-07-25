import random
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0','1','2','3','4','5','6','7','8','8','9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '-']

print("Welcome to the PyPassword Generator!")

password_list = []

lenght_letters = int(input("how many letters: "))
for _ in range(0, lenght_letters):
    random_letter = random.choice(Letters)
    password_list += random_letter

lenght_numbers = int(input("how many numbers: "))
for _ in range(0, lenght_letters):
    random_number = random.choice(Numbers)
    password_list += random_number

lenght_symbols = int(input("how many symbols: "))
for _ in range(0, lenght_symbols):
    random_symbols = random.choice(Symbols)
    password_list += random_symbols


# # print as string 
# passowrd_str = ""
# for c in password_list:
#     passowrd_str += c
# print(passowrd_str)


# Print after shuffled 
random.shuffle(password_list)
passowrd_shuffled = ""

for ch in password_list:
    passowrd_shuffled += ch
print(passowrd_shuffled)
