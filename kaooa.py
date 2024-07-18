import turtle
import time
import math


class Game:
    def __init__(self):
        self.points = []
        self.occupy = [0]*10
        self.flag = 0
        self.crows_count = 0
        self.vulture_count = 0
        self.crow_select = 0
        self.points = []
        self.cow_prev = 0
        self.vulture_position = -1
        self.crows_died = 0
        self.myturtle = turtle.Turtle()
        self.myturtle.speed(0)
        self.myturtle.hideturtle()
        self.valid_moves_crows = []
        self.valid_moves_vultures = []

    def setup(self):
        self.myturtle.penup()
        self.myturtle.setpos(-400,80)
        self.myturtle.pendown()
        for i in range(5):
            point = self.myturtle.pos()
            self.myturtle.forward(800)
            self.points.append(point)
            self.myturtle.right(144)
        self.points.append(self.find_intersection_point(self.points[0],self.points[1],self.points[2],self.points[3]))
        self.points.append(self.find_intersection_point(self.points[0],self.points[1],self.points[3],self.points[4]))
        self.points.append(self.find_intersection_point(self.points[0],self.points[4],self.points[3],self.points[2]))
        self.points.append(self.find_intersection_point(self.points[2],self.points[1],self.points[0],self.points[4]))
        self.points.append(self.find_intersection_point(self.points[2],self.points[1],self.points[3],self.points[4]))

        self.valid_moves_vultures = [[5,6,7,8],
                        [5,6,8,9],
                        [5,7,8,9],
                        [5,6,7,9],
                        [6,7,8,9],
                        [0,1,2,3,6,7],
                        [0,1,3,4,5,9],
                        [0,2,3,4,5,8],
                        [0,1,2,4,7,9],
                        [1,2,3,4,6,8]]
        
        self.valid_moves_crows = [[self.points[5],self.points[7]],
                     [self.points[6],self.points[9]],
                     [self.points[7],self.points[8]],
                     [self.points[5],self.points[6]],
                     [self.points[8],self.points[9]],
                     [self.points[0],self.points[3],self.points[6],self.points[7]],
                     [self.points[1],self.points[3],self.points[5],self.points[9]],
                     [self.points[0],self.points[2],self.points[5],self.points[8]],
                     [self.points[2],self.points[4],self.points[7],self.points[9]],
                     [self.points[1],self.points[4],self.points[6],self.points[8]]]
        
        for i in range(len(self.points)):
            self.draw_circle(self.points[i][0],self.points[i][1])


    def find_intersection_point(self,point1_line1, point2_line1, point1_line2, point2_line2):
    
        m1 = (point2_line1[1] - point1_line1[1]) / (point2_line1[0] - point1_line1[0])
        m2 = (point2_line2[1] - point1_line2[1]) / (point2_line2[0] - point1_line2[0])
        

        b1 = point1_line1[1] - m1 * point1_line1[0]
        b2 = point1_line2[1] - m2 * point1_line2[0]
        
        x_intersect = (b2 - b1) / (m1 - m2)
        y_intersect = m1 * x_intersect + b1
        
        return x_intersect, y_intersect
    

    def draw_circle(self,x,y):
        # print(x,y)
        self.myturtle.up()
        self.myturtle.setheading(270)
        self.myturtle.setpos(x-50,y)
        self.myturtle.color("white")
        self.myturtle.pencolor("black")
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(50)
        self.myturtle.end_fill()
        self.myturtle.color("black")

    def remove_crow(self,point):
        self.myturtle.up()
        self.myturtle.setheading(270)
        self.myturtle.setpos(point[0]-50,point[1])
        self.myturtle.color("white")
        self.myturtle.pencolor("black")
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(50)
        self.myturtle.end_fill()
        self.myturtle.color("black")

    def place_crow(self,point):
        self.myturtle.up()
        self.myturtle.setheading(270)
        self.myturtle.setpos(point[0]-50,point[1])
        self.myturtle.color("green")
        self.myturtle.pencolor("black")
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(50)
        self.myturtle.end_fill()
        self.myturtle.color("black")

    def remove_vulture(self,point):
        self.myturtle.up()
        self.myturtle.setheading(270)
        self.myturtle.setpos(self.points[point][0]-50,self.points[point][1])
        self.myturtle.color("white")
        self.myturtle.pencolor("black")
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(50)
        self.myturtle.end_fill()
        self.myturtle.color("black")

    def place_vulture(self,point):
        self.myturtle.up()
        self.myturtle.setheading(270)
        self.myturtle.setpos(self.points[point][0]-50,self.points[point][1])
        self.myturtle.color("yellow")
        self.myturtle.pencolor("black")
        self.myturtle.down()
        self.myturtle.begin_fill()
        self.myturtle.circle(50)
        self.myturtle.end_fill()
        self.myturtle.color("black")

    def playing_game(self,x,y):
        selected = -1

        for i in range(len(self.points)):
            if (self.points[i][0] - x)*(self.points[i][0] - x) + (self.points[i][1] - y)*(self.points[i][1] - y) < 2500:
                selected = i
                break

        i =  selected
        if i != -1:
            if self.occupy[i] == 0 and self.crows_count < 7 and self.flag == 0:
                self.occupy[i] = 1
                self.crows_count += 1
                self.place_crow(self.points[i])
                self.flag = 1
            elif self.occupy[i] == 0 and self.vulture_count < 1 and self.flag == 1:
                self.occupy[i] = 2
                self.vulture_position = i
                self.vulture_count += 1
                self.place_vulture(i)
                self.flag = 0
            elif self.crow_select == 0 and self.occupy[i] == 1 and self.flag == 0:
                self.crow_prev = i
                self.crow_select = 1
            elif self.crow_select == 1 and self.flag == 0:
                if self.points[i] in self.valid_moves_crows[self.crow_prev]:
                    if self.occupy[i] == 0:
                        self.remove_crow(self.points[self.crow_prev])
                        self.occupy[self.crow_prev] = 0
                        self.place_crow(self.points[i])
                        self.occupy[i] = 1
                        self.flag = 1
                        countt = 0
                        for j in range(len(self.valid_moves_vultures[self.vulture_position])):
                            pos = self.valid_moves_vultures[self.vulture_position][j]
                            if self.occupy[pos] == 0:
                                countt += 1
                        
                        if countt == 0:
                            self.myturtle.write("crow wins",font=("Verdana",
                                                30, "normal"),align="center")
                            time.sleep(3)
                            turtle.bye()
                            return

                self.crow_prev = -1
                self.crow_select = 0
            elif self.flag == 1:
                countt = 0
                sure_kill = 0
                flg = 0

                #if i in valid_moves
                if self.occupy[i] == 0 and i in self.valid_moves_vultures[self.vulture_position]:
                    valid_move = 0

                    for j in range(len(self.valid_moves_vultures[self.vulture_position])):
                        if valid_move:
                            break
                        pos = self.valid_moves_vultures[self.vulture_position][j]
                        if self.occupy[pos] == 1:
                            for k in range(len(self.valid_moves_vultures[self.vulture_position])):
                                if k != j:
                                    pos1 = self.valid_moves_vultures[self.vulture_position][k]
                                    dist1 = (self.points[pos][0] - self.points[self.vulture_position][0])**2 + (self.points[pos][1] - self.points[self.vulture_position][1])**2
                                    dist2 = (self.points[pos][0] - self.points[pos1][0])**2 + (self.points[pos][1] - self.points[pos1][1])**2
                                    dist =  (self.points[pos1][0] - self.points[self.vulture_position][0])**2 + (self.points[pos1][1] - self.points[self.vulture_position][1])**2
                                    if int(math.sqrt(dist)) == int(math.sqrt(dist1) + math.sqrt(dist2)):
                                        if self.occupy[pos1] == 0:
                                            # print("jilp")
                                            sure_kill = 1
                                            # print(self.vulture_position,pos1,i)
                                            if pos1 == i:
                                                valid_move = 1
                                                # print("peop")
                                                self.remove_crow(self.points[pos])
                                                self.occupy[pos] = 0
                                                self.crows_died += 1
                                                if self.crows_died == 4:
                                                    self.myturtle.write("vulture wins",font=("Verdana",30, "normal"),align="center")
                                                    time.sleep(3)
                                                    turtle.bye()
                                                    return
                                                break
                                                
                    if sure_kill:
                        if valid_move:
                            self.remove_vulture(self.vulture_position)
                            self.occupy[self.vulture_position] = 0
                            self.place_vulture(i)
                            self.vulture_position = i
                            self.occupy[i] = 2
                            self.flag = 0                      
                    else:
                        for j in range(len(self.valid_moves_vultures[self.vulture_position])):
                            pos = self.valid_moves_vultures[self.vulture_position][j]
                            if self.occupy[pos] == 0:
                                countt += 1
                                if pos != i:
                                    dist1 = (self.points[pos][0] - self.points[self.vulture_position][0])**2 + (self.points[pos][1] - self.points[self.vulture_position][1])**2
                                    dist2 = (self.points[pos][0] - self.points[i][0])**2 + (self.points[pos][1] - self.points[i][1])**2
                                    dist =  (self.points[i][0] - self.points[self.vulture_position][0])**2 + (self.points[i][1] - self.points[self.vulture_position][1])**2
                                    if int(math.sqrt(dist)) == int(math.sqrt(dist1) + math.sqrt(dist2)):
                                        flg = 1
                                        break
                        
                        if flg == 0:
                            self.remove_vulture(self.vulture_position)
                            self.occupy[self.vulture_position] = 0
                            self.place_vulture(i)
                            self.vulture_position = i
                            self.occupy[i] = 2
                            self.flag = 0
       
    def run(self):
        ws = turtle.Screen()
        self.setup()
        turtle.onscreenclick(self.playing_game)
        turtle.done()   

game = Game()
game.run()

