# len()
# A-built-in Python fuction to get the length of a list
# When we apply len() to a list, we get the number of elements in that list

my_list = ["Icecream", "Twix", "Pepsi", "Dorito"]
print(len(my_list))

numbers = [1,2,4,5,6,8,0]
print(len(numbers))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

long_list_len = len(long_list)
print(long_list_len)

big_range_length = (len(big_range))
print(big_range_length)

big_range = range(2, 3000, 100)
big_range_length = (len(big_range))
print(big_range_length)