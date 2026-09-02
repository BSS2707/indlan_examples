import indlan as ind

hpp = r'''
maano name = aalao("Enter the Name:")
maano age = number_dalao("Enter the age:")

agar age >= 18 {
    chhap(f"App Votr de sakte {name}")
}
nahito {
    chhap(f"App Votr de nahisakte {name}")
}
'''

ind.run(hpp)