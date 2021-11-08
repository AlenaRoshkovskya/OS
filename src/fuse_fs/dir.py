from random import uniform

from .file import File 
from .consts import DEVIATION_FROM_POINT, PHASE_VOLTAGE, BASE_LINE_VOLTAGE_POS, LINE_VOLTAGE_DELTA

class Dir: 
    def __init__(self, name: str):
        self.name = name 
        self.dirs = []
        self.files = []
        
        self._create_voltage_files()

    def _create_voltage_files(self):
        for ind in range(1, 4):
            phase_file = File(f"phase{ind}", "phase")
            phase_file.content = PHASE_VOLTAGE
            self.files.append(phase_file)

        self.files.append(self._generate_line_file(1, 2))
        self.files.append(self._generate_line_file(2, 3))
        self.files.append(self._generate_line_file(3, 1))
        

    def _generate_line_file(self, line_a, line_b):
        line_file = File(f"line{line_a}-{line_b}", "line")
        line_file.content = uniform(
            BASE_LINE_VOLTAGE_POS - LINE_VOLTAGE_DELTA, 
            BASE_LINE_VOLTAGE_POS + LINE_VOLTAGE_DELTA
        ) * DEVIATION_FROM_POINT

        return line_file