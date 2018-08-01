person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {i[0]: i[1] for i in person}


# ALTERNATIVE SOLUTION 1
# answer = {k: v for k, v in person}
#
# ALTERNATIVE SOLUTION 2
# answer = dict(person)


print(answer)
