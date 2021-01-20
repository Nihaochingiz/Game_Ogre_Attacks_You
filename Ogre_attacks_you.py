class Hero():
    def __init__(self,weapon,health):
        self.weapon=weapon
        self.health=health

    def hero_is_on_the_way(self):
        print("Вы идете в деревню за золотом, проходите через зимний лес")
        print("Откуда ни возьмись из кустов появляется страшный Огр")

class Ogre():

    def __init__(self,weapon,health):
        self.weapon=weapon
        self.health=health

    def Go_Ogre(self):
        print("Огр достает лук")


    def Ogre_Attacks_You(self,damage):
        print("Огр начинает по вам стрелять")

        if damage > 5:
            print("Вы мертвы")

        else:
            print("Вас ранили")

    def Your_Answer_to_Ogre(self,damage):
         print("Вы подходите к огру и начинаете бить его своим мечом")

         if damage > 7:
             print("Огр мертв")
             print("Вот вы и убили зеленого и страшного Огра,вперед за приключениями")
         elif damage < 7:
             print("Вы только ранили Огра")
             print("Нужно продолжать сражение")

         


class Wizard():
    def __init__(self,weapon,health):
        self.weapon=weapon
        self.health=health

    def Wizard_weapon(self,weapon):
        print( "Волшебник дал вам новое оружие" + weapon)
class hero_is_on_the_way():
    def __init__(self,weapon,health):
        self.health=health
        
    def Cave(self,weapon,health):
        print("Вы двигаетесь дальше и на пути видите зловещую пещеру там " + weapon)
    def Nastya(self,weapon,health):
        print("Появилась красавица Анастасия двигайтесь за ней " )

    




Hero.hero_is_on_the_way(0)
Ogre.Go_Ogre(1)
Ogre.Ogre_Attacks_You(2,3)
Ogre.Your_Answer_to_Ogre(3,5)
Wizard.Wizard_weapon(4," арбалет из костей дракона")
hero_is_on_the_way.Cave(7,"копье",9)
hero_is_on_the_way.Nastya(7,"копье",9)