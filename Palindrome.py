Palin = input("input a word: ")


Palin = Palin.replace(" ","")
Pain = Palin.lower()

Palin_rev = Palin[::-1]

if Palin_rev == Palin:
    print ("\n\n\n Yes! it's a palindrome")
else:
    print ("\n\n\n Sorry it's not a palindrome")