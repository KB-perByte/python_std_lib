# day - 3
# define test scores
# * operator works on all iterators
# one * unpack expression per level

test_scores = [90, 92, 93, 87, 67, 54]

first_score, *other_score = test_scores

first_char, *char, last_char = set("ABCDE") #unstable order has non-deterministic behavior

first_char, *char, (last_char_first, *last_chars) = ["A", "B", "C", "D", "EFGHI"]

# join iterable types

csv_get = [1,2,3,4,5,6,7,8]
lms_get = [9,10,11,12,13,14]

combines_csv_lms = [*csv_get, *lms_get]


csv_dic = {1 : "A", 2: "B"}
lms_dic = {3 : "C", 4: "D"}

combined_dics = {**csv_dic, **lms_dic}
combines__dic_l = [*csv_dic, *lms_dic] #keys only

#same for dicts just **
def keyword_only_func(*, key1, key2): #rigid
    print(key1, key2)

def keyword_only_func(*_, key1, key2): #bit lucid wont break but will not consider postiional arugment
    print(key1, key2)

keyword_only_func(0000, key1="this", key2="wont work") # only takes keyword argument no positional argument, gets error

#python 3.8 + having support to /

def mixed_agrs_func(arg1, arg2, /, arg3, arg4, *, arg5, arg6):
    pass

#positional / can be positional can be keyword * strict keyword



