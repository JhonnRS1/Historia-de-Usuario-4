from informe import Gerente

def test_generar_informe_exitoso():
    gerente = Gerente()
    resultado = gerente.generar_informe()
    assert resultado == True
