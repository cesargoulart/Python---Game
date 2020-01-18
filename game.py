

game_running = True


while game_running == True:
    new_round = True
    player = {'name': 'Manuel', 'attack': 10, 'heal':16, 'health': 100}
    monster = {'name': 'Max', 'attack': 12, 'health': 100}
    print('Entre o nome do Jogador? ')

    print('---' * 7)
    player['name'] = input()
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')


    while new_round == True:

        player_won = False
        monster_won = False

        print('Por favor escolhe uma opçao')
        print ('1) Attack')
        print('2) Heal')
        print ('3) Sair')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True


      
        elif player_choice == '2':
            player['health'] = player['health'] + player['health']

            player['health'] = player['health'] - monster['attack']

            if player['health'] <= 0:
                monster_won = True


        elif player_choice == '3':
            new_round = False
            game_running = False

        else:
            print('Escolha errada')

        if player_won == False and monster_won == False:
            print(player['name'] + ' tem ' + str(player['health']))
            print(monster['name'] + ' tem ' + str(monster['health']))

        elif  player_won:
            print(player['name'] + ' won')
            new_round = False

        elif monster_won:
            print('The monster won')
            new_round = False

            

        if player_won == True or monster_won == True:
            game_running = False