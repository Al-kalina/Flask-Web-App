class User:
    def __init__(self, id, age, sex, university, faculty=None):
        self.id = id
        self.age = age
        self.sex = sex
        self.university = university
        self.faculty = faculty

    def returnAnswers(self):
        return self.id, self.age, self.sex, self.university, self.faculty


class Page1:
    def __init__(self, id, q5, q6, q7, q8_1, q8_2):
        self.id = id
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8_1 = q8_1
        self.q8_2 = q8_2

    def returnAnswers(self):
        return self.id, self.q5, self.q6, self.q7, self.q8_1, self.q8_2


class Page2:
    def __init__(self, id, q9, q10, q11, q12, q13 = None):
        self.id = id
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13

    def returnAnswers(self):
        return self.id, self.q9, self.q10, self.q11, self.q12, self.q13


class Page3:
    def __init__(self, id, q14, q15, q16, q17):
        self.id = id
        self.q14 = q14
        self.q15 = q15
        self.q16 = q16
        self.q17 = q17

    def returnAnswers(self):
        return self.id, self.q14, self.q15, self.q16, self.q17


class Page4:
    def __init__(self, id, q18, q19, q20, q21, q22=None):
        self.id = id
        self.q18 = q18
        self.q19 = q19
        self.q20 = q20
        self.q21 = q21
        self.q22 = q22

    def returnAnswers(self):
        return self.id, self.q18, self.q19, self.q20, self.q21, self.q22


class Page5:
    def __init__(self, id, q23, q24, q25, q26, q27):
        self.id = id
        self.q23 = q23
        self.q24 = q24
        self.q25 = q25
        self.q26 = q26
        self.q27 = q27

    def returnAnswers(self):
        return self.id, self.q23, self.q24, self.q25, self.q26, self.q27
