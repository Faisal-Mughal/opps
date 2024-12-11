#TASK 1
class Veh:
    def __init__(self, make, model):
       
        self.make = make
        self.model = model

    def display_info(self):
        
        print(f"Make: {self.make}, Model: {self.model}")



class gadi(Veh):
    def __init__(self, make, model, num_doors):
       
        super().__init__(make, model) 
        self.num_doors = num_doors

    def additional_info(self):
    
        print(f"Number of doors: {self.num_doors}")



class mengigadi(gadi):
    def __init__(self, make, model, num_doors, features):
       
        super().__init__(make, model, num_doors)  
        self.features = features

    def additional_info(self):
       
        print(f"Number of doors: {self.num_doors}")
        print(f"Luxury Features: {', '.join(self.features)}")



def main():
   
    veh = Veh("Toyota", "Corolla")
    print("Veh Info:")
    veh.display_info()
    print()


    gadi = gadi("rolla", "altis", 3)
    print("gadi Info:")
    gadi.display_info()
    gadi.additional_info()
    print()

   
    mengi_gadi = mengigadi("kia", "7 Series", 4, ["Leather Seats", "Sunroof", "Heated Steering Wheel"])
    print("mengi gadi Info:")
    mengi_gadi.display_info()
    mengi_gadi.additional_info()


if __name__ == "__main__":
    main()