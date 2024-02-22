##ev3の動作確認後
##__init__でできる範囲ならそこで定義
##規模大きかったら別でクラス化

class LegoController():
    def __init__(self):
        #ev3動くように定義
        #self.ev3 = ev3()
        return


    def candy():
        #lego動作記述
        print("act candy move!!(^-^)")
        return

    def stick():
        #lego動作記述
        print("act stick move!!(>_<)")
        return
    
    def decide_action(self,status):
        if status == 0:
            self.candy()
        elif status == 1:
            self.stick()
        return 0
