def card(credit_card_number: str) -> str:
    credit_card_number = list(credit_card_number)
    for i in range(len(credit_card_number) - 4):
        credit_card_number[i] = "*"
    return ''.join(credit_card_number)


credit_card_number = input("Введите номер кредитной карты ")
print(f"Hомер карты защищен: {card(credit_card_number)}")