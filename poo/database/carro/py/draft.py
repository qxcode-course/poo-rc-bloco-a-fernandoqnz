class Car:
    def __init__(self):
        self.passengers = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def __str__(self):
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"

    def show(self):
        print(self.__str__())

    def enter(self):
        if self.passengers < self.passMax:
            self.passengers += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passengers > 0:
            self.passengers -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, increment: int):
        if increment < 0:
            return
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int):
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
            return

        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if distance <= self.gas:
            self.gas -= distance
            self.km += distance
        else:
            gasAvailable = self.gas
            self.km += gasAvailable
            print(f"fail: tanque vazio apos andar {gasAvailable} km")
            self.gas = 0


def main() -> None:
    car = Car()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            car.show()
        elif args[0] == "enter":
            car.enter()
        elif args[0] == "leave":
            car.leave()
        elif args[0] == "fuel":
            val = int(args[1])
            car.fuel(val)
        elif args[0] == "drive":
            distance = int(args[1])
            car.drive(distance)
        else:
            print("fail: comando invalido")


if __name__ == "__main__":
    main()
