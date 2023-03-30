"""
 Title:         Problem
 Description:   For defining the MOGA problem
 Author:        Janzen Choi

"""

# Libraries
import warnings
import numpy as np
from pymoo.core.problem import ElementwiseProblem
from modules.moga.objective import Objective
from modules.recorder import Recorder

# The Problem class
class Problem(ElementwiseProblem):

    # Constructor
    def __init__(self, objective:Objective, recorder:Recorder):
        
        # Initialise
        self.objective  = objective
        self.model      = objective.get_model()
        self.recorder   = recorder
        
        # Define the element wise problem
        super().__init__(
            n_var = len(self.model.get_param_info()),
            n_obj = len(self.objective.get_error_names()),
            xl    = np.array(self.model.get_param_lower_bounds()),
            xu    = np.array(self.model.get_param_upper_bounds()),
        )
    
    # Minimises expression "F" such that the expression "G <= 0" is satisfied
    def _evaluate(self, params:list[float], out:dict, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore") # ignore warnings

            # Get curves
            prd_curves = self.model.get_prd_curves(*params)
            prd_curves = self.model.ensure_validity(prd_curves)

            # Check constraints and adjust error values
            error_values = self.objective.get_error_values(prd_curves)
            constraint_values = self.objective.get_constraint_values(prd_curves)
            error_values = self.objective.get_penalised_error_values(error_values, constraint_values)
            
            # Update the recorder and pass in error values
            self.recorder.update_results(params, error_values, constraint_values)
            out["F"] = error_values