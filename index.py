import json




def get():

	with open('city.json', 'r', encoding='utf-8') as file:
				
		data = json.load(file)

		for city in data:

			print(f"№: {city['id']}, Название: {city['name']}, Страна: {city['country']}, Является ли большим: {city['is_big']}, Численность населения: {city['people_count']}")


def get_by_id():

	numb = input("Введите id записи, по которой хотите сделать вывод информации: \n")

	if numb.isdigit():

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

	else:
		print(f"ID не число.")


def post():


	new_name = input("Введите название города: \n")
	new_country = input("Введите страны города: \n")
	new_is_big = input("Введите является ли большим(>100k)(True/False): \n")=="True"
	new_people_count = input("Введите численность населения города: \n")
	
	if new_people_count.isdigit():
		with open('city.json', 'r+', encoding='utf-8') as file:

			data = json.load(file)

			if not data:
				new_id = 1
			else:
				
				new_id = max(int(city['id']) for city in data) + 1

			new_city={
				"id": str(new_id),
				"name": new_name,
				"country": new_country,
				"is_big": new_is_big,
				"people_count": new_people_count
			}

			
			data.append(new_city)
			
			
			file.seek(0)
			json.dump(data, file, ensure_ascii=False, indent=4)
			file.truncate()

		print("Запись добавлена!")
	
	else:
		print(f"Численность населения должно быть числом!")
		


def delete():

	deletе = input("Введите номер записи которую вы хотите удалить: ")
	
	if deletе.isdigit():
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
				json.dump(data, file, ensure_ascii=False, indent=4)
				file.truncate()

				print(f"Запись с {deletе} id удалена!")

	else:
		print("ID должно быть числом!")
		


def main():

	count=0

	while True:

		print("\nВыберите пункт из предложенного МЕНЮ!")
		print("1. Вывести все записи")
		print("2. Вывести запись по id города")
		print("3. Добавить запись города")
		print("4. Удалить запись по id города")
		print("5. Выйти из программы")

		res = input("\nВыберай (1/2/3/4/5): ")

		if res =="1":
			
			get()

			count+=1

		elif res == "2":

			get_by_id()

			count+=1

		elif res == "3":

			post()

			count+=1

		elif  res =="4":

			delete()

			count+=1 
			
		elif res =="5":

			print(f"\nВсего выполненных операций с записями: {count}")
			break

		else:
			print("Неправильный ввод, попробуйте снова.")



if __name__ == "__main__":
    main()

