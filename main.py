#reference to master doc
def addSheetToMaster():
    scoresheet_link = input("Input link to scoresheet to add to DB")

    return

def undoEdit():
    
    return

def main():
    config = open("config.txt", "r")
    master_sheet = config.readline()
    organization = config.readline()
    if (master_sheet == "" or organization == ""):
        print("Please edit config to add necessary data:\n" +
                "<Line1> Organization name </Line1>\n" +
                "<Line2> Link to master sheet</Line2>")
        mode = input("Please select mode:\n"+
                "1. add new sheet to master\n" +
                "2. undo last modification\n" +
                "3. edit config\n" +
                "4. close application")

        
        if (mode == 1):
            addSheetToMaster()
        elif (mode == 2):
            undoEdit()
