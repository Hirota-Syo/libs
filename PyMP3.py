#import
import pydub
from pydub import AudioSegment

#変数

class CMP3(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        self.value = "Class2Init"
        self.file = None

    ############################################
    ## 機能	：CSVをlistのlistで返す
    ############################################
    def OpenMP3(self, strFile):
        self.file = AudioSegment.from_mp3(strFile)


###########################################
#引用1
#self_development, "PydubによりWAVをMP3に変換する【Python】", ジコログ, https://qiita.com/ikura1/items/17e6dd19f98145afc2eb (閲覧：2022年06月12日)
###########################################
