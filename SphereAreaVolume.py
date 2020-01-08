radius=int(input("Enter the radius "))

a=0
v=0
p=22/7

def circle():
    area=areaOfSphere(radius,p)
    volume=volumeOfSphere(radius,p)
    print("The surface area of the sphere is ",area," and the volume of the Sphere is ",volume)

def areaOfSphere(r,pi):
    a=4*pi*r
    return a

def volumeOfSphere(r,pi):
    v=4/3
    v=v*pi*r*r*r
    return v

circle()
