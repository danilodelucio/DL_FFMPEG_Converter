import os
from datetime import datetime

print("")
print("Desenvolvido por: Danilo de Lucio")
print("www.danilodelucio.com")
print("15/04/2022")
print("")

while True:
    try:
        path = input("Por favor insira o diretório dos seus arquivos: ")

        show_path = os.listdir(path)
        cmd = "ffmpeg -i"
        file_list = []

        for file in show_path:
            old_ext = file.split(".")[1]
            file_name = file.split(".")[0]
            new_ext = ".mp4"
            final_file = cmd + " " + file + " " + file_name + new_ext + " \r"
            file_list.append(final_file)

        with open("Arquivos_para_converter.txt", "w") as txt_file:
            for i in file_list:
                txt_file.writelines(i)

        print("")
        print("[FEITO!] Arquivo de texto criado com sucesso!")
        print("")

    except:
        print("")
        print("[ERRO!] Diretório inválido, ou existem arquivos sem extensão.")
        print("")