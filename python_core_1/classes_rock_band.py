class RockBand:
    def __init__(self, name: str, members: list) -> None:
        self.name = name
        self.members = members

    def add_new_member(self, new_member: str) -> None:
        if new_member in self.members:
            print(f"{new_member} is already in the band!")
        else:
            self.members.append(new_member)

    def __add__(self, other: "RockBand") -> "RockBand":
        new_members = list(self.members)
        for member in other.members:
            if member not in new_members:
                new_members.append(member)
        return RockBand(
            name=self.name + " " + other.name + " United",
            members=new_members
        )

first_band = RockBand("First", ["Ivan", "Sergey"])
second_band = RockBand("Second", ["Sergey", "Max"])
united = first_band + second_band
print(united.name, united.members) # "First Second United" ["Ivan", "Sergey", "Max"]
