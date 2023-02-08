def solution(skill, skill_trees):
    error = 0

    for tree in skill_trees:
        c = 0
        for i in tree:
            if c == len(skill):
                break
            prev = skill[c]
            if i in set(skill):
                if i == prev:
                    c += 1
                else:
                    error += 1
                    break
            else:
                continue
    return len(skill_trees) - error