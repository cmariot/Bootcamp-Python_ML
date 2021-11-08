if __name__ == "__main__":
    t = ( 0, 4, 132.42222, 10000, 12345.67)
    print("module_0%d" %t[0], end=', ') 
    print("ex_0%d" %t[1], end=', ') 
    print("%.2f" %t[2], end=', ') 
    print(format(t[3],'.2e'), end=', ')
    print(format(t[4],'.2e'))
