#______________________________________________________________________________________________________________________________________________________
#[QUES1]

print('ANS 1')

A='Python is a case sensitive language'                                     #inp_str= input string

#(a)
print('\n(a)length of input string is:\n', len(A))                            #printing the length of the given input string
#......................................................................................................................................................

#(b)
print('\n(b)string in reverse order is:\n', A[::-1])                        #reversing the order of input string in one line code
#......................................................................................................................................................

#(c)
s1=A[10:26]                                                #storing 'a case sensitive' in a new string named new_str using slice function
print('\n(c)s1=\n', s1)                                               
#......................................................................................................................................................

#(d)
s2=A[0:10]+'object oriented'+A[27:]                    #replacing 'a case sensitive' with 'object oriented'
print('\n(d)new string after replacing:\n', s2)


#.......................................................................................................................................................

#(e)
index=A.find("a")                                                  #finding index of substring "a" in the given input string
print('\n(e)The index of substring "a" is:\n', index)
#........................................................................................................................................................

#(f)
s3=A.replace(' ', '')                                        #removing all white spaces from the given input string
print('\n(f)input string with white spaces removed:\n', s3)


#_______________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________


#QUES2

print('ANS 2')

Name=input('Please enter your name:\n')
SID=int(input('\nPlease enter your SID:\n'))
Dep_name=input('\nPlease enter your Department name:\n')
CGPA=float(input('\nPlease enter your CGPA:\n'))

print('Hey, {s} Here!'.format(s=Name))
print('My SID is {d}'.format(d=SID))
print('I am from {s} department and my CGPA is {f}'.format(s=Dep_name,f=CGPA))

#_______________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________________________________________________________________________________

#QUES3

print('ANS 3')

a=56
b=10

#(a)
print('\n(a)  a&b =', a&b)

#.......................................................................................................................................................

#(b)
print('\n(b) a|b =', a|b)

#.......................................................................................................................................................

#(c)
print('\n(c) a^b =', a^b)

#........................................................................................................................................................

#(d)
print('\n(d)')
print('After left shift by 2-bits, a =', a<<2)
print('After left shift by 2-bits, b =', b<<2)

#........................................................................................................................................................

#(e)
print('\n(e)')
print('After right shift by 2-bits, a=', a>>2)
print('After right shift by 4-bits, b=',b>>4)

#_________________________________________________________________________________________________________________________________________________________
#_________________________________________________________________________________________________________________________________________________________

#QUES4

print ('Ans 4')
                                              # Function that returns true if the word is found
def isWordPresent(sentence, word):
     
                                           # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
 
                                         # Comparing the current word
                                 # with the word to be searched
        if (i == word):
            return True
    return False

B = input('Enter the sentence/string -\n')
word ='name'
if word in B:
    print('\nYes')
else:
    print('\nNo')


#___________________________________________________________________________________________________________________________________________________________
#___________________________________________________________________________________________________________________________________________________________

#QUES5

    
print('Ans 5')


L1 = int(input('\nEnter the 1st length:\n'))
L2 = int(input('\nEnter the 2nd length:\n'))
L3 = int(input('\nEnter the 3rd length:\n'))

if L1>(L2+L3) or L2>(L1+L2) or L3>(L1+L2):
    print('\n No,entered three lengths can not form a triangle')
else:
    print('\n Yes,entered three lengths can form a triangle')



#_____________________________________________________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________________________________________

#QUES6

print('Ans6')


def countFlips(a, b):
     
                                                #initially flips is equal to 0
    flips = 0
     


                                              
    while(a > 0 or b > 0):                        # & each bits of a && b with 1
      t1 = (a & 1)                                 # and store them if t1 and t2
      t2 = (b & 1)                                     
    
      if(t1 != t2):                             # if t1 != t2 then we will flip that bit          
            flips += 1
             
      a>>=1                                 # right shifting a and b
      b>>=1
     
    return flips



a = int(input('enter value of a:\n'))

b = int(input('enter value of b:\n'))

print(countFlips(a, b))
 

    









