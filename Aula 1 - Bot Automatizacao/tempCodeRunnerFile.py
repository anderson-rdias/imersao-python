# Passo 1 - Entrar no sistema da empresa
    # Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Importar a base de dados
# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir o passo 4, até cadastrar todos produtos

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl + C)
# pyautogui.scroll - rolar a tela para cima ou baixo

pyautogui.PAUSE = 0.5


# Passo 1 - Entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2 - Fazer login
pyautogui.click(x=507, y=384)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("teste@teste.com")

# Passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("1234dsadsa@")
pyautogui.click(x=483, y=525)
time.sleep(3)

# Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print (tabela)

# Passo 4 - Cadastrar um produto

# tabela.index == lista com todas linhas da tabela
for linha in tabela.index:
    # codigo
    pyautogui.click(x=348, y=274)
    codigo = str(tabela.loc[linha, "codigo"]) # func str pra transform em texto
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
    if obs != "nan":
        pyautogui.write(obs)

    # clicar no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


# Passo 5 - Repetir o passo 4, até cadastrar todos produtos
