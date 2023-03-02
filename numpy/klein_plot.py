import numpy as np
import matplotlib.pyplot as plt

def klein_bottle(u, v):
    x=(-2/15)*np.cos(u)*(3*np.cos(v)-30*np.sin(u)+90*np.power(np.cos(u),4)*np.sin(u)-60*np.power(np.cos(u),6)*np.sin(u)+5*np.cos(u)*np.cos(v)*np.sin(u))
    t1=3*np.cos(v)-3*np.cos(u)*np.cos(u)*np.cos(v)-48*np.power(np.cos(u),4)*np.cos(v)+48*np.power(np.cos(u),6)*np.cos(v)-60
    y=-1/15*np.sin(u)*(t1*np.sin(u)+5*np.cos(u)*np.cos(v)*np.sin(v)-5*np.power(np.cos(u),3)*np.cos(v)*np.sin(u)-80*np.power(np.cos(u),5)*np.cos(v)*np.sin(u)+80*np.power(np.cos(u),7)*np.cos(v)*np.sin(u))
    z=(2/15)*(3+5*np.cos(u)*np.sin(u))*np.sin(v)
    return x, y, z

def torus(u,v):
    r = 1
    b = 3
    x = (r*np.cos(u)+b)*np.cos(v)
    y = (r*np.cos(u)+b)*np.sin(v)
    z = (r*np.sin(u))
    return x, y, z

def saddle(x,y):
    z = np.power(x,2)-np.power(y,2)
    return x, y, z

def bowl(x,y):
    z = np.power(x,2)+np.power(y,2)
    return x, y, z

def wave(x,y):
    z = np.cos(x)+np.sin(y)
    return x, y, z

def fedora(x,y):
    d = np.power(x,2)+np.power(y,2)
    z=np.sin(d/10)
    return x, y, z

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2* np.pi, 100)

#u = np.linspace(-10, 10, 100)
#v = np.linspace(-10, 10, 100)

u, v = np.meshgrid(u, v)
x,y,z= klein_bottle(u, v)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.plot_surface(x, y, z,
                 rstride=1, cstride=1,
                 cmap=plt.get_cmap(''),
                 linewidth=0, antialiased=False)

plt.show()
