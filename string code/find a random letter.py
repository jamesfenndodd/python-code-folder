import string
import random
rand_l=random.choice(string.ascii_uppercase)
print("the random letter you are serching for is:")
print(rand_l)
word=("PSEUDOPSEUDOHYPOPARATHYROIDISM")
num=word.count(rand_l)
if num > 0:
    print("the occurance of this letter in the phrase is:")
    print(num)
else:
    print("this letter does not appear in the phrase")
