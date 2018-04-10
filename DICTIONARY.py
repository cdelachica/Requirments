print (
"\n\t\t PBA TEAMS\n\t\t\tQUICK FACTS \n\n 1. ALASKA \t\t\t\t\t 2. GINEBRA \n 3. RAIN OR SHINE \t\t\t 4. MAGNOLIA HOTSHOTS \n 5. TALK&TEXT\n")


def chica():
    dc = {
        "1": " Name: CALVIN ABUEVA \n NONOY BACLAO \n CHRIS BANCHERO \n JVEE CASIO \n JERON TENG \n SONNY THOSS \n SIMON ENCISCO ",
        "2": " Name: JAPETH AGUILAR \n MARK CAGUIOA \n JOE DEVANCE \n GREGORY SLAUGHTER \n LA TENERIO \n JOHN MARION WILSON \n SCOTTIE THOMPSON ",
        "3": " Name: NORBERT TORRES \n RAYMOND ALMAZAN \n BEAU BELGA \n GABE NORWOOD \n CHRIS TIU \n ANTHONY WASHINGTON \n SIDNEY ONWUBERE ",
        "4": " Name: IAN SANGALANG \n ANDY MARK BARROCA \n PAUL LEE \n MARC JEAN PINGRIS \n RAFI REAVIS \n PETER JUNE SIMON \n ALDRECH RAMOS ",
        "5": " Name: WILLIAM CASTRO \n JERICHO CRUZ \n FRANK GOLLA \n ALEX NUYLES \n TERRENCE ROMEO \n KELLY WILLIAMS \n DON TROLLANO ",
    }

    christian = input("\n NO.  ")
    if christian == "1":
        print (dc["1"])
    elif christian == "2":
        print (dc["2"])
    elif christian == "3":
        print (dc["3"])
    elif christian == "4":
        print (dc["4"])
    elif christian == "5":
        print (dc["5"])
    else:
        print ("No name matched with the no. you've entered!!!")
        return chica()
    return chica()


chica()
