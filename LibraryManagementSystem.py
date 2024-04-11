from datetime import date
global actnDate
actnDate =  str(date.today())



class Library:
    def __init__(self,booksAvailable, booksBorrowed):
        self.booksAvailable = booksAvailable
        self.booksBorrowed = booksBorrowed


    def showBooks_available(self):
        print("\n".join(self.booksAvailable))

    def showBooks_borrowed(self):
        print("\n".join(self.booksBorrowed))

    def update(self,updated_booksAvailable,updated_booksBorrwed):
        with open("available.txt","w") as f:
            f.write("\n".join(updated_booksAvailable))
    
        with open("borrowed.txt","w") as f:
            f.write("\n".join(updated_booksBorrwed))


    # def allRecords(self,studentName):
    #     with open(f"{studentName}records.txt","r") as f2:
    #                     for entry in f2.readlines():
    #                         data = self.name + " " + entry.strip() + " " + "\n"  #removes new line characters
    #                         with open("allRecords.txt","a") as f1:  
    #                             f1.write(data)       
    
class Student(Library):
    
    def __init__(self,name, unversityRollno,library_instance):
        self.name = name
        self.universityRollno = unversityRollno
        self.libInstance = library_instance

    def borrow(self):
            #  Library.showBooks_available(self.libInstance)
            self.libInstance.showBooks_available()
            reqBook = input(" Enter name :")
            try:
                if reqBook in self.libInstance.booksAvailable:
                    self.libInstance.booksAvailable.remove(reqBook)
                    self.libInstance.booksBorrowed.append(reqBook) 
                    self.libInstance.update(booksAvailable,booksBorrowed)   

                    #student Records
                    self.records(self.name,reqBook,None)
                else:
                    print("Requested books not avilable in Library...Kindly check again!")
            
            except Exception as e:
                print(f"something went wrong...{e}")
            
            finally:
                print("thank you for visiting")

    def returning(self):
            retBook = input(" Enter name :")
            try:
                if retBook in self.libInstance.booksBorrowed:
                    self.libInstance.booksBorrowed.remove(retBook)     
                else:
                    print("Book being returned here was not borrowed...Thank you for your donation..!")
                
                self.libInstance.booksAvailable.append(retBook)
                self.libInstance.update(booksAvailable,booksBorrowed)
                #student Records
                self.records(self.name,None,retBook)
            except Exception as e:
                print(f"something went wrong...{e}")
            
            finally:
                print("thank you for visiting")

    def records(self,studentName,reqBook = None,retBook = None):
        with open(f"{studentName}records.txt","a") as f:
            if reqBook:
                statement ="borrowed"+ " " + reqBook + " " +actnDate + "\n"
                f.write(statement)
            if retBook:
                statement ="returned"+ " " + retBook +" " + actnDate + "\n"
                f.write(statement )
            with open("allRecords.txt","a") as f1:
                entry = studentName + " " + statement
                f1.write(entry)
            
                 
                 

if __name__ == "__main__":
    print("**************************************************************************************************************",end ="\n\n")
    print("+++++++++++++++++++++++++++++++++++++++++    Welcome to Digital Library    +++++++++++++++++++++++++++++++++++",end ="\n\n")
    print("**************************************************************************************************************",end ="\n\n")
    
    name = input("Enter your full name -")
    university_rollNo = int(input("Enter your University Roll number -"))

    with open("available.txt","r") as f:
            booksAvailable = [line.strip() for line in f.readlines()]

    with open("borrowed.txt","r") as f:
            booksBorrowed = [line.strip() for line in f.readlines()]
    
    lib = Library(booksAvailable,booksBorrowed)
    stud = Student(name,university_rollNo,lib)

    while True:
        menu ="""
                1.Display Available books
                2.Display Borrowed books
                3.Borrow Book
                4.Return BooK
                5.My Records
                6.All Records
                7.Exit
                """        
        print(menu)
        choice = int(input("Enter your choice:"))
        
        match choice:
            case 1:
                    lib.showBooks_available()
            case 2:
                    lib.showBooks_borrowed()
            case 3:
                    stud.borrow()
            case 4:
                    stud.returning() 
            case 5:
                    with open(f"{name}records.txt","r") as f:
                        print(f.read())
            case 6:
                    with open("allRecords.txt","r") as f:
                        print(f.read())
            case 7:
                    break
            case default:
                    print("something went wrong here...Try Again!")
    print("See You Again...Keep Visiting...")          




