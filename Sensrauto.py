import customtkinter as tk
from pynput import mouse
import keyboard
import time
import pyperclip
from pynput.mouse import Button, Controller
from playsound import playsound
from datetime import datetime, timedelta
from workalendar.america import Brazil
from PyQt5.QtCore import QTimer
import subprocess
import sys
import os
import tkinter.messagebox as messagebox



mouse = Controller()

cal = Brazil()

paused = False  # Variable to track the paused state






####################################################################################

# Categorizador
def chamado_pesso1():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('segurança da informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('cassiara stork')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-329, 333)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    keyboard.write('suporte inter')
    keyboard.press_and_release('tab')
    time.sleep(0.3)
    mouse.scroll(0, -500)
    mouse.position = (-626, 648)
    time.sleep(0.3)
    mouse.click(Button.left, 1)


def chamado_pessoa2():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('Tecnologia da Informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('Gustavo/')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-329, 333)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    keyboard.write('suporte inter')
    keyboard.press_and_release('tab')
    time.sleep(0.3)
    mouse.scroll(0, -500)
    mouse.position = (-626, 648)
    time.sleep(0.3)
    mouse.click(Button.left, 1)

def chamado_pessoa3():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('Tecnologia da Informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('Itacir Gui')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-329, 333)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    keyboard.write('suporte inter')
    keyboard.press_and_release('tab')
    time.sleep(0.3)
    mouse.scroll(0, -500)
    mouse.position = (-626, 648)
    time.sleep(0.3)
    mouse.click(Button.left, 1)
########################################################################################

#vpn e férias:

def type_slowly(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)
def is_weekday(date):
    """Verifica se a data é um dia útil"""
    return cal.is_working_day(date)

def next_working_day(date):
    """Retorna o próximo dia útil a partir da data"""
    date += timedelta(days=1)
    while not is_weekday(date):
        date += timedelta(days=1)
    return date

def previous_working_day(date):
    """Retorna o dia útil anterior a partir da data"""
    date -= timedelta(days=1)
    while not is_weekday(date):
        date -= timedelta(days=1)
    return date


def vpn_ferias():
    playsound('audios\sf.mp3')
    # Create a Tkinter window
    root = tk.CTk()

    # Set the window title
    root.title("VPN&Férias")

    # Set the window size   
    root.geometry("300x120")

    vpn = tk.CTkButton(master=root, text="VPN", command=ativar_vpn, width=200, height=50, anchor="center")
    vpn.pack()

    ferias = tk.CTkButton(master=root, text="férias", command=ativar_ferias, width=200, height=50, anchor="center")
    ferias.pack()
    
    root.mainloop()

def ativar_vpn():
   global nome_vpn, data_inicial_vpn, data_final_vpn
   vpnwin = tk.CTk()
   vpnwin.title("VPN")
   vpnwin.geometry("500x220")
   nome_vpn = tk.CTkEntry(vpnwin, placeholder_text="Nome", width=200, height=50)
   nome_vpn.pack()
   data_inicial_vpn = tk.CTkEntry(vpnwin, placeholder_text="Data inicial", width=200, height=50)
   data_inicial_vpn.pack()
   data_final_vpn = tk.CTkEntry(vpnwin, placeholder_text="Data final", width=200, height=50)
   data_final_vpn.pack()
   iniciar_vpn = tk.CTkButton(vpnwin, text="Iniciar", command=chamado_vpn, width=200, height=50, anchor="center")
   iniciar_vpn.pack()
   vpnwin.mainloop()



def chamado_vpn():

    agora = datetime.now()
    arredondado = agora.replace(minute=0, second=0, microsecond=0)
    tempo_arredondado = arredondado.strftime("%H:%M")

    nome = nome_vpn.get()
    data_inicial = data_inicial_vpn.get()
    data_final = data_final_vpn.get()

    try:
        # Converte as datas de string para datetime
        data_inicial_dt = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        data_final_dt = datetime.strptime(data_final, '%d/%m/%Y').date()
    except ValueError:
        playsound('audios\\alert.mp3')
        print('Erro ao converter as datas. Verifique se as datas estão no formato DDMMYYYY.')
        return


    # Verifica se a data inicial é hoje, senão ajusta para o próximo dia útil
    if data_inicial_dt == datetime.now().date():
        print(f'Data inicial é hoje: {data_inicial_dt.strftime("%d/%m/%Y")}')
    else:
        data_inicial_dt = previous_working_day(data_inicial_dt)
        print(f'Data inicial ajustada para o dia útil anterior: {data_inicial_dt.strftime("%d/%m/%Y")}')
        

    data_final_dt = next_working_day(data_final_dt)
    print(f'Data final ajustada para o proximo dia útil: {data_final_dt.strftime("%d/%m/%Y")}')

    data_inicial = data_inicial_dt.strftime('%d/%m/%Y')
    data_final = data_final_dt.strftime('%d/%m/%Y')

    print('\nPara liberação inicie o Fluxo e aperte enter')

    print('Iniciado Liberação VPN')
    time.sleep(3) 
    playsound('audios\\pause.mp3')
    # Liberação VPN
    keyboard.write(f"Liberação VPN - {nome}")
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.write('0030')
    keyboard.press_and_release('tab')
    time.sleep(1)
    type_slowly(data_inicial)
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write(tempo_arredondado)
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('Favor Liberar a VPN para o colaborador')
    time.sleep(2)
    keyboard.write('tecnologia da info')
    time.sleep(0.5)
    time.sleep(4)
    keyboard.write('Itacir Gui')
    playsound('audios\\alert.mp3')

    print('\nPara remoção inicie o Fluxo e aperte enter')
    print('Iniciado Remoção VPN\n')
    time.sleep(10)
    playsound('audios\\pause.mp3')
    time.sleep(1)

    # Remover VPN
    keyboard.write(f"Remover VPN - {nome}")
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.write('0030')
    keyboard.press_and_release('tab')
    time.sleep(1)
    type_slowly(data_final)
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('1000')
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('Favor remover a permissão da VPN do colaborador')
    time.sleep(2)
    keyboard.write('tecnologia da informação')
    time.sleep(4)
    keyboard.write('Itacir Gui')

def ativar_ferias():
    global nome_ferias, data_inicial_ferias, data_final_ferias
    feriawin = tk.CTk()
    feriawin.title("Férias")
    feriawin.geometry("500x220")
    
    # Entrada para o nome
    nome_ferias = tk.CTkEntry(feriawin, placeholder_text="Nome", width=200, height=50)
    nome_ferias.pack()
    
    # Entrada para a data inicial
    data_inicial_ferias = tk.CTkEntry(feriawin, placeholder_text="Data inicial", width=200, height=50)
    data_inicial_ferias.pack()
    
    # Entrada para a data final
    data_final_ferias = tk.CTkEntry(feriawin, placeholder_text="Data final", width=200, height=50)
    data_final_ferias.pack()
    
    # Botão para iniciar
    iniciar_ferias = tk.CTkButton(feriawin, text="Iniciar", command=chamado_ferias, width=200, height=50, anchor="center")
    iniciar_ferias.pack()
    
    feriawin.mainloop()

def chamado_ferias():
    # Obter dados da interface gráfica
    nome = nome_ferias.get()
    data_inicial = data_inicial_ferias.get()
    data_final = data_final_ferias.get()

    try:
        # Converte as datas de string para datetime
        data_inicial_dt = datetime.strptime(data_inicial, '%d/%m/%Y').date()
        data_final_dt = datetime.strptime(data_final, '%d/%m/%Y').date()
    except ValueError:
        playsound('audios\\alert.mp3')
        print('Erro ao converter as datas. Verifique se as datas estão no formato DD/MM/YYYY.')
        return

    # Ajusta a data inicial para o próximo dia útil
    data_inicial_dt = next_working_day(data_inicial_dt)
    print(f'Data inicial ajustada para o próximo dia útil: {data_inicial_dt.strftime("%d/%m/%Y")}')

    # Ajusta a data final para o dia útil anterior
    data_final_dt = previous_working_day(data_final_dt)
    print(f'Data final ajustada para o dia útil anterior: {data_final_dt.strftime("%d/%m/%Y")}')

    # Atualiza as datas formatadas
    data_inicial = data_inicial_dt.strftime('%d/%m/%Y')
    data_final = data_final_dt.strftime('%d/%m/%Y')

    # Imprime o fluxo de liberação de férias
    print('\nIniciado Liberação de Férias')
    time.sleep(3)
    playsound('audios\\pause.mp3')
    
    # Liberação de férias
    keyboard.write(f"Bloquear usuário (Férias) - {nome}")
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.write('0030')
    keyboard.press_and_release('tab')
    time.sleep(1)
    type_slowly(data_inicial)
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write(data_inicial)  # Tempo arredondado
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('Favor bloquear o usuário por motivo de férias')
    time.sleep(2)
    keyboard.write('tecnologia da info')
    time.sleep(0.5)
    time.sleep(4)
    keyboard.write('Itacir Gui')
    playsound('audios\\alert.mp3')

    print('\nPara remoção inicie o Fluxo e aperte enter')
    print('Iniciado Remoção de Férias\n')
    time.sleep(10)
    playsound('audios\\pause.mp3')
    time.sleep(1)

    # Remover férias
    keyboard.write(f"Desbloquear usuário (Férias) - {nome}")
    keyboard.press_and_release('tab')
    time.sleep(0.5)
    keyboard.write('0030')
    keyboard.press_and_release('tab')
    time.sleep(1)
    type_slowly(data_final)
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('1000')  # Tempo final
    time.sleep(2)
    playsound('audios\\confirm_sound.mp3')
    time.sleep(1)
    keyboard.write('Favor desbloquear o usuário para o retorno de suas férias')
    time.sleep(2)
    keyboard.write('tecnologia da informação')
    time.sleep(4)
    keyboard.write('Itacir Gui')



##################################################################################

#exterminador
def exterminadorwin():
    global palavra_chave_entry
    exterwin = tk.CTk()
    exterwin.title("Exterminador")
    exterwin.geometry("300x150")
    palavra_chave_entry = tk.CTkEntry(exterwin, placeholder_text="Palavra Chave", width=200, height=50)
    instruções = tk.CTkLabel(exterwin, text="segura esc para pausar, separe cada frase em ','")
    iniciar = tk.CTkButton(exterwin, text="Iniciar", command=exterminador, width=200, height=50, anchor="center")
    instruções.pack()
    palavra_chave_entry.pack()
    iniciar.pack()
    exterwin.mainloop()


def check_word_in_clipboard():
    global palavra
    # Get text from the clipboard and convert it to lowercase
    palavras_chave = palavra_chave_entry.get().lower()
    clipboard_text = pyperclip.paste().lower()

    

    # Check if any of the words in 'palavras_chave' are in the clipboard text
    if any(word in clipboard_text for word in palavras_chave):
        print("The word was found in the clipboard text.")
        palavra = True
    else:
        print("The word was not found in the clipboard text.")
        palavra = False

def toggle_pause():
    global paused  # To modify the paused state
    if keyboard.is_pressed('esc'):
        paused = not paused  # Toggle the paused state
        if paused:
            print("Script paused.")
            playsound('audios\\pause.mp3')
            return True  # Return True if paused
        else:
            print("Script resumed.")
            playsound('audios\\pause.mp3')
            return False  # Return False if resumed
    return paused  # Return the current state

def exterminador():
    global paused  # Ensure paused is global so it's shared across functions
    global palavra  # Ensure palavra is global so it's shared across functions
    print(palavra_chave_entry.get())
    playsound('audios\sf.mp3')
    palavra = False
    repetições = 0
    chamados_fechados = 0
    chamados = 0
    paused = False
    
    time.sleep(3)
    
    
    # Main loop with pause checking
    for i in range(131):
        # Check if the script is paused
        if toggle_pause():  # If paused, exit the function
            print("Exiting loop due to pause.")
            paused = False
            return  # Exit the function completely if paused
        
        print(chamados_fechados)
        print(chamados)

        # abertura do primeiro chamado
        mouse.position = (-1164, 442)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(5)

        # Verificação 
        mouse.position = (-1324, 130)
        time.sleep(0.5)
        mouse.press(Button.left)
        time.sleep(0.5)
        mouse.position = (-100, 567)
        time.sleep(0.5)
        keyboard.press('ctrl')
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release('ctrl')
        mouse.release(Button.left)
        time.sleep(1)
        
        # Call the function to check the clipboard for the keyword
        check_word_in_clipboard()
        
        # Now, since "palavra" is global, it will correctly reflect the result of check_word_in_clipboard()
        if palavra:
            messagebox.showinfo("Palavra Encontrada", "A palavra foi encontrada no clipboard.")
            time.sleep(1)
            mouse.position = (-1164, 442)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            # Scroll down (negative value for down, positive for up)
            mouse.scroll(0, -21)  # (horizontal scroll, vertical scroll)
            mouse.position = (-245, 650)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            time.sleep(7)


            mouse.position = (-936, 194)
            mouse.click(Button.left, 1)
            keyboard.write('gustavo hetrich da cunha')
            time.sleep(0.5)
            keyboard.press_and_release('backspace')
            time.sleep(0.5)
            mouse.position = (-951, 239)
            mouse.click(Button.left, 1)
            mouse.position = (-321, 338)
            mouse.click(Button.left, 1)
            time.sleep(0.5)
            keyboard.write('suporte interno')
            keyboard.press_and_release('tab')
            time.sleep(1)
            mouse.scroll(0, -21)
            mouse.position = (-632, 658)
            time.sleep(2)
            mouse.click(Button.left, 1)
            time.sleep(7)

            mouse.position = (-160, 333)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            time.sleep(1)

            mouse.scroll(0, -21)
            mouse.position = (-1167, 476)
            time.sleep(4)
            keyboard.write('Foi lançada a versão 2.4.0 do aplicativo no qual é resolvido o Bug de Módulo de segurança incorreto, favor auxiliar o cooperado e atualizar o aplicativo')
            time.sleep(7)
            mouse.position = (-57, 148)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            
        else:
            mouse.position = (-57, 148)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            time.sleep(1)
            mouse.position = (-1164, 442)
            time.sleep(1)
            keyboard.press_and_release('down')
            keyboard.press_and_release('down')
            keyboard.press_and_release('down')
            keyboard.press_and_release('down')
            chamados += 1
            repetições += 1
            if repetições == 5:
                keyboard.press_and_release('down')

        toggle_pause()

##############################################################################

# Leitor

def check_word_in_clipboard_leitor():
    global palavra
    # Get text from the clipboard
    clipboard_text = pyperclip.paste()

def toggle_pause_leitor():
    global paused  # To modify the paused state
    if keyboard.is_pressed('esc'):
        paused = not paused  # Toggle the paused state
        if paused:
            print("Script paused.")
            playsound('audios\\pause.mp3')
            return True  # Return True if paused
        else:
            print("Script resumed.")
            playsound('audios\\pause.mp3')
            return False  # Return False if resumed
    return paused  # Return the current state

def leitor():
    playsound('audios\\SF.mp3')
    time.sleep(3)
    for i in range(131):
        # Check if the script is paused, and wait if it is
        while paused:
            time.sleep(0.1)  # Sleep for a short time to avoid high CPU usage
        

        # abertura do primeiro chamado
        mouse.position = (-1164, 442)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(5)

        mouse.position = (-57, 148)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.5)
        mouse.position = (-1164, 442)
        time.sleep(0.5)
        keyboard.press_and_release('down')
        keyboard.press_and_release('down')
        keyboard.press_and_release('down')
        keyboard.press_and_release('down')

    toggle_pause_leitor()

##################################################################################

#sub_categorizador

def sub_categorizador():
    playsound('audios\\SF.mp3')

    # Defina o caminho completo do script que deseja executar
    script_path = os.path.join(os.getcwd(), 'sub_categorizador.py')

    # Caminho para pythonw.exe
    pythonw_path = os.path.join(os.path.dirname(sys.executable), 'pythonw.exe')

    # Inicia o script em segundo plano usando pythonw
    try:
        subprocess.Popen([pythonw_path, script_path])
        print("O script sub_categorizador.py foi iniciado em segundo plano.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


##################################################################################

# desbloquear_front

def desbloquear_front():
    playsound('audios\\SF.mp3')

    # Defina o caminho completo do script que deseja executar
    script_path = os.path.join(os.getcwd(), 'desbloquear_front.py')

    # Caminho para pythonw.exe
    pythonw_path = os.path.join(os.path.dirname(sys.executable), 'pythonw.exe')

    # Inicia o script em segundo plano usando pythonw
    try:
        subprocess.Popen([pythonw_path, script_path])
        print("O script desbloquear_front.py foi iniciado em segundo plano.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


##################################################################################

while True:
    keyboard.add_hotkey('alt+c', chamado_pesso1)
    keyboard.add_hotkey('alt+g', chamado_pessoa2)
    keyboard.add_hotkey('alt+x', chamado_pessoa3)
    keyboard.add_hotkey('alt+v', vpn_ferias)
    keyboard.add_hotkey('alt+k', exterminadorwin)
    keyboard.add_hotkey('alt+q', leitor)
    keyboard.add_hotkey('alt+l', sub_categorizador)
    keyboard.add_hotkey('alt+f', desbloquear_front)

    keyboard.wait('f2')
