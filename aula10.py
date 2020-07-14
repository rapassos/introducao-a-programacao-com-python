###############################################
# Author: Rafael Passos Guimarães
# E-mail: rapassos@gmail.com
# Date: 13/Jul/2020
###############################################

from datetime import date,time,datetime,timedelta

def trabalhando_com_date():
    hoje = date.today()
    print('Hoje é {}'.format(hoje.strftime('%d/%m/%Y')))

def trabalhando_com_time():
    hora = time(hour=22,minute=31,second=25)
    print('Agora é {}'.format(hora.strftime('%H:%M:%S')))

def trabalhando_com_datetime():
    dataHora = datetime.now()
    hoje = dataHora.strftime('%d de %b de %Y')
    agora = dataHora.strftime('%H:%M')
    print('Hoje é {} e agora são {}'.format(hoje,agora))

    diaSemana = dataHora.weekday()
    semana = ('segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo')
    print('Hoje é {}'.format(semana[diaSemana]))

    dataCriada = datetime(2025,9,5,17,23,55)
    print(dataCriada.strftime('%d de %b de %Y %H:%M'))

    dataStr = '17/01/2008 07:25:13'
    dataConvertida = datetime.strptime(dataStr,'%d/%m/%Y %H:%M:%S')
    print(dataConvertida)

    menosUmAno = dataConvertida - timedelta(days=365)
    print(menosUmAno)


if __name__ == "__main__":
    pass
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()