from . import ApproverABS

class EjecutiveTeamLeader(ApproverABS):
    def __init__(self) -> None:
        self.next = None

    def setNext(self, approver: ApproverABS) -> None:
        self.next = approver

    def getNext(self) -> ApproverABS:
        return self.next

    def requestLoan(self, money: int) -> None:
        if 10000 < money <= 50000:
            print("Solicitud gestionada por el lider de equipo ejecutivo.")
        else:
            self.next.requestLoan(money)
