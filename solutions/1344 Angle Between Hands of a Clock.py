"""
1344. Angle Between Hands of a Clock
Difficulty: Medium

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 60 minutos em 360° do relógio: O ponteiro se move 6° a cada minuto que passa
        minutesAngle = minutes * 6

        # 12 horas em 360° do relógio: O ponteiro se move 30° a cada hora
        # Precisamos ajustar o ângulo pois o ponteiro de horas se move conforme os minutos passam
        # Se a cada hora os minutos andam 360° graus e a hora anda 30° então a proporção é de
        # (360/30)*(minutos/60) = 30*minutos/60
        if hour == 12:
            hour = 0
        hourAngle = hour * 30 + 30 * minutes / 60

        hourMinutesAngle = max(hourAngle - minutesAngle, minutesAngle - hourAngle)
        if hourMinutesAngle > 180:
            return 360 - hourMinutesAngle
        return hourMinutesAngle
