class Account:
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    # Q2: Retirement
    def time_to_retire(self, amount):
        years = 0
        while self.balance < amount:
            self.balance = self.balance + (self.balance * self.interest)
            years = years + 1
        return years


# Q3: FreeChecking
class FreeChecking(Account):
    withdraw_fee = 1
    free_withdrawals = 2

    def withdraw(self, amount):
        if self.free_withdrawals > 0:
            self.balance = self.balance - self.withdraw_fee
            self.free_withdrawals -= 1
            super().withdraw(amount)
        else:
            super().withdraw(amount + 1)


# Q4: Making Cards
class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, opponent_card):
        return self.attack - opponent_card.defense

    def copy(self):
        return Card(self.name, self.attack, self.defense)


# Q5: Making a Player
class Player:
    def __init__(self, deck, name):
        self.deck = deck
        self.name = name
        self.hand = []

    def draw(self):
        card = self.deck.draw()
        self.hand.append(card)


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def draw(self):
        card = self.cards.pop()
        return card

    def play(self, index):
        return self.cards.pop(index)


# Q6: AIs: Resourceful Resources
class AICard(Card):
    cardtype = 'AI'

    def __init__(self, name, attack, defense):
        super(AICard, self).__init__(name, attack, defense)

    def effect(self, opponent_card, player, opponent):
        implemented = False
        if self.name == 'AICard':
            for i in range(2):
                player.draw()
            implemented = True
        if implemented:
            print(f"{self.name} allows me to draw two cards!")


# Q7: Tutors: Sneaky Search
class TutorCard(Card):
    cardtype = 'TUTOR'

    def __init__(self, name, attack, defense):
        super(TutorCard, self).__init__(name, attack, defense)

    def effect(self, opponent_card, player, opponent):
        added = False
        if self.name == 'TutorCard' and player.deck.cards:
            added = True
            player.hand.append(player.deck.cards[0])
        if added:
            print(f"{self.name} allows me to add a copy of a card to my hand!")


# Q8: TAs: Power Transfer
class TACard(Card):
    cardtype = 'TA'

    def effect(self, opponent_card, player, opponent, arg=None):
        best_card = None
        if player.hand == 'TACard' and player.hand:
            for i in player.hand:
                best_card = max(player.hand, key=lambda card: card.attack)
                self.attack += best_card.attack
                player.hand.remove(best_card)
        if best_card:
            print(f"{self.name} discards {best_card.name} from my hand to increase its own power!")


# Q9: Instructors: Immovable
class InstructorCard(Card):
    cardtype = 'Instructor'

    def effect(self, opponent_card, player, opponent, arg=None):
        re_add = False
        if self.name == 'InstructorCard':
            self.defense -= 1000
            self.attack -= 1000
            if self.attack >= 0 or self.defense >= 0:
                player.hand.append(self)
                re_add = True
            if re_add:
                print(f"{self.name} returns to my hand!")
