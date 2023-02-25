#import
import os
import sys
import glob
import time
#変数

class CAudacity(object):

    ###########################################
    # 機能	：コンストラクタ
    ###########################################
    def __init__(self, ):
        self.TONAME = ""
        self.FROMNAME = ""
        self.TOFILE = ""
        self.FROMFILE = ""
        self.EOL = ""
    ###########################################
    # 機能	：名前付きパイプを開始する
    ###########################################
    def StartPipe(self, ):
        if sys.platform == 'win32':
            self.TONAME = '\\\\.\\pipe\\ToSrvPipe'
            self.FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
            self.EOL = '\r\n\0'
        else:
            self.TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
            self.FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
            self.EOL = '\n'
        self.TOFILE = open(self.TONAME, 'w')
        self.FROMFILE = open(self.FROMNAME, 'rt')

    ###########################################
    # 機能	：名前付きパイプを開始する
    ###########################################
    def QuitPipe(self, ):
        self.TOFILE.close()
        self.FROMFILE.close()

    ###########################################
    # 機能	：コマンドを送る
    ###########################################
    def send_command(self, command):
        self.TOFILE.write(command + self.EOL)
        self.TOFILE.flush()

    ###########################################
    # 機能	：コマンドを取得する
    ###########################################
    def get_response(self, ):
        result = ''
        line = ''
        while True:
            result += line
            line = self.FROMFILE.readline()
            if line == '\n' and len(result) > 0:
                break
        return result

    ###########################################
    # 機能	：コマンドを実行する
    ###########################################
    def do_command(self, command):
        self.send_command(command)
        response = self.get_response()
        return response
    
    ###########################################
    # 機能	：コマンドを実行する
    ###########################################
    def do_command_Export2(self, ):
        self.do_command('Export2:')


###########################################
#引用1
#@mimuro_syunya, "PythonのSeleniumを使って、起動済みのブラウザを操作する。", qiita, https://qiita.com/mimuro_syunya/items/2464cd2404b67ea5da56 (閲覧：2022年01月09日)
#引用2
#Octopus Data Inc., "XPathとは？基本概念や書き方をわかりやすく解説！", octoparse, https://www.octoparse.jp/blog/xpath-introduction/#%EF%BD%82 (閲覧：2022年01月09日)
#引用3
#spatel4140, "Wait for Download to finish in selenium webdriver JAVA", Stack Exchange Inc, https://stackoverflow.com/questions/22714112/wait-for-download-to-finish-in-selenium-webdriver-java (閲覧：2022年01月09日)
###########################################