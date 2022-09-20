from domain import Position, Player
from optapy import constraint_provider
from optapy.constraint import Joiners, ConstraintFactory
from optapy.score import HardSoftScore

@constraint_provider
def define_constraints(constraint_factory: ConstraintFactory):
    return [
        # Hard constraints
        room_conflict(constraint_factory),
        teacher_conflict(constraint_factory),
        student_group_conflict(constraint_factory),
        # Soft constraints are only implemented in the optapy-quickstarts code
    ]

def position_conflict(constraint_factory: ConstraintFactory):
    # A position can only be played by at most one player
    return constraint_factory.for_each(Player) \
        .join(Player,
              Joiners.equal(lambda player: player.position),
              Joiners.less_than(lambda player: player.id)        
        ) \ 
        .penalize("Position Conflict", HardSoftScore.ONE_HARD)