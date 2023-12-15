# set() 到底怎麼用
s = [1,2,3,4] # 第1種,用大括號
print(s)
s = set( (1,3,5,7) ) # 地2種, 用set() 裡面放你一開始要加入的東西,可用[圖括號] tuple
print(s)
s = set( [1,2,4,3] ) # 地2種的 set() 裡面也可以放[方括號]list的陣列的東西
print(s)
s = set( 'Hello' ) #第2種的 set() 裡面也可以[字串]會把他一個個拆開求
print(s)

# 下面試試 .add() 和 .remove()
s.add(100)
print(s)
s.remove('H')
print(s)