class tracker:
    def mount(self):
        try:
            input_amount = float(input('Insert the amount: '))
            return input_amount
        except:
            print('Sorry just can receive a number not text')
    
    def category(self):
        options_category = {
            '1': 'Food',
            '2': 'Transport',
            '3': 'Entertaiment',
            '4': 'Clothes',
            '5': 'Education',
            '6': 'Healthy'
        }
        try:
            print('Choose the category that represent the amount:')
            print('' \
            '1.-Food' \
            '2.-Transport' \
            '3.-Entertaiment' \
            '4.-Clothes' \
            '5.-Education' \
            '6.-Healthy' \
            '')

            input_category = input('Insert the category')
            if input_category != '':
                options_category[input_category];
                #Insert to cvs
            else:
                print('You must choose a category')
        except:
            print('You must choose a valid category ')
    
    def description_Of_mount(self):
        input_description = input("Add a description: ")
        if len(input_description) >= 8:
            #insert the description to csv
            print("pass")
        else:
            print("You must insert a description of more than 8 characters.")
    
    def add_mount(self):
        self.mount()
        self.category()
        self.description_Of_mount()