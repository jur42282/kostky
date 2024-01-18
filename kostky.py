import random as rd

score_limit = int(input("Zadej max. skóre: "))
u_input = "null"
score = 0
while score < score_limit and u_input != "end":
    u_input = str(input("Zmáčkni enter pro hod kostkou, pro ukončení napiš end\n"))
    nums = []
    for i in range(1, 7):
        
        num = rd.randint(1,6)
        print(f"Kostka {i}: {num}")
        nums.append(num)

    # logika sčítání skóre
    for i in range(1, 7):
        score_calc = nums.count(i)
        if i == 1:
            if score_calc >= 3:
                score += 1000 * (2 ** (score_calc - 3))
            else:
                score += 100 * score_calc
        elif i == 5:
            if score_calc >= 3:
                score += 500 * (2 ** (score_calc - 3))
            else:
                score += 50 * score_calc
        elif score_calc >= 3:
            score += i * 100 * (2 ** (score_calc - 3))

    # 3 páry
    pairs = [nums.count(i) for i in set(nums) if nums.count(i) == 2]
    if len(pairs) == 3:
        score += 1000

    # postupka
    if sorted(nums) == list(range(1, 7)):
        score += 1500

    print(f"Aktuální skóre: {score}")
    
    if score == score_limit:
        print("Vyhrál jsi!")
        break