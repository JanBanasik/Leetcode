class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourly_angle = self.calculate_angle((hour if hour < 12 else 0) + minutes / 60, 12)
        minutely_angle = self.calculate_angle(minutes, 60)
        print(hourly_angle, minutely_angle)
        return min(abs(hourly_angle - minutely_angle), 360 - abs(hourly_angle - minutely_angle))

    def calculate_angle(self, current_measure, measure_count):
        return 360 * (current_measure / measure_count)