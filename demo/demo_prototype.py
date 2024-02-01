from client.ufc_betting.ufc_betting import UFCBetting
from client.ufc_betting.fighter import Fighter
from client.ufc_betting.fight import Fight
from client.ufc_betting.bet import Bet
from client.ufc_betting.weight_class import WeightClass
from datetime import date

if __name__ == '__main__':

    # Create instances of your classes

    weight_class = WeightClass(code=1, weight='Lightweight')

    fighter = Fighter(code=101, name='John Doe', height=180.0, reach=74.0, stance='Orthodox')

    fight = Fight(code=201, referee='Ref Name', location='Las Vegas', fight_date='2021-03-20',
                  age_rc=30, weight_rc=155.0, win_streak_rc=5, wins_rc=10, losses_rc=2,
                  age_bc=28, weight_bc=155.0, win_streak_bc=3, wins_bc=8, losses_bc=3,
                  weight_class_code=1, fighter_rc_code=1, fighter_bc_code=2, winner='Red')

    bet = Bet(amount=100.0, date_bet='2021-03-20', fight_id=201, winner='Red')

    print("== Displaying Weight Class ==")
    print(weight_class)

    print("\n== Displaying Fighter Information ==")
    print(fighter)

    print("\n== Displaying Fight Information ==")
    print(fight)

    print("\n== Displaying Bet Information ==")
    print(bet)

    # print("\n== Fetching All Fights (First 10) ==")
    # fights = UFCBetting.get_all_fights()
    # for f in fights[:10]:
    #     print(f)

    print("\n== Fetching Fights by Date (First 3) ==")
    fights_by_date = UFCBetting.get_fights_by_date('2021-03-20')
    for f in fights_by_date[:3]:
        print(f)

    print("\n== Fetching Fights by Location (First 3) ==")
    fights_by_location = UFCBetting.get_fights_by_location('Albany, New York, USA')
    for f in fights_by_location[:3]:
        print(f)

    print("\n== Fetching Fight by ID ==")
    specific_fight = UFCBetting.get_fight_by_id(201)
    print(specific_fight)

    print("\n== Adding a Fight ==")
    success = UFCBetting.add_fight(fight)
    if success:
        print(f'Fight: {fight} added successfully')

    print("\n== Fetching All Fighters (First 3) ==")
    fighters = UFCBetting.get_all_fighters()
    for f in fighters[:3]:
        print(f)

    print("\n== Adding a Fighter ==")
    success = UFCBetting.add_fighter(fighter)
    if success:
        print(f'Fighter: {fighter} added successfully')

    print("\n== Fetching Fighters by Name ==")
    fighters_by_name = UFCBetting.get_fighters_by_name('John Doe')
    for f in fighters_by_name:
        print(f)

    print("\n== Fetching Fighters by Stance (First 3) ==")
    fighters_by_stance = UFCBetting.get_fighters_by_stance('Orthodox')
    for f in fighters_by_stance[:3]:
        print(f)

    print("\n== Placing a Bet ==")
    success = UFCBetting.place_bet(bet)
    if success:
        print(f'Bet: {bet} added successfully')

    print("\n== Printing all Bets ==")
    bets = UFCBetting.get_all_bets()
    for bet in bets:
        print(bet)

    print("\n== Changing Bet amount and winner ==")
    bet.winner = 'Blue'
    bet.amount = 69
    print(bet)

    print("\n==Testing change")
    bets = UFCBetting.get_all_bets()
    for bet in bets:
        print(bet)

    print("\n== Ending Event and Calculating Results ==")
    success = UFCBetting.end_event()
    if success:
        print('Event ended successfully')

    print("\n== Printing all Bets ==")
    bets = UFCBetting.get_all_bets()
    for bet in bets:
        print(bet)

    print("\n== Deleting a Fighter ==")
    UFCBetting.delete_fighter(fighter)
