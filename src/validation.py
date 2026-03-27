def getOption (options):
    while True:
        for i, option in enumerate(options,start=1):
            print(f"{i} - {option}")
        try :
            seletedOption = int(input("please, select an option: "))
            return seletedOption
        except ValueError:
            print ("Select a valid option")


