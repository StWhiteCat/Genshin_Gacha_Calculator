import random
choushu = 348   #现有抽数
baodi = 27   #现有保底
dabaodi =  1  #是不是大保底(是则为1，否则为0.5)
mubiao = 5   #目标UP五星数
cishu = 100000   #世界线测试次数
gailv = 0.006
five_number = 0
chouka = 0
upchara = 0
heji = 0
choukaheji = 0
ii = baodi
upcharaheji = 0
unupcharaheji = 0
if dabaodi == 1:
    haha = "是"
else:
    haha = "不是"
dadibao = dabaodi
for h in range(cishu):
    while upchara < mubiao:
        baodi += 1
        if baodi > 73:
            gailv = min(1,gailv+0.06)
        ram = random.uniform(0,1)
        if ram <= gailv:
            chouka += 1
            five_number += 1
            gailv = 0.006
            baodi = 0
            nim = random.uniform(0,1)
            if nim <= dadibao:
                dadibao = 0.5
                upchara += 1
                upcharaheji += 1

            else:
                dadibao = 1
                unupcharaheji += 1
        else:
            chouka += 1
    yuanshi = (chouka - choushu - ii) * 160
    kejin = max((yuanshi * 648 / 8080),0)
    heji = heji + kejin
    choukaheji = choukaheji + chouka
    chouka = 0
    upchara = 0
    dadibao = dabaodi
    baodi = ii
chulv = choukaheji / cishu / mubiao
pingjun = heji / cishu
wailv = upcharaheji / (upcharaheji+unupcharaheji)
print(f"当前现有抽数为{choushu}抽，现有保底数为{ii}抽，{haha}大保底。目标UP五星数为{mubiao}个，世界线重置了{cishu}次，平均UP五星期望为{chulv}抽,平均UP五星占五星角色的{wailv}，平均需要氪{pingjun}块钱。")


