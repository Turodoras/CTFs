#!/usr/bin/env python3

import gmpy2
import binascii

f = open("factors")
factors = []
e = 65537
n = 7735208939848985079680614633581782274371148157293352904905313315409418467322726702848189532721490121708517697848255948254656192793679424796954743649810878292688507385952920229483776389922650388739975072587660866986603080986980359219525111589659191172937047869008331982383695605801970189336227832715706317
ct = 5300731709583714451062905238531972160518525080858095184581839366680022995297863013911612079520115435945472004626222058696229239285358638047675780769773922795279074074633888720787195549544835291528116093909456225670152733191556650639553906195856979794273349598903501654956482056938935258794217285615471681

for factor in f:
    factors.append(int(factor[:-1]))

phi = 1
for factor in factors:
    phi *= factor - 1

d = gmpy2.invert(e, phi)
pt = pow(ct, d, n)

readable = binascii.unhexlify(hex(pt)[2:])
print(readable)