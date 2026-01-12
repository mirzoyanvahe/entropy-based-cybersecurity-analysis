import sys
import networkx as nx

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib.figure import Figure

from load_data import load_logs
from transitions import build_event_timeline, extract_transitions


USER_ID = "DTAA/FDP0500"


class GraphCanvas(FigureCanvas):
    def __init__(self, transitions, parent=None):
        self.fig = Figure(figsize=(10, 8))
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.draw_graph(transitions)

    def draw_graph(self, transitions):
        G = nx.DiGraph()

        for (src, dst), weight in transitions.items():
            G.add_edge(src, dst, weight=weight)

        pos = nx.spring_layout(G, seed=42)

        nx.draw(
            G,
            pos,
            ax=self.ax,
            with_labels=True,
            node_size=3000,
            font_size=10,
            arrows=True,
            arrowstyle='-|>',
            arrowsize=20
        )

        edge_labels = {
            (u, v): d["weight"]
            for u, v, d in G.edges(data=True)
        }

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edge_labels,
            ax=self.ax
        )

        self.ax.set_title("Interactive Event Transition Graph")
        self.ax.axis("off")


class GraphApp(QMainWindow):
    def __init__(self, transitions):
        super().__init__()
        self.setWindowTitle("Cybersecurity Event Graph – Application View")
        self.resize(1000, 800)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        canvas = GraphCanvas(transitions, self)
        toolbar = NavigationToolbar(canvas, self)

        layout.addWidget(toolbar)
        layout.addWidget(canvas)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    print("Launching desktop application...")

    # Load data
    logon, device, http = load_logs()

    # Build timeline
    timeline = build_event_timeline(logon, device, http, USER_ID)

    # Extract transitions
    transitions = extract_transitions(timeline)

    app = QApplication(sys.argv)
    window = GraphApp(transitions)
    window.show()
    sys.exit(app.exec_())