import requests as req
import json
import time
import random


def main(jwt):
    head = {
        'Authorization': 'Bearer' + jwt,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    resp = req.get('https://game-domain.blum.codes/api/v1/user/balance', headers=head)
    count = json.loads(resp.text)['playPasses']
    total_point = 0
    if count != 0:
        print("Начал играть...")
        for i in range(count):
            head = {
                'Authorization': 'Bearer' + jwt,
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
            }
            post_id = req.post('https://game-domain.blum.codes/api/v1/game/play', headers=head)
            id = json.loads(post_id.text)['gameId']
            time.sleep(random.randrange(30, 60, 5))
            points = random.randint(150, 250)
            endGame = req.post('https://game-domain.blum.codes/api/v1/game/claim', headers=head, json={
                "gameId": id, "points": points})
            print(str(i + 1) + ' / ' + str(count) + " игр")
            time.sleep(random.randint(1, 5))
            total_point += points
        print("Всего зафармленно поинтов:", total_point)
    else:
        print("Нету кристалов для игры :(")
        exit()

if __name__ == '__main__':
    jwt = input("Введите Bearer токен: ")
    main(jwt)
