with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def fight(player, enemy):
    player_hp, player_dmg, player_armor = player
    enemy_hp, enemy_dmg, enemy_armor = enemy
    turn = 0
    while player_hp > 0 and enemy_hp > 0:
        if turn % 2 == 0:
            enemy_hp -= max(1, player_dmg - enemy_armor)
        else:
            player_hp -= max(1, enemy_dmg - player_armor)
        turn += 1
    if player_hp > 0:
        return True
    return False


shop_weapons = []
shop_armor = []
shop_rings = []

shop_weapons.append((8, 4, 0))
shop_weapons.append((10, 5, 0))
shop_weapons.append((25, 6, 0))
shop_weapons.append((40, 7, 0))
shop_weapons.append((74, 8, 0))

shop_armor.append((13, 0, 1))
shop_armor.append((31, 0, 2))
shop_armor.append((53, 0, 3))
shop_armor.append((75, 0, 4))
shop_armor.append((102, 0, 5))
shop_armor.append((0, 0, 0))

shop_rings.append((25, 1, 0))
shop_rings.append((50, 2, 0))
shop_rings.append((100, 3, 0))
shop_rings.append((20, 0, 1))
shop_rings.append((40, 0, 2))
shop_rings.append((80, 0, 3))
shop_rings.append((0, 0, 0))
shop_rings.append((0, 0, 0))

boss_hp = int(lines[0].split(" ")[-1])
boss_dmg = int(lines[1].split(" ")[-1])
boss_armor = int(lines[2].split(" ")[-1])

enemy = (boss_hp, boss_dmg, boss_armor)

winning_costs = set()
losing_costs = set()

for w in shop_weapons:
    for a in shop_armor:
        for i1, r1 in enumerate(shop_rings):
            for i2, r2 in enumerate(shop_rings):
                if i1 != i2:
                    items = [w, a, r1, r2]
                    costs = sum([x[0] for x in items])
                    dmg = sum([x[1] for x in items])
                    armor = sum([x[2] for x in items])
                    if fight((100, dmg, armor), enemy):
                        winning_costs.add(costs)
                    else:
                        losing_costs.add(costs)

p1 = min(winning_costs)
p2 = max(losing_costs)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
