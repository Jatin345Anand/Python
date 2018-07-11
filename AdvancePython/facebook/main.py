from datetime import datetime

class Facebook():

    def __init__(self,users):
        self.users = users

    def homeScreen(self):
        print("""
        1. Login
        2. Register
        """)

        userChoice = input("Enter your choice : ")
        todo = {
            "1" : self.login,
            "2" : self.register
        }

        todo.get(userChoice)()

    def login(self):
        self.loginId = input("Enter your mail : ")
        self.loginPwd = input("Enter your pwd : ")

        for users in self.users:
            if self.loginId == users['userMail'] and self.loginPwd == users['userPwd']:
                print("Welcome User")
                userObj.userOptions(users['userName'],users['userMail'])
            else:
                print("Incorrect Mail or Password")
                self.homeScreen()

    def register(self):
        self.userData = {}
        self.userName = input("Enter your name : ")

        while True:
            self.userMail = input("Enter your mail : ")


            for users in self.users:
                if users['userMail'] == self.userMail:
                    print("EmailID Already Exist")
                    self.register()
                else:
                    break

            if '@' in self.userMail:
                break
            else:
                print("Invalid EmailID")
                print("Try Again")

        while True:
            self.userpwd = input("Enter your password : ")
            self.confpwd = input("Confirm password : ")
            if self.userpwd == self.confpwd:
                break
            else:
                print("Password do not match")

        self.userData['userName'] = self.userName
        self.userData['userMail'] = self.userMail
        self.userData['userPwd'] = self.userpwd

        self.users.append(self.userData)

        self.showUser()

    def showUser(self):
        for user in self.users:
            print(user)

        self.homeScreen()


class UserActivites(Facebook):

    def __init__(self):
        self.users = []
        super().__init__(self.users)
        self.all_posts = []
        self.postData = {}

    def userOptions(self, userName, userEmail):
        print("""
        1. Post Something
        2. View Profile
        3. Update Profile
        4. Delete Profile
        """)

        todo = {
            "1" : self.post,
            "2" : self.viewProfile,
            "3" : self.updateProfile,
            "4" : self.deleteProfile
        }

        userChoice = input("Enter your choice : ")

        todo.get(userChoice)(userName, userEmail)

    def post(self, userName, userEmail):
        print("Hello {}".format(userName))
        userpost = input("What's in your mind : ")
        current_time = datetime.now()
        self.postData['userPost'] = userpost
        self.postData['userName'] = userName
        self.postData['postTime'] =  current_time

        self.all_posts.append(self.postData)
        for posts in self.all_posts:
            print(posts)


    def viewProfile(self, userName, userEmail):
        pass

    def updateProfile(self, userName, userEmail):
        pass

    def deleteProfile(self, userName, userEmail):
        pass


# obj = Facebook()
# obj.homeScreen()

userObj = UserActivites()
userObj.homeScreen()

# obj = UserActivites()
# obj.userOptions('Ram','ram@gmail.com')
# obj.homeScreen()