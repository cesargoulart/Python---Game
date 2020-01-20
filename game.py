
from random import randint

game_running = True
game_results = []

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def games_ends(thewinnergame):
    print (f'{thewinnergame} ganhou o jogo')

while game_running == True:
    counter = 0

    new_round = True
    player = {'name': 'Manuel', 'attack': 10, 'heal':16, 'health': 100}
    
    monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 20,  'health': 100}
    print(calculate_monster_attack(monster['attack_min'], monster['attack_max']))
    print('Entre o nome do Jogador? ')

    print('---' * 7)
    player['name'] = input()
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')


    while new_round == True:
        counter = counter + 1
        player_won = False
        monster_won = False

        print('Por favor escolhe uma opçao')
        print ('1) Atacar')
        print('2) Curar')
        print ('3) Sair')
        print ('4) Resultados')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                
                
                if player['health'] <= 0:
                    monster_won = True


      
        elif player_choice == '2':
            player['health'] = player['health'] + player['health']

            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])

            if player['health'] <= 0:
                monster_won = True


        elif player_choice == '3':
            new_round = False
            game_running = False
        
        elif player_choice == '4':
            for item in game_results:
                print(item)

        else:
            print('Escolha errada')

        if player_won == False and monster_won == False:
            print(player['name'] + ' tem ' + str(player['health']))
            print(monster['name'] + ' tem ' + str(monster['health']))

        elif  player_won:
            games_ends(player['name'])
            round_result = {'name': player['name'], 'Saude': player['health'], 'voltas: ': counter}
            game_results.append(round_result)
            
            new_round = False

        elif monster_won:
            games_ends(monster['name'])
            round_result = {'name': monster['name'], 'Saude': monster['health'], 'voltas: ': counter}
            game_results.append(round_result)
            new_round = False

