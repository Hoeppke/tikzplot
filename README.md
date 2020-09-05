# tikzplot
Python package for simple latex / tikz based plots


## Quick start
Tikplot allows for matplotlib style generation of standalone
latex code, using the tikz library. There is no dependency
on matplotlib, and no graphics processing is done in python,
so that all the plotting can be handled by latex. As tikz only
supports 2d plots, so does tikzplot.


Use the following code as a starting point for creating
2d line plots.

    import unittest
    import tikzplot.plotter as plotter
    import numpy as np

    def test_single_plot():
        xarr = np.linspace(-1.0, +1.0)
        yarr = np.cos(8 * xarr)*np.exp(xarr)
        plt = plotter.Plotter()
        green = (0.2, 0.9, 0.2)
        plt.plot(xarr, yarr, label=r'$\cos(8 x)e^x$', color=green)
        plt.plot(xarr, yarr/2.0, label=r'$\frac{1}{2}\cos(8 x)e^x$')
        plt.parameters['grid'] = 'both'
        plt.parameters['title'] = r'{Hello World $\sin, \cos$!}'
        plt.set_xlabel(r'Some input $x \in [-1, +1]$')
        plt.set_ylabel(r'Some input $y=f(x)$')
        plt.save()

    if __name__ == '__main__':
        test_single_plot()
