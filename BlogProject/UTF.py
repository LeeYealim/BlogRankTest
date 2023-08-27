import urllib.request

str = '다이어리'
encoded = str.encode('EUC-KR')
print(encoded)

encText = urllib.parse.quote("한의원")
print(encText)
