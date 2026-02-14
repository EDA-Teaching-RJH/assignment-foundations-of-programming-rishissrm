# System to track data points per crew member using Parallel Lists

# Create a function init_database() which returns 4 lists which are pre-populated with 5 Star Trek Characters

def init_database():
    Names = ["Picard", "Riker", "Data", "Worf","Hikaru"]
    Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant","Captain"]
    Divisions = ["Command", "Command", "Operations", "Security","Command"]
    IDs =["101" , "102", "103", "104","105"]
    return Names,Ranks,Divisions,IDs

