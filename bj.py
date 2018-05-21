# -*- coding: utf-8 -*-
#練習用プログラム　ブラックジャックゲームの作成

import random
import sys

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

    def getPointMessage(self):
        totalPoint = self.getPoint()
        print("カードの合計値は" + str(totalPoint) + "になりました\r\n")

    def drawMessage(self,drawcard):
        pass

# プレイヤークラス
class player(playerBase):
    def drawMessage(self,drawcard):
        print(drawcard.getmark() + "の" + drawcard.getpict() + "を引きました")

# ディーラークラス
class dealer(playerBase):
    def drawMessage(self,drawcard):
        print("ディーラーは" + drawcard.getmark() + "の" + drawcard.getpict() + "を引きました")

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
    # １枚目ドロー
    newcard = myDeck.draw()
    pl.drawMessage(newcard)
    pl.tefuda.append(newcard)
    # ２枚目ドロー
    newcard = myDeck.draw()
    pl.drawMessage(newcard)
    pl.tefuda.append(newcard)
    pl.getPointMessage()
    
    # ディーラー初期セット
    # １枚目ドロー
    newcard = myDeck.draw()
    dl.drawMessage(newcard)
    dl.tefuda.append(newcard)
    # ２枚目ドロー
    newcard = myDeck.draw()
    print("ディーラーはもう１枚のカードを引きました\r\n")
    dl.tefuda.append(newcard)
    
    while True:
        print("カードを引きますか？[y/n]")
        ans = input()
        if ans == "n":
            # スタンド
            print("スタンド！")
            break
        elif ans == "y":
            # ヒット
            print("ヒット！")
            newcard = myDeck.draw()
            pl.drawMessage(newcard)
            pl.getPointMessage()
            if pl.getPoint() > 21:
                # バスト！！
                print("バスト！！あなたの負けです\r\n")
                sys.exit()
            elif pl.getPoint() == 21:
                # ブラックジャック！
                print("ブラックジャックです\r\n")
                break

    print("ディーラーのターンです")
    derlerPoint = dl.getPoint()
    print("ディーラーのホールカードオープン\r\nカード合計値は" + str(derlerPoint) + "です")
    while True:
        if derlerPoint >= 17:
            print("ディーラーはカードを引き終わりました\r\n")
            break
        else:
            newcard = myDeck.draw()
            dl.drawMessage(newcard)
            dl.tefuda.append(newcard)
            derlerPoint = dl.getPoint()

    print("勝負！\r\n")

    print("プレイヤー[" + str(pl.getPoint()) + "] vs [" + str(dl.getPoint()) + "]ディーラー" )

    if pl.getPoint() == dl.getPoint():
        # ドロー
        print("ドロー！引き分けです")
    elif dl.getPoint() > 21 or pl.getPoint() > dl.getPoint():
        # プレイヤーＷＩＮ
        print("あなたの勝ちです！")
    else:
        # プレイヤーＬＯＳＥ
        print("あなたの負けです")

    print("ゲームを終了します")

    
    


# メイン処理起動
if __name__ == "__main__":
    main()
