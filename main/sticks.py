class LoliPop:
    counter_sticks = 1
    length_main_stick = 13

    def counter(self, count):
        return self.counter_sticks + count

    def stick_enlarger(self, centimeters):
        if not isinstance(centimeters, (int, float)):
            raise TypeError("Сантиметры должны быть числами!")
        if centimeters < 1:
            raise ValueError("Нельзя увеличить на число меньше 1!")
        return self.length_main_stick + centimeters

    def stick_reducing(self, centimeters):
        if not isinstance(centimeters, (int, float)):
            raise TypeError("Сантиметры должны быть числами!")
        if centimeters < 1:
            raise ValueError("Нельзя уменьшить на число меньше 1!")
        return self.length_main_stick - centimeters
