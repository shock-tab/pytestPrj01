# -*- coding: utf-8 -*-
#練習用プログラム　ブラックジャックゲームの作成

import random
import sys
import time

BLACK_JACK = 21
DEALER_UNDER_LIMIT = 17

class PlayerBase:
    """プレイヤーベースクラス"""

    def __init__(self):
        self.tefuda = []

    def get_point(self):
        """手札合計値を取得"""
        total = 0
        if len(self.tefuda) > 0:
            for cards in self.tefuda:
                total += cards.get_num()
            return total
        else:
            return total

    def get_pointmessage(self):
        """プレイヤーの手札合計値のメッセージを取得"""
        total_point = self.get_point()
        print("カードの合計値は" + str(total_point) + "になりました\r\n")
        stop()

    def draw_message(self, drawcard):
        """山札からドローする時のメッセージ取得"""

class Player(PlayerBase):
    """プレイヤークラス"""

    def __init__(self):
        super().__init__()

    def draw_message(self, drawcard):
        print(drawcard.get_mark() + "の" + drawcard.get_pict() + "を引きました")
        stop()

class Dealer(PlayerBase):
    """ディーラークラス"""

    def __init__(self):
        super().__init__()

    def draw_message(self, drawcard):
        print("ディーラーは" + drawcard.get_mark() + "の" + drawcard.get_pict() + "を引きました")
        stop()

class Deck:
    """デッキクラス"""
    yamafuda = []

    def __init__(self):
        """コンストラクタ"""
        self.create_deck()

    def create_deck(self):
        """デッキ作成&初期化"""
        marks = ["ダイヤ", "ハート", "スペード", "クラブ"]
        pictures = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        for mark in marks:
            for i in range(13):
                cardstatus = Card()
                cardstatus.set_mark(mark)
                cardstatus.set_pict(pictures[i])
                cardstatus.set_num(numbers[i])
                self.yamafuda.append(cardstatus)

        random.shuffle(self.yamafuda)

    def draw(self):
        """カードを引く"""
        if len(self.yamafuda) >= 1:
            drawcard = self.yamafuda.pop(0)
            return drawcard
        else:
            emptycard = Card()
            return emptycard

class Card:
    """カードクラス"""

    def __init__(self):
        self._mark = ""
        self._pict = ""
        self._num = 0

    def get_mark(self): return self._mark
    def set_mark(self, value): self._mark = value
    def del_mark(self): del self._mark
    mark = property(get_mark, set_mark, del_mark, "I'm the 'mark' property.")

    def get_pict(self): return self._pict
    def set_pict(self, value): self._pict = value
    def del_pict(self): del self._pict
    pict = property(get_pict, set_pict, del_pict, "I'm the 'pict' property.")

    def get_num(self): return self._num
    def set_num(self, value): self._num = value
    def del_num(self): del self._num
    num = property(get_num, set_num, del_num, "I'm the 'num' property.")

def main():
    """メイン処理"""

    # 初期化
    my_deck = Deck()
    plr = Player()
    dlr = Dealer()

    # プレイヤー初期セット
    # １枚目ドロー
    newcard = my_deck.draw()
    plr.draw_message(newcard)
    plr.tefuda.append(newcard)
    # ２枚目ドロー
    newcard = my_deck.draw()
    plr.draw_message(newcard)
    plr.tefuda.append(newcard)
    plr.get_pointmessage()

    # ディーラー初期セット
    # １枚目ドロー
    newcard = my_deck.draw()
    dlr.draw_message(newcard)
    dlr.tefuda.append(newcard)
    # ２枚目ドロー
    newcard = my_deck.draw()
    print("ディーラーはもう１枚のカードを引きました\r\n")
    dlr.tefuda.append(newcard)

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
            newcard = my_deck.draw()
            plr.draw_message(newcard)
            plr.tefuda.append(newcard)
            plr.get_pointmessage()
            if plr.get_point() > BLACK_JACK:
                # バスト
                print("バスト！！あなたの負けです\r\n")
                sys.exit()
            elif plr.get_point() == BLACK_JACK:
                # ブラックジャック
                print("ブラックジャックです\r\n")
                break

    print("ディーラーのターンです")
    derler_point = dlr.get_point()
    print("ディーラーのホールカードオープン\r\nカード合計値は" + str(derler_point) + "です")
    while True:
        if derler_point >= DEALER_UNDER_LIMIT:
            print("ディーラーはカードを引き終わりました\r\n")
            break
        else:
            newcard = my_deck.draw()
            dlr.draw_message(newcard)
            dlr.tefuda.append(newcard)
            derler_point = dlr.get_point()

    print("勝負！\r\n")
    stop()
    print("プレイヤー[" + str(plr.get_point()) + "] vs [" + str(dlr.get_point()) + "]ディーラー")

    if plr.get_point() == dlr.get_point():
        # ドロー
        print("ドロー！引き分けです\r\n")
    elif dlr.get_point() > BLACK_JACK or plr.get_point() > dlr.get_point():
        # プレイヤーＷＩＮ
        print("あなたの勝ちです！\r\n")
    else:
        # プレイヤーＬＯＳＥ
        print("あなたの負けです\r\n")

def stop():
    """１秒停止"""
    time.sleep(1)

# メイン処理起動
if __name__ == "__main__":

    print("ブラックジャックゲームを開始します[press any key]\r\n")
    input()

    while True:
        main()
        stop()
        print("続けて遊びますか？[y(continue)/anyKey(fin)]")
        if input() != "y":
            break

    print("ゲームを終了します")
