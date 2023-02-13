"""Class-based Sphere Calculator.

Description: This module contains a class that should be used for making calculations of a sphere using pi and the radius.

Programmer: Aiden Ruthsatz

"""

import unittest

class Sphere:
        def __init__(self, user_input):
                total = 0
                sign = 1
                for i in range(user_input):
                        term = 1/(2*i+1)
                        total += term * sign
                        sign *= -1
                total *= 4
                self.pi = total
                self.valuelist = []
                

        def radius(self, user_rad):
            """Returns the user generated radius value"""
            self.valuelist.append(user_rad)
            return user_rad

        def diameter(self, user_rad):
            """Calculates the diameter of the sphere"""
            dia = round(2 * user_rad, 3)
            self.valuelist.append(dia)
            return dia

        def circumference(self, user_rad):
            """Calculates the circumference of the sphere"""
            cir = round(2*user_rad*self.pi, 3)
            self.valuelist.append(cir)
            return cir

        def surface_area(self, user_rad):
            """Calculates the surface area of the sphere"""
            surf = round(4*self.pi*user_rad**2, 3)
            self.valuelist.append(surf)
            return surf

        def volume(self, user_rad):
            """Calculates the volume of the sphere"""
            vol = round(4/3*self.pi*user_rad**3, 3)
            self.valuelist.append(vol)
            return vol

        def mass(self, user_rad):
            """Calculates the mass of the sphere"""
            density = 6.692
            mass = round((4/3*self.pi*user_rad**3)*density, 3)
            self.valuelist.append(mass)
            return mass

class Test(unittest.TestCase):
        """a unittest class"""
        def setUp(self):
            self.object = Sphere(12)
        

        def tearDown(self):
            pass

        def test_radius(self):
            """Tests if the radius value is correct for the given input"""
            result = self.object.radius(4.5)
            self.assertEqual(result, 4.5)
        
        def test_diameter(self):
            """Tests if the diameter value is correct"""
            result = self.object.diameter(4.5)
            self.assertEqual(result, 9.0)
        
        def test_circumference(self):
            """Tests if the circumference value is correct"""
            result = self.object.circumference(4.5)
            self.assertEqual(result, 27.526) 


        def test_surface_area(self):
            """Tests if the surface area value is correct"""
            result = self.object.surface_area(4.5)
            self.assertEqual(result, 247.731)

        def test_volume(self):
            """Tests if the volume value is correct"""
            result = self.object.volume(4.5)
            self.assertEqual(result, 371.596)

        def test_mass(self):
            """Tests if the mass value is correct"""
            result = self.object.mass(4.5)
            self.assertEqual(result, 2486.72)

        






    
    #def test_sphere1(self):
        #"""Test value list"""
        #result = self.object.valuelist
        #self.assertEqual(result, [4.5,9.0,27.525624893346,247.73062404011398,371.5959360601709,2486.720004114664,])


if __name__ == '__main__':
    unittest.main()
     

        

       
                
                



