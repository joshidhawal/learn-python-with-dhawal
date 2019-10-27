input_string="aaabbccccaaa"
input_list=list(input_string)
counter=1
character_list=[]
print("The Input we have is : ",input_list)
character_list.append(input_list[0])
for i in range(1,len(input_list)):
    if(input_list[i-1]==input_list[i]):
        counter=counter+1
        print("Counter inside loop",counter)
    else:
        character_list.append(counter)
        counter=1
        character_list.append(input_list[i])
character_list.append(counter)
print(character_list)