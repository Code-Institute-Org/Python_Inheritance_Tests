from employee import Employee


class Developer(Employee):
    def __init__(self, fname, sname, no_of_years, prog_language):
        self.prog_language = prog_language
        super(Developer, self).__init__(fname, sname, no_of_years)


    def details(self):
        return super(Developer, self).details() + 'Programming Language: %s' % self.prog_language

    def calculate_salary(self):
        standard = super(Developer, self).calculate_salary()
        if self.prog_language.lower() == 'python':
            bonus = standard * .05
        else:
            bonus = standard * .01

        return standard + bonus
