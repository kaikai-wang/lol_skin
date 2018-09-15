#!usr/bin/python3
# _*_ coding: utf-8 _*_
import requests
import json
import os

main_dir = 'G:\\lol_skin\\'
if os.path.exists(main_dir):
    os.mkdir(main_dir)


class Hero:
    def __init__(self, name):
        self.name = name
        self.hero_dir = main_dir + name
        self.cname = ''

    def makedir(self):
        os.mkdir(self.hero_dir)


class Skin:
    def __init__(self, id):
        self.id = id
        self.url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'.format(id)

    def download(self, dir_name):
        res = requests.get(self.url)
        f = open(dir_name, 'wb')
        f.write(res.content)
        f.close()


def get_names():  # 获取所有英雄名字
    url = 'http://lol.qq.com/biz/hero/champion.js'
    res = requests.get(url)
    t = res.text.split('=', 2)[2][:-1]
    names = json.loads(t)['keys']
    names = list(names.values())
    print('获取所有英雄名称...')
    print(names)
    return names


def get_skins(name='Aatrox'):  # 通过英雄名找到该英雄的皮肤列表
    url = 'http://lol.qq.com/biz/hero/{}.js'.format(name)
    res = requests.get(url)
    t = res.text.split('=', 2)[2][:-1]
    hero_info = json.loads(t)
    print('获取{}的所有皮肤...'.format(name))
    return hero_info['data']['skins']


def main():
    names = get_names()
    for hero_name in names:
        hero = Hero(hero_name)
        hero.makedir()
        skins = get_skins(hero_name)
        for skin in skins:
            skin_id = skin['id']
            skin_name = skin['name']
            dir_name = '{}\\{}.jpg'.format(hero.hero_dir, skin_name)
            this_skin = Skin(skin_id)
            this_skin.download(dir_name)
    print('-'*20)
    print('所有皮肤图片获取完毕！')
    print('请到 {} 文件夹下查看'.format(main_dir))


main()
