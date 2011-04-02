import sys;
def generate_perms(N,key):
	out = []
	for _ in range(N):
		out.append(range(alpha_size));
	key_l = list(key)
	for p in range(len(out)):
		for i in range(len(out[p])):
			out[p][i] = (out[p][i]+ord(key_l[p]))%len(out[p]);
	return out;
	


alpha_size = 8;
N = int(sys.argv[1]);
key = sys.argv[2];

perm_list = generate_perms(N,key);
for i in perm_list:
	print i
