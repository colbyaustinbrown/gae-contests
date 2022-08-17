cases = int(input())

for case_number in range(0, cases):
    n = int(input())
    votes = {}
    for i in range(0, n):
        name = input()
        if name == "abstain": continue
        if not name in votes:
            votes[name] = 0
        votes[name] = votes[name] + 1

    max_votes = 0
    max_name = ""
    for k in votes:
        if votes[k] == max_votes:
            max_name = None
        elif votes[k] > max_votes:
            max_votes = votes[k]
            max_name = k
    if max_votes == 0:
        print("No accusations.")
    elif max_name == None:
        print("Tie!")
    else:
        print(max_name + " is the pretender!")
