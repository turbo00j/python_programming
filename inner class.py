class mobile:
    def mobile_model(self):
        self.mobile_model="s1256"
        self.mobike_model="samsung s7"
    def display(self):
        print(self.__dict__)
    class SIM:
        def sim(self):
            self.sim_model=['3g','4g','5g']
            self.sim_name='Airtel'
        def sim_display(self):
            print(self.__dict__)


m1=mobile()
m1.mobile_model()
m1.display()
s1=m1.SIM()
s1.sim()
s1.sim_display()
