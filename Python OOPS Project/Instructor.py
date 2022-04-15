import User.py
class Instructor(User.User):
    def __init__(self, id, username, password, display_name, job_title, image_100x100, course_id_list):
        User.__init__(id, username, password)
        self.display_name = ""
        self.job_title = ""
        self.image_100x100 = ""
        self.course_id_list=[]
    def view_courses(args=[]):
        pass
    def view_reviews(args=[]):
        pass
    def __str__():
        pass

