from time import time
import morse_code as m


class Morse():

    def __init__(self, code) -> None:
        self.code = code
        self.s = ''
        self.temp = []

    def split(self) -> None:
        self.temp = self.code.split('   ')
        for i in range(len(self.temp)):
            self.temp[i] = self.temp[i].split(' ')
        while [''] in self.temp:
            self.temp.remove([''])
        for i in self.temp:
            while '' in i:
                i.remove('')
        while [] in self.temp:
            self.temp.remove([])

    def decode(self):
        temp = ''
        self.split()
        for i in range(len(self.temp)):
            for j in self.temp[i]:
                temp += m.MORSE_CODE[j]
            self.temp[i] = temp
            temp = ''
        self.s = ' '.join(self.temp)
    @classmethod
    def decode_bits(self, bits):
        temp = '';flag = 0
        for i in bits:
            flag=not flag;
            if not flag:
                temp += i
        bits = temp
        # ToDo: Accept 0's and 1's, return dots, dashes and spaces
        return bits.replace('0000000','   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')


t1 = time()
c = Morse.decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')
x = Morse(c)
x.decode()

t2 = time()
print(t2 - t1)


