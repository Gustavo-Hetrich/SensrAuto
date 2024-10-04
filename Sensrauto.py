import customtkinter as tk
from pynput import mouse
import keyboard
import time
import pyperclip
from pynput.mouse import Button, Controller
from playsound import playsound
from datetime import datetime, timedelta
from workalendar.america import Brazil


mouse = Controller()
cal = Brazil()

paused = False  # Variable to track the paused state


####################################################################################

# Categorizador
def chamado_cassi():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('cassiara stork')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('segurança da informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
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


def chamado_gusta():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('gustavo hetrich da cunha')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('tecnico de informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
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

def chamado_ita():
    print('Script started')
    playsound('audios\confirm_sound.mp3')
    time.sleep(1)
    mouse.position = (-903, 198)
    mouse.click(Button.left, 1)
    keyboard.write('itacir gui')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-921, 243)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.position = (-466, 202)
    mouse.click(Button.left, 1)
    keyboard.write('tecnologia da informação')
    time.sleep(0.5)
    keyboard.press_and_release('backspace')
    time.sleep(0.5)
    mouse.position = (-473, 245)
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
        data_inicial_dt = datetime.strptime(data_inicial, '%d%m%Y').date()
        data_final_dt = datetime.strptime(data_final, '%d%m%Y').date()
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
    keyboard.write('tecnologia da informação')
    time.sleep(4)
    keyboard.write('Itacir Gui')

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
   feriawin = tk.CTk()
   feriawin.title("Férias")
   feriawin.geometry("500x500")
   feriawin.mainloop()



##################################################################################

#exterminador

def check_word_in_clipboard():
    global palavra  # Ensure palavra is global
    # Get text from the clipboard and convert it to lowercase
    clipboard_text = pyperclip.paste().lower()

    palavras_chave = ('bloqueado', 'desbloqueio')

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
            playsound('audios\\alert.mp3')
            keyboard.wait('enter')
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
            keyboard.write('O Erro de "Código de segurança incorreto ocorre quando os minutos do celular do cooperado está fora do fuso correto, favor verificar se os minutos no celular do cooperado batem com os de outros dispositivos. Caso mesmo após verificar o horário o erro persista favor reabrir este chamado relatando o caso com uma foto do celular se possível.')
            time.sleep(7)
            mouse.position = (-57, 148)
            time.sleep(0.5)
            mouse.click(Button.left, 1)
            chamados_fechados += 1
            
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

keyboard.add_hotkey('alt+c', chamado_cassi)
keyboard.add_hotkey('alt+g', chamado_gusta)
keyboard.add_hotkey('alt+x', chamado_ita)
keyboard.add_hotkey('alt+v', vpn_ferias)
keyboard.add_hotkey('alt+k', exterminador)

keyboard.wait('f2')
