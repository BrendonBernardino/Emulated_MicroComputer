import memory as mem
import clock
import processor as cpu
import disk

disk.read('op_or.bin')

clock.start([cpu])
print(mem.read_word(3))

#myprog0.bin        result mem[5]   (12 passos)
#multi_por_2.bin    result mem[2]   (12 passos)
#multi_por_4.bin    result mem[2]   (12 passos)
#divide_por_2.bin   result mem[2]   (12 passos)
#divide_por_4.bin   result mem[2]   (12 passos)
#op_and.bin         result mem[3]   (17 passos)
#op_or.bin          result mem[3]   (17 passos)