from pathlib import Path

from architecture_factory import ArchitectureFactory


def trial():

    arf = ArchitectureFactory()
    ar = arf.generateArchitecture("Example Architecture", Path("./architecture"))


if __name__ == "__main__":
    trial()
