import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x]  for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2) 

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = input("Enter the question :- ")
text2 = 'One of the fastest economy of world is India.'
text3 = 'India is biggest democracy in the world.'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
vector3 = text_to_vector(text3)

cosine1 = get_cosine(vector1, vector2)
cosine2 = get_cosine(vector1, vector3)

print ('The similarity between first and second sentences is ', cosine1)
print ('The similarity between first and third sentences is ', cosine2)
print(text1)
print('-----------------------------------------------------------------')
if (cosine1>cosine2):
  print(text2)
  print(text3)
else :
  print(text3)
  print(text2)
