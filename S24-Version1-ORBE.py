Name = (input("Enter your name: "))
LName = (input("Enter your Lastname: "))
Section = (input("Enter your section: "))
FavSub = (input("Enter your Favorite subject: "))

FName = Name+"  "+LName
print("Name:", FName.title())
CName = FName.upper()
print("Name Code:", CName)
print("Section:", Section.upper())
print("Favorite Subject:", FavSub.title())
Character_Count = print("Character Count:", len(FName))