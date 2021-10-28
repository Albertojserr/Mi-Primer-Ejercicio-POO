from Guerrero import Guerrero
from Marciano import Marciano
from Terricola import Terricola

class Nave():

    def __init__(self, warrior_type, name="Millenium Falcon", crew=1):
        if(not isinstance(crew,int)):
            raise TypeError("crew is the number of warriors and should be an int")
        elif(crew < 0):
            raise ValueError("crew is the number of warriors and should be an int > 0")
        elif(warrior_type == Marciano):
            self.__type = warrior_type
            self.__name = name
            self.__crew = list()
            for i in range (0,crew):
                marciano_name="marciano" + str(i)
                self.__crew.append(Marciano(marciano_name))
        elif(warrior_type == Terricola):
            self.__type = warrior_type
            self.__name = name
            self.__crew = list()
            for i in range (0,crew):
                terricola_name="terricola" + str(i)
                self.__crew.append(Terricola(terricola_name))
        else:
            raise TypeError("TYPE of GUERREROS WRONG")

        print("Created a ship " + self.__name + " of " + str(self.__type) + " with " + str(crew) + " members")

    def __str__(self):
        return self.__name + " OF " + str(len(self.__crew)) + " " + str(self.__type)

    def get_shot(self,shot):
        if(not isinstance(shot,int)):
            raise TypeError("shot should be an int")
        elif(shot == -1):
            # A shot from a dead member
            pass
        elif(shot < 0 or shot > Guerrero.get_maxTarget()):
            raise ValueError("shot OUT OF RANGE")
        for i in range(0,len(self.__crew)):
            if(self.__type == Marciano or self.__type == Terricola):
                self.__crew[i].get_shot(shot)
            else:
                raise TypeError("TYPE of GUERREROS WRONG in the crew " + self.__crew)

    def shoot(self,warrior):

        if(warrior >= 0 and warrior < len(self.__crew)):
            return self.__crew[warrior].shoot()
        else:
            raise ValueError("The warrior: " + str(warrior) +  " does not exist in the ship: " + self.__name)

    def membersAlive(self):

        membersAlive=0
        # I AM LAUNCHING AN IMPOSSIBLE EXCEPTION, SINCE IT CANT BE ANY NAVEWITH OTHER TYPE THAN MARCIANO OR TERRICOLA
        # Read Constructor to double check it. That is why the exception is not documented
        if(self.__type == Marciano or self.__type ==Terricola):
            for warrior in self.__crew:
                #We access the member of the grandparent class (SerVivo), that is shared by all warriors (Marciano and Terricola)! 
                if(warrior.is_vivo()):
                    membersAlive+=1
        else:
            raise TypeError("TYPE of GUERREROS WRONG ")

        return membersAlive

    def isWarriorAlive(self, warrior):
        if(warrior >= 0 and warrior < len(self.__crew)):
            return self.__crew[warrior].is_vivo()
        else:
            raise ValueError("The warrior: " + str(warrior) +  " does not exist in the ship: " + self.__name)

    def number_of_members(self):
        return len(self.__crew)