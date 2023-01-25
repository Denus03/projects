import random

random.seed()


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} балів.')
        else:
            print(f'Крупє попалась карта {current}. У крупье {score} балів')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Будете брати карту? y/n\n')
            if choice == 'y':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score > 21 or bot_score == 21:
                    print('Вибачте ви програли')
                    break
                elif score == 21 and bot_score == 21:
                    print('нічия')
                elif score == 21 or bot_score > 21:
                    print('Вітаю ви виграли!')
                    break
            elif choice == 'n':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Ви програли, у вас {score} балів, у крупє {bot_score} балів')
                else:
                    print(f'Ви виграли, у вас {score} балів, у крупє {bot_score} балів')

                break

    def start(self):
        random.shuffle(self.deck)
        print('Гра в BlackJack розпочалась')
        print('Мета гри в Блекджек — набрати 21 очко, або суму очок, яка була б ближчою до 21, але не перевищувала б 21.')
        print('В BlackJack десятки, валети, дами і королі коштують по 10 балів.\nТуз може коштувати 1 або 11 балів')
        print('----------------------------------')
        self.choice()

        print('До нових зустрічей!')


game = BlackJack()
game.start()