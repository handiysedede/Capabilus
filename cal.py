# -*- coding: utf-8 -*-
avarage_speed_per_km= float(12.62)
goal_kg=float(20)
cal_to_burn=float(154323)
cal_per_km=float(90)

goal_km=(cal_to_burn/cal_per_km)
goal_time=(goal_km/avarage_speed_per_km)
print(round(goal_km))
print("km koşman gerekmektedir")
print("Onu da ")
print(round(goal_time))
print("saatte anca yaparsın")