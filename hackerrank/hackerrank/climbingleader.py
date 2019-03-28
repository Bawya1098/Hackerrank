scores = [100, 90, 90, 80, 75, 60]
alice = [50, 65, 77, 90, 102]


def binary_search(scores, alice_score):
    low_index = 0
    high_index = len(scores) - 1
    while low_index < high_index:
        mid_index = int((low_index + high_index) / 2)
        mid_score = scores[mid_index]
        if mid_score > alice_score:
            low_index = mid_index + 1
        elif mid_score < alice_score:
            high_index = mid_index - 1
        else:
            return mid_score
    return scores[low_index]


def climbingLeaderboard(scores, alice):
    rankMap = {}
    rank = 1
    alice_ranks = []
    high_score = scores[0]
    for index in range(0, len(scores)):
        key = scores[index]
        if key not in rankMap.keys():
            rankMap[key] = rank
            rank += 1
    for index in range(0, len(alice)):
        alice_score = alice[index]
        if alice_score > high_score:
            alice_ranks.append(1)
        elif alice_score in rankMap.keys():
            alice_ranks.append(rankMap[alice_score])
        else:
            nearest_score = binary_search(scores, alice_score)
            rank_of_nearest_score = rankMap[nearest_score]
            if nearest_score < alice_score:
                alice_ranks.append(rank_of_nearest_score)
            elif nearest_score > alice_score:
                alice_ranks.append(rank_of_nearest_score + 1)

    return alice_ranks


if __name__ == '__main__':
    result = climbingLeaderboard(scores, alice)
    print(result)
