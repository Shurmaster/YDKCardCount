import glob, os
import sqlite3

main = {}
extra = {}
side = {}
outfile = "CardsUsed.txt"


def addCards(strMe):
    # Using readlines()
    file1 = open(strMe, 'r')
    Lines = file1.readlines()
    for line in Lines:
        if '#' not in line:
            if '!' not in line:
                if line.strip() not in main:
                    main[line.strip()] = 1
                else:
                    main[line.strip()] += 1

    #file1.close()

def allCards():
    fileA = open(outfile, 'w')
    fileA.write("")
    fileA.close()

    olddirpath = os.getcwd()
    dirpath = os.getcwd() + "/deck"
    os.chdir(dirpath)
    #print("Currently in {}; \nProgram is in {}".format(dirpath, olddirpath))
    #for file in glob.glob("*.txt"):
    for file in glob.glob("*.ydk"):
        addCards(file)
    os.chdir(olddirpath)

def printCards():
    #if 3 not in lst else lst
    try:
        conn = sqlite3.connect('cards.cdb')
        c = conn.cursor()
        if len(main) != 0:
            sort_orders = sorted(main.items(), key=lambda main: main[1], reverse=True)
            fileA = open(outfile, 'a+')
            count = 0   #
            for i in sort_orders:
                c.execute("SELECT name FROM texts WHERE id==:IDe", {'IDe': i[0],})
                cardname = c.fetchone()[0].ljust(50, ' ')
                print("{} {}".format(cardname, i[1]))
                fileA.write("{} {}\n".format(cardname, i[1]))
        else:
            print("Error: No cards inserted...")
    except:
        conn.rollback()
        fileA.close()
        print("Error")
    finally:
        fileA.close()
        conn.close()

def menu():
    print("=============================================")
    print("1 - View and export List to to \'CardsUsed.txt\'")
    print("2 - Import cards from single deck in Directory")
    print("3 - Import cards from every deck in Directory")
    print("9 - exit")
    print("=============================================")


if __name__ == '__main__':
    n = 0
    menu()
    while n != '9':
        n = input("Enter Selection: ")
        if n == '1':
            printCards()
        if n == '2':
            m = input("Name of file: ")
            print("checking {} out.".format(m))
            addCards(m)
        if n == '3':
            allCards()
        if n == '9':
            print("Good Bye")
        menu()
#for items in main:
#    print( "{}: {}".format(count, items))
#    count += 1
