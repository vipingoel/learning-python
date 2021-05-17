def mt(n):
    return n**2

if __name__ == "__main__":
    import sys
    print(sys.argv)
    print(sys.path)
    print(mt(int(sys.argv[1])))