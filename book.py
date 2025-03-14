
class Book():
    '''
    This class is use to create a book object and the method used are check_out and returned
    '''
    def __init__(self, Book_name:str, Author:str, ISBA:int) -> None:
        self.Book_name = Book_name
        self.Author = Author
        self.ISBA = ISBA
        self.is_checked_out:bool = False
        self.borrowID:int 
        
    
   
    def check_out(self) -> None:
        '''
        this method does 3 things checks if the person is taking the book, checks for last item in the file
        and take out the booking id and new item with new booking id
        '''
        if self.is_checked_out:
            print("this book is checked out")
        else:
            print('This book is avilable')
            new = input("do you want to check out the book(y/n)?\n:")
            if new == 'y':
                print("alright its ready to go")
                self.is_checked_out = True
                Person_name = input('Enter the name of person borrowing the book.\n:')
                now = 0
                with open('book.txt', 'r') as file:
                    lines = file.readlines()
                    a = 0
                    borrowid = ''
                    for line in reversed(lines):
                        if line == '\n':
                            continue
                        else:
                            now = lines.index(line)
                            break
                    for i in lines[now]:
                        if i == ':':
                            if a == 0:
                                print(a)
                                a = lines[now].index(i)
                                break
                    for i in range(a+2, a+5):
                        borrowid = borrowid + lines[now][i]
                    self.ISBA = int(borrowid) + 1
                new_line = (f'{self.Book_name} : {self.ISBA} : {Person_name}\n')
                if 0<=now-1<len(lines):
                    lines[now+1] = new_line
                with open('book.txt', 'w') as file:
                    file.writelines(lines)
                print(f'This is your borrowed id: {self.ISBA}')
                print('alright you can take it now')
            else:
                print('let me know you need it in the future')
                
                
    def returned(self):
        '''
        thie method is used to compare the booking of all the previous books that are checked out and if they are 
        and if they are checked out it will remove the booking id of the book
        '''
        ## Initialization area
        a = 0
        index = 0
        ## Initialization Area
        ## Input area
        try: BorrowedId = int(input('Enter the borrowed id of the book.\n:'))
        except ValueError:
            print('this is not a valie input')
        ## Input area
        with open('book.txt', 'r') as file:
            lines = file.readlines()
            for this_line in lines:
                ## Initialization area
                borrowid = ''
                ## Initialization area
                if this_line == '\n':
                    continue
                else:
                    line = this_line.strip('\n')
                    for i in line:
                        if i == ':':
                            a = line.index(i)
                            break
                    for i in range(a+2, a+5):
                        borrowid = borrowid + line[i]
                    if int(borrowid) == BorrowedId:
                        index = lines.index(this_line)
                    if 0<=index<len(lines):
                        lines[index] = ''
                    with open('book.txt', 'w') as file:
                        file.writelines(lines)
                        
                        
                        
                
                    
        

book = Book(Book_name='Law of human nature', Author='Dr. Robert Greene', ISBA=100)
book.returned()