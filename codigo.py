# colocar hashtag para escrever um comentário
# pyauto - pacote de código para automação (mouse, teclado e tela do computador)

import pyautogui 
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# passo 1 - entrar no sistema
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#tempo para carregar a página
time.sleep(3)

# passo 2 - fazer login
pyautogui.click(x=815, y=511)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com") 

#passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.click(x=948, y=700)

time.sleep(3)

# paao 3 - importar a base de dados
import pandas

#PyPDF - para o pandas ler pdf
#escolher o nome de uma variavel(caixa) para armazenamento (tabela)
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4 - cadastrar produto
# para cada linha da minha tabela:
for linha in tabela.index:

    # codigo
    pyautogui.click(x=861, y=364)

    codigo = str(tabela.loc[linha, "codigo"]) #string (str)= textos
    pyautogui.write(codigo)

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": #!= - significa diferente
        pyautogui.write(obs)

    #clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# passo 5 - repetir (passo 4) para todos os produtos - para todas as linhas da tabela