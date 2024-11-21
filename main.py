import json

count=0

while True:
	print("\nВыберите пункт из предложенного МЕНЮ!")
	print("1. Вывести все записи")
	print("2. Вывести запись по id города")
	print("3. Добавить запись города")
	print("4. Удалить запись по id города")
	print("5. Выйти из программы")

	res = input("\nВыберай (1/2/3/4/5): ")

	if res =='1':
		
		with open('city.json', 'r', encoding='utf-8') as file:
			
			data = json.load(file)

			for city in data:

				print(f"№: {city['id']}, Название: {city['name']}, Страна: {city['country']}, Является ли большим: {city['is_big']}, Численность населения: {city['people_count']}")

		count+=1

	elif res == '2':

		numb = input("Введите id записи, по которой хотите сделать вывод информации: \n")
		with open('city.json', 'r', encoding='utf-8') as file:
			
			data = json.load(file)
			
			found = False

			for city in data:
				if city['id'] == numb:

					print(f"\n=============== Найдено ===============")
					print(f"{city['id']} >> Название: {city['name']}, Страна: {city['country']}")
					print(f"Является ли большим: {city['is_big']}, Численность населения: {city['people_count']}")
					found = True
					break

			if not found:
				print(f"\n=============== Не найдено ===============")

		count+=1

	elif res == '3':

		new_id = input("Введите номер записи: \n")
		new_name = input("Введите название города: \n")
		new_country = input("Введите страны города: \n")
		new_is_big = input("Введите является ли большим(>100k): \n")=="True"
		new_people_count = int(input("Введите численность населения города: \n"))

		new_city={
			"id": new_id,
			"name": new_name,
			"country": new_country,
			"is_big": new_is_big,
			"people_count": new_people_count
		}

		with open('city.json', 'r+', encoding='utf-8') as file:
			data = json.load(file)
			data.append(new_city)
			file.seek(0)
			json.dump(data, file, ensure_ascii=False, indent=4)

		count+=1

	elif  res =="4":

		deletе = input("Введите номер записи которую вы хотите удалить: ")

		with open('city.json', 'r+', encoding='utf-8') as file:
			data = json.load(file)
			found = False

			for city in data:
				if city['id'] == deletе:
					data.remove(city)
					found = True
					break

			if not found:

				print("\n=============== Не найдено ===============")
		
			else:

				file.seek(0)
				file.truncate()
				json.dump(data, file, ensure_ascii=False, indent=4)

		count+=1 
           
	elif res =="5":

		print(f"\nВсего выполненных операций с записями: {count}")
		break

	else:
		print("Неправильный ввод, попробуйте снова.")
