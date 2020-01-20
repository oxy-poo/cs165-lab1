import hashlib
import struct

def generate_Permutations(depth,temp):
	permutation_list = [ ('password','hash')]
	l = "abcdefghijklmnopqrstuvwxyz"
	if(depth < 6):
			
		for i in l:
			t_s = temp
			t_s += i
			t_s_hash = Compute_Hash(t_s)

			#permutation_list.append((t_s,compute_hash(t_s)))
			#f.write(t_s)
			#f.write(':')
			#f.write(t_s_hash)
			#f.write('\n')
			print(t_s,t_s_hash)
			if t_s_hash == "nd4.kYa98cdFa3X85Ho8j1":
				print(t_s)
				return t_s
			generate_Permutations(depth + 1, t_s)

def Compute_Hash(pw):
	pw.encode('utf-8')
	salt = "4fTgjp6q".encode('utf-8')

	magic = "$1$".encode('utf-8')
	pwlen = len(pw)
	itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

	a = hashlib.md5(pw + salt + pw).digest()
	#print("alternate sum:", hashlib.md5(pw + salt + pw).hexdigest())
	#print("alternate sum digest:", a)
	b = pw + magic + salt + a[:len(pw)]
	#print(b)
	lp = len(pw)
	while lp != 0:
		if(lp & 1):
			b += b'\0'
		else:
			b += pw[0]
		lp >>= 1
	#print(b)

	intermediate = hashlib.md5(b).hexdigest()

	inter = hashlib.md5(b)

	#print(intermediate)

	for i in range(1000):
		c = hashlib.md5()
		if i & 1:
			c.update(pw)
		else:
			c.update(inter.digest())
		if i % 3:
			c.update(salt)
		if i % 7:
			c.update(pw)
		if i & 1:
			c.update(inter.digest())
		else:
			c.update(pw)
		inter = c

	s = inter.digest()


	final = ''
	for a, b, c in ((0, 6, 12), (1, 7, 13), (2, 8, 14), (3, 9, 15), (4, 10, 5)):
	  v = ord(s[a]) << 16 | ord(s[b]) << 8 | ord(s[c])
	  for i in range(4):
		final += itoa64[v & 0x3f]
		v >>= 6
	v = ord(s[11])
	for i in range(2):
	  final += itoa64[v & 0x3f]
	  v >>= 6
	#print(final)
	return final

#permutation_list = [ ('password','hash')]
#gp(0,"",permutation_list)
print(generate_Permutations(0,""))

