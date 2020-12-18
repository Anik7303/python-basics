temps = [221, 230, 240, 320]

new_temps = [temp / 10 for temp in temps]

print(new_temps)

temps = [221, 230, -9999, 240, 320, -9999, 218, 157]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

temps = [221, 230, -9999, 240, 320, -9999, 218, 157]

# this is wrong -> new_temps = [temp / 10 for temp in temps if temp != -9999 else 0]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)