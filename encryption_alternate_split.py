def decrypt(encrypted_text, n):
  if n <= 0:
    return encrypted_text

  text_list = list(encrypted_text)
  length = len(text_list)
  if length % 2 == 0:
    splitOn = length//2
  else:
    splitOn = (length-1)//2

  first = text_list[0:splitOn]
  second = text_list[splitOn:length]

  result_list = [second[i//2] if i % 2 == 0 else first[(i-1)//2] for i in range(0,length)]
  result = ''.join(result_list)
  return decrypt(result,n-1)

def encrypt(text,n):
  if n <= 0:
    return text
  out = text
  for i in range(n):
    out = out[1::2] + out[::2]
  return out
