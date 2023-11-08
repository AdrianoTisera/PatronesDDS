from . import TrianguloProductABC

class EquilateroProduct(TrianguloProductABC):

    def getDescripcion(self) -> str:
        return "Es un triángulo equilátero."

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass
