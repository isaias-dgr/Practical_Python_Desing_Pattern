class User:

    def __init__(self, wallet) -> None:
        self.wallet = wallet
        self.badges = []
        self.experience = 0

    def add_experiences(self, amount):
        self.experience += amount

    def __str__(self):
        badges = "\n\t".join([str(b) for b in self.badges])
        return f"""
        \rWallet\t{self.wallet}
        \rExperience\t{self.experience  }
        \rBadge\n\t{badges}
        """


class Task:

    def __init__(self, user, _type) -> None:
        self.user = user
        self._type = _type

    def complete(self):
        self.user.add_experiences(1)
        self.user.wallet.increase_balance(5)

        for badge in self.user.badges:
            if self._type == badge._type:
                badge.add_points(2)


class Wallet:

    def __init__(self) -> None:
        self.amount = 0

    def increase_balance(self, amount):
        self.amount += amount

    def decrease_balance(self, amount):
        self.amount -= amount

    def __str__(self) -> str:
        return str(self.amount)


class Badges:
    def __init__(self, name, _type) -> None:
        self.points = 0
        self.name = name
        self._type = _type
        self.awarded = False

    def add_points(self, amount):
        self.points += amount

        if self.points > 3:
            self.awarded = True

    def __str__(self):
        if self.awarded:
            award_string = "Earned"
        else:
            award_string = "Unearned"

        return f"{self.name}: {award_string}[{self.points}]"


def main():
    wallet = Wallet()
    user = User(wallet)

    user.badges.append(Badges("Fun Badge", 1))
    user.badges.append(Badges("Bravery Badge", 2))
    user.badges.append(Badges("Missing Badge", 3))

    task = [
        Task(user, 1),
        Task(user, 1),
        Task(user, 3),
    ]

    for task in task:
        task.complete()

    print(user)


if __name__ == "__main__":
    main()
