
class Cors:
    def __init__(self, cors_code, cors_name):
        
        self.cors_code = cors_code
        self.cors_name = cors_name

    def display_info(self):
       
        print(f"Cors Code: {self.cors_code}, Cors Name: {self.cors_name}")

class UnderCors(Cors):
    def __init__(self, cors_code, cors_name, year_level):
        
        super().__init__(cors_code, cors_name) 
        self.year_level = year_level

    def additional_info(self):
        
        print(f"Year Level: {self.year_level}")



class GraduateCors(Cors):
    def __init__(self, cors_code, cors_name, research_area):
        
        super().__init__(cors_code, cors_name)  
        self.research_area = research_area

    def additional_info(self):
        
        print(f"Research Area: {self.research_area}")

def register_cors():
   
    cors_code = input("Enter the cors code: ")
    cors_name = input("Enter the cors name: ")
    
    cors_type = input("Is this an undercors or graduate cors? (U/G): ").upper()

    if cors_type == 'U':
        year_level = int(input("Enter the year level (1-4): "))
        cors = UnderCors(cors_code, cors_name, year_level)
    elif cors_type == 'G':
        research_area = input("Enter the research area: ")
        cors = GraduateCors(cors_code, cors_name, research_area)
    else:
        print("Invalid cors type. Please enter 'U' for Under or 'G' for Graduate.")
        return
    
   
    cors.display_info()
    cors.additional_info()



if __name__ == "__main__":
    register_cors()
