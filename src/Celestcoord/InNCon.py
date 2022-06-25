#To take input from User and convert RA and Dec to degrees
from decimal import Decimal
from astropy.coordinates import Angle
from astropy import units as u
import numpy as np

class INC:
    def In(self): #Method to take input
            print("Please separate the values by colons")
            print("Enter Right Ascension in HMS format:")
            self.RA=input()
            print("Enter Declination in DMS format:")
            self.Dec=input()

    def Convert(self):#Method to convert RA and Dec to degrees
        try:
            h,m,s = self.RA.split(':')
            d,m2,s2= self.Dec.split(':')
            #Converting to RA
            angle = Angle('{0}h{1}m{2}s'.format(h,m,s))
            self.RA_deg=angle.to(u.degree).value

            #Converting Dec to degrees
            angle = Angle('{0}d{1}m{2}s'.format(self.d,self.m2,self.s2))
            self.Dec_deg=angle.to(u.degree).value

            print("RA in degrees:",self.RA_deg)
            print("Dec in degrees:",self.Dec_deg)
        except ValueError:
            print("Input.py says: Please enter the correct values in the correct format")
            self.RA_deg=np.NaN
            self.Dec_deg=np.NaN
    def main():
        obj=INC()
        obj.In()
        obj.Convert()
        return obj.RA_deg, obj.Dec_deg
if __name__ == '__main__':
    INC.main()