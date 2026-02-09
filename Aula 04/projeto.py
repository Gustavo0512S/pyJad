#!/usr/bin/env python
# coding: utf-8

# Importando bibliotecas
# 

# In[32]:


import os
import smtplib
import shutil
import pyautogui
import pywhatkit as kit
from time import sleep
from datetime import datetime
from email.message import EmailMessage 
import win32com.client as win32


# In[33]:


import sys
import subprocess

# Desinstalar pywin32
subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "pywin32", "-y"])

# Instalar pywin32 novamente
subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])

# Executar o post-install
subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pywin32"])


# Organizando arquivos

# In[13]:


arquivo_excel = r'Aula 04/contas_processadas.xlsx'
pasta_base = 'base'


# In[14]:


import os

print("Diretório atual:", os.getcwd())


# Verificando se o arquivo existe

# In[15]:


if not os.path.exists(arquivo_excel):
    raise FileNotFoundError('Arquivo não encontrado')

print('Arquivo encontrado')


# Criando a pasta base dentro da aula 04

# In[12]:


if not os.path.exists(pasta_base):
    os.makedirs(pasta_base)
    print('Pasta criada com sucesso')

else:
    print('Pasta Base ja existe')


# Movendo arquivo para dentro da pasta base

# In[16]:


destino = os.path.join(pasta_base, os.path.basename(arquivo_excel))

if not os.path.exists(destino):
    shutil.move(arquivo_excel, destino)
    print('Arquivo movido com sucesso')

else:
    print('Arquivo já existe na pasta Base')


# Criando corpo do Email

# In[23]:


hoje = datetime.now().strftime('%d . %m . %Y | %H:%M')

corpo_email = f"""
Prezados, bom dia!

Anexo penências de conciliação referente ao mês 02/2025.
Data da atualização: {hoje}

Atenciosamente

 """

print(corpo_email)


# Configurando Outlook

# In[ ]:




