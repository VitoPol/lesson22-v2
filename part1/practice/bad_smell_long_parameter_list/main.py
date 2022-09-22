# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self,x_coord, y_coord, direction, state, speed):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = direction
        self.state = state
        self.speed = speed
    def move(self, field):
        speed = self._get_speed()

        if self.direction == 'UP':
            new_y = self.y_coord + speed
            new_x = self.x_coord
        elif self.direction == 'DOWN':
            new_y = self.y_coord - speed
            new_x = self.x_coord
        elif self.direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - speed
        elif self.direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + speed

        field.set_unit(x=new_x, y=new_y, unit=self)

    def _get_speed(self):
        if self.state == "fly":
            return sleff.speed * 1.2
        elif self.state == "crawl":
            return sleff.speed * 0.5
        else:
            raise ValueError("косячина")

#     ...
