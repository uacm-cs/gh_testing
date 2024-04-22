from src.descuento import calcular_descuento
import pytest

@pytest.mark.parametrize("precio, tasa_descuento, valor_esperado",
                         [(100, 0.5, 50),
                          (50, 0.5, 25)] )
def test_descuento_ok(precio, tasa_descuento, valor_esperado):
    precio_final  = calcular_descuento(precio, tasa_descuento)
    assert precio_final == valor_esperado


# @pytest.mark.parametrize("precio, tasa_descuento, valor_esperado",
#                          [(-10, 0.5, ValueError)] )
# def test_descuento_error(precio, tasa_descuento, valor_esperado):
#     with pytest.raises(ValueError) as error:
#         calcular_descuento(precio, tasa_descuento)
        
#     assert isinstance(error.value, valor_esperado)
#     assert type(error.value) == valor_esperado
#     assert error.type  == valor_esperado
#     assert error.errisinstance(valor_esperado)
    
