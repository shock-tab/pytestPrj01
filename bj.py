# -*- coding: utf-8 -*-
#練習用プログラム　ブラックジャックゲームの作成

import random

# プレイヤーベースクラス
class playerBase:
    tefuda = []

    def getPoint(self):
        total = 0
        if len(self.tefuda) > 0:
            for cards in self.tefuda:
                total += cards.getnum()
            return total
        else:
            return total

# プレイヤークラス
class player(playerBase):
    pass

# ディーラークラス
class dealer(playerBase):
    pass

# デッキクラス
class deck:
    yamafuda = []
    # コンストラクタ
    def __init__(self):
        self.createDeck()
    # デッキ作成/初期化
    def createDeck(self):
        marks = ["ダイヤ","ハート","スペード","クラブ"]
        pictures = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
        numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10]

        for mark in marks:
            for i in range(13):
                cardstatus = card()
                cardstatus.setmark(mark)
                cardstatus.setpict(pictures[i])
                cardstatus.setnum(numbers[i])
                self.yamafuda.append(cardstatus)

        random.shuffle(self.yamafuda)
    # カードを引く
    def draw(self):
        if len(self.yamafuda) >= 1:
            drawcard = self.yamafuda.pop(0)
            return drawcard
        else:
            emptycard = card()
            return emptycard

# カードクラス
class card:
    
    def getmark(self): return self._mark  
    def setmark(self, value): self._mark = value  
    def delmark(self): del self._mark  
    mark = property(getmark, setmark, delmark, "I'm the 'mark' property.") 

    def getpict(self): return self._pict  
    def setpict(self, value): self._pict = value  
    def delpict(self): del self._pict  
    pict = property(getpict, setpict, delpict, "I'm the 'pict' property.") 

    def getnum(self): return self._num  
    def setnum(self, value): self._num = value  
    def delnum(self): del self._num  
    num = property(getnum, setnum, delnum, "I'm the 'num' property.") 

    
# メイン処理
def main():
    # 初期化
    myDeck = deck()
    pl = player()
    dl = dealer()

    print("ブラックジャックゲームを開始します\r\n")

    # プレイヤー初期セット
    newcard = myDeck.draw()
    print(newcard.getmark() + "の" + newcard.getpict() + "を引きました")
    pl.tefuda.append(newcard)
    newcard = myDeck.draw()
    print(newcard.getmark() + "の" + newcard.getpict() + "を引きました")
    pl.tefuda.append(newcard)
    print("カードの合計値は" + str(pl.getPoint()) + "になりました\r\n")
    
    # ディーラー初期セット
    newcard = myDeck.draw()
    print("ディーラーは" + newcard.getmark() + "の" + newcard.getpict() + "を引きました")
    dl.tefuda.append(newcard)
    newcard = myDeck.draw()
    print("ディーラーはもう１枚のカードを引きました\r\n")
    dl.tefuda.append(newcard)
    
    print("カードを引きますか？[y/n]")
    while True:
        ans = input()
        if ans == "n":
            break
        elif ans == "y":
            newcard = myDeck.draw()

    
    


# メイン処理起動
if __name__ == "__main__":
    main()
