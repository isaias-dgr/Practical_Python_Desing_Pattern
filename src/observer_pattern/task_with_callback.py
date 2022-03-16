from psutil import users


class Task:

    def __init__(self, user, _type) -> None:
        self.user = user
        self._type = _type
        self.callbacks = [
            self.user,
            self.user.wallet
        ]
        self.callbacks.extend(self.user.badges)

    def complete(self):
        for item in self.callbacks:
            item.complete_task(self)


class User:

    def __init__(self, wallet) -> None:
        self.wallet = wallet
        self.badges = []
        self.experience = 0

    def add_experiences(self, amount):
        self.experience += amount

    def complete_task(self, task):
        self.add_experiences(1)

    def __str__(self):
        badges = "\n\t".join([str(b) for b in self.badges])
        return f"""
        \rWallet\t{self.wallet}
        \rExperience\t{self.experience  }
        \rBadge\n\t{badges}
        """


class Wallet:

    def __init__(self) -> None:
        self.amount = 0

    def increase_balance(self, amount):
        self.amount += amount

    def decrease_balance(self, amount):
        self.amount -= amount

    def complete_task(self, task):
        self.increase_balance(5)

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

    def complete_task(self, task):
        if task._type == self._type:
            self.add_points(2)

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

    tasks = [
        Task(user, 1),
        Task(user, 1),
        Task(user, 3),
    ]

    for task in tasks:
        task.complete()

    print(user)


if __name__ == "__main__":
    main()
