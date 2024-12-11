class Rectangle:
    def __init__(self, wid, heigt):
        """
        Constructor method to initialize the width and height of the rectangle.
        
        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        self.wid = wid
        self.heigt= higt

    def __str__(self):
        """
        Method to return a string representation of the rectangle object.
        
        Returns:
        str: A string representing the dimensions of the rectangle.
        """
        return f"Rectangle: {self.wid} x {self.heigt}"

    def area(self):
        """
        Method to calculate and return the area of the rectangle.
        
        Returns:
        float: The area of the rectangle (width * height).
        """
        return self.wid * self.heigt

    def perimeter(self):
        """
        Method to calculate and return the perimeter of the rectangle.
        
        Returns:
        float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.wid+ self.heigt)


# Example of how to use the Rectangle class
if __name__ == "__main__":
    # Taking input from the user
    wid = float(input("Enter the widof the rectangle: "))
    heigt = float(input("Enter the heigt of the rectangle: "))

    # Creating a Rectangle object
    rect = Rectangle(wid, heigt)

    # Display the rectangle details using the __str__ method
    print(rect)

    # Calculate and display the area of the rectangle
    print(f"Area: {rect.area()}")

    # Calculate and display the perimeter of the rectangle
    print(f"Perimeter: {rect.perimeter()}")
class Rectangle:
    def __init__(self, wid, heigt):
        """
        Constructor method to initialize the width and height of the rectangle.
        
        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        self.wid = wid
        self.heigt = heigt

    def __str__(self):
        """
        Method to return a string representation of the rectangle object.
        
        Returns:
        str: A string representing the dimensions of the rectangle.
        """
        return f"Rectangle: {self.wid} x {self.heigt}"

    def area(self):
        """
        Method to calculate and return the area of the rectangle.
        
        Returns:
        float: The area of the rectangle (width * height).
        """
        return self.wid * self.heigt

    def perimeter(self):
        """
        Method to calculate and return the perimeter of the rectangle.
        
        Returns:
        float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.wid + self.heigt)


# Main program to take input from the user and perform operations
if __name__ == "__main__":
    # Taking user input for width and height
    wid = float(input("Enter the wid of the rectangle: "))
    heigt = float(input("Enter the heigt of the rectangle: "))

    # Create an instance of the Rectangle class
    rect = Rectangle(wid, heigt)

    # 1. Display rectangle details using the __str__ method
    print(rect)

    # 2. Calculate and display the area using the area method
    print(f"Area of the rectangle: {rect.area()}")

    # 3. Calculate and display the perimeter using the perimeter method
    print(f"Perimeter of the rectangle: {rect.perimeter()}")
