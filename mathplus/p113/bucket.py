b_w = 1.00; #lbs
r_r = 0.6; #lb/ft
deep = 30; #ft
w_w =  40; #lbs
w_o =  20; #lbs
result = b_w*deep + r_r*deep*deep/2 + (w_w+w_o)/2*deep;
print("%g" % result)