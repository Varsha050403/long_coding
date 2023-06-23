l = []
movie_language = {1: 'Tamil', 2: 'Malayalam'}


class user_profiles:
    print("Welcome to my app!!!!")

    def __init__(self, user_id, user_name, user_emailid, user_phno, user_gender):
        self.user_id = user_id
        self.user_name = user_name
        self.user_emailid = user_emailid
        self.phno = user_phno
        self.gender = user_gender


class login(user_profiles):
    def __init__(self, user_id, user_name, user_emailid, user_phno, user_gender, user_password):
        self.password = user_password
        user_profiles.__init__(self, user_id, user_name, user_emailid, user_phno, user_gender)
        l.append(self.user_emailid)
        l.append(user_password)

    def sign_in(self):
        email = input("Enter the email id: ")
        l.append(email)
        password = input("Enter the password: ")
        l.append(password)
        print("Successfully Sign in!")

    def check(self, password, user_email_id):
        for i in range(len(l)):
            if (l[i - 1] == password and l[i] == self.user_emailid):
                print("Sussfull login!")
                break
            else:
                print("Please sign in with your email id and valid password!!")
                self.sign_in()
                break


class movie_listing:
    def __init__(self, movie_id, movie_name, language, starting_time, length_time, release_date):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.language = language
        self.length_time = length_time
        self.starting_time = starting_time
        self.release_date = release_date

    def choice(self):
        print(movie_language)
        sel_choice = int(input("Select the prefer language: "))
        if (sel_choice == 1):
            m1 = movie_listing(1, 'Don', 'Tamil', '10:10 am', 2, '28.07.2023')
            m2 = movie_listing(2, 'Prince', 'Tamil', '10:00 am', 2.30, '29.07.2023')
            m3 = movie_listing(3, 'Lio', 'Tamil', '12:10 am', 2.15, '25.07.2023')
            print("Available Tamil Movie's are: ")
            print(m1.movie_name)
            print(m2.movie_name)
            print(m3.movie_name)
        elif (sel_choice == 2):
            m1 = movie_listing(1, 'Premam', 'Malayalam', '10:10 am', 2, '28.07.2023')
            m2 = movie_listing(2, 'Hridayam', 'Malayalam', '10:00 am', 2.30, '29.07.2023')
            m3 = movie_listing(3, 'Jana Gana Mana', 'Malayalam', '12:10 am', 2.15, '25.07.2023')
            print("Available Tamil Movie's are: ")
            print(m1.movie_name)
            print(m2.movie_name)
            print(m3.movie_name)

        else:
            print('Enter the valid movie language')
            self.choice()


if __name__ == "__main__":
    l1 = login(1, 'Varsha', 'aaa@gmail.com', '1234567890', 'Female', 'aaa*2003')
    # l2=login(2,'priya','bpriya@gmail.com','2345678901','Female','bbbb2004')
    #l3=login(3,'ccc','ccc@gmail.com','34567789012','Male','Pggg05')
    l1.check('aaa*2003', 'aaa@gmail.com')
    m1 = movie_listing(1, 'sami', 'tamil', 78, 79, 27827)
    m1.choice()