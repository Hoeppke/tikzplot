import unittest
import tikzplot.plotter as plotter
import numpy as np

class BasicPlot(unittest.TestCase):

    def single_plot(self):
        xarr = np.linspace(-1.0, +1.0)
        yarr = np.cos(8 * xarr)*np.exp(xarr)
        plt = plotter.Plotter()
        plt.plot(xarr, yarr, label=r'$\cos(8 x)e^x$', color=(0.2, 0.9, 0.2))
        plt.plot(xarr, yarr/2.0, label=r'$\frac{1}{2}\cos(8 x)e^x$')
        plt.parameters['grid'] = 'both'
        plt.parameters['title'] = r'{Hello World $\sin, \cos$!}'
        plt.save()

    def logplot(self):
        xarr = np.linspace(1.0, 400.0, num=600)
        plt = plotter.Plotter()
        for k in [-2.0, -3.0, -4.0, -5.0, -6.0, -7.0]:
            yarr = 1e-14*np.random.rand(len(xarr)) + (xarr**k) *(1.0 + 0.5*np.cos(2.0*xarr))
            yarr = np.abs(yarr)
            plt.plot(xarr, yarr, label=r'$\vert I_\omega - Q_{'+str(-k)+r'}\vert$', linewidth=0.5)
        plt.set_yscale('log')
        plt.parameters['grid'] = 'both'
        plt.save()

    def test_sctterplot(self):
        plt = plotter.Plotter()
        for k in [-2.0, -3.0, -4.0, -5.0, -6.0, -7.0]:
            xarr = np.linspace(1.0, 400.0, num=25)
            yarr = 1e-14*np.random.rand(len(xarr)) + (xarr**k) *(1.0 + 0.5*np.cos(2.0*xarr))
            scatter = plt.scatter(xarr, yarr)
            xarr = np.linspace(1.0, 400.0, num=800)
            yarr = 1e-14*np.random.randn(len(xarr)) + (xarr**k) *(1.0 + 0.5*np.cos(2.0*xarr))
            line = plt.plot(xarr, yarr, label=r'$\vert I_\omega - Q_{'+str(-k)+r'}\vert$', linewidth=0.5)
            line['color'] = scatter['color']
        plt.set_yscale('log')
        plt.parameters['grid'] = 'both'
        plt.save()


if __name__ == '__main__':
    unittest.main()
