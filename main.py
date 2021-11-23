import fnmatch
import os
import pathlib
from tkinter import Text


import PySimpleGUI as sg

sg.theme('Dark Blue 3')


def GetFilesToCompare():
    form_rows = [[sg.Text('Elige la carpeta a Organizar')],
                [sg.Text('Carpeta a Organizar', size=(15, 1)),
                sg.InputText(key='-folder-'), sg.FolderBrowse("Buscar")],
                [sg.Submit("Organizar"), sg.Cancel("Cancelar")]]
    

    window = sg.Window('Organizador de Archivos', form_rows)
    event, values = window.read()
    window.close()
    return event, values

def directory(path,extension):
    list_dir = []
    list_dir = os.listdir(path)
    count = 0
    for file in list_dir:
        if file.endswith(extension): # eg: '.txt'
            count += 1
    return count

def main():
    button, values = GetFilesToCompare()
    f = values['-folder-']

    if any((button != 'Organizar', f == '')):
        sg.popup_error('Operacion Cancelada')
        return
    
    a = f

    ruta = pathlib.Path(a)
    diccionario = {k: [v for v in ruta.glob(f'*{k}')]
                for k in {archivo.suffix for archivo in ruta.iterdir()}}
    countPdf = 0
    countJpeg = 0
    countPng = 0
    countMp3 = 0
    countMp4 = 0
    countDocs = 0
    countXlsx = 0
    countPptx = 0
    list = os.listdir(a) 
    number_files = len(list) 
    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:]
        carpeta.mkdir()
        if extension == '.pdf':
            countPdf = directory(a,extension)
        if extension == '.jpeg':
            countJpeg = directory(a,extension) 
        if extension == '.png':
            countPng = directory(a,extension)     
        if extension == '.mp3':
            countMp3 = directory(a,extension)
        if extension == '.mp4':
            countMp4 = directory(a,extension)
        if extension == '.docs':
            countDocs = directory(a,extension) 
        if extension == '.xlsx':
            countXlsx = directory(a,extension)
        if extension == '.pptx':
            countPptx = directory(a,extension)               
        for archivo in archivos:
            archivo = carpeta / archivo
            archivo.replace(carpeta / archivo.name)          
    cPdf = str(countPdf)
    cJepg = str(countJpeg)
    cPng = str(countPng)
    cMp3 = str(countMp3)
    cMp4 = str(countMp4)
    cDocs = str(countDocs)
    cXlsx = str(countXlsx)
    cPptx = str(countPptx)
    parseo = str(number_files)
    print(diccionario);
    sg.popup('Se organizaron '+ parseo + ' archivos con exito. Son: '
                + cPdf + ' .pdf, '+ cJepg + ' .jpeg,  '
                + cMp4 + ' .mp4,   '+ cDocs+'.docs'+ cPng+'.mp4,   '
                + cMp3 +'.mp3'+ cXlsx+'.xlsx'+ cPptx +'.pptx')  
if __name__ == '__main__':
    main()
