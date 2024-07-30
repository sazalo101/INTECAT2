x1, y1=2.00,7.2
x2, y2=4.25,7.1

x=4.0
y=y1+(y2-y1)/(x2-x1)*(x-x1)

print(f"The value of y at x={x} is{y:.2f}")