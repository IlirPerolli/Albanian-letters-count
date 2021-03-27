from matplotlib import pyplot as plt
import itertools
from collections import Counter
letters = {'a':0,'b':0,'c':0,'ç':0,'d':0,'dh':0,'e':0,'ë':0,'f':0,'g':0,'gj':0,'h':0,'i':0,'j':0,'k':0,'l':0,'ll':0,'m':0,
           'n':0,'nj':0,'o':0,'p':0,'q':0,'r':0,'rr':0,'s':0,'sh':0,'t':0,'th':0,'u':0,'v':0,'x':0,'xh':0,'y':0,'z':0,'zh':0, '.':0, ',':0, '?':0, '!':0}
zanoret = ['a','e','ë','i','o', 'u', 'y']
bigramet = ['dh','gj','ll','nj','rr', 'sh', 'th', 'xh', 'zh']

def sort_dict(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1],reverse=True))
    sorted_dict = dict(itertools.islice(sorted_dict.items(), 15)) #merr 15 elementet e para
    return sorted_dict

def draw_bar(input_dict, title, ylabel, xlabel):
    plt.bar(input_dict.keys(), input_dict.values(), color='#117892')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

def draw_plot(input_dict, title, ylabel, xlabel):
    plt.plot(input_dict.keys(), input_dict.values(), color='#117892', marker='o')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

file = open("article.txt", "r", encoding='utf8')
input = file.read().lower()
file.close()
file = open('output.txt', 'w+')
file.write('')
file.close()
fjalet_input = input.split()
fjalet = Counter(fjalet_input) #numero fjalet
counter_to_dictionary = dict(fjalet) #kthe ne dictionary
fjalet_me_te_perseritura = sort_dict(counter_to_dictionary)

print ('\nFjala me e shpeshte eshte: ' +str(list(fjalet_me_te_perseritura)[0]) + " -> "+ str(fjalet_me_te_perseritura[list(fjalet_me_te_perseritura)[0]])+ ' here')
file = open('output.txt', 'a+')
file.write('Fjala me e shpeshte eshte: ' +str(list(fjalet_me_te_perseritura)[0]) + " -> "+ str(fjalet_me_te_perseritura[list(fjalet_me_te_perseritura)[0]])+ ' here. \n \n')
file.close()
print(" ")
for i in letters:
    if (i in input):
        for j in bigramet:
            if (i == j):
                letters[i[0]]= letters[i[0]]-input.count(i);
                letters[i[1]]= letters[i[1]]-input.count(i);
                break
        letters[i]= input.count(i)

print ('Shkronjat e perseritura: \n')
file = open('output.txt', 'a+', encoding='utf8')
file.write('Shkronjat e perseritura: \n')
for i in letters:
    print(str(i) +' -> '+ str(letters[i]))
    file.write(str(i) +' -> '+ str(letters[i]) + '\n')
file.close()
print("")
sorted_letters = sort_dict(letters)

most_common_letter = list(sorted_letters)

print('Shkronja me e shpeshte eshte: ' + str(most_common_letter[0]) + " -> "+ str(letters[most_common_letter[0]]) + " here. \n ")
file = open('output.txt', 'a+', encoding='utf8')
file.write('\nShkronja me e shpeshte eshte: ' + str(most_common_letter[0]) + " -> "+ str(letters[most_common_letter[0]]) + " here. \n")
file.close()

file = open('output.txt', 'a+', encoding='utf8')
print ('Perseritja e zanoreve:')
file.write('\nPerseritja e zanoreve: \n')

for i in zanoret:
    print (str(i) + ' -> ' + str(letters[i]))
    file.write(str(i) + ' -> ' + str(letters[i]) + "\n")
    file.write('')
print ('')
file.close()

file = open('output.txt', 'a+', encoding='utf8')
print ('Perseritja e bigrameve:')
file.write('\nPerseritja e bigrameve: \n')

for i in bigramet:
    print (str(i) + ' -> ' + str(letters[i]))
    file.write(str(i) + ' -> ' + str(letters[i]) + "\n")
    file.write('')
print ('')
file.close()

plot1 = plt.figure(1)
draw_bar(sorted_letters,"Shkronjat më të shpeshta",  "Numri i përseritjeve","Shkronjat")

zanoret_e_perseritura = {i:j for i , j in zip(zanoret, [letters[i] for i in zanoret])}
zanoret_e_sortuara = sort_dict(zanoret_e_perseritura)

bigramet_e_perseritura = {i:j for i , j in zip(bigramet, [letters[i] for i in bigramet])}
bigramet_e_sortuara = sort_dict(bigramet_e_perseritura)

plot2 = plt.figure(2)
draw_bar(fjalet_me_te_perseritura,"Fjalet më të shpeshta",  "Numri i përseritjeve","Fjalet")

# print (zanoret_e_sortuara)
plot3 = plt.figure(3)
draw_plot(zanoret_e_sortuara,"Zanoret më të shpeshta",  "Numri i përseritjeve","Shkronjat")

plot4 = plt.figure(4)
draw_plot(bigramet_e_sortuara,"Bigramet më të shpeshta",  "Numri i përseritjeve","Shkronjat")

plt.show()