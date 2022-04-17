from itertools import cycle

import pandas as pd
from faker import Faker

Faker.seed(1)
fake = Faker()

dates = [fake.date_this_year().strftime('%m/%d/%Y') for _ in range(60)]
costs = [fake.pricetag() for _ in range(60)]
utility_names = cycle('electric water internet phones gas'.split())
utilities = [next(utility_names) for _ in range(60)]

data = {
    'date': sorted(dates),
    'utility': utilities,
    'amount': costs,
}
df = pd.DataFrame(data)
df.head()
df.to_csv('utilities.csv', index=False)
