import User
class Student(User.User):
    def __init__(self, id, username, password, user_title, user_image_50x50, user_initials, review_id):
        User.__init__(id, username, password)
        self.user_title=""
        self.user_image_50x50=""
        self.user_initials=""
        self.review_id=-1

    def view_courses(args=[]):
        pass
    def view_reviews(args=[]):
        pass
    def __str__():
        pass