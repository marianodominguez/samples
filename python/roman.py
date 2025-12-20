'''
Convert an integer to a Roman numeral.
''' 

class Solution:

    # Symbol lookup table
    symbols= {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    # Subtractive lookup table
    subtractive={ 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

    # Find the largest symbol less than or equal to num
    def maximal(self, num: int, lut: dict) -> str:
        i=0
        values = list(lut.keys())
        while i<len(values) and values[i]<=num:
            i+=1
        j = values[i-1]
        return (lut[j],j)
 
    
    # Check if num is a power of 10
    def ispow10(self, num: int) -> bool:
        i=1
        while i<4:
            if i==num: return True
            i*=10;
        return False

    # Convert an integer to a Roman numeral
    def intToRoman(self, num: int) -> str:
        result=""
        # Handle edge cases, no zero and no numbers greater than 3999
        if num==0 or num >=4000: return ""
        num_str=str(num)
        
        # Handle powers of 10
        if self.ispow10(num):
            k=0
            while k<3 and num>10:
                k+=1
                (new_symbol, value)=self.maximal(num, self.symbols)
                num-=value
                result=f"{result}{new_symbol}{self.intToRoman(num)}"
        
        # Handle non-powers of 10
        if num_str[0]!='4' and num_str[0]!='9':
            (new_symbol, value)=self.maximal(num, self.symbols)
            num-=value
            result=f"{result}{new_symbol}{self.intToRoman(num)}"
        
        # Handle subtractive cases
        if num_str[0]=='4' or num_str[0]=='9':
            (new_symbol, value)=self.maximal(num, self.subtractive)
            num-=value
            result=f"{result}{new_symbol}{self.intToRoman(num)}"
        return result

# Test the function
if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(1994))  # Output: "MCMXCIV"
    print(s.intToRoman(58))    # Output: "LVIII"
    print(s.intToRoman(4))     # Output: "IV"
    print(s.intToRoman(9))     # Output: "IX"
    print(s.intToRoman(44))    # Output: "XLIV"