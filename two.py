import vk_api
import random

GROUP_ID = 202706139
TOKEN = 'b0d92af4223aaa0659a63f7638e34804ad1db6784be516c3e446571ed55b94b31c7d6cfad129f7cbd2454'

stickers = ['53100', '53101', '12985', '53116']


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    while True:
        soo = input()
        vk = vk_session.get_api()
        if soo in stickers:
            vk.messages.send(
                peer_id=2000000002,
                sticker_id=int(soo),
                random_id=random.randint(0, 2 ** 64))
        else:
            vk.messages.send(
                peer_id=2000000002,
                message=soo,
                random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
'''
'''