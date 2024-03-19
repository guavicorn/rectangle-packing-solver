#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2022 Kotaro Terada
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rectangle_packing_solver as rps

def main():
    # Define a problem
    problem = rps.Problem(
        rectangles=[
            {"width": 2.53, "height": 2.53, "rotatable": True},
            {"width": 3.1, "height": 3, "rotatable": True},
            {"width": 5, "height": 5, "rotatable": True},
            {"width": 5, "height": 5, "rotatable": True},
            {"width": 4, "height": 4, "rotatable": True},
            {"width": 2.6, "height": 6, "rotatable": True},
            {"width": 14.75, "height": 3.65, "rotatable": True},
        ]
    )
    print("problem:", problem)

    # Find a solution
    print("\n=== Solving without width/height constraints ===")
    solution = rps.Solver().solve(problem=problem,simanneal_steps=20600,max_temp=1460,min_temp=0.84,show_progress=True)
    print("solution:", solution)
    rps.Visualizer().visualize(solution=solution, path="./figs/floorplan_example.png")

    # We can also give a solution width (and/or height) limit
    print("\n=== Solving with width/height constraints ===")
    solution = rps.Solver().solve(problem=problem,simanneal_steps=15400,max_temp=1020,min_temp=0.6,width_limit=12,show_progress=True)
    print("solution:", solution)
    rps.Visualizer().visualize(solution=solution, path="./figs/floorplan_example_limit.png")


if __name__ == "__main__":
    main()
