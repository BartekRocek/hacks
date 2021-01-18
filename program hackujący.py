import random
print("wpisz cztero-literowy kod aby go zhakować:")
hacks = random.randint(1000, 9000)
number_input = input()
number_input = int(number_input)
kod = number_input
while hacks != kod:
    hacks = random.randint(1000, 9000)
    print(hacks)
    if hacks == kod:
        print("gotowe!")
