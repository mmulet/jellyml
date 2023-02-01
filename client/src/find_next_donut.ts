import { Donut } from "./Donut";
import { eaten } from "./DonutState";
import { RectPosition } from "./RectPosition";

export interface Donut_Holder {
  donut: Donut | null;
  x: number;
  y: number;
  left: boolean;
}

export interface Input {
  donut_holder: Donut_Holder;
  main_position: RectPosition;
  donuts: Donut[];
  time_threshold: number;
  animation_length: number;
  pure_only: boolean;
}

/**
 *

 * @returns False on success, true on failure
 */
export const find_next_donut = ({
  donut_holder,
  main_position,
  donuts,
  time_threshold,
  animation_length,
  pure_only,
}: Input) => {
  let lowest_possible_donut_index = -1;

  for (let index = 0; index < donuts.length; index++) {
    const donut = donuts[index];
    if (donut.left !== donut_holder.left) {
      continue;
    }

    const y_in_absolute_coords = donut.y + main_position.top;

    if (y_in_absolute_coords > donut_holder.y) {
      /**
       * This donut is below the tentacle
       */
      continue;
    }

    const distance_in_a_second = donut.vy * animation_length;

    const y_in_a_second = y_in_absolute_coords + distance_in_a_second;
    if (y_in_a_second > donut_holder.y) {
      /**
       * This donut will be below the tentacle
       */
      continue;
    }

    if (y_in_absolute_coords < donut_holder.y - donut.vy * time_threshold) {
      /**
       * Too far, wait for it to get closer
       */
      continue;
    }

    if (
      pure_only &&
      (donut.state.bottom == eaten ||
        donut.state.left == eaten ||
        donut.state.right == eaten ||
        donut.state.top == eaten)
    ) {
      continue;
    }

    if (lowest_possible_donut_index == -1) {
      lowest_possible_donut_index = index;
      continue;
    }

    const lowest_donut = donuts[lowest_possible_donut_index];
    if (donut.y >= lowest_donut.y) {
      lowest_possible_donut_index = index;
    }
  }
  if (lowest_possible_donut_index == -1) {
    return true;
  }

  const index = lowest_possible_donut_index;
  const donut = donuts[index];

  const y_in_absolute_coords = donut.y + main_position.top;
  const x_in_absolute_coords =
    donut.x + (donut.left ? main_position.left : main_position.right);

  donut.x = x_in_absolute_coords - donut_holder.x;
  donut.y = y_in_absolute_coords - donut_holder.y;
  donut_holder.donut = donut;

  donuts.splice(index, 1);

  return false;
};
