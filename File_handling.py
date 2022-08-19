import os

def main():
    directory = r"J:\ESDS\Training\SEM 2\staff notes\Python\Practicals_Python_ML\GroupA\ "
    filename = input("\n enter file name: ")
    filepath = directory + filename
    print("filepath:", filepath)

    choice = 0
    print("\n Welcome to File Handling \n")

    while choice >= 0:
        print("1. create file")
        print("2. write file")
        print("3. append file")
        print("4. read file")
        print("5. delete file")
        print("6. exit")

        choice = int(input("Enter your choice:  "))

        if choice == 1:
            f = open(filepath, "w")
            #f.write("\n ")
            print("\n" + filename + " file Created"+"\n")
            f.close()

        if choice == 2:
            message = input("\n write data into file: ")
            f = open(filepath, "w")
            f.write("\n" + message + "\n")
            f.close()

        if choice == 3:
            message = input("\n Append data into file: ")
            f = open(filepath, "a")
            f.write("\n" + message + "\n")
            f.close()

        if choice == 4:
            f = open(filepath, "r")
            for x in f:
                print(x)
            f.close()

        if choice == 5:
            os.remove(filepath)
            print("You have deleted the file")

        if choice == 6:
            print("Thank yor for using file handling app")
            break


if __name__ == '__main__':
    main()