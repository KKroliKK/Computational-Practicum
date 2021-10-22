import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from ivp import InitialValueProblem
from graph import Graph


class GUI:
    """
    Main class of the application
    It runs graphical user interface
    """
    def __init__(self, IVP: InitialValueProblem):
        self._IVP = IVP

    def startApplication(self):

        tab1Col1 = sg.Column([[sg.Frame('Variant 12', [[sg.Canvas(key="-CANVAS1-")]])]])

        tab1Col2 = sg.Column([[sg.Text(self._IVP.getException())],
                              [sg.Frame('Parameters', [[sg.Text("x0"), sg.Input(key='-x0-', default_text=self._IVP.getX0(), size=(10, None))],
                                                       [sg.Text("y0"), sg.Input(key='-y0-', default_text=self._IVP.getY0(), size=(10, None))],
                                                       [sg.Text("X "), sg.Input(key='-X-', default_text=self._IVP.getX(), size=(10, None))],
                                                       [sg.Text("N "), sg.Input(key='-N-', default_text=self._IVP.getN(), size=(10, None))]])],
                              [sg.Button('Apply', key='-apply1-')],
                              [sg.Frame('Show', [[sg.Checkbox(text="Euler's Method", key='-EM1-', default=True, enable_events=True)],
                                                 [sg.Checkbox(text="Improved Euler's Method", key='-IEM1-', default=True, enable_events=True)],
                                                 [sg.Checkbox(text='Runge-Kutta Method', key='-RK1-', default=True, enable_events=True)],
                                                 [sg.Checkbox(text='Exact Solution', key='-ES1-', default=True, enable_events=True)]])]])
        # Layout for the first page                                                                                                                        
        tab1Layout = [[tab1Col1, tab1Col2]]


        tab2Col1 = sg.Column([[sg.Frame('Variant 12', [[sg.Canvas(key="-CANVAS2-")]])]])

        tab2Col2 = sg.Column([[sg.Frame('Parameters', [[sg.Text("min N"), sg.Input(key='-minN-', default_text=self._IVP.getN(), size=(10, None))],
                                                       [sg.Text("max N"), sg.Input(key='-maxN-', default_text=self._IVP.getN() + 100, size=(10, None))]])],
                              [sg.Button('Apply', key='-apply2-')],
                              [sg.Frame('Show', [[sg.Checkbox(text="Euler's Method", key='-EM2-', default=True, enable_events=True)],
                                                 [sg.Checkbox(text="Improved Euler's Method", key='-IEM2-', default=True, enable_events=True)],
                                                 [sg.Checkbox(text='Runge-Kutta Method', key='-RK2-', default=True, enable_events=True)]])]])
        # Layout for second page
        tab2Layout = [[tab2Col1, tab2Col2]]

        layout = [[sg.TabGroup([[sg.Tab('Page 1', tab1Layout),
                                 sg.Tab('Page 2', tab2Layout)]])]]

        # Create window with application
        window = sg.Window('Computational Practicum', layout, finalize=True, font='Arial 15', )


        def draw_figure(canvas, figure):
            """Aluxiliary finction for adding graphs to the interface"""

            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
            return figure_canvas_agg

        # Add the plots to the window
        fig_canvas_agg1 = draw_figure(window['-CANVAS1-'].TKCanvas, Graph(self._IVP).plotPage1())
        fig_canvas_agg2 = draw_figure(window['-CANVAS2-'].TKCanvas, Graph(self._IVP).plotPage2(self._IVP.getN(), self._IVP.getN() + 100))


        while True:
            """Execution of GUI"""

            event, values = window.read()

            if event == '-EM1-' or event == '-IEM1-' or event == '-RK1-' or event == '-ES1-':
                """Defines which graphs to show"""
                fig_canvas_agg1.get_tk_widget().destroy()
                fig_canvas_agg1 = draw_figure(window['-CANVAS1-'].TKCanvas, Graph(self._IVP).plotPage1(values['-EM1-'], values['-IEM1-'], values['-RK1-'], values['-ES1-']))

            elif event == '-apply1-':
                """Redraw graphs for changed conditions"""
                fig_canvas_agg1.get_tk_widget().destroy()
                self._IVP.recompute(float(values['-x0-']), float(values['-y0-']), float(values['-X-']), int(values['-N-']))
                fig_canvas_agg1 = draw_figure(window['-CANVAS1-'].TKCanvas, Graph(self._IVP).plotPage1(values['-EM1-'], values['-IEM1-'], values['-RK1-'], values['-ES1-']))
                fig_canvas_agg2.get_tk_widget().destroy()
                fig_canvas_agg2 = draw_figure(window['-CANVAS2-'].TKCanvas, Graph(self._IVP).plotPage2(int(values['-minN-']), int(values['-maxN-']), values['-EM2-'], values['-IEM2-'], values['-RK2-']))

            elif event == '-apply2-' or event == '-EM2-' or event == '-IEM2-' or event == '-RK2-':
                """Redraw graphs of global errors for changed N's or to define which graphs to show"""
                fig_canvas_agg2.get_tk_widget().destroy()
                fig_canvas_agg2 = draw_figure(window['-CANVAS2-'].TKCanvas, Graph(self._IVP).plotPage2(int(values['-minN-']), int(values['-maxN-']), values['-EM2-'], values['-IEM2-'], values['-RK2-']))

            elif event == sg.WIN_CLOSED:
                break

        window.close()