import processor as cpu
import memory as mem
import clock as clk

# 50 & 2 = 2

mem.write_word(60, 50)
mem.write_word(61, 2)

# X <- X + memory[60]
mem.write_byte(1, 2)
mem.write_byte(2, 60)
# X <- X & memory[61]
mem.write_byte(3, 33)
mem.write_byte(4, 61)
# memory[62] = X
mem.write_byte(5, 10)
mem.write_byte(6, 62)
    
# stop
mem.write_byte(7, 255)


clk.start([cpu])

# print(cpu.X)
print(mem.read_word(62))