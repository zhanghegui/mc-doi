import os
sets_to_copy_path = '/nfs/maciej/mcdoi/paper/estimated_cc+a'

with open('/nfs/maciej/mcdoi/paper/independent-cascade/predicted','r',encoding='utf-8') as f:
    predicted = f.readlines()

with open(sets_to_copy_path, 'r', encoding='utf-8') as f:
    sets = f.readlines()

new_sets = []
for path in sets:
    if path not in predicted:
        with open('/nfs/maciej/mcdoi/paper/independent-cascade/predicted', 'a', encoding='utf-8') as f:
            f.write(path)
    new_path = path.split('/')
    new_path[4] = 'independent-cascade'
    new_path = '/' + os.path.join(*new_path)
    new_sets.append(new_path)

for path in new_sets:
    new_path = path.split('/')
    new_path[4] = 'paper/independent-cascade'
    new_path = '/' + os.path.join(*new_path)
    os.makedirs(new_path[:-1],exist_ok=True)
    os.system('sudo cp -r '+path[:-1]+'/* '+new_path[:-1]+'/')

