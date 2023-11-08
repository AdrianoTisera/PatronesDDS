from . import TrianguloProductABC

class EscalenoProduct(TrianguloProductABC):

    def getDescripcion(self) -> str:
        return "Es un triángulo escaleno."

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass
