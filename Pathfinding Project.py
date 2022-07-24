import numpy as np
import matplotlib.pyplot as plt
import math

running = True


# weight Gamemode
class Personal_gamemode:
    def __init__(self, Height, Width, repeat_grid, poisson_choice, poisson_weight, minimum_weight, maximum_weight):
        self.Height = Height
        self.Width = Width
        if not np.any(repeat_grid == None):
            self.grid = repeat_grid
        else:
            if poisson_choice:
                if not poisson_weight == None:
                    grid = np.ones((self.Height, self.Width), dtype=int)
                    for i in range(self.Height):
                        for j in range(self.Width):
                            grid[i][j] = np.random.poisson(poisson_weight)
            else:
                self.grid = np.random.randint(minimum_weight, maximum_weight, (self.Height, self.Width))
        self.temporary_grid = np.ones((self.Height, self.Width), dtype=float) * np.nan
        self.finished = False
        self.pathlength = self.grid[0][0]
        self.personal_algorithm()

    def personal_algorithm(self):
        x, y = 0, 0
        while not self.finished:
            down = 10000
            right = 10000
            if x < self.Height - 1:
                down = self.grid[x + 1, y]
            if y < self.Width - 1:
                right = self.grid[x, y + 1]
            if down < right:
                x, y = x + 1, y
            elif right < down:
                x, y = x, y + 1
            elif right == down:
                x, y = x, y + 1

            self.pathlength += self.grid[x][y]
            self.temporary_grid[x, y] = self.grid[x][y]

            if x == self.Height - 1 and y == self.Width - 1:
                self.finished = True

    def display(self):
        self.temporary_grid[0][0] = self.grid[0][0]
        plt.figure(figsize=(10, 10))
        plt.matshow(self.temporary_grid, cmap=plt.cm.Wistia)
        for j in range(self.Height):
            for i in range(self.Width):
                number = self.grid[j, i]
                plt.text(i, j, str(number))
        plt.show()
        print('The path length is: ' + str(self.pathlength))
        print(" ")

    def get_path(self):
        return self.pathlength

    def get_grid(self):
        return self.grid


# Dijkstras Gamemode
class Gamemode_one_two:
    def __init__(self, Height, Width, repeat_grid, dijkstras, poisson_choice, poisson_weight, minimum_weight,
                 maximum_weight):
        self.dijkstras = dijkstras
        self.Height = Height
        self.Width = Width
        if not np.any(repeat_grid == None):
            self.grid = repeat_grid
        else:
            if poisson_choice:
                if not poisson_weight == None:
                    grid = np.ones((self.Height, self.Width), dtype=int)
                    for i in range(self.Height):
                        for j in range(self.Width):
                            grid[i][j] = np.random.poisson(poisson_weight)
            else:
                self.grid = np.random.randint(minimum_weight, maximum_weight, (self.Height, self.Width))

        self.grid_distance = np.ones((self.Height, self.Width), dtype=int) * np.inf
        if dijkstras:
            self.grid_distance[0, 0] = self.grid[0][0]
        else:
            self.grid_distance[0, 0] = 0
        self.Boolean_grid = np.ones((self.Height, self.Width), dtype=int) * np.nan
        self.visited = np.zeros((self.Height, self.Width), dtype=bool)
        self.finished = False
        self.temp_distance_grid = None
        self.dijkstras_algorithm()

    def get_path(self):
        return self.grid_distance[self.Height - 1, self.Width - 1]

    def get_grid(self):
        return self.grid

    def dijkstras_algorithm(self):
        x, y = 0, 0
        while not self.finished:
            if x < self.Height - 1:
                if self.grid_distance[x + 1, y] > self.grid[x + 1, y] + self.grid_distance[x, y] and not self.visited[
                    x + 1, y]:
                    if self.dijkstras:
                        self.grid_distance[x + 1, y] = self.grid[x + 1, y] + self.grid_distance[x, y]
                    else:
                        self.grid_distance[x + 1, y] = abs(self.grid[x + 1, y] - self.grid[x, y])
                        self.grid_distance[x + 1, y] += self.grid_distance[x, y]
                    self.Boolean_grid[x + 1, y] = np.ravel_multi_index([x, y], (self.Height, self.Width))
            if x > 0:
                if self.grid_distance[x - 1, y] > self.grid[x - 1, y] + self.grid_distance[x, y] and not self.visited[
                    x - 1, y]:
                    if self.dijkstras:
                        self.grid_distance[x - 1, y] = self.grid[x - 1, y] + self.grid_distance[x, y]
                    else:
                        self.grid_distance[x - 1, y] = abs(self.grid[x - 1, y] - self.grid[x, y])
                        self.grid_distance[x - 1, y] += self.grid_distance[x, y]
                    self.Boolean_grid[x - 1, y] = np.ravel_multi_index([x, y], (self.Height, self.Width))
            if y < self.Width - 1:
                if self.grid_distance[x, y + 1] > self.grid[x, y + 1] + self.grid_distance[x, y] and not self.visited[
                    x, y + 1]:
                    if self.dijkstras:
                        self.grid_distance[x, y + 1] = self.grid[x - 1, y] + self.grid_distance[x, y]
                    else:
                        self.grid_distance[x, y + 1] = abs(self.grid[x - 1, y] - self.grid[x, y])
                        self.grid_distance[x, y + 1] += self.grid_distance[x, y]
                    self.Boolean_grid[x, y + 1] = np.ravel_multi_index([x, y], (self.Height, self.Width))
            if y > 0:
                if self.grid_distance[x, y - 1] > self.grid[x, y - 1] + self.grid_distance[x, y] and not self.visited[
                    x, y - 1]:
                    if self.dijkstras:
                        self.grid_distance[x, y - 1] = self.grid[x - 1, y] + self.grid_distance[x, y]
                    else:
                        self.grid_distance[x, y - 1] = abs(self.grid[x - 1, y] - self.grid[x, y])
                        self.grid_distance[x, y - 1] += self.grid_distance[x, y]
                    self.Boolean_grid[x, y - 1] = np.ravel_multi_index([x, y], (self.Height, self.Width))

            self.visited[x, y] = True
            self.temp_distance_grid = self.grid_distance
            for i in range(self.Height):
                for j in range(self.Width):
                    if self.visited[i][j]:
                        self.temp_distance_grid[i][j] = np.Infinity

            current_distance = np.unravel_index(np.argmin(self.temp_distance_grid), np.shape(self.temp_distance_grid))
            x, y = current_distance[0], current_distance[1]
            if current_distance[0] == self.Height - 1 and current_distance[1] == self.Width - 1:
                self.finished = True

        x, y = self.Height - 1, self.Width - 1
        path = []
        self.temporary_grid = np.ones((self.Height, self.Width), dtype=float) * np.nan
        self.temporary_grid[self.Height - 1][self.Width - 1] = self.grid[self.Height - 1][self.Width - 1]

        while x > 0 or y > 0:
            path.append([x, y])
            unravel_path = np.unravel_index(int(self.Boolean_grid[x, y]), (self.Height, self.Width))
            x = unravel_path[0]
            y = unravel_path[1]
            self.temporary_grid[x, y] = self.grid[x][y]

    def display(self):
        plt.matshow(self.temporary_grid, cmap=plt.cm.Wistia)
        for j in range(self.Height):
            for i in range(self.Width):
                number = self.grid[j, i]
                plt.text(i, j, str(number))
        plt.show()
        print('The path length is: ' + str(self.grid_distance[self.Height - 1, self.Width - 1]))
        print(" ")


# Main Loop
print("Welcome to my Task 1")
print("You can choose to do a series of large tests in which results will be displayed using matplotlib" + "\n" +
      " or you can choose to do individual runs and select the specific diameters or range. The choice of" + "\n" +
      " gamemode will be given.")
while running:
    series_single_choice = input("Would you like to run a series of tests or a single simple test '(O)ne/(M)ultiple'")
    if series_single_choice == "O" or series_single_choice == "o":
        print("Minimum max width and max height of the grid is 3")
        single_diameter_choice = False
        while not single_diameter_choice:
            single_random_choice = input(
                "Do you want a randomly generated max for the height and width of the grid? (Y/N) ")
            if single_random_choice == "N" or single_random_choice == "n":
                random_specific_choice = input("Would you like to select a specific grid size or choose limits for " +
                                               "random generation (S/R)")
                if random_specific_choice == "R" or random_specific_choice == "r":
                    valid = False
                    while not valid:
                        max_Height = input("Input a max grid height: ")
                        max_Width = input("Input a max grid width: ")
                        try:
                            int(max_Height)
                            int(max_Width)
                            if int(max_Height) > 2 and int(max_Width) > 2:
                                valid = True
                        except ValueError:
                            valid = False
                    Width, Height = np.random.randint(2, max_Width), np.random.randint(2, max_Height)
                    single_diameter_choice = True
                if random_specific_choice == "S" or random_specific_choice == "s":
                    valid = False
                    while not valid:
                        Height = input("Input a grid height: ")
                        Width = input("Input a grid width: ")
                        try:
                            int(Height)
                            int(Width)
                            if int(Height) > 1 and int(Width) > 1:
                                valid = True
                        except ValueError:
                            valid = False

                    Height = int(Height)
                    Width = int(Width)
                    single_diameter_choice = True
            if single_random_choice == "Y" or single_random_choice == "y":
                Width, Height = np.random.randint(2, 20), np.random.randint(2, 20)
                single_diameter_choice = True
        minimum_weight = 0
        maximum_weight = 10
        poisson_weight = 0
        poisson_choice = False
        repeat = True
        gamemode_choice = False
        grid = None
        dijkstras = False
        while repeat:
            while not gamemode_choice:
                print(" ")
                print("Which Gamemode would you like to use (1/2/3)")
                print("1 - Naive Algorithm ")
                print("2 - Dijkstras Algorithm ")
                print("3 - Weight Algorithm ")
                gamemode_option = input("Choose by selecting a number in respect to the option: ")
                if gamemode_option == "1":
                    Personal_algorithm = Personal_gamemode(Height, Width, grid, poisson_choice, poisson_weight,
                                                           minimum_weight, maximum_weight)
                    Personal_algorithm.display()
                    grid = Personal_algorithm.get_grid()
                    gamemode_choice = True
                elif gamemode_option == "2":
                    dijkstras = True
                    dijkstras_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras, poisson_choice,
                                                           poisson_weight, minimum_weight, maximum_weight)
                    dijkstras_algorithm.display()
                    grid = dijkstras_algorithm.get_grid()
                    gamemode_choice = True
                elif gamemode_option == "3":
                    dijkstras = False
                    weight_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras, poisson_choice, poisson_weight,
                                                        minimum_weight, maximum_weight)
                    weight_algorithm.display()
                    grid = weight_algorithm.get_grid()
                    gamemode_choice = True
                print("")
            repeat_option = input("Would you like to use the same grid (Y/N) ")
            if repeat_option == "Y" or repeat_option == "y":
                gamemode_choice = False
            elif repeat_option == "N" or repeat_option == "n":
                repeat = False

    if series_single_choice == "M" or series_single_choice == "m":
        multiple_confirmed = False
        while not multiple_confirmed:
            print("Run one grid size up to 50 times and recieve a calculated avergae for that grid size - option (A)")
            print("Run multiple grid sizes but you choose the weight range of the cells and which random distribution" +
                  " is used. - option (B)")
            multiple_option = input()
            if multiple_option == "A" or multiple_option == "a":
                print("Minimum max width and max height of the grid is 3")
                print("Maximum max width and max height of the grid is 50")
                single_diameter_choice = False
                while not single_diameter_choice:
                    single_random_choice = input(
                        "Do you want a randomly generated max for the height and width of the grid? (Y/N) ")
                    if single_random_choice == "N" or single_random_choice == "n":
                        random_specific_choice = input(
                            "Would you like to select a specific grid size or choose limits for " +
                            "random generation (S/R)")
                        if random_specific_choice == "R" or random_specific_choice == "r":
                            valid = False
                            while not valid:
                                max_Height = input("Input a max grid height: ")
                                max_Width = input("Input a max grid width: ")
                                try:
                                    int(max_Height)
                                    int(max_Width)
                                    if int(max_Height) > 2 and int(max_Width) > 2 and int(max_Height) < 51 and int(
                                            max_Width) < 51:
                                        valid = True
                                except ValueError:
                                    valid = False
                            Width, Height = np.random.randint(2, max_Width), np.random.randint(2, max_Height)
                            single_diameter_choice = True
                        if random_specific_choice == "S" or random_specific_choice == "s":
                            valid = False
                            while not valid:
                                Height = input("Input a grid height: ")
                                Width = input("Input a grid width: ")
                                try:
                                    int(Height)
                                    int(Width)
                                    if int(Height) > 1 and int(Width) > 1 and int(Height) < 51 and int(Width) < 51:
                                        valid = True
                                except ValueError:
                                    valid = False

                            Height = int(Height)
                            Width = int(Width)
                            single_diameter_choice = True
                    if single_random_choice == "Y" or single_random_choice == "y":
                        Width, Height = np.random.randint(2, 20), np.random.randint(2, 20)
                        single_diameter_choice = True

                valid = False
                while not valid:
                    run = input("How many times would you like the program to run (minimum is 1/maximmum is 50) ")
                    try:
                        print(run)
                        if int(run) > 0 and int(run) < 51:
                            valid = True
                    except ValueError:
                        valid = False
                minimum_weight = 0
                maximum_weight = 10
                poisson_choice = False
                runs = int(run)
                gamemode_choice = False
                grid = None
                dijkstras = False
                mean = 0
                while not gamemode_choice:
                    print(" ")
                    print("Which Gamemode would you like to use (1/2/3)")
                    print("1 - Naive Algorithm ")
                    print("2 - Dijkstras Algorithm ")
                    print("3 - Weight Algorithm ")
                    gamemode_option = input("Choose by selecting a number in respect to the option: ")
                    if gamemode_option == "1":
                        for i in range(runs):
                            Personal_algorithm = Personal_gamemode(Height, Width, grid, poisson_choice, poisson_weight,
                                                                   minimum_weight, maximum_weight)
                            mean = mean + Personal_algorithm.get_path()
                        mean = mean / runs
                        print("Gamemode: Naive")
                        gamemode_choice = True
                    elif gamemode_option == "2":
                        dijkstras = True
                        for i in range(runs):
                            dijkstras_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras, poisson_choice,
                                                                   poisson_weight, minimum_weight, maximum_weight)

                            mean = mean + dijkstras_algorithm.get_path()
                        mean = mean / runs
                        print("Gamemode: Dijkstras")
                        gamemode_choice = True
                    elif gamemode_option == "3":
                        dijkstras = False
                        for i in range(runs):
                            weight_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras, poisson_choice,
                                                                poisson_weight, minimum_weight, maximum_weight)
                            mean = mean + weight_algorithm.get_path()
                        mean = mean / runs
                        print("Gamemode: Weight")
                        gamemode_choice = True
                    print("Grid Size: Height = ", Height, " Width = ", Width)
                    print("Mean for ", runs, " runs is ", mean)
                    print("")
            elif multiple_option == "B" or multiple_option == "b":
                runs = 30
                Height = 0
                Width = 0
                mean = 0
                means = []
                grid = None
                y_axis = [5, 10, 15, 20, 25]
                poisson_choice = False
                weights_decided = False
                random_decided = False
                dijkstras = False
                poisson_weight = 0
                weights = []
                while not random_decided:
                    distribution_choice = input("Would you like to use Poisson distribution or generic random (P/R) ")
                    if distribution_choice == "P" or distribution_choice == "p":
                        Poisson_choice = True
                        while not weights_decided:
                            valid = False
                            while not valid:
                                Poisson_weight = input("Please input a weight between 0 and 10 ")
                                try:
                                    if int(Poisson_weight) > 0 and int(Poisson_weight) < 10:
                                        valid = True
                                except ValueError:
                                    valid = False
                            weight_range = (Poisson_weight)
                            weights.append(weight_range)
                            if len(weights) == 3:
                                weights_decided = True
                        gamemode_choice = False
                        while not gamemode_choice:
                            print(" ")
                            print("Which Gamemode would you like to use (1/2/3)")
                            print("1 - Naive Algorithm ")
                            print("2 - Dijkstras Algorithm ")
                            print("3 - Weight Algorithm ")
                            gamemode_option = input("Choose by selecting a number in respect to the option: ")
                            if gamemode_option == "1" or gamemode_option == "2" or gamemode_option == "3":
                                plt.figure(figsize=(10, 10))
                                plt.title('mean/grid size - Line')
                                plt.xlabel('Grid size', fontsize=14)
                                plt.ylabel('mean', fontsize=14)
                                for j in range(len(weights)):
                                    poisson_weight = weights[j]
                                    Height = 0
                                    Width = 0
                                    summ = 0
                                    sum_of_squares = []
                                    for x in range(5):
                                        Height += 5
                                        Width += 5
                                        for i in range(runs):
                                            if gamemode_option == "1":
                                                Personal_algorithm = Personal_gamemode(Height, Width, grid,
                                                                                       poisson_choice, poisson_weight,
                                                                                       minimum_weight, maximum_weight)
                                                mean = mean + Personal_algorithm.get_path()
                                                sum_of_squares.append(Personal_algorithm.get_path())
                                            elif gamemode_option == "2":
                                                dijkstras_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras,
                                                                                       poisson_choice, poisson_weight,
                                                                                       minimum_weight, maximum_weight)
                                                mean = mean + dijkstras_algorithm.get_path()
                                                sum_of_squares.append(dijkstras_algorithm.get_path())
                                            elif gamemode_option == "3":
                                                weight_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras,
                                                                                    poisson_choice, poisson_weight,
                                                                                    minimum_weight, maximum_weight)
                                                mean = mean + weight_algorithm.get_path()
                                                sum_of_squares.append(weight_algorithm.get_path())
                                        summ += mean
                                        mean = mean / runs
                                        means.append(mean)
                                        mean = 0
                                        sum_of_squares[:] = [sum_of_squares - mean for sum_of_squares in sum_of_squares]
                                        sum_of_squares[:] = [sum_of_squares ** 2 for sum_of_squares in sum_of_squares]
                                        SD = math.sqrt(sum(sum_of_squares) / 150)
                                        print("Standard Deviation: ", SD, " Weight range:", weights[j])
                                        SD = 0
                                        sum_of_squares = []

                                    pw = str(poisson_weight)
                                    plt.plot(y_axis, means, label=("Weight: " + pw))
                                    means = []
                                plt.legend()
                                plt.show()

                                gamemode_choice = True
                                random_decided = True

                    elif distribution_choice == "R" or distribution_choice == "r":
                        while not weights_decided:
                            valid = False
                            while not valid:
                                print("Choose 3 weight ranges.Maximum weight range is 10.Minumum weight range is 0. " +
                                      "There must be a minimum of 1 weight difference between minimum and max weight" +
                                      "ie. (3,4) , (0,9) ")
                                try:
                                    minimum_weight = input("input a minimum range ")
                                    maximum_weight = input("input a maximum range ")
                                    if int(minimum_weight) > -1 and int(minimum_weight) < int(maximum_weight) and int(
                                            maximum_weight) < 11:
                                        valid = True
                                except ValueError:
                                    valid = False
                            minimum_weight = int(minimum_weight)
                            maximum_weight = int(maximum_weight)
                            weight_range = (minimum_weight, maximum_weight)
                            weights.append(weight_range)
                            if len(weights) == 3:
                                weights_decided = True
                        gamemode_choice = False
                        while not gamemode_choice:
                            print(" ")
                            print("Which Gamemode would you like to use (1/2/3)")
                            print("1 - Naive Algorithm ")
                            print("2 - Dijkstras Algorithm ")
                            print("3 - Weight Algorithm ")
                            gamemode_option = input("Choose by selecting a number in respect to the option: ")
                            if gamemode_option == "1" or gamemode_option == "2" or gamemode_option == "3":
                                plt.figure(figsize=(10, 10))
                                plt.title('mean/grid size - Line')
                                plt.xlabel('Grid size', fontsize=14)
                                plt.ylabel('mean', fontsize=14)
                                for j in range(len(weights)):
                                    minimum_weight = weights[j][0]
                                    maximum_weight = weights[j][1]
                                    Height = 0
                                    Width = 0
                                    summ = 0
                                    sum_of_squares = []
                                    for x in range(5):
                                        Height += 5
                                        Width += 5
                                        for i in range(runs):
                                            if gamemode_option == "1":
                                                Personal_algorithm = Personal_gamemode(Height, Width, grid,
                                                                                       poisson_choice, poisson_weight,
                                                                                       minimum_weight, maximum_weight)
                                                mean = mean + Personal_algorithm.get_path()
                                                sum_of_squares.append(Personal_algorithm.get_path())
                                            elif gamemode_option == "2":
                                                dijkstras_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras,
                                                                                       poisson_choice, poisson_weight,
                                                                                       minimum_weight, maximum_weight)
                                                mean = mean + dijkstras_algorithm.get_path()
                                                sum_of_squares.append(dijkstras_algorithm.get_path())
                                            elif gamemode_option == "3":
                                                weight_algorithm = Gamemode_one_two(Height, Width, grid, dijkstras,
                                                                                    poisson_choice, poisson_weight,
                                                                                    minimum_weight, maximum_weight)
                                                mean = mean + weight_algorithm.get_path()
                                                sum_of_squares.append(weight_algorithm.get_path())
                                        summ += mean
                                        mean = mean / runs
                                        means.append(mean)
                                        mean = 0
                                        sum_of_squares[:] = [sum_of_squares - mean for sum_of_squares in sum_of_squares]
                                        sum_of_squares[:] = [sum_of_squares ** 2 for sum_of_squares in sum_of_squares]
                                        SD = math.sqrt(sum(sum_of_squares) / 150)
                                        print("Standard Deviation: ", SD, " Weight range:", weights[j][0], ", ",
                                              weights[j][1])
                                        SD = 0
                                        sum_of_squares = []

                                    minw = str(minimum_weight)
                                    maxw = str(maximum_weight)
                                    plt.plot(y_axis, means, label=("Weight: " + minw + ", " + maxw))

                                    means = []

                                plt.legend()
                                plt.show()

                                gamemode_choice = True
                                random_decided = True
            multiple_confirmed = True