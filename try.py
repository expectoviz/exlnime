import random
import calendar

# Coded By AN
# https://cybergd-article.gq

def title(placed,nama):
	placed.append(nama)
	print("Berhasil menginput!")
	
def batch():
	print("\n1. https://www.samehadaku.tv")
	print("2. https://batchkun.com")
	print("3. https://batch.id")
	print("4. https://meownime.my.id")
	print("5. https://anikyojin.net")
	print("6. https://drivenime.com")
	print("7. https://kusonime.com")
	print("8. https://awsubs.tv")
	print("9. https://www.oploverz.in")
	print("10. http://neosubs.net\n")
	
def generated(placed,n):
	
	print("\n===[ Hasil Generated! ]===")
	for i in range(n):
		result = random.choice(placed)
		print(str(i+1)+"."+str(result))
		placed.remove(result)
		
def kalender(xy):
	year = calendar.calendar(xy)
	print("Kalender tahun "+str(xy))
	print(year)

def main():
	
	data = []
	
	program = True
	
	while(program == True):
		
		print("===={ EXL-SEKAI }====")
		print("1. Random Judul")
		print("2. Tempat download BATCH")
		print("3. Kalender Tahunan")
		print("0. Exit")
		inp = int(input("Masukan Pilihan: "))
		
		if(inp == 1):
			x = int(input("Masukan Jumlah Judul : "))
			print("\nMasukan nama judul anime favoritmu (Bisa didefinisikan sebagai A,B,C,D...)\n")
			for i in range(x):
				y = input("Judul Anime ke-"+str(i+1)+" : ")
				title(data,y)
			generated(data,x)
		
		elif(inp == 2):
			batch()
		
		elif(inp == 3):
			thn = int(input("Masukan Tahun: "))
			kalender(thn)
		
		elif(inp == 0):
			program = False

if __name__ == "__main__":
	main()
