class Towel:
    def __init__(self, color: str, size: str):  # construtor
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None:  # aumenta a umidade
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            self.wetness = self.getMaxWetness()
            print("toalha encharcada")

    def isDry(self) -> bool:
        return self.wetness == 0

    def wringOut(self) -> None:  # torcer
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":  # early return
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def show(self) -> None:
        print(f"{self.color} {self.size} {self.wetness}")

    def __str__(self) -> str:  # toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"


def main():
    towel: Towel = Towel("", "")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "criar":  # criar cor tamanho
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color, size)
        elif args[0] == "seca":
            print("sim" if towel.isDry() else "nao")
        elif args[0] == "torcer":
            towel.wringOut()
        elif args[0] == "enxugar":
            amount: int = int(args[1])
            towel.dry(amount)
        elif args[0] == "mostrar":
            print(towel)
        else:
            print("fail: comando não encontrado")


if __name__ == "__main__":
    main()
