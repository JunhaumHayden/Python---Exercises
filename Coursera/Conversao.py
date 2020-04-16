Segundos = input("Por favor, entre com o numero de segundos que deseja converter:")
ConversaoSegundos = int(Segundos)

Dias = ConversaoSegundos // 8600
segundos_restantes = ConversaoSegundos % 84600
Horas = ConversaoSegundos // 3600
segundos_restantes = ConversaoSegundos % 3600
Minutos = segundos_restantes // 60
Segundo = ConversaoSegundos % 60
print(Dias,":dias",Horas,":horas",Minutos,":minutos",Segundo,":segundo")
