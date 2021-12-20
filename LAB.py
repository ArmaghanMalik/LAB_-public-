print("edited by user 3
      ")
      print("HELLO")
      
      
string = "abcdeee"
decrypt=""
alphabet_dictionary = {'a':1,'b':2,'c':3,'d':4, 'e':5}  #, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}
    
digit_dictionary = {1:'a', 2:'b', 3:'c',  4:'d' , 5:'e'}
shift=3
for i in string:
    print(alphabet_dictionary[i])
    #print(digit_dictionary[alphabet_dictionary[i]])
    #print(type(int(digit_dictionary[alphabet_dictionary[i]])))
    if alphabet_dictionary[i]+shift >=5:
        decrypt += digit_dictionary[(alphabet_dictionary[i] + shift) % 5  +1]
    else:
        decrypt += digit_dictionary[(alphabet_dictionary[i] + shift) % 5]

print(decrypt)


