import sys

test_string = sys.argv
if len(test_string) > 0:
    test_string = test_string[1::]
    test_string = ' '.join(test_string)[::-1]
    print(test_string.upper())


#if test_string is not None:
#if test_string != None:

# print(test_string)

# for x in test_string:
#     print(x.upper())


