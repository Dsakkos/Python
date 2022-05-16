class User:
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.member_status = False
        self.gold_card_points = 0
    
    
    def display_info(self):
        print("First Name", self.first_name)
        print("Last Name", self.last_name)
        print("Email is", self.email)
        print("My Age is", self.age)
        print("Memeber Status", self.member_status)
        print("My Card Balance", self.gold_card_points)

    def enroll(self):
        if self.member_status == True:
            print("User already a member.")
        else:
            self.member_status = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points <= amount:
            print("sorry try again")
        else:
            self.gold_card_points -= amount

user_jim = User("Jimmy", "Smith", "JSmith@Gmail.com", 25)
user_joe = User("joe", "Smith", "JSmith@Gmail.com", 31)
user_jack = User("jack", "Smith", "JSmith@Gmail.com", 32)
user_jack.enroll()
user_jack.spend_points(40)
user_jack.display_info()
user_joe.enroll()
user_joe.spend_points(80)
user_joe.display_info()
user_jim.enroll()
user_jim.spend_points(50)
user_jim.display_info()
