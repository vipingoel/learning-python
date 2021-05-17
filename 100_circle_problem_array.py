# In a circle of 100 people if one person is killing the 2nd person and the 3rd person is killing 4th person..who lives at the end
# create a ircular linked list of 100 people

if __name__ == "__main__":
    l = [n for n in range (1, 101)]
    print(l)

    current_index = 0
    next_index = 1
    


    while current_index != next_index:
        l[next_index] = 0

        while l[next_index]!=0:
            next_index = (next_index + 1)%len(l)

        current_index = next_index

        next_index = (next_index + 1)%len(l)
        while l[next_index]!=0:
            next_index = (next_index + 1)%len(l)

    print(l[current_index])