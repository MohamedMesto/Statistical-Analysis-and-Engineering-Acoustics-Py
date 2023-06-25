import codecs
 

text = r"Was Du s\u00e4st, das wist Du ernten ."

decoded_text = codecs.decode(text, 'unicode_escape')
print(decoded_text)

