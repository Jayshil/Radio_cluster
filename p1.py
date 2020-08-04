import numpy as np
import matplotlib.pyplot as plt

ra_r, dec_r = np.loadtxt('list_rossetti.dat', usecols=(1,2), unpack=True)
ra_l, dec_l = np.loadtxt('list_lovisari.dat', usecols=(1,2), unpack=True)

plt.figure(figsize=(10,10))

plt.scatter(ra_r, dec_r, marker='.', c='orangered', label='Rossetti et al.')
plt.scatter(ra_l, dec_l, marker='.', c='cornflowerblue', label='Lovisari et al.')

plt.xlabel('RA (in deg)')
plt.ylabel('DEC (in deg)')

plt.legend(loc='best')
plt.grid()
plt.show()
plt.savefig('ra_dec.png')
