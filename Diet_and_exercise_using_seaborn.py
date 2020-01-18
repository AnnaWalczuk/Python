import seaborn as sns



exercise = sns.load_dataset("exercise")





def group_by_diet():
    print(exercise.groupby(["diet"]).mean())


def group_by_activity():
    print(exercise.groupby(["kind"]).mean())

def sample_results():
    print(exercise.sample(10)) # 10 losowych rekordów

def ffilter():
    fil1 = input("D - diet; A - activity\n")
    if fil1 == "D":
        low_fat = exercise[exercise['diet'] == "low fat"]
        no_fat = exercise[exercise['diet'] == "no fat"]
        fil2 = input("N - no fat; L - low fat ")
        if fil2 == "N":
            print(no_fat)
        elif fil2 == "L":
            print(low_fat)
    elif fil1 == "A":
        rodz_aktywnosci1 = exercise[exercise['kind'] == "running"]
        rodz_aktywnosci2 = exercise[exercise['kind'] == "walking"]
        rodz_aktywnosci3 = exercise[exercise['kind'] == "rest"]
        fil3 = input("1 - running; 2 - walking; 3 - rest\n")
        if fil3 == "1":
            print(rodz_aktywnosci1)
        elif fil3 == "2":
            print(rodz_aktywnosci2)
        elif fil3 == "3":
            print(rodz_aktywnosci3)
    else:
        print("Wrong input")

    
 



def first_results():
    how_much = input("How many results? ")
    if how_much.isdigit() == False:
        print("Wrong input")
    else:
        print(exercise.head(int(how_much)))


def ssort():
    sort1 = input("P - pulse; T- time\n")
    if sort1 == "P":
        sort2 = input("A - ascending; D - descending\n")
        if sort2 == "A":
            print(exercise.sort_values("pulse"))
        elif sort2 == "D":
            print(exercise.sort_values("pulse", ascending=False))
    elif sort1 == "T":
        sort3 = input("A - ascending; D - descending\n")
        if sort3 == "A":
            print(exercise.sort_values("time"))
        elif sort3 == "D":
            print(exercise.sort_values("time", ascending=False))
    else:
        print("Wrong input")



def analyse():

    while (True):

        dec = input("***MENU - Diet and exercises***\n"
                    " 1 - filter\n 2 - sort\n 3 - first results\n 4 - 10 sample records\n "
                    "5 - group_by_diet\n 6 - group_by_activity\n E - exit \n ")

        if (dec == "1"):
            ffilter()
        elif (dec == "E"):
            exit()
        elif (dec == "2"):
            ssort()
        elif (dec == "3"):
            first_results()
        elif (dec == "4"):
            sample_results()
        elif (dec == "5"):
            group_by_diet()
        elif (dec == "6"):
            group_by_activity()
        else:
            print("Wrong input")


analyse()


