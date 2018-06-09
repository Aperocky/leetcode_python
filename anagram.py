""" This is what ruyi.ai tests you for """

def checkAnagram(str1, str2):
    # Remove space
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    dict1 = str_to_dict(str1)
    dict2 = str_to_dict(str2)
    if dict1 == dict2:
        return True
    return False

def str_to_dict(inputString):
    dict1 = dict()
    for char in inputString:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1
    return dict1

print(checkAnagram("William Shakespeare", "I am a weakish speller"))
print(checkAnagram("上海","海上"))
print(checkAnagram("rail safety", "fairy tales"))
