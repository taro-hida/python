import sys

line = sys.argv[1]
array_str = line.split(',')
array = []

for array_value in array_str:
    #ここの処理はもっとキレイにできそうなのでなんとかしたい
    array_value = int(array_value)
    array.append(array_value)

array_max_index = len(array) -1

print('---array before swapping---')
print(array)
condition=True
while condition:
    condition = False
    for index in range(array_max_index):
        if array[index] > array[index + 1]:
            #swap value
            #変数の値を入れ替え（交換）とかでググると出てくる処理
            array[index], array[index+1] = array[index+1], array[index]
            condition = True

print('---array after swapping---')
print(array)
