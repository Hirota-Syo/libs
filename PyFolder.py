#import
import os
from os import listdir
from os.path import isfile, join

#変数

class CFolder(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        #入出力ディレクトリ
        self.strInDir = os.getcwd( ) + "/input/"
        self.strPrcsDir = os.getcwd( ) + "/process/"
        self.strOutDir = os.getcwd( ) + "/output/"

    ############################################
    ## 機能	：入力ファイル名リストを取得
    ############################################
    def GetInFiles(self, ):
        strInFiles = [f for f in listdir(self.strInDir) if isfile(join(self.strInDir, f))]
        strInFiles = [os.path.splitext(x)[0] for x in strInFiles]
        return strInFiles


###########################################
#引用1
###########################################
