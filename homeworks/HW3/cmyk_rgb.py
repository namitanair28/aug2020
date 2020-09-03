# Namita Nair, hw3a

def CMYK_to_RGB(C, M, Y, K):
    RGBlist = []
    R = 255.0 * (1.0 - C) * (1.0 - K)
    RGBlist.append(int(round(R)))
    G = 255.0 * (1.0 - M) * (1.0 - K)
    RGBlist.append(int(round(G)))
    B = 255.0 * (1.0 - Y) * (1.0 - K)
    RGBlist.append(int(round(B)))
    return RGBlist
    
def main():
    C = int((input("Cyan component: ")))
    M = int((input("Magenta component: ")))
    Y = int((input("Yellow component: ")))
    K = int((input("Black (Key) Component: ")))
    C /= 100
    M /= 100
    Y /= 100
    K /= 100
    print(CMYK_to_RGB(C, M, Y, K)[0], CMYK_to_RGB(C, M, Y, K)[1], CMYK_to_RGB(C, M, Y, K)[2] )
    
if __name__ == "__main__":
    main()
