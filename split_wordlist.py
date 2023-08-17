"""
    * By MIGUEL PÉREZ RODRÍGUEZ
    * Github: https://github.com/Miguelpr123
    * Source: https://github.com/Miguelpr123/split_wordlist 
"""

import math

# ------------- CONFIG ---------------
num_files_to_divide = 3
file_path = ''
file_name = 'parameters' 
file_extension = '.txt'
# --------------------------------------


file = open( file_path + file_name + file_extension , 'rt' )
arr = file.readlines()
num_lines_for_file = math.ceil( len(arr)/num_files_to_divide ) 
file.close()

bucle = 1
while(bucle<=num_files_to_divide):
    f = open( file_path + file_name + '_' + str(bucle) + file_extension , 'w' )
    a = arr[ slice( (bucle-1)*num_lines_for_file , bucle*num_lines_for_file ) ]
    f.writelines( a )
    f.close()
    bucle+=1










