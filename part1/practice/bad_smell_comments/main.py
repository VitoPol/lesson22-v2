class Unit:
    def move_to_object(self, field, coordinate_x, coordinate_y, direction, is_fly, is_creep, points_per_action=1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param coordinate_x: x-координата юнита
        :param coordinate_y: у-координата юнита
        :param direction: направление перемещения
        :param is_fly: летит ли юнит
        :param is_creep: крадется ли юнит
        :param points_per_action: базовый параметр скорости
        """
        if is_fly and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            points_per_action *= 1.2
            if direction == 'UP':
                new_y = coordinate_y + points_per_action
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - points_per_action
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - points_per_action
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + points_per_action
        if is_creep:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = coordinate_y + points_per_action
                new_x = coordinate_x
            elif direction == 'DOWN':
                new_y = coordinate_y - points_per_action
                new_x = coordinate_x
            elif direction == 'LEFT':
                new_y = coordinate_y
                new_x = coordinate_x - points_per_action
            elif direction == 'RIGHT':
                new_y = coordinate_y
                new_x = coordinate_x + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)

