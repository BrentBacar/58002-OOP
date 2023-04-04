class TempConversion():
    def __init__(self, temp):
        self.__temp = temp

    # K to F°
    def kf(self):
         return (self.__temp * 1.8) - 459.67

    # F° to K
    def fk(self):
         return (self.__temp + 459.67) / 1.8

    # K to C°
    def kc(self):
        return self.__temp - 273.15

    # C° to F°
    def cf(self):
        return (self.__temp * 9 / 5) + 32


    # C° to K
    def ck(self):
        return self.__temp + 273.15

    # F° to C°
    def fc(self):
        return (self.__temp - 32) * 5 / 9


# input
temp = float(input("Enter Your Temperature: "))
# tempconversion
temp_obj = TempConversion(temp)
# outputs
print("Fahrenheit(F°) to Celsius(C°):", temp_obj.fc())
print("Kelvin(K) to Celsius(C°):", temp_obj.kc())
print("Celsius(C°) to Fahrenheit(F°):", temp_obj.cf())
print("Kelvin(K) to Fahrenheit(F°):", temp_obj.kf())
print("Celsius(C°) to Kelvin(K):", temp_obj.ck())
print("Fahrenheit(F°) to Kelvin(K):", temp_obj.fk())
