print("**********WELCOME TO ROT13**********")
alphabet="abcdefghijklmnopqrstuvwxyz"
#al=list(alphabet)
out=''

shift=13
print("Shift=",shift)
empty=[]
char=input("enter the character=")
print("The entered character =",char)
char=char.lower()
for i in char:
    #print(i)
    if i  not in alphabet:
        print("hey man u should enter the character ya")
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
