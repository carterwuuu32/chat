


def read_file(filename):
	lines = []
	with open(filename, 'r', encoding= 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	Viki_word_count = 0
	Viki_sticker_count = 0
	Viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for massage in s[2:]:
					allen_word_count += len(massage)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count += 1
			elif s[2] == '圖片':
				Viki_image_count += 1
			else:
				for massage in s[2:]:
					Viki_word_count += len(massage)
	print('Allen說了', allen_word_count, '個字')
	print('傳了',allen_sticker_count , '個貼圖') 
	print('貼了', allen_image_count, '張圖片')

	print('Viki說了', Viki_word_count, '個字')
	print('傳了',Viki_sticker_count , '個貼圖')
	print('貼了', Viki_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()