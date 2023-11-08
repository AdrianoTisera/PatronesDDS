from . import TrianguloProductABC

class InvalidoProduct(TrianguloProductABC):

    def getDescripcion(self) -> str:
        return "No es un triángulo válido."

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass

