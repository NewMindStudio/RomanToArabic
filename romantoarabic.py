def to_arabic_digits(numeral):
    numerals = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    nums = [numerals[n] for n in numeral]

    return sum( x if x >= next_x else -x for x, next_x in zip(nums[:-1], nums[1:]) ) + nums[-1]

def enc_dig(dig, one, five, nine):
    return ( nine                   if dig == 9 else
             five + one * (dig - 5) if dig >= 5 else
             one + five             if dig == 4 else
             one * digit )


def to_roman_numerals(num):
    num = int(num)
    return (
            'M' * (num // 1000) +
            enc_dig((num // 100) % 10, 'C', 'D', 'CM') +
            enc_dig((num //  10) % 10, 'X', 'L', 'XC') +
            enc_dig( num         % 10, 'I', 'V', 'IX') 
            )
