############################################################################
#   *This tutorial is a basic password controller                          #
#   *Author:Benj4min                                                       #
#                                                                          #
#                                                                          #
#                                                                          #
############################################################################
print("""
      Password Rules:
      At least 1 letter between [a-z] and 1 letter between [A-Z].
      At least 1 number between [0-9].
      At least 1 character from [$#@].
      Minimum length 6 characters.
      Maximum length 16 character
""")
A=0
B=0
C=0
D=0
a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="1234567890"
d="!@#$%^&*()_+"
password=input("please enter a password:")

if(len(password)<6 and len(password)>16):
    print("Please enter between 6-16 lenght password")
else:
	for i in password:
		if i in a:
			A+=1
		if i in b:
			B+=1
		if i in c:
			C+=1
		if i in d:
			D+=1
		else:
			pass
if A==0:
    print('Must have atlease 1 character from (a-z)')
if B==0:
    print('Must have atlease 1 character from (A-Z)')
if C==0:
    print('Must have atlease 1 character from (1-9)')
if D==0:
    print('Must have atlease 1 character from (!@#$%^&*_+)')
			
