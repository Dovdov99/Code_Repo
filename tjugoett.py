import random
import pyinputplus as pyip #type: ignore

class Cards:
    def __init__(self,) -> None:
        self.num_of_card: list = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king'] #lista med alla kort.
        self.allcards = self.num_of_card * 4 #multiplicera listan för att ha fyra av varje kort.
        self.hand: list = [] #skapa en tom lista som representerar spelarens hand.

    def shuffle_cards(self):
        return random.shuffle(self.allcards) #blanda alla värden i listan med alla kort.

    def give_cards(self):
        self.hand.append(random.choice(self.allcards)) #ta en kort från listan med alla kort och lägg till det kortet till spelarens hand.
        return self.hand
    
    def calculate_hand(self): #funktion för att räkna ut poäng varje kort. Returnera sedan total poäng efter uträkning.
        self.total_points = 0
        for card in self.hand:
            if card in ('jack', 'queen', 'king'):
                self.total_points += 10
            elif card == 'ace' and self.total_points <= 7:
                    self.total_points += 14
            elif card == 'ace' and self.total_points > 7:
                    self.total_points += 1
            else:
                self.total_points += card
        return self.total_points

    
class Player:
    def __init__(self) -> None:
        self.card_instance = Cards() #anropar Cards klassen för att kunna använda mig av metoder och atribut.
        self.computer_instance = Computer() #anropar Computer klassen för att kunna använda mig av metoder och atribut.
        

    def player_turn(self): #metod som ger kort, räknar ut poäng, printar kort samt poäng och sedan kör en metod som överlåter turen till datorn.
        self.card_instance.give_cards()
        self.card_instance.calculate_hand()
        print('\nYour first given card is:', self.card_instance.hand, '\ntotal points:', self.card_instance.total_points)
        self.computer_instance.computer_turn()


        while True: #loop för att kunna forsätta fråga spelaren ifall de vill ha ett till kort. i denna loop som kommer det kontrolleras om någon av datorn eller spelaren vinner /
            # efter varje draget kort.
            another_card = pyip.inputYesNo('\nWould you like to take another card? (Yes/No): ')
            if another_card == 'yes' or another_card == 'y':
                self.card_instance.give_cards()
                self.card_instance.calculate_hand()
                print('\nYour hand:', self.card_instance.hand, '\ntotal points:', self.card_instance.total_points)
                self.computer_instance.computer_turn()
                self.check_winner()


            elif another_card == 'no' or another_card == 'n': #ifall spelaren inte tar ett till kort så kommer det bli datorns tur. När datorn slutar ta kort så kontrolleras /
                # dessa vilkor för att se vem som vunnit.
                self.computer_instance.computer_turn()
                if self.card_instance.total_points > self.computer_instance.card_instance.total_points:
                    print('------------------------------------------')
                    print(f'FINAL SCORE:', 'Player points:', self.card_instance.total_points, 'Computer points:' ,self.computer_instance.card_instance.total_points)
                    print('\nPlayer wins!')
                    raise Exception() #denna kod är till för att hoppa ur ALL kod och gå tillbaka till huvudkoden. Har jag inte denna kod så kommer loopen forsätta /
                # och spelaren kommer bli tillfrågad om de vill ha ett till kort fast spelet är slut.
                
                elif self.card_instance.total_points < self.computer_instance.card_instance.total_points and  self.computer_instance.card_instance.total_points <= 21:
                    print('------------------------------------------')
                    print(f'FINAL SCORE:', 'Player points:', self.card_instance.total_points, 'Computer points:' ,self.computer_instance.card_instance.total_points)
                    print('\nComputer wins!')
                    raise Exception()
                break
            
    def check_winner(self): #metod för att kontrollera vinnaren.
        player_points = self.card_instance.total_points
        computer_points = self.computer_instance.card_instance.total_points
        

        if player_points > 21:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nPlayer busted... Computer wins!')
            raise Exception()

        elif computer_points > 21:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nComputer busted... Player wins!')
            raise Exception()

        elif player_points == 21 and computer_points != 21:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nPlayer Wins!')
            raise Exception()

        elif computer_points == 21 and player_points != 21:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nComputer Wins!')
            raise Exception()

        elif computer_points == 17 and player_points > computer_points:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nPlayer wins!')
            raise Exception()
        elif computer_points == 17 and player_points < 17:
            self.player_turn()
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nComputer wins!')
            raise Exception()

        elif computer_points == player_points:
            print('------------------------------------------')
            print(f'FINAL SCORE:', 'Player points:', player_points, 'Computer points:' , computer_points)
            print('\nIts a tie!')
            raise Exception()


class Computer:
    def __init__(self) -> None:
        self.card_instance = Cards() #anropar Cards klassen för att kunna använda mig av metoder och atribut.


    def computer_turn(self): #denna metod är för att fortsätta ge datorn kort fram tills att de har 17 poäng, efter det så slutar datorn ta kort.
            self.card_instance.calculate_hand()
            while self.card_instance.total_points < 17:
                self.card_instance.give_cards()
                self.card_instance.calculate_hand()
                print('\nComputers drew a card. Comupters hand is:', self.card_instance.hand, '\ntotal points:', self.card_instance.total_points)
                

                if self.card_instance.total_points > 17:
                    print('\nComputer cant take anymore cards. Final points', self.card_instance.total_points)
                break    
            return

#huvudkod
print('Welcome to Tjugoett!\n')
game_starter = pyip.inputChoice(['', 'exit'], blank=True, prompt='To start press enter / To quit type exit\ninput: ') #ge användaren alternativet att spela eller inte.
if game_starter == 'exit':
    exit()

while True: #loop som gör det möjligt för spelaren att spela flera gånger.
    try:
        start_game = Player()
        start_game.player_turn()
    except Exception as e: #denna del är kod som kommer köras när något av vinnar vilkoren körs för att hoppa ur alla köade metoder och loopar. Game is over kommer printas.
        print(f"\nGame is over! {e}")
        play_again = pyip.inputStr(prompt='To play again press enter / To quit type exit: ', blank=True)
        if play_again == '':
            continue
        else:
            break
   
