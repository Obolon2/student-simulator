import random


class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.active = True

    def to_study(self):
        print('Time to study!')
        self.progress += 0.12
        self.happiness -= 5

    def to_sleep(self):
        print('ZZzzzz!')
        self.happiness += 3

    def to_chill(self):
        print('Chill time!')
        self.happiness += 5
        self.progress -= 0.1

    def is_active(self):
        if self.progress < -0.5:
            print('Vidrahuvannya!')
            self.active = False
        elif self.happiness < 0:
            print('Depression!')
            self.active = False
        elif self.progress > 5:
            print('Passed externally!')
            self.active = False

    def status(self):
        print(f'Happiness: {self.happiness}')
        print(f'Progress: {round(self.progress, 2)}')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.name} life'
        print(f'{day_str:=^50}')
        dice = random.randint(1, 3)
        if dice == 1:
            self.to_study()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_chill()
        self.status()
        self.is_active()


dmytro = Student(name='Dmytro')
for day in range(365):
    if dmytro.active:
        dmytro.live_a_day(day)
    else:
        break

if dmytro.active:
    print('HURRAH! End of the year!')
