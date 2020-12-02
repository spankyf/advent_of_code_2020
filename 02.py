import pandas as pd

df = pd.read_csv('02.csv', delim_whitespace=True, header=None)


def bool_password_accepted(row):
    min, max = map(int, row[0].split('-'))
    occurences = row[2].count(row[1].strip(':'))
    if occurences != 0 and occurences >= min and occurences <= max:
        return 1
    else:
        return 0


# ttl = sum(df.apply(bool_password_accepted, axis=1).tolist())
# print(ttl)

#  Part Deux
def format_ind(pos):
    return (int(pos) - 1)


def new_password_check(row):
    pos_one, pos_two = map(format_ind, row[0].split('-'))
    char = row[1].strip(':')
    if sum([row[2][pos_one] == char, row[2][pos_two] == char]) == 1:
        return 1
    else:
        return 0


ttl = sum(df.apply(new_password_check, axis=1).tolist())
print(ttl)
