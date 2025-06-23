import pdb 
import pytest

def first_unique_char(s):
    s_len = (len(s))
    for i in range(s_len):
        counter = i+1
        for j in range (s_len-i):
            if s[i] == s[j+ counter]:
                break
            else: 
                if j+counter == s_len-1:
                    return i    
    return -1

@pytest.mark.parametrize("input_text, expected",[
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
])

def test_eval(input_text, expected):
    assert first_unique_char(input_text) == expected

   
	# •	"correctable" error sets bit 3 (i.e. bitmask 0b00001000)
	# •	"uncorrectable" error sets bit 7 (i.e. bitmask 0b10000000)
	# •	"fatal" error sets both bits 3 and 7    

def inject_error(register_value, error_type=None):
    if error_type == None:
        print("It is mandatory select an error type")
    if (error_type == 'correctable'):
        register_value = (register_value & 0xFFFF) | 0x0008
    elif (error_type == 'uncorrectable'):
        register_value = (register_value & 0xFFFF) | 0x0080
    elif (error_type == 'fatl'):
        register_value = (register_value & 0xFFFF) | 0x0088    
    return (register_value)

print(inject_error(0xf00, 'uncorrectable'))
    # for i in range(len(s)):
    #     if count < (len(s)-2):
    #         if (s[i+count]== s[i]):
    #             unique = -1
    #             continue
    #         else:
    #             unique = i
    # return unique
        
#result = first_unique_char("loveleetcode")
#print(result)