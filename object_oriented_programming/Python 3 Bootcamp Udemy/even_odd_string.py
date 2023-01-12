def myfunc(*args):
    even_odd_list = list(args[0]) #tuple unpack and then cast it into a list
    counter = 0
    for element in even_odd_list:
        if counter % 2 == 0:
            even_odd_list[counter] = element.upper()
        counter += 1
    return "".join(even_odd_list) #convert it back into a string