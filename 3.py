class Monitor:
    displayResolution = 0
    screenSize = 0
    rate = 0
    def __init__(self,px,dm,Hz):
        print("Create nem Monitor")
        self.displayResolution = px
        self.screenSize = dm
        self.rate = Hz
    def printInfo(self,name):
        print(f"{name:-^10}")
        print("Display Resolution:", lg.displayResolution)
        print("Screen Size:", lg.screenSize)
        print("Image refresh rate:", lg.rate)


lg = Monitor(1500,500,1000)
philips = Monitor(500,345,6789)
print("___LG___")
print("Display Resolution:",lg.displayResolution)
print("Screen Size:",lg.screenSize)
print("Image refresh rate:",lg.rate)
print("___PHILIPS___")
print("Display Resolution:",philips.displayResolution)
print("Screen Size:",philips.screenSize)
print("Image refresh rate:",philips.rate)
lg.printInfo("LG")
philips.printInfo("PHILIPS")