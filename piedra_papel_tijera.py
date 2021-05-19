import random

def cpu_choice():
    rnd = random.randint(1,3);
    if rnd==1:
        return "piedra"
    elif rnd==2:
        return "papel"
    else:
        return "tijera"

def player_choice():
    valid_input = ["piedra", "papel", "tijera"]
    invalid = True
    while invalid:
        choice = input("Elije tu jugada (piedra, papel o tijera): ");
        if choice in valid_input:
            invalid = False
        else:
            print("Jugada invalida")
    return choice

def get_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "Empate";
    elif player1_choice == "piedra":
        if(player2_choice == "tijera"):
            return "Jugador 1"
        else:
            return "CPU"
    elif player1_choice == "papel":
        if(player2_choice == "piedra"):
            return "Jugador 1"
        else:
            return "CPU"
    elif player1_choice == "tijera":
        if(player2_choice == "papel"):
            return "Jugador 1"
        else:
            return "CPU"

def simple_game():
    p1 = player_choice()
    cpu = cpu_choice()
    print("Jugador1 elige: "+p1+" CPU elige: "+cpu)
    return get_winner(p1,cpu)

def two_out_of_three():
    p1_count = 0
    cpu_count = 0
    count = 1
    while p1_count<2 and cpu_count<2:
        print("Ronda "+str(count))
        winner = simple_game()
        if winner=="Jugador 1":
            p1_count += 1
            count += 1
        elif winner=="CPU":
            cpu_count += 1
            count += 1
        print("El ganador de esta ronda es: "+winner)
    if p1_count > cpu_count:
        return "Jugador 1"
    else:
        return"CPU"

def main():
    winner = False
    while not winner:
        print("Bienvenido a pieda_papel_tijera.py")
        print("--Elije el modo de juego--")
        print("1. 1 Ronda")
        print("2. 2 de 3 Rondas")
        seleccion = int(input("Seleccion: "))
        if seleccion==1:
            winner = simple_game()
        elif seleccion==2:
            winner = two_out_of_three()
        else:
            print("Seleccion invalida")
    print("El ganador del juego es: " + winner)

if __name__ == '__main__':
    main()
    