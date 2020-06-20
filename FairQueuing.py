import os

packetsArray = []
error = False


class Packet:
    def __init__(self, number, arrival_time, duration, flux):
        self.number = int(number)
        self.arrival_time = int(arrival_time)
        self.duration = int(duration)
        self.flux = int(flux)
        self.time_exec = 0

    def act_time_exec(self, time):
        self.time_exec = max(time, self.arrival_time) + self.duration


def reader():
    global error
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "values.txt")
    with open(path) as file:
        for line in file:
            line = line.strip().split(",")
            if len(line) == 4:
                package_1 = Packet(line[0], line[1], line[2], line[3])
                packetsArray.append(package_1)
            else:
                error = True
                break


def solver_FQ():
    time = 0
    best_packet = Packet(0, 0, 0, 0)
    best_packet.act_time_exec(int(1000))
    while len(packetsArray) != 0:
        for package in packetsArray:
            package.act_time_exec(time)
            if package.arrival_time <= time and package.time_exec < best_packet.time_exec:
                best_packet = package
        print(best_packet.number)

        time = best_packet.time_exec


reader()
if not error:
    solver_FQ()
else:
    print("Hi ha algún error al entrar les dades")

