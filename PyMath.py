#import
import matplotlib
import numpy as np
from matplotlib import pyplot
import itertools

#変数
class CMath ( object ):

    ###########################################
    # 機能 ：コンストラクタ
    ###########################################
    def __init__ ( self, ):
        self.value = "Class2Init"

    ###########################################
    # 機能 ：グラフを描画してみる
    ###########################################
    def TestDrawGraph ( self, ):

        # データの定義(サンプルなのでテキトー)
        x = list( range( 10 ) )
        y = list( range( 10 ) )

        # グラフの描画
        pyplot.plot( x, y )
        pyplot.show( )
        
    ###########################################
    # 機能 ：配列を作る
    ###########################################
    def Conv2Arr ( self,obj ):
        return np.array( obj )
        
    ###########################################
    # 機能 ：グラフを描画する
    ###########################################
    def DrawGraph ( self,x ):
        
        ## グラフの描画
        #pyplot.plot(x, y)
        #pyplot.show()

        # グラフ化
        matplotlib.pyplot.plot( x[::10] )
        matplotlib.pyplot.grid( )
        matplotlib.pyplot.show( )

    ###########################################
    # 機能 ：配列の要素が一定個数以上0が連続している区間を返す
    # 例 ：arr = np.array( [0,1,2,0,0,0,6,7,0,0,10,11,0,0,0,0] )
    # 例 ：val = 0
    # 例 ：width = 3
    # 例 ：iSeqRanges = [[3,6],[12,15]]
    # 例 ：x = [3,6,12,15]
    # 例 ：y = [0,0,0,0]
    ###########################################
    def SearchIntervalWithSameVal ( self,arr,val,width ):
        iSeqRanges = [ ]
        iTmpL :int = 0
        iTmpR :int = 0
        bInPrgrs = False
        iCnt = 0
        for idx in range( len( arr ) ):

            #値が一致⇒カウント増加
            if( arr[idx] == val ): 
                iCnt = iCnt + 1
            else:
                iCnt = 0

            #カウントに応じて判断
            if( ( 0 >= iCnt ) or ( len( arr ) == idx ) ):
                if( bInPrgrs == True ):
                    iTmpR = idx - 1
                    bInPrgrs = False
                    iSeqRanges.append( [iTmpL,iTmpR] )
            elif ( 1 >= iCnt ):
                iTmpL = idx
            elif( width >= iCnt ):
                pass
            else:
                bInPrgrs = True

        ## 結果の確認
        #iNdarrTmp = np.array( iSeqRanges )
        #x = list(itertools.chain.from_iterable(iNdarrTmp))
        #y = np.zeros( len( x ) )
        #pyplot.plot( arr[:],c="blue",zorder=1 )
        #pyplot.scatter( x[:],y[:],c="red", zorder=2 )
        #pyplot.show( )
        
        return iSeqRanges


    ###########################################
    # 機能 ：グラフを描画する
    ###########################################
    def search_sequence_numpy ( self,arr,seq ):
    #""" Find sequence in an array using NumPy only.

    #Parameters
    #----------
    #arr : input 1D array
    #seq : input 1D array

    #Output
    #------
    #Output : 1D Array of indices in the input array that satisfy the
    #matching of input sequence in the input array.
    #In case of no match, an empty list is returned.
    #"""Q

        # Store sizes of input array and sequence
        Na, Nseq = arr.size, seq.size

        # Range of sequence
        r_seq = np.arange( Nseq )

        # Create a 2D array of sliding indices across the entire length of
        # input array.
        # Match up with the input sequence & get the matching starting indices.
        M = ( arr[np.arange( Na - Nseq + 1 )[:,None] + r_seq] == seq ).all( 1 )

        # Get the range of those indices as final output
        if M.any( ) > 0:
            return np.where( np.convolve( M,np.ones( ( Nseq ),dtype=int ) ) > 0 )[0]
        else:
            return [ ]         # No match found

###########################################
#引用1
###########################################