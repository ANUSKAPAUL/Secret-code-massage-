# secret code massege 
#coding:
#if the word contains atleast 3 characters, remove the first letter and append it at the end 
#  now append three random charecters at the starting and the end
#else:
 # simply reverse the string

#decoding:
# if the word contains less than 3 charecters, reverse it
#else:
# remove 3 randome charecters from start and end . Now remove the last letter and append it to the beginning
import random
import string

DL=input("enter the massege : ").strip()
if not DL :
  print("(no input)")
  raise SystemExit
words = DL.split(" ")# split on whitespace
print("choose mode : 1 = prefix/suffix transform , 2 = rotate middile")
mode = input("Mode ( 1 or 2 , default 2 ) :").strip() or "2"
nwords = []
if mode == "1" :
  #r1 / r2 transform
  r1 = ''.join(random.choices(string.ascii_lowercase,k=3))
  r2 =''.join(random.choices(string.ascii_lowercase,k=3))


  
  for word in words:
    if (len(word)>=1):#move first character to end and add r1 , r2
    
     DL1=r1+ word[1:]+word[0]+r2
     nwords.append(DL1)
    else:
     nwords.append(words[::-1]) 
    
else:
  # rotate middle block (safe : check lenght)
     
  for word in words:#need atleast 7 chars so word[:3],middle,word[-3:] are valid 
   if (len(word)>=7):
     DL1=word[3:-3]
     DL1 = DL1[-1]+DL1[:-1]
     new_word = word[:3] + DL1 + word[-3:]
     nwords.append(new_word)#append string 
   else:#for short words just reverse the string 
     nwords.append(word[::-1])#join requires every item in nwords to be a string - we ansured that 

print(" ".join(nwords))

