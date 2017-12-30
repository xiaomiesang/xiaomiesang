class myclass:
    name = 'sam'
    def sayhi(self):
        print ('hello%s'%self.name)

mc = myclass()
print (mc.name)
mc.name = 'lily'
mc.sayhi()
