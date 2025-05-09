c = 0
frequent_word = ""
frequency = 0 
word = []
# Ask the user for a file name
with open(r'data.txt','r') as file:

    data = file.read()
    
    word = data.split()
    #Count and display the number of words in the file
    c += len(word)
    count=len(word)
print(c)
#Also, identify the most frequent word and how many times it appears.
filename="data.txt"
def most_frequent_word(filename):
       
        for line in file:
         line_word = line.lower().replace(',','').replace('.','').split(" ");  

        for w in line_word:  
         word.append(w);  
         
for i in range(0, len(word)):  
     
    count = 1;  
     
    for j in range(i+1, len(word)):  
        if(word[i] == word[j]):  
            count = count + 1;  
 
    
    if(count > frequency):  
        frequency = count;  
        frequent_word = word[i];  
 
print("Most frequent word: " + frequent_word)
print("Frequency: " + str(frequency))
most_frequent_word('data.txt')
file.close()
