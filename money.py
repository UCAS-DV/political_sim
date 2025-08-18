def update_balance(country, income_sources, expenses):
    for source in income_sources:
        country.balance += source
    for expense in expenses:
        country.balance -= source