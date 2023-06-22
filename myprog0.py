import processor as cpu
import memory as mem
import clock as clk

mem.write_word(50, 400)
mem.write_word(100, 19)
mem.write_word(130, 10)

# X <- mem[50] / 2
mem.write_byte(1, 17)   # X <- X >> 1 <- X + memory...
mem.write_byte(2, 50)   # ...[50]

# if X=0 goto 7
mem.write_byte(3, 15)
mem.write_byte(4, 7)

# memory[60] = X
mem.write_byte(5, 10)
mem.write_byte(6, 60)

# X <- mem[60] * 4
mem.write_byte(7, 29)   # X <- X << 2 <- X + memory...
mem.write_byte(8, 60)   # ...[50]

# X <- X + memory[50]
mem.write_byte(9, 2)      # X <- X + memory...
mem.write_byte(10, 50)     # ...[50]

# X <- X + memory[100]
mem.write_byte(11, 2)      # X <- X + memory...
mem.write_byte(12, 100)     # ...[100]

# X <- X - memory[130]
mem.write_byte(13, 6)     # X <- X - memory...
mem.write_byte(14, 130)     # ...[130]

# memory[150] = X
mem.write_byte(15, 10)
mem.write_byte(16, 150)
    
# stop
mem.write_byte(17, 255)


clk.start([cpu])

# print(cpu.X)
print(mem.read_word(150))