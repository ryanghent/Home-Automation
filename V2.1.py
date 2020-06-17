import matplotlib.pyplot as plt
import numpy as np

h = open("humidityvalues.txt", 'r')
x = h.read()
x = x.replace("\x00","").split(", ") #remove null characters
h.close()
x.pop(0)#remove initial first value error
th = []

j = 0
while True:
	x[j] = float(x[j])#convert to float
	th.append(j*10)#10s interval between readings, so *10 for time axis
	j += 1
	if (j+1) > len(x):
		break

X = np.array(x)
TH = np.array(th)

fig = plt.figure(figsize = (10,8))
plt.plot(TH,X)
#plt.show()
plt.yscale('linear')
fig.savefig("0-Humidity-plot.png", dpi = 300)

#####
t = open("temperaturevalues.txt", 'r')
y = t.read()
y = y.replace("\x00","").split(", ")
t.close()
y.pop(0)
tt = []

j = 0
while True:
	y[j] = float(y[j])
	tt.append(j*10)
	j += 1
	if (j+1) > len(y):
		break

Y = np.array(y)
TT = np.array(tt)

fig = plt.figure(figsize = (10,8))
plt.plot(TT,Y)
#plt.show()
plt.yscale('linear')
fig.savefig("1-Temperature-plot.png", dpi = 300)
####################
#Light value plot
l = open("lightvalues.txt", 'r')
z = l.read()
z = z.replace("\x00","").split(", ")
l.close()
z.pop(0)
tl = []

j = 0
while True:
	z[j] = int(z[j])
	tl.append(j*10)
	j += 1
	if (j+1) > len(z):
		break

Z = np.array(z)
TL = np.array(tl)

fig = plt.figure(figsize = (10,8))
plt.plot(TL,Z)
#plt.show()
plt.yscale('linear')
fig.savefig("2-Light-plot.png", dpi = 300)
