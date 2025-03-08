

Scores = []
names = []

def sorting(): # This is basic bubble sorting
    for a in range(len(Scores)):
        for b in range(1,len(Scores)):
            if Scores[b-1] < Scores[b]:
                temp = Scores[b-1]
                Scores[b-1] = Scores[b]
                Scores[b] = temp
                temp2 = names[b-1]
                names[b-1] = names[b]
                names[b] = temp2
                
def FileToList(filename): #this function will take out the things form the file and put it in the Array
    with open(filename,'r') as file:
        for num,line in enumerate(file):
            file_to_list = list(line)
            name = ''
            score = ''
            for i,stri in enumerate(file_to_list):
                if stri == ":":
                    number = i
                    for x in range(0,number):#this one is separating name
                        name = name + file_to_list[x]
                    for y in range(number+1,len(file_to_list)):#this one is saperating scores
                        score = score + file_to_list[y]
            Scores.append(int(score))
            names.append(name)
        for a in range(len(Scores)):#this is another basics bubble sort
            for b in range(1,len(Scores)):
                if Scores[b-1] < Scores[b]:
                    temp = Scores[b-1]
                    Scores[b-1] = Scores[b]
                    Scores[b] = temp
                    temp2 = names[b-1]
                    names[b-1] = names[b]
                    names[b] = temp2
    return newAddition()
        
def newAddition():# as the name suggests this will add new names and scores in the file 
    This = True
    while This:
        new_name = input("Enter the name of the player.\n:")        
        new_score = input("Enter the score of the player.\n:")
        if new_name == "" :
            This = False
        else:
            names.append(new_name)
            Scores.append(int(new_score))
    return sorting()

def ListToFile(filename):# this will put from Array to file
    with open(filename, 'w') as file:
        for i in range(len(Scores)):
            convert = str(Scores[i])
            joints = names[i]+":"+convert
            file.write(joints+'\n')

def initiallization(): #this is the main function from which other functions are initiallized
    files = input('enter the file you wanna check.\n:')
    FileToList(files)
    ListToFile(files)
    return print(names, Scores)


initiallization()