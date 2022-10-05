class Computer:
    def __init__(self,gen,ram):
        self.gen=gen
        self.ram=ram
    def config(self):
        print("Config is:",self.gen,self.ram)

c1=Computer("i3","4GB")
c2=Computer("i5","8GB")

c1.config()
c2.config()