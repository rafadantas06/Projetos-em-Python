import turtle

tela = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.speed(3)

def desenhar_tronco():
    tartaruga.penup()
    tartaruga.goto(-20, -150)
    tartaruga.color("brown")
    tartaruga.begin_fill()
    tartaruga.pendown()
    for i in range(2):
        tartaruga.forward(40)
        tartaruga.left(90)
        tartaruga.forward(100)
        tartaruga.left(90)
    tartaruga.end_fill()

def desenhar_folha(x, y, tamanho):
    tartaruga.penup()
    tartaruga.goto(x, y)
    tartaruga.color("green")
    tartaruga.begin_fill()
    tartaruga.pendown()
    tartaruga.goto(x + tamanho, y)
    tartaruga.goto(x + tamanho/2, y + tamanho)
    tartaruga.goto(x, y)
    tartaruga.end_fill()

def desenhar_folhas():
    x = -60
    y = -50
    tamanho = 120
    for i in range(3):
        desenhar_folha(x, y + i * 40, tamanho)
        x += 10
        tamanho -= 20

def desenhar_arvore():
    desenhar_tronco()
    desenhar_folhas()
    tartaruga.hideturtle()

desenhar_arvore()
tela.mainloop()