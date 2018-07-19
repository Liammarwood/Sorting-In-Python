from Stacks import Stack
#data = 2
#s=Stack(the_list)
#s.push(data)
#s.pop()
word = input("Enter a word to be reversed:   ")
the_list=[]
for i in reversed(word):
    the_list.append(i)
nword =''.join(the_list)
print (nword)

    
