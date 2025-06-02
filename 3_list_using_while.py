l = [1, "harry", True, "ram", "krish", "shubhi", "akriti"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1


# l[0] = 1
# l[1] = "harry"
# l[2] = True
# l[3] = "ram"
# l[4] = "krish"
# l[5] = "shubhi"
# l[6] = "akriti" ← This is the last item, and it is included because 6 < 7.

# In short:
# The length is 7, so indices go from 0 to 6.

# The loop runs while i < 7, so it runs for i = 0 to 6.

# That's 7 iterations, which includes the last element.

# So "akriti" will be printed as expected
