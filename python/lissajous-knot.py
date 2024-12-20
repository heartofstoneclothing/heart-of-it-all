import math
import time
import os

class LissajousKnot:
    def __init__(self, A, B, C, delta_x=0, delta_y=0, twists=0):
        """
        Initialize a Lissajous knot.

        Parameters:
        - A, B, C: Frequencies for x, y, and z axes.
        - delta_x, delta_y: Phase shifts in radians for x and y.
        - twists: Number of twists to add to the knot.
        """
        self.A = A
        self.B = B
        self.C = C
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.twists = twists

    def generate_points(self, steps=100):
        """
        Generate points for the Lissajous knot.
        
        Parameters:
        - steps: Number of points to generate.
        
        Returns:
        - A list of (x, y, z) tuples.
        """
        points = []
        for t in range(steps):
            t_norm = 2 * math.pi * t / steps  # Normalize t to [0, 2π]
            x = math.sin(self.A * t_norm + self.delta_x)
            y = math.sin(self.B * t_norm + self.delta_y)
            z = math.sin(self.C * t_norm + self.twists * t_norm)
            points.append((x, y, z))
        return points

    def __str__(self):
        """
        String representation of the knot parameters.
        """
        return f"Lissajous Knot(A={self.A}, B={self.B}, C={self.C}, twists={self.twists})"


class LissajousKnotLibrary:
    def __init__(self):
        """
        Initialize the library to hold multiple knots.
        """
        self.knots = []

    def add_knot(self, A, B, C, delta_x=0, delta_y=0, twists=2):
        """
        Add a new knot to the library.
        """
        knot = LissajousKnot(A, B, C, delta_x, delta_y, twists)
        self.knots.append(knot)
        print(f"Added: {knot}")

    def list_knots(self):
        """
        List all knots in the library.
        """
        for i, knot in enumerate(self.knots):
            print(f"{i + 1}: {knot}")

    def plot_knot(self, knot_index, steps=1000, animate=True, color='cyan'):
        """
        ASCII-style plot of a knot. Limited to 2D (x, y) view.
        
        Parameters:
        - knot_index: Index of the knot to plot.
        - steps: Number of points to sample.
        - animate: Boolean flag to animate the plot.
        - color: Color for the ASCII plot (using ANSI escape codes).
        """
        if knot_index < 1 or knot_index > len(self.knots):
            print("Invalid knot index!")
            return

        knot = self.knots[knot_index - 1]
        points = knot.generate_points(steps)

        # Generate an ASCII plot (x, y projection)
        grid_size = 20
        grid = [['[]' for _ in range(grid_size)] for _ in range(grid_size)]

        # ANSI color codes
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'cyan': '\033[96m',
            'reset': '\033[0m'
        }

        color_code = colors.get(color, colors['cyan'])

        for x, y, _ in points:
            i = int((x + 1) * (grid_size - 1) / 2)  # Scale x to grid
            j = int((y + 1) * (grid_size - 1) / 2)  # Scale y to grid
            grid[j][i] = color_code + '][' + colors['reset']

        if animate:
            for i in range(steps):
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
                print(f"Plot for {knot}:")
                for row in grid:
                    print(''.join(row))
                time.sleep(0.01)  # Slow down the animation
        else:
            print(f"Plot for {knot}:")
            for row in grid:
                print(''.join(row))


# Example usage
if __name__ == "__main__":
    library = LissajousKnotLibrary()
    library.add_knot(2, 4, 6, twists=2)
    library.add_knot(2, 4, 6, twists=3, delta_x=0.5, delta_y=1.0)
    library.list_knots()
    
    # Plot the first knot with color and motion
    library.plot_knot(1, animate=False, color='green')  # Animate with green color
    
    # Plot the second knot with color
    library.plot_knot(2, animate=False, color='yellow')  # Static plot with yellow color
