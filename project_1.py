#BOOK INFORMATON
def book_1():
    print("Title: Deep End")
    print("Author: Ali Hazelwood")
    print("Launch date: 4 february,2025")
    print("Description:Two collegiate swimmers—a burntout Olympic hopeful and an analytics obsessed sports scientist—clash in early morning practices before slow burn attraction turns heat up. Sharp internal monologue, foundfamily vibes, and swimming tension")
    print("Price in INR: 429")

def book_2():
    print("Title: What happes in Amsterdam")
    print("Author: Rachel Lynn Soloman")
    print("Launch date: 6 May,2025")
    print("Description:An American podcast host fakes a date with a Dutch sound engineer across Amsterdam’s canals, weaving in local flavor, witty banter, and questions about belonging in a global world")
    print("Price in INR: 1325")

def book_3():
    print("Title: Once upon a time in Dollywood")
    print("Author: Ashley Jordan")
    print("Launch date: 5 August,2025")
    print("Description:A blocked NYC playwright moves to Tennessee and becomes entangled with her single dad neighbor. Set against Dollywood’s musical backdrop, the story blends charm, family dynamics, and cozy emotional stakes")
    print("Price in INR: 1668")

def book_4():
    print("Title: I have some questions for you")
    print("Author: Rebecca Makkai")
    print("Launch date: 21 February,2023")
    print("Description:A film professor returns to her elite boarding school to teach a class, confronting a cold case murder from her past. A gripping, layered investigation into memory, bias, and justice.")
    print("Price in INR:1715")

def book_5():
    print("Title: The Hobbit")
    print("Author: J.R.R Tolkien")
    print("Launch date: 21 September,1937")
    print("Description: A reluctant hobbit named Bilbo Baggins is swept into a perilous quest involving dwarves, dragons, and hidden treasure, discovering courage and adventure in Middle-earth’s richly imagined world.")
    print("Price in INR: 1300")


#TO DISPLAY
def menu():
    print("Press 1 for 101 book information")
    print("Press 2 for 102 book information")
    print("Press 3 for 103 book information")
    print("Press 4 for 104 book information")
    print("Press 5 for 105 book information")
  
#MAIN THING 
def main_menu():# to call the func again and again
    menu()

    option=int(input("Enter any option from 1-5:"))
    if option==1:
        book_1()
    elif option==2:
        book_2()
    elif option==3:
        book_3()
    elif option==4:
        book_4()
    elif option == 5:
        book_5()
    else:
        print("Invalid option, Please choose from 1-5")


    again=input('Do you want to continue?, Enter "yes" to continue or "no" to exit')
    if again=="yes":
        main_menu()
    else:
        print("Thankyou for visiting Skillcircle Library System")
# #start again
main_menu()
