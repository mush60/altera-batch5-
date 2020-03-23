import unittest

def changeVocals(kata):
    new_kata = ''
    vocals = ['a', 'i', 'e', 'u', 'o']
    for c in kata:
        ord_c = ord(c)
        if c in vocals:
            ord_c += 1
        new_kata += chr(ord_c)
    return new_kata

def reverse(kata):
    # new_kata = ''
    # for i in range(len(kata) -1 -1):
    #     new_kata += kata[i]
    return kata[::-1]

def lowerUpper(kata):
    new_kata = ''
    for c in kata:
        ord_c = ord(c)
        if ord_c in range(65, 91):
            c = c.lower()
        elif ord_c in range(97, 123):
            c = c.upper()
        new_kata += c
    return new_kata

def removeSpace(kata):
    new_kata = ''
    for i in kata :
        if ord(i) != 32 :
            new_kata += i
    return new_kata

def passwordGenerator(kata):
    # A 65 Z 90 a 97 z 122
    if len(kata) < 5:
        return "Minimal karakter yang diinputkan adalah 5 karakter"
    chaged = changeVocals(kata)
    reversed_kata = reverse(chaged)
    low_up = lowerUpper(reversed_kata)
    no_space = removeSpace(low_up)
    return no_space


# ============= UNIT TESTING ==============
class TestSolution(unittest.TestCase):
  def testChangeVocals(self):
    result = changeVocals('abiueoa')
    self.assertEqual(result, 'bbjvfpb')

  def testReverse(self):
    result = reverse('abcdefg')
    self.assertEqual(result, 'gfedcba')

  def testlowerUpper(self):
    result = lowerUpper('aBcDeFg')
    self.assertEqual(result, 'AbCdEfG')
  
  def testRemoveSpace(self):
    result = removeSpace('a b c d e')
    self.assertEqual(result, 'abcde')

  def testPasswordGenerator(self):
    result = passwordGenerator('Sergei Dragunov')
    self.assertEqual(result, 'VPNVGBRdJFGRFs')

    result = passwordGenerator('Dimitri Wahyudiputra')
    self.assertEqual(result, 'BRTVPJDVYHBwJRTJMJd')

    result = passwordGenerator('Alexei')
    self.assertEqual(result, 'JFXFLa')

if __name__ == '__main__':
    unittest.main()