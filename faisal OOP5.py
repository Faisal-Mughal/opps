
class Item:
    def __init__(self, title, author):
       
        self.title = title
        self.author = author

    def display_info(self):
        
        print(f"Title: {self.title}, Author: {self.author}")


class kitab(Item):
    def __init__(self, title, author, pages):
       
        super().__init__(title, author)  
        self.pages = pages

    def additional_info(self):
       
        print(f"Pages: {self.pages}")



class khbr(Item):
    def __init__(self, title, author, issue_number):
      
        super().__init__(title, author)  
        self.issue_number = issue_number

    def additional_info(self):
      
        print(f"Issue Number: {self.issue_number}")



if __name__ == "__main__":
   
    my_kitab = kitab("1888", "sarfaraz", 25)
    my_kitab.display_info() 
    my_kitab.additional_info()  
    
    print()  

    my_khbr = khbr("pakvind", "Bobby", 56)
    my_khbr.display_info() 
    my_khbr.additional_info()  