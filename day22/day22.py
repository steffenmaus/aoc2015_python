with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


# effect: (id, duration_remaining, armor, dmg, mana_regen)
def f(player, enemy, mana_spent, hard):
    player_hp, player_mana, player_effects = player
    enemy_hp, enemy_dmg = enemy

    if hard:
        player_hp -= 1

    if player_hp <= 0:
        return None

    if spent_mana_during_win and mana_spent > min(spent_mana_during_win):
        return None

    next_effects = []
    active_spells_ids = set()
    for e in player_effects:
        if e[1] > 1:
            next_effects.append((e[0], e[1] - 1, e[2], e[3], e[4]))
            active_spells_ids.add(e[0])
        enemy_hp -= e[3]
        player_mana += e[4]

    if enemy_hp <= 0:
        spent_mana_during_win.add(mana_spent)
        return None

    for i, s in enumerate(spells):
        if i not in active_spells_ids:
            if s[0] <= player_mana:
                if s[3] is not None:
                    e = (i, s[3][0], s[3][1], s[3][2], s[3][3])
                    g((player_hp, player_mana - s[0], next_effects + [e]), (enemy_hp, enemy_dmg), mana_spent + s[0],
                      hard)
                else:
                    g((player_hp + s[2], player_mana - s[0], next_effects), (enemy_hp - s[1], enemy_dmg),
                      mana_spent + s[0], hard)

    return None


def g(player, enemy, mana_spent, hard):
    player_hp, player_mana, player_effects = player
    player_armor = 0
    enemy_hp, enemy_dmg = enemy

    if enemy_hp <= 0:
        spent_mana_during_win.add(mana_spent)
        return None

    next_effects = []
    for e in player_effects:
        if e[1] > 1:
            next_effects.append((e[0], e[1] - 1, e[2], e[3], e[4]))
        player_armor += e[2]
        enemy_hp -= e[3]
        player_mana += e[4]

    if enemy_hp <= 0:
        spent_mana_during_win.add(mana_spent)
        return None

    f((player_hp - max(1, enemy_dmg - player_armor), player_mana, next_effects), (enemy_hp, enemy_dmg), mana_spent,
      hard)

    return None


spells = []
# costs, dmg, hp, effect
# effect: duration, armor, dmg ,mana_regen
spells.append((53, 4, 0, None))
spells.append((73, 2, 2, None))
spells.append((113, 0, 0, (6, 7, 0, 0)))
spells.append((173, 0, 0, (6, 0, 3, 0)))
spells.append((229, 0, 0, (5, 0, 0, 101)))

boss_hp = int(lines[0].split(" ")[-1])
boss_dmg = int(lines[1].split(" ")[-1])

enemy = (boss_hp, boss_dmg)
player = (50, 500, [])

spent_mana_during_win = set()
f(player, enemy, 0, False)
p1 = min(spent_mana_during_win)

spent_mana_during_win = set()
f(player, enemy, 0, True)
p2 = min(spent_mana_during_win)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
