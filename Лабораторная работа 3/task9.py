salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(months):
    if i < 1:
        delta = spend - salary
        money_capital += delta  # TODO Оформить решение
    else:
        spend *= 1 + increase
        delta = spend - salary
        money_capital += delta

print(round(money_capital))
