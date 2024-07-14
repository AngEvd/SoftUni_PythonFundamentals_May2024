def main():
    tickets = [ticket.strip() for ticket in input().split(", ")]

    for ticket in tickets:
        print(check_ticket(ticket))


def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ("@", "#", "$", "^")
    left_side = ticket[:10]
    right_side = ticket[10:]
    for symbol in winning_symbols:
        for appearance in range(10, 5, -1):
            symbol_repetition = appearance * symbol
            if symbol_repetition in left_side and symbol_repetition in right_side:
                if appearance == 10:
                    return f"ticket \"{ticket}\" - {appearance}{symbol} Jackpot!"

                return f"ticket \"{ticket}\" - {appearance}{symbol}"

    return f"ticket \"{ticket}\" - no match"
