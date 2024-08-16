time_sec = int(input("enter your time in secund"))
hour = time_sec // 3600
minute = (time_sec % 3600) // 60
secund = (time_sec % 3600) % 60
print(f"{hour:02}:{minute:02}:{secund:02}")
