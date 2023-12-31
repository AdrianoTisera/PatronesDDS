from . import TrianguloProductABC

class IsoscelesProduct(TrianguloProductABC):

    def getDescripcion(self) -> str:
        return "Es un triángulo isósceles."

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass
