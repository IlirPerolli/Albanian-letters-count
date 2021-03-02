letters = {'a':0,'b':0,'c':0,'ç':0,'d':0,'dh':0,'e':0,'ë':0,'f':0,'g':0,'gj':0,'h':0,'i':0,'j':0,'k':0,'l':0,'ll':0,'m':0,
           'n':0,'nj':0,'o':0,'p':0,'q':0,'r':0,'rr':0,'s':0,'sh':0,'t':0,'th':0,'u':0,'v':0,'x':0,'xh':0,'y':0,'z':0,'zh':0}
input = input('Shkruani tekstin: ')
print(" ")
for i in letters:
    if (i in input):
        if (i =='dh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='gj'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='ll'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='nj'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='rr'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='sh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='th'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='xh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        if (i =='zh'):
            letters[i[0]]= letters[i[0]]-input.count(i);
            letters[i[1]]= letters[i[1]]-input.count(i);
        letters[i]= input.count(i)

for i in letters:
    print(str(i) +' -> '+ str(letters[i]))
print("")
sorted_letters = (dict(sorted(letters.items(), key=lambda item: item[1],reverse=True)))
most_common_letter = list(sorted_letters)
print('Shkronja me e shpeshte eshte: ' + most_common_letter[0])