# Passo a Passo do projeto
# Passo 1: Entrar no sistema da Empresa
# URL da produção

import pyautogui 
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

#Abrir o navegador
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")

# Acessar a URL 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer o Login

# selecionar o campo de email
pyautogui.click(x=756, y=555)
# escrever o seu email
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.click(x=899, y=792)
time.sleep(3)
# Passo 3: Importar a base de produtos para cadastrar

tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clickar no campo
    pyautogui.click(x=931, y=371)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o próximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    # da scroll para cima
    pyautogui.scroll(5000)
    time.sleep(2)

    # Passo 5: Repetir o processo de cadastro até o fim


    