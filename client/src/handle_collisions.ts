import { Donut } from "./Donut";
import { DonutState, eaten } from "./DonutState";
import { JellySprite } from "./JellySprite";
import { MouseOrTouchInput } from "./MouseOrTouchInput";
import { Touches } from "./Touches";

export interface HasInputAndDonuts {
  mouse: MouseOrTouchInput | null;
  touches: Touches;
  donuts: Donut[];
  main_position: {
    left: number;
    right: number;
    top: number;
  };
  jelly_sprites: JellySprite[];
}

/**
 * Already assumes that the point
 * is inside the donut.
 */
const get_eaten_parts = (
  donut: Donut,
  x: number,
  y: number
): keyof DonutState => {
  const x_relative_to_donut = x - (donut.x + 16);
  const y_relative_to_donut = y - (donut.y + 16);

  if (y_relative_to_donut >= 0) {
    if (x_relative_to_donut > y_relative_to_donut) {
      return "right";
    }
    if (x_relative_to_donut >= -y_relative_to_donut) {
      return "bottom";
    }
    return "left";
  }
  if (x_relative_to_donut < y_relative_to_donut) {
    return "left";
  }
  if (x_relative_to_donut <= -y_relative_to_donut) {
    return "top";
  }
  return "right";
};

export const handle_collisions = ({
  mouse: in_mouse,
  touches: in_touches,
  donuts,
  main_position,
  jelly_sprites,
}: HasInputAndDonuts) => {
  const un_translated_inputs: MouseOrTouchInput[] = [];
  if (in_mouse != null && !in_mouse.affected_a_donut) {
    un_translated_inputs.push(in_mouse);
  }
  for (const [, touch] of in_touches) {
    if (touch.affected_a_donut) {
      continue;
    }
    un_translated_inputs.push(touch);
  }
  if (un_translated_inputs.length <= 0) {
    return;
  }

  const inputs: {
    left_x: number;
    left_y: number;
    right_x: number;
    right_y: number;
  }[] = [];
  for (const input of un_translated_inputs) {
    inputs.push({
      left_x: input.clientX - main_position.left,
      left_y: input.clientY - main_position.top,
      right_x: input.clientX - main_position.right,
      right_y: input.clientY - main_position.top,
    });
  }
  const indices_to_remove: number[] = [];
  for (let i = 0; i < donuts.length; i++) {
    const donut = donuts[i];
    for (let input_i = 0; input_i < inputs.length; input_i++) {
      const input = inputs[input_i];
      const x = donut.left ? input.left_x : input.right_x;
      const y = donut.left ? input.left_y : input.right_y;
      if (
        !(x > donut.x && x < donut.x + 32 && y > donut.y && y < donut.y + 32)
      ) {
        continue;
      }
      const part = get_eaten_parts(donut, x, y);
      if (donut.state[part] == eaten) {
        /**
         * Already ate this part, so it's not a match
         */
        continue;
      }

      jelly_sprites.push({
        x: x - 32,
        y: y - 32,
        age: 0,
        vertical: part == "left" || part == "right" ? true : false,
        left: donut.left,
      });
      if (jelly_sprites.length > 500) {
        jelly_sprites.shift();
      }

      donut.state[part] = eaten;
      un_translated_inputs[input_i].affected_a_donut = true;
      if (
        donut.state.left == eaten &&
        donut.state.right == eaten &&
        donut.state.top == eaten &&
        donut.state.bottom == eaten
      ) {
        indices_to_remove.push(i);
      }
      break;
    }
  }
  indices_to_remove.sort();
  for (let i = indices_to_remove.length - 1; i >= 0; i--) {
    donuts.splice(indices_to_remove[i], 1);
  }
};
