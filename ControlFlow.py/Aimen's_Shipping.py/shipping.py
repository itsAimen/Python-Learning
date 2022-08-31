# Ground Shipping

# Weight of Package	Price per Pound	Flat Charge
# 2 lb or less	$1.50	$20.00
# Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
# Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
# Over 10 lb	$4.75	$20.00

weight = 51

#Ground shipping

if weight <= 2:
    cost_ground = weight * 1.5 + 20
elif weight <= 6:
    cost_ground = weight * 3.0 + 20
elif weight <= 10:
    cost_ground = weight * 4.0 + 20
else:
    cost_ground = weight * 4.75 + 20

print(cost_ground)
