class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_letters_s1 = s1[::2]
        odd_letters_s1 = s1[1::2]
        even_letters_s2 = s2[::2]
        odd_letters_s2 = s2[1::2]

        # I didn't know we could use libs
        even_check = False
        odd_check = False

        for i in even_letters_s1:
            if i in even_letters_s2:
                even_letters_s2 = even_letters_s2.replace(i, '', 1)
        if even_letters_s2 == '':
            even_check = True

        for i in odd_letters_s1:
            if i in odd_letters_s2:
                odd_letters_s2 = odd_letters_s2.replace(i, '', 1)
        if odd_letters_s2 == '':
            odd_check = True
            
        return even_check and odd_check