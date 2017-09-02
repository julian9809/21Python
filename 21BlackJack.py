from random import *

def generar_mazo():
	return sample([(x,y) for x in ['A','J','Q','K','2','3','4','5','6','7','8','9','10'] for y in ['♠','♣','♦','♥']],52)

def valor_carta(carta):
	if carta[0] == '2':
		return 2
	if carta[0] == '3':
		return 3
	if carta[0] == '4':
		return 4
	if carta[0] == '5':
		return 5
	if carta[0] == '6':
		return 6
	if carta[0] == '7':
		return 7
	if carta[0] == '8':
		return 8
	if carta[0] == '9':
		return 9
	if carta[0] == '10':
		return 10	
	if carta[0] in "JQK":
		return 10
	if carta[0] == 'A':
		return 1
	return int(carta[0])

def existe_az(mano):
    if mano!=[] :
        if mano[0]=='A' :
            return 10
    return 0

def valor_mano(mano):
 	if mano == []:
 		return 0
 		if  valor_carta(mano[0]) + valor_mano(mano[1:]) <=10:
 			return valor_carta(mano[0]) + valor_mano(mano[1:]) + existe_az(mano[0])
 		if  valor_carta(mano[0]) + valor_mano(mano[1:]) >10:
 			return valor_carta(mano[0]) + valor_mano(mano[1:])
 	return valor_carta(mano[0]) + valor_mano(mano[1:])


def jugar(mazo, casa, jugador):
	if mazo != []:
		print("acumulado jugador ", valor_mano(jugador))
		# print("acumulado casa ", valor_mano(casa))
		if casa == [] and jugador == []:
			print("Carta Jugador")
			print(jugador+mazo[1:2])
			print("Carta Casa")
			print(casa+mazo[:1])
			return jugar(mazo[2:],casa+mazo[:1],jugador+mazo[1:2])
		if len(casa) == 1 and len(jugador) == 1 :
			print("Carta Jugador")
			print(jugador+mazo[1:2])
			return jugar(mazo[2:],casa+[mazo[0]],jugador+[mazo[1]])
		if valor_mano(casa)<21 and valor_mano(jugador)<21:
			d = input("Desea Continuar(s/n) ")
			if d == "s":                                
				print("carta jugador" , jugador+[mazo[1]])
				return jugar(mazo[2:],casa,jugador+[mazo[1]])
			else:
				if valor_mano(casa)<valor_mano(jugador):
					return jugar(mazo[2:],casa+[mazo[0]],jugador)
				if valor_mano(casa)>valor_mano(jugador):
					print("carta casa" , casa)
					print("acumulado casa ", valor_mano(casa))
					print(">>>PERDISTE<<<")
				if valor_mano(casa)==valor_mano(jugador):
					print("carta casa" , casa)
					print("acumulado casa ", valor_mano(casa))
					print(">>>PERDISTE<<<")
			return 0
		else:
			if valor_mano(casa)>valor_mano(jugador) and valor_mano(casa)<=21 and valor_mano(jugador)<=21:
				print("carta casa" , casa)
				print("acumulado casa ", valor_mano(casa))
				print(">>>PERDISTE<<<")
			if valor_mano(casa)<valor_mano(jugador) and valor_mano(casa)<=21 and valor_mano(jugador)<=21:
				print("carta casa" , casa)
				print("acumulado casa ", valor_mano(casa))
				print("<<<GANASTE>>>")
			if valor_mano(casa)>21 and valor_mano(jugador)<21:
				print("carta casa" , casa)
				print("acumulado casa ", valor_mano(casa))
				print("<<<GANASTE>>>")
			if valor_mano(jugador)>21:
				print(">>>PERDISTE<<<")					
					
jugar(generar_mazo(),[],[])


