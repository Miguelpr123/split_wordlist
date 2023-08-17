"""
    * By MIGUEL PÉREZ RODRÍGUEZ
    * Github: https://github.com/Miguelpr123
    * Source: https://github.com/Miguelpr123/split_wordlist 
"""

import math

# ------------- CONFIG ---------------
num_files_to_divide = 3
file_path = '/home/<user>/Desktop' #or ''
file_name = 'example'   #example.txt 
file_extension = '.txt'
file_output = '/home/<user>/Desktop' #or ''
# --------------------------------------


file = open( file_path + '/' + file_name + file_extension , 'rt' )
arr = file.readlines()
num_lines_for_file = math.ceil( len(arr)/num_files_to_divide ) 
file.close()

loop = 1
while(loop<=num_files_to_divide):
    f = open( file_output + '/' + file_name + '_' + str(loop) + file_extension , 'w' )
    a = arr[ slice( (loop-1)*num_lines_for_file , loop*num_lines_for_file ) ]
    f.writelines( a )
    f.close()
    loop+=1










