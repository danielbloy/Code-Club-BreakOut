import tkinter as tk

class Game(tk.Frame):
  def __init__(self, master):
    super(Game, self).__init__(master)
    self.live = 3
    self.width=610
    self.height=400
    self.canvas = tk.Canvas(self, width=self.width,height=self.height,bg='#aaaaff')
    self.canvas.pack()
    self.pack()
    
    self.ball = None

    self.setup_game()

  def setup_game(self):
    self.add_ball()
    self.text = self.draw_text(300, 200, 'Press Space to start')
    lambda_: self.start_game()

  def add_ball(self):
    if self.ball is not None:
      self.ball.delete()

    x = 200
    self.ball = Ball(self.canvas, x, 310)

  def draw_text(self, x, y, text, size='40'):
    font = ('Helvetica', size)
    return self.canvas.create_text(x, y, text=text, font=font)

  def start_game(self):
    pass

class GameObject(object):
  def __init__(self, canvas, item):
    self.canvas = canvas
    self.item = item

  def get_position(self):
    return self.canvas.coords(self.item)

  def move(self, x, y):
    self.canvas.move(self.item, x, y)

  def delete(self):
    self.canvas.delete(self.item)

class Ball(GameObject):
  def __init__(self, canvas, x, y):
    self.radius = 10
    self.direction = [1, -1]
    self.speed = 10
    item = canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius,fill='white')
    super(Ball, self).__init__(canvas, item)


if __name__ == '__main__':
  root = tk.Tk()
  root.title('Hello, Pong!')
  game = Game(root)
  game.mainloop()

