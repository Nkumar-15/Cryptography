print("**********WELCOME TO ROT13**********")
alphabet="abcdefghijklmnopqrstuvwxyz"
#al=list(alphabet)
out=''

shift=13
print("Shift=",shift)
empty=[]
print("*Select your function: ")
print("\t1.ROT13_Encode\n\t2.ROT13_Decode")
m=int(input("Enter your option="))

char=input("Enter the character=")
print("The entered character =",char)
char=char.lower()

if m==1 :
    for i in char:
        #print(i)
        if i  not in alphabet:
            print("Hey man you should enter the character yaar :(")
            break
        
        else:
            n=alphabet.find(i)
            n_shift=n+shift
            if n_shift>=25 :
                n_shift=n_shift-26
            #print(n_shift)
            outchar=alphabet[n_shift]
            empty.append(outchar)
            out="".join([str(j) for j in empty])
            print(out)
            
elif m==2:
    for i in char:
    #print(i)
        if i  not in alphabet:
            print("\nHey man u should enter the character ya :(")
            break
        else:
            n=alphabet.find(i)
            n_shift=n-shift
            if n_shift>=25 :
                n_shift=n_shift-26
            #print(n_shift)
            outchar=alphabet[n_shift]
            empty.append(outchar)
            out="".join([str(j) for j in empty])
            print(out)
        
        
        
else:
    print("Your options are invalid :)")
   
    

   
 
