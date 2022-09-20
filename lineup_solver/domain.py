from tkinter import scrolledtext
from turtle import position
from optapy import problem_fact, planning_id
from optapy import planning_solution, planning_entity_collection_property, \
                   problem_fact_collection_property, \
                   value_range_provider, planning_score
from optapy.score import HardSoftScore

@problem_fact
class Position:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self) -> str:
        return f"Position(id={self.id}, name={self.name})"

@planning_entity
class Player:
    def __init__(self, id, position=None) -> None:
        self.id = id
        self.position = position

    @planning_id
    def get_id(self):
        return self.id

    @planning_variable(Position, ["positionRange"])
    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def __str__(self) -> str:
        return f"Player(id={self.id}, position={self.position})"

def format_list(a_list):
    return ',\n'.join(map(str, a_list))

@planning_solution
class TimeTable:
    def __init__(self, player_list, score=None):
        self.player_list = player_list
        self.score = score

    @problem_fact_collection_property(Position)
    @value_range_provider("positionRange")
    def get_position_list(self):
        return self.position_list

    @planning_entity_collection_property(Player)
    def get_player_list(self):
        return self.player_list

    @planning_score(HardSoftScore)
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self) -> str:
        return (f"TimeTable("
            f"position_list={format_list(self.position_list)},\n"
            f")"
        )

def generate_problem():
    position_list = [Position(1,"C"),
                     Position(2,"C"),
                     Position(3,"1B"),
                     Position(4,"2B"),
                     Position(5,"SS"),
                     Position(5,"MI"),
                     Position(6,"3B"),
                     Position(7,"OF"),
                     Position(8,"OF"),
                     Position(9,"OF"),
                     Position(10,"OF"),
                     Position(11,"OF"),
                     Position(12,"UTIL"),
    ]

    player_list = [Player(1,"OF",)]

