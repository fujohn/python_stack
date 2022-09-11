def varargs(arg1, *args):
    print("Got ", arg1, " and ", args)
varargs("one") 			# output: Got one and ()
varargs("one", "two") 	        # output: Got one and ('two',)
varargs("one", "two", "three")  # output: Got one and ('two', 'three')

def varargs(arg1, *args):
    for a in args:
        print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)


