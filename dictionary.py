alient_0 = {'x_pos':0 , 'y_pos': 25, 'speed':'medium'}

print(f"original position: {alient_0['x_pos']}")
alient_0['speed'] = "fast"

if alient_0['speed'] == 'slow':
    x_increment = 1
elif alient_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

alient_0['x_pos'] = alient_0['x_pos'] +  x_increment

print(f"new position: {alient_0['x_pos']}")
