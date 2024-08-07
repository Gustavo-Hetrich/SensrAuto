from pynput.keyboard import Key, Controller 
import time
from datetime import datetime, timedelta
from workalendar.america import Brazil

keyboard = Controller()

# Inicializa o calendário do Brasil
cal = Brazil()

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

while True:
    agora = datetime.now()
    arredondado = agora.replace(minute=0, second=0, microsecond=0)
    tempo_arredondado = arredondado.strftime("%H:%M")

    action = input('VPN(1) OU Férias(2)? (Digite "sair" para sair) ')

    if action.lower() == 'sair':
        break

    if action == '1':

        nome = input('Insira o nome do colaborador: ')
        data_inicial = input('Data inicial: ')
        data_final = input('Data final: ')

        # Converte as datas de string para datetime
        data_inicial_dt = datetime.strptime(data_inicial, '%d%m%Y').date()
        data_final_dt = datetime.strptime(data_final, '%d%m%Y').date()

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

        input('aperte enter e clique no nome da tarefas para iniciar')
        time.sleep(3)

        # Liberação VPN
        keyboard.type(f"Liberação VPN - {nome}")
        keyboard.tap(Key.tab)
        time.sleep(0.5)
        keyboard.type('0030')
        keyboard.tap(Key.tab)
        time.sleep(1)
        type_slowly(data_inicial)
        time.sleep(3)
        keyboard.type(tempo_arredondado)
        time.sleep(5)
        keyboard.type('Favor Liberar a VPN para o colaborador')

        input('Para remoção inicie o Fluxo e aperte enter')
        time.sleep(5)

        # Remover VPN
        keyboard.type(f"Remover VPN - {nome}")
        keyboard.tap(Key.tab)
        time.sleep(0.5)
        keyboard.type('0030')
        keyboard.tap(Key.tab)
        time.sleep(1)
        type_slowly(data_final)
        time.sleep(3)
        keyboard.type(tempo_arredondado)
        time.sleep(5)
        keyboard.type('Favor remover a permissão da VPN do colaborador')

    if action == '2':
        nome = input('Insira o nome do colaborador: ')
        data_inicial = input('Data inicial: ')
        data_final = input('Data final: ')

        # Converte as datas de string para datetime
        data_inicial_dt = datetime.strptime(data_inicial, '%d%m%Y').date()
        data_final_dt = datetime.strptime(data_final, '%d%m%Y').date()

        # Verifica e ajusta as datas para dias úteis, se necessário
        if not is_weekday(data_inicial_dt):
            data_inicial_dt = next_working_day(data_inicial_dt)
            print(f'Data inicial ajustada para o próximo dia útil: {data_inicial_dt.strftime("%d/%m/%Y")}')
        
        data_final_dt = previous_working_day(data_final_dt)
        print(f'Data final ajustada para o dia útil anterior: {data_final_dt.strftime("%d/%m/%Y")}')

        data_inicial = data_inicial_dt.strftime('%d/%m/%Y')
        data_final = data_final_dt.strftime('%d/%m/%Y')

        input('aperte enter e clique no nome da tarefas para iniciar')
        time.sleep(3)

        # Bloquear férias
        keyboard.type(f"Bloquear usuário (Férias) - {nome}")
        keyboard.tap(Key.tab)
        time.sleep(0.5)
        keyboard.type('0030')
        keyboard.tap(Key.tab)
        time.sleep(1)
        type_slowly(data_inicial) 
        time.sleep(3)
        keyboard.type(tempo_arredondado)
        time.sleep(5)
        keyboard.type('Favor bloquear o usuário por motivo de férias')
        
        input('Para remoção inicie o Fluxo e aperte enter')
        time.sleep(5)

        # Desbloquear férias
        keyboard.type(f"Desbloquear usuário (Férias) - {nome}")
        keyboard.tap(Key.tab)
        time.sleep(0.5)
        keyboard.type('0030')
        keyboard.tap(Key.tab)
        time.sleep(1)
        type_slowly(data_final) 
        time.sleep(3)
        keyboard.type(tempo_arredondado)
        time.sleep(5)
        keyboard.type('Favor desbloquear o usuário para o retorno de suas férias')

print("Script encerrado.")
