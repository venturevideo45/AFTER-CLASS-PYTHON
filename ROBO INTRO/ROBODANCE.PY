class fruit:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    # instance method
    def intro(self):
        print("hello, I am", self.name)
        print("I am a", self.typ, "robot")


ROBO = fruit('CHATBOT', 'AI, INTERACTIVE AND VIRTUAL')
ROBO.intro()