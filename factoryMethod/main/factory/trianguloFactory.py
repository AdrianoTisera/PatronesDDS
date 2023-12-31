from . import TrianguloFactoryABC
from main.product import TrianguloProductABC, EquilateroProduct, EscalenoProduct, IsoscelesProduct, InvalidoProduct

class TrianguloFactory(TrianguloFactoryABC):

    def createTriangulo(self, ladoA: int, ladoB: int, ladoC: int) -> TrianguloProductABC:

        if (ladoA + ladoB < ladoC) or (ladoB + ladoC < ladoA) or (ladoA + ladoC < ladoB):
            invalidoProduct = InvalidoProduct(ladoA,ladoB,ladoC)
            return invalidoProduct
        
        elif (ladoA == ladoB) and (ladoB == ladoC) and (ladoA == ladoC):
            equilateroProduct = EquilateroProduct(ladoA,ladoB,ladoC)
            return equilateroProduct
        
        elif (ladoA!=ladoB) and (ladoB!=ladoC) and (ladoA!=ladoC):
            escalenoProduct = EscalenoProduct(ladoA,ladoB,ladoC)
            return escalenoProduct
        
        else:
            isoscelesProduct = IsoscelesProduct(ladoA,ladoB,ladoC)
            return isoscelesProduct
