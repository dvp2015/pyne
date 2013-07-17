from pyne import transmute as tm, nucname as nn
import numpy as np
import tables as tb
nuc = nn.zzaaam('FE56')
inp = {nuc : 1.}
t_sim = 3153600
tree = True
# fluxin1 from ALARA
list = [0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00, 0.00000E+00,\
 0.00000E+00, 8.98755E+13, 9.77446E+12, 8.06925E+12, 1.70726E+12, 1.28302E+12,\
 1.89143E+12, 2.04175E+12, 2.07250E+12, 1.80384E+12, 1.54256E+12, 1.42579E+12,\
 1.24872E+12, 1.17419E+12, 1.14707E+12, 1.19572E+12, 1.22437E+12, 1.26141E+12,\
 4.38938E+11, 9.07635E+11, 1.39910E+12, 1.45818E+12, 1.48523E+12, 1.43566E+12,\
 1.41561E+12, 1.40784E+12, 1.35321E+12, 2.71459E+12, 2.62508E+12, 2.66233E+12,\
 1.40292E+12, 1.42487E+12, 1.37130E+12, 1.37665E+12, 1.52025E+12, 1.59680E+12,\
 1.07723E+12, 2.77969E+11, 2.78790E+11, 5.53898E+11, 1.09314E+12, 1.64561E+12,\
 1.68331E+12, 1.74677E+12, 1.80254E+12, 1.93480E+12, 1.96231E+12, 1.93938E+12,\
 1.92934E+12, 1.93774E+12, 1.90789E+12, 1.82967E+12, 1.88061E+12, 1.89368E+12,\
 1.81907E+12, 3.42703E+12, 1.43106E+12, 2.05052E+12, 1.78729E+12, 1.86431E+12,\
 1.83209E+12, 1.87158E+12, 1.80219E+12, 1.73173E+12, 1.60686E+12, 1.29878E+12,\
 1.48781E+12, 1.61671E+12, 1.60349E+12, 1.59722E+12, 3.03722E+12, 2.90241E+12,\
 1.42928E+12, 1.35835E+12, 2.69252E+12, 2.55807E+12, 2.86956E+11, 1.05539E+11,\
 2.25492E+11, 5.88210E+11, 1.19440E+12, 2.20287E+12, 1.08398E+12, 1.03200E+12,\
 9.75760E+11, 9.46015E+11, 9.12835E+11, 9.29522E+11, 8.90411E+11, 8.30228E+11,\
 8.45313E+11, 8.07049E+11, 7.71896E+11, 7.07755E+11, 8.21782E+11, 7.22692E+11,\
 7.33346E+11, 6.91441E+11, 1.63354E+12, 1.56807E+12, 5.29641E+11, 4.48653E+11,\
 1.07702E+12, 8.07461E+11, 1.82087E+12, 7.58110E+11, 1.26259E+12, 1.12779E+12,\
 1.54243E+12, 6.74366E+11, 8.42541E+11, 4.34202E+11, 2.89471E+11, 3.71251E+11,\
 2.64038E+11, 2.30016E+11, 5.82748E+11, 9.47843E+11, 1.71492E+12, 1.80379E+12,\
 5.48701E+11, 8.73235E+11, 1.82674E+12, 1.52497E+12, 1.48336E+12, 9.67624E+11,\
 6.31697E+11, 6.03210E+11, 5.84716E+11, 1.49733E+11, 1.84075E+11, 7.72799E+11,\
 1.82977E+11, 1.80083E+12, 1.48029E+12, 1.45254E+12, 1.44214E+12, 1.34832E+12,\
 1.10171E+12, 1.27549E+12, 1.33060E+12, 1.27163E+12, 1.32883E+12, 1.32596E+12,\
 1.35429E+12, 1.34940E+12, 1.34862E+12, 1.34699E+12, 1.32883E+12, 1.33697E+12,\
 1.33352E+12, 1.32882E+12, 1.32283E+12, 1.31655E+12, 1.30955E+12, 1.30178E+12,\
 1.29327E+12, 1.28377E+12, 1.27355E+12, 1.26193E+12, 1.24944E+12, 1.23535E+12,\
 1.21970E+12, 1.20272E+12, 1.18312E+12, 1.16152E+12, 1.13736E+12, 2.82140E+12,\
 5.36871E+13]
phi = np.zeros((175,1))
for i in np.arange(len(list)):
    phi[i] = list[i]
print('Flux initialized.')
filename = 'test.tree'
tol = 1e-7
print('Begin transmutation.')
with open(filename,'w') as tree:
    out = tm.transmute(inp,t_sim,phi,tree,tol)
h5file = tb.openFile('h5test.h5','w')
group = h5file.createGroup('/','transmute_parentGroup','Transmute Output')
print('Writing to hdf5.')
tm.write_hdf5(h5file, group, out, 'test_volume')
h5file.close()
print('Closed hdf5.')
print('Total density: ' + str(sum(out.values())) + '.')
