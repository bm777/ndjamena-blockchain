import random
import pandas as pd


first_name =  ["Mohammed", "Ali", "Bichara", "Hassan", "Jacques", 
				"Marie", "Isabelle", "Christine", "Magne", "Adele",
				"Chriss", "Bayang", "Benjamin", "Djelassem", "Emile",
				"Yannick", "Narcisse", "Josue", "Jean", "Idriss", "",
				 "Alain", "Billie", "Moussa", "Ghyslain", "Sylvain",]

last_name = ["Al-bachar", "Zakaria", "Oumar", "Djibril", "Abdel",
			"Issa", "Kalman", "Edison", "Akoro", "Nick",
			"Iboko", "Bouva", "Abba", "Souleyman", "Hissein",
			"Adam", "Mounir", "Alphonse", "Itno", "Hinda",
			"Sankara", "Hadje", "Ache", "Haoua", "Nasser",]




names = []
for i in range(1000050):

	index_f = random.randint(0, len(first_name)-1)
	index_l = random.randint(0, len(last_name)-1)

	fname = first_name[index_f]

	tmp = fname + " "+last_name[index_l]

	# naissance
	anne = random.randint(1990, 2000)
	mois = random.randint(1, 12)
	mois = "0"+ str(mois) if len(str(mois))==1 else str(mois)
	jour = 28 if mois == 2 else random.randint(1, 31)
	jour = "0"+str(jour) if len(str(jour))==1 else str(jour)
	naissance = str(anne)+"/"+str(mois)+"/"+str(jour)

	# status
	status = ["Condamnee", "non Condamnee"]
	status = status[random.randint(0,1)]

	tribunal = ["Tribuanl 1", "Tribuanl 2", "Tribuanl 3", "Tribuanl 4", "Tribuanl 5"]
	idx = random.randint(0, len(tribunal)-1)
	tribunal = tribunal[idx]


	if tmp != "":

		if status == "Condamnee":
			_anne = random.randint(2009, 2017)
			_mois = random.randint(1, 12)
			_mois = "0"+ str(_mois) if len(str(_mois))==1 else str(_mois)
			_jour = 28 if _mois == 2 else random.randint(1, 31)
			_jour = "0"+str(_jour) if len(str(_jour))==1 else str(_jour)
			_naissance = str(_anne)+"/"+str(_mois)+"/"+str(_jour)

			names.append([tmp, naissance, status, _naissance, tribunal])
		else:
			names.append([tmp, naissance, status, "n/a", "n/a"])

	print("citoyen ", i, " : ", names[-1])

# saving to csv file
df = pd.DataFrame(names)
df.to_csv("citoyen.csv", index=False, header=["Noms", "Naissance", "Status", "cond", "Tribunal"])