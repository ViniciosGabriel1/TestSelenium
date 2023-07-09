
# O assert sempre verifica se o retorno ds condições é verdadeira


#assert numbers
numero_recebido = 1
numero_atual = 2

assert numero_recebido != numero_atual, "error"


#assert text
text_esperado = "Vini lindo"
text_atual = "Vini lindo"

assert text_atual.lower() == text_esperado.lower(), f"O texto {text_esperado} não é igual a {text_atual}. "


#assert text in string
text_esperado = "Vini lindo"
text_atual = "Vini mais lindo"

assert text_atual not in text_esperado, f" Esperado '{text_esperado}' dentro da string  '{text_atual}'. "


