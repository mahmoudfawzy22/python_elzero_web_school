class User:
    def __init__(self, fisrt_name, middel_name, age, gender) :
        self.fname = fisrt_name
        self.mname = middel_name
        self.age = age
        self.gender = gender

    def full_details(self) :

        years_to_40 = 40 - self.age

        if self.gender == "Male" :
            return f"Hello Mr {self.fname} {self.mname[0].upper()}. {str(years_to_40).zfill(2)} To Reach 40"
        
        else :
            return f"Hello Mrs {self.fname} {self.mname[0].upper()}. {str(years_to_40).zfill(2)} To Reach 40"



user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

