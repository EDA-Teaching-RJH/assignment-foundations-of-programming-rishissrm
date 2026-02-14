# System to track data points per crew member using Parallel Lists

# Create a function init_database() which returns 4 lists which are pre-populated with 5 Star Trek Characters

def init_database():
    Names = ["Picard", "Riker", "Data", "Worf","Hikaru"]
    Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant","Captain"]
    Divisions = ["Command", "Command", "Operations", "Security","Command"]
    IDs =["101" , "102", "103", "104","105"]
    return Names,Ranks,Divisions,IDs

# display menu options
def display_menu():
    user = input("Enter your full name : ")
    print("Hello current student logged in  "+ user)
    print("*******Menu***********")
    print("1.Display Roaster")
    print("2.Add Member")
    print("3.Remove Memeber")
    print("4.Update Rank")
    print("5.Search Crew")
    print("6.Filter By Division")
    print("7.Calculate Payroll")
    print("8.Count Officers")
    print("9.Exit")

    choice = input("Choose an option: ")

display_menu()

