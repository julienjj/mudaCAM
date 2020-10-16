import os, re, shutil
from tkinter import filedialog
from tkinter import messagebox
from tkinter import messagebox as mb
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory(initialdir='c://',title="SELECIONE A OF-XXXXX")
res=mb.askquestion('Alterar OF', 'Pasta selecionada: -> '+folder_selected+' - Voce tem certeza?')
if res == 'yes' :
    shutil.copytree(folder_selected, folder_selected+"-p_imprimir")
    messagebox.showinfo('Feito!',' Pasta selecionada: -> '+folder_selected)
else:
    messagebox.showinfo('Cancelado',' Pasta selecionada: -> '+folder_selected)


directory = os.listdir(folder_selected+"-p_imprimir")
os.chdir(folder_selected+"-p_imprimir")


espaco= []
num_de_espacos=400
esp=' '
for i in range(1,num_de_espacos+1):
    espaco.append(esp*i) # criando a lista



texto =[]
lista = []
lista_normal=[]
i=0
j=0
k=0
l=0

for file in directory:
    open_file = open(file,'r')
    texto= open_file.readlines()
    material=(texto[26])
    material1=material.replace('\n','')
    qualidade=(texto[31])
    qualidade1=qualidade.replace('\n','')
    lista.append(material1+';'+qualidade1+';'+file+'\n')
    i=i+1
    open_file.close()

lista.sort()


for i in range(0,len(lista)):
    nome=lista[i].split(";")
    file_open=open(folder_selected+"-p_imprimir/"+nome[2].replace('\n',''),'r')
    read_file = file_open.read()
    regex = re.compile('POS_PEZ:')
    read_file = regex.sub('POS_PEZ:'+espaco[i],read_file) # aqui deve alterar para espaço dinamico
    write_file = open(folder_selected+"-p_imprimir/"+nome[2].replace('\n',''),'w')
    write_file.write(read_file)
    file_open.close()

    
