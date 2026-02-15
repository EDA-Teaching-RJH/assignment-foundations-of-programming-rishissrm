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

    choice = input("Choose an option:")
    return choice

# Function to display the data of all the crew members
def display_roaster(names,ranks,divs,ids):
    print ("current crew memebers")
    if len(names)==0:
        print("no crew members in data base")
        return
    for i in range(len(names)):
        print(ids[i],names[i],ranks[i],divs[i])

def add_member(names,ranks,divs,ids):
    print("*****Add Member********")
    new_id =input("Enter ID: ")

    #check unique ID
    if new_id in ids:
        print("That ID already exists.Please input other ID : ")
        return

    new_name = input("Enter name: ")
    new_rank = input("Enter rank (Captain, Commander, Lt. Commander, Lieutenant):")
    new_div = input("Enter Division (Command, Operations, Security)")

    #add to all lists
    ids.append(new_id)
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)

    print("Member successfully added!!!")

#Function to remove a member from the list
def remove_member(names,ranks,divs,ids):
    print("******Remove Member*********")

    rem_id=input("Enter ID to remove: ")
    if rem_id not in ids:
        print("ID not found, Nothing removed")
        return

    idx=ids.index(rem_id)

    #remove from all the lists
    print("Removing: ", names[idx])
    ids.pop(idx)
    names.pop(idx)
    ranks.pop(idx)
    divs.pop(idx)

    print("Successfully Removed.")


def main():
    Names,Ranks,Divisions,IDs=init_database()

    while True:
        choice=display_menu()

        if choice == "1":
            display_roaster(Names,Ranks,Divisions,IDs)

        elif choice == "2":
            add_member(Names,Ranks,Divisions,IDs)

        elif choice == "3":
            remove_member(Names,Ranks,Divisions,IDs)

        else:
            print("invaild options")

main()