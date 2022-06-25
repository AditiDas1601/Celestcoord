
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from InNCon import INC
import math

class CSphere:

    def CelestialSphere(self):
        fig = plt.figure()
        self.ax = fig.gca(projection='3d')
        self.u=np.linspace(0,np.pi,100)
        self.v=np.linspace(0,2*np.pi,100)
        r=1
        #Converting r,u,v to Cartesian Co-ordinates
        self.x=r* np.outer(np.cos(self.u), np.sin(self.v))
        self.y=r* np.outer(np.sin(self.u), np.sin(self.v))
        z=r*np.outer(np.ones(np.size(self.u)), np.cos(self.v))
        #Plotting a wireframe Celestial Sphere
        self.plot1=self.ax.plot_wireframe(self.x,self.y,z,rstride=5,cstride=5,label="Celestial Sphere")
        

    def EqPlane(self):
        zcircle=0*np.outer(np.ones(np.size(self.u)), np.ones(np.size(self.v)))
        self.PL=self.ax.plot_surface(self.x,self.y,zcircle,rstride=5,cstride=5,color="yellow",label="Equtorial Plane")
        self.PL._edgecolors2d = self.PL._edgecolors3d
        self.PL._facecolors2d = self.PL._facecolors3d

    def VEquVector(self): 
        class Arrow3D(FancyArrowPatch):

            def __init__(self, xs, ys, zs, *args, **kwargs):
                FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
                self._verts3d = xs, ys, zs

            def draw(self, renderer):
                xs3d, ys3d, zs3d = self._verts3d
                xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
                self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
                FancyArrowPatch.draw(self, renderer)

        a = Arrow3D([0, 0], [0, 1.5], [0, 0], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
        self.ax.add_artist(a)

    def Plot(self):
        self.CelestialSphere()
        self.EqPlane()
        self.VEquVector()
        first_legend = plt.legend(handles=[self.plot1,self.PL])
        plt.gca().add_artist(first_legend)
        # legend for vector
        fake2Dline = mpl.lines.Line2D([0],[0], linestyle="none", c='k', marker = 'o',label="Vernal Equinox")
        self.ax.legend(handles=[fake2Dline],loc='lower left')
        self.ax.set_xlabel('X', fontsize=20)
        self.ax.set_ylabel('Y',fontsize=20)
        self.ax.set_zlabel('Z',fontsize=20)
        self.ax.invert_xaxis()
    
    def RDPlt(self):
        try:
            RA_deg,Dec_deg=INC.main() 
            if( math.isnan(RA_deg)==True or math.isnan(Dec_deg)==True):
                raise Exception("RDEmpty") 
            x_deg=math.cos(math.radians(RA_deg))*math.cos(math.radians(Dec_deg))
            y_deg=math.sin(math.radians(RA_deg))*math.cos(math.radians(Dec_deg))
            z_deg=math.sin(math.radians(Dec_deg))
            self.ax.scatter([x_deg],[y_deg],[z_deg],color="r")
            plt.show()
        except Exception:
            print("CelSphere.py says: RA and Dec Values are empty")

if __name__ == '__main__':
    obj=CSphere()
    obj.Plot()
    obj.RDPlt()