import csv
from datetime import datetime

class Tracker:
    def mount(self):
        try:
            input_amount = float(input('Insert the amount: '))
            return input_amount
        except:
            print('Sorry, only numbers are accepted.')
            return self.mount()

    def category(self):
        options_category = {
            '1': 'Food',
            '2': 'Transport',
            '3': 'Entertainment',
            '4': 'Clothes',
            '5': 'Education',
            '6': 'Health'
        }
        print('Choose the category that represents the amount:')
        for key, value in options_category.items():
            print(f"{key} - {value}")

        input_category = input('Insert the category number: ')
        if input_category in options_category:
            return options_category[input_category]
        else:
            print('Invalid category, please try again.')
            return self.category()

    def description_of_mount(self):
        input_description = input("Add a description: ")
        if len(input_description) >= 8:
            return input_description
        else:
            print("Description must be at least 8 characters.")
            return self.description_of_mount()

    def save_information(self, amount, category, description):
        now = datetime.now()
        with open('src/data/expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, description, now.strftime('%Y-%m-%d')])
        print("Expense saved! ✅")

    def add_mount(self):
        amount = self.mount()
        category = self.category()
        description = self.description_of_mount()
        self.save_information(amount, category, description)

