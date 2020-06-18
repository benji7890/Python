class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def user_input(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                choice = input()
                if choice in ('1','2','3'):
                    self.buy(int(choice))
                else:
                    continue
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break
            else:
                print("Invalid input")
                continue

    def buy(self,x):
        if x == 1:
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
            else:
                if self.water < 250:
                    print('Sorry, not enough water!')
                elif self.beans < 16:
                    print('Sorry, not enough beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')
        elif x == 2:
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
            else:
                if self.water < 350:
                    print('Sorry, not enough water!')
                elif self.milk < 75:
                    print('Sorry, not enough milk!')
                elif self.beans < 20:
                    print('Sorry, not enough beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')
        elif x == 3:
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
            else:
                if self.water < 200:
                    print('Sorry, not enough water!')
                elif self.milk < 100:
                    print('Sorry, not enough milk!')
                elif self.beans < 12:
                    print('Sorry, not enough beans!')
                elif self.cups < 1:
                    print('Sorry, not enough cups!')

    def fill(self):
        addw = int(input("Write how many ml of water do you want to add:"))
        self.water += addw
        addm = int(input("Write how many ml of milk do you want to add:"))
        self.milk += addm
        addb = int(input("Write how many grams of coffee beans do you want to add:"))
        self.beans += addb
        addc = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.cups += addc

    def take(self):
        print("I gave you $", self.money)
        self.money -= self.money

    def remaining(self):
        print("The coffee machine has:")
        print(self.water, " of water")
        print(self.milk, " of milk")
        print(self.beans, " of coffee beans")
        print(self.cups, " of disposable cups")
        print("$", self.money, " of money")

newMachine = CoffeeMachine(400, 540, 120, 9, 550)
newMachine.user_input()






