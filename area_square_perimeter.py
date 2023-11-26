class Hexagon:
  def __init__(self, side):
      self.side = side

  def calarea(self):
      return 1.5 * 1.732 * self.side ** 2

  def calperi(self):
      return 6 * self.side

  def sum_of_angles(self):
      return 6 * 120


class Square:
  def __init__(self, side):
      self.side = side

  def calarea(self):
      return self.side ** 2

  def calperi(self):
      return 4 * self.side


def main():
  cnic = input("Enter the last digit of your CNIC number: ")
  hexagon_side = int(cnic[-1])
  square_side = hexagon_side + 1

  while True:
      print("\nEnter 1 to calculate area, perimeter and sum of all angles of hexagon")
      print("Enter 2 to calculate area and perimeter of square")
      print("Enter any other key to exit")
      print ("")
      choice = input("Enter your choice: ")

      if choice == "1":
          hexagon = Hexagon(hexagon_side)
          print("\nHexagon:")
          print(f"Area of hexagon: {hexagon.calarea():.2f}")
          print(f"Perimeter of hexagon: {hexagon.calperi():.2f}")
          print(f"Sum of all angles of hexagon: {hexagon.sum_of_angles()} degrees")
      elif choice == "2":
          square = Square(square_side)
          print("\nSquare:")
          print(f"Area of square: {square.calarea():.2f}")
          print(f"Perimeter of square: {square.calperi():.2f}")
      else:
          print("Program Exit.")
          break


if __name__ == "__main__":
  main()
