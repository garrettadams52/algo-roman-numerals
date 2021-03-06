def to_roman(num):
    # write your code here!
    ans = ''
    roman = {
        'M':1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C':100,
        'XC':90,
        'L':50,
        'XL':40,
        'X':10,
        'IX':9,
        'V':5,
        'IV':4,
        'I':1
    }

    while num > 0:
        for k in roman:
            if num >= roman[k]:
                ans = ans + k
                num = num - roman[k]
                break
    #print(ans)
    return ans