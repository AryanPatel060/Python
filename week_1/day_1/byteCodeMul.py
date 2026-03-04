import dis
def sum(a ,b):
    return a*b

dis.dis(sum)

# =================== out put ======================
#   2           0 RESUME                   0

#   3           2 LOAD_FAST                0 (a)
#               4 LOAD_FAST                1 (b)
#               6 BINARY_OP                5 (*)
#              10 RETURN_VALUE