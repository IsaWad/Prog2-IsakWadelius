from datetime import date
today = date.today()

class student:
    def __init__(self, skola, namn, personnumber):
        self.skola = skola
        self.__namn = namn
        self.__personnumber = personnumber
    
    def getname(self):
        return self.__namn
    
    def getage(self):
        dagensdatum = str(today)
        dagensdatum = dagensdatum[2:]
        dagensdatum = dagensdatum.split("-")
        år = self.__personnumber[0:2]                            # str(self.__personnumber[0]) + str(self.__personnumber[1])
        månad = self.__personnumber[2:4]                        #str(self.__personnumber[2]) + str(self.__personnumber[3])
        dag = self.__personnumber[4:6]                           #str(self.__personnumber[4]) + str(self.__personnumber[5])
    
        if int(månad) < int(dagensdatum[1]):
            return (int(dagensdatum[0]) - int(år))
        
        elif int(månad) == int(dagensdatum[1]):
            if int(dag) <= int(dagensdatum[2]):
                return (int(dagensdatum[0]) - int(år))
            else:
                return (int(dagensdatum[0])- int(år) - 1)
        else:
            return (int(dagensdatum[0])- int(år) - 1)


student1 = student("Åva", "Hans", "050922")

print(student1.getname())
print(student1.getage())