class TA(Professor, Student):
    def get_role(self):
        return "I am a teaching assistant!"

ta = TA("Maureen", 123, 1213)
print(ta.study())