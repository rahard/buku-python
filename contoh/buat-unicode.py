unicode_text = u'BUDI Rahardjo'
myencoded = unicode_text.encode('utf-16-le')
#myencoded = unicode_text.encode('utf-16-be')

a_file = open("budi-unicode.txt", "wb")
a_file.write(myencoded)

a_file = open("budi-unicode.txt", "r", encoding='utf-16-le')
#a_file = open("budi-unicode.txt", "r", encoding='utf-16-be')
# reads contents of a file
contents = a_file.read()
print(contents)
