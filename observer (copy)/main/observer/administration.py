from . import BookBadConditionABC

class Administration(BookBadConditionABC):

    def update(self) -> None:
        print("Administration: ")
        print("Se suspende al socio hasta la reposición o reparación del daño causado.")
